"""Fixtures, displays and short experiment drivers, NOT the exercise solutions.

All images and labels here are generated teaching data. No files are downloaded,
no course notebook is executed, and no performance claim concerns a real sorter.
"""
from __future__ import annotations

import copy
import time

import cv2
import matplotlib.pyplot as plt
import numpy as np
from scipy import ndimage, signal
import torch
from torch import nn
from torch.utils.data import DataLoader, TensorDataset

LABELS = ("cardboard tile", "bottle cap", "can")
SEED = 2601


def seed_all(seed=SEED):
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.set_num_threads(2)
    cv2.setNumThreads(1)


def gray(rgb):
    return np.asarray(rgb, dtype=float) @ np.array([.299, .587, .114])


def tile(label, seed, size=32):
    """One independently generated object; colour is independent of its label."""
    rng = np.random.default_rng(seed)
    y, x = np.indices((size, size))
    image = np.full((size, size, 3), .10) + rng.normal(0, .012, (size, size, 1))
    cx, cy = size/2 + rng.uniform(-2, 2, 2)
    theta = rng.uniform(-.2, .2)
    xx = (x-cx)*np.cos(theta) + (y-cy)*np.sin(theta)
    yy = -(x-cx)*np.sin(theta) + (y-cy)*np.cos(theta)
    if label == 0:
        mask = (np.abs(xx) < 11) & (np.abs(yy) < 7)
    elif label == 1:
        mask = xx**2 + yy**2 < rng.uniform(7, 9)**2
    else:
        mask = (np.abs(xx) < 5) & (np.abs(yy) < 12)
    colour = rng.uniform(.38, .72, 3)
    texture = 1 + .08*np.sin(xx*1.3) + rng.normal(0, .025, (size, size))
    image[mask] = colour * texture[mask, None]
    return np.clip(image, 0, 1).astype(np.float32)


def make_packet():
    """Separate captures: fixed-view lighting burst, moving belt, camera pair."""
    rng = np.random.default_rng(SEED)
    h, w = 144, 420
    world = np.full((h, w, 3), .16, np.float32)
    for _ in range(1100):
        x, y = int(rng.integers(w)), int(rng.integers(h))
        colour = tuple(float(v) for v in rng.uniform(.08, .45, 3))
        cv2.circle(world, (x, y), int(rng.integers(1, 3)), colour, -1)
    for i, x in enumerate(range(20, 380, 45)):
        y = 18 + (i % 3)*35
        world[y:y+32, x:x+32] = tile(i % 3, 100+i)
        cv2.putText(world, str(i), (x, y+42), cv2.FONT_HERSHEY_SIMPLEX, .4, (.7, .7, .7), 1)
    # A neutral card gives an honest diagnostic for the scene-average assumption.
    world[112:132, 12:80] = .55
    colour_raw = world[:, :220] * np.array([1.25, .8, 1.1])
    y, x = np.indices((48, 48), dtype=float)
    height = 5*np.exp(-((x-23.5)**2+(y-23.5)**2)/(2*11**2))
    q, p = np.gradient(height)
    normals = np.stack([-p, -q, np.ones_like(p)], -1)
    normals /= np.linalg.norm(normals, axis=-1, keepdims=True)
    rho = .5 + .08*np.sin(x/7)*np.cos(y/9)
    lights = np.array([[0, 0, 1], [.65, 0, .76], [-.65, 0, .76],
                       [0, .65, .76], [0, -.65, .76], [.45, .45, .77], [-.45, .45, .77]])
    lights /= np.linalg.norm(lights, axis=1, keepdims=True)
    burst = np.einsum("mc,hwc->mhw", lights, normals*rho[..., None])
    shadow = burst.copy()
    shadow[1, 10:36, 12:32] = 0
    shadow[3, 20:40, 16:36] = 0
    specular = burst.copy()  # isolate highlights from shadows in this comparison
    specular[5, 12:28, 16:32] += .8
    albedo = rho[..., None]*np.array([.7, .5, .3])
    shading = burst[0]/rho
    mask = (x-23.5)**2+(y-23.5)**2 < 22**2
    albedo[~mask] = 0
    clean = gray(world[:, :220])
    noisy = np.clip(clean + rng.normal(0, .035, clean.shape), 0, 1)
    frame0 = gray(world[:112, :200])
    displacement = np.array([.8, .5])  # x right, y down, pixels per frame
    frame1 = cv2.warpAffine(frame0, np.array([[1., 0., .8], [0., 1., .5]]),
                           (200, 112), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT_101)
    f0 = ndimage.gaussian_filter(frame0, 1)
    f1 = ndimage.gaussian_filter(frame1, 1)
    average = (f0+f1)/2
    gy, gx = np.gradient(average)
    view_a = world[:, :280].copy()
    rotation = cv2.getRotationMatrix2D((140, 72), 2., .98)
    view_b = cv2.warpAffine(world[:, 140:], rotation, (280, h), borderMode=cv2.BORDER_REFLECT_101)
    true_affine = (np.vstack([rotation, [0, 0, 1]]) @
                   np.array([[1, 0, -140], [0, 1, 0], [0, 0, 1]]))[:2]
    return dict(world=world, raw=colour_raw, albedo=albedo, shading=shading, mask=mask,
                burst=burst, shadow=shadow, specular=specular, lights=lights,
                normals=normals, rho=rho, height=height, clean=clean, noisy=noisy,
                frame0=frame0, frame1=frame1, gx=gx, gy=gy, it=f1-f0,
                displacement=displacement, view_a=view_a, view_b=view_b, true_affine=true_affine)


def gallery(images, titles=None, columns=3, cmap="gray", size=3):
    titles = titles or [""]*len(images)
    rows = (len(images)+columns-1)//columns
    fig, axes = plt.subplots(rows, columns, figsize=(columns*size, rows*size), squeeze=False)
    for ax in axes.flat:
        ax.axis("off")
    for ax, image, title in zip(axes.flat, images, titles):
        ax.imshow(np.asarray(image), cmap=cmap)
        ax.set_title(title, fontsize=10)
    fig.tight_layout()
    plt.show()
    plt.close(fig)  # no duplicate rich display of a returned Figure in Jupyter


def colour_views(rgb):
    rgb = np.asarray(rgb, np.float32)
    hsv = cv2.cvtColor(rgb, cv2.COLOR_RGB2HSV)
    ycrcb = cv2.cvtColor(rgb, cv2.COLOR_RGB2YCrCb)
    gallery([rgb, hsv[..., 0], hsv[..., 2], ycrcb[..., 0]],
            ["RGB [0,1]", "HSV hue: degrees, not RGB", "HSV value", "Y (luma)"], columns=4)
    print("Float OpenCV HSV: H in [0,360), S,V in [0,1]. YCrCb order is Y,Cr,Cb; Lab1 asks Y,Cb,Cr.")


def photo_summary(packet, solver):
    rows = []
    for label in ("burst", "shadow", "specular"):
        for weighted in (False, True):
            rho, normals = solver(packet[label], packet["lights"], weighted=weighted)
            dots = np.sum(normals*packet["normals"], axis=-1)
            angle = np.degrees(np.arccos(np.clip(dots, -1, 1)))
            rows.append((label, "weighted" if weighted else "plain", float(np.mean(angle))))
    print("Capture       fit         mean normal error (degrees; generated ground truth)")
    for label, fit, error in rows:
        print(f"{label:12} {fit:10} {error:8.3f}")


def sample_bilinear(image, xs, ys):
    """Supplied interpolation only; you must compute the inverse coordinates."""
    h, w = image.shape[:2]
    valid = (xs >= 0) & (xs <= w-1) & (ys >= 0) & (ys <= h-1)
    x0 = np.floor(np.clip(xs, 0, w-1)).astype(int)
    y0 = np.floor(np.clip(ys, 0, h-1)).astype(int)
    x1, y1 = np.minimum(x0+1, w-1), np.minimum(y0+1, h-1)
    a, b = np.clip(xs, 0, w-1)-x0, np.clip(ys, 0, h-1)-y0
    if image.ndim == 3:
        a, b = a[..., None], b[..., None]
    values = ((1-a)*(1-b)*image[y0, x0] + a*(1-b)*image[y0, x1] +
              (1-a)*b*image[y1, x0] + a*b*image[y1, x1])
    values[~valid] = 0
    return values, valid


def select_points(score, count=24, border=9):
    score = np.asarray(score).copy()
    score[:border] = score[-border:] = 0
    score[:, :border] = score[:, -border:] = 0
    candidates = (score == ndimage.maximum_filter(score, size=11)) & (score > .05*score.max())
    ys, xs = np.where(candidates)
    order = np.argsort(score[ys, xs])[::-1][:count]
    return np.column_stack([xs[order], ys[order]])


def tracks(packet, scores, solver):
    points = select_points(scores["shi"])
    flow = []
    for x, y in points:
        region = np.s_[y-5:y+6, x-5:x+6]
        flow.append(solver(packet["gx"][region], packet["gy"][region], packet["it"][region]))
    flow = np.asarray(flow).reshape(-1, 2)
    valid = np.all(np.isfinite(flow), axis=1)
    fig, ax = plt.subplots(figsize=(9, 4))
    ax.imshow(packet["frame0"], cmap="gray")
    ax.quiver(points[valid, 0], points[valid, 1], flow[valid, 0], flow[valid, 1],
              color="tomato", angles="xy", scale_units="xy", scale=.15)
    ax.set_title("Your tracks (arrows enlarged for visibility)")
    plt.show()
    estimate = np.median(flow[valid], axis=0) if valid.any() else np.array([np.nan, np.nan])
    print("Median dx,dy:", estimate.round(3), " | generated truth:", packet["displacement"])
    print("Calibration GIVEN for this toy rig: 2 mm/pixel, 25 frames/s.")
    print("Estimated belt speed:", round(float(np.linalg.norm(estimate)*.002*25), 4), "m/s")
    return estimate


def sift_pair(packet):
    sift = cv2.SIFT_create(nfeatures=240, contrastThreshold=.015)
    images = [np.rint(gray(packet[k])*255).astype(np.uint8) for k in ("view_a", "view_b")]
    kp_a, desc_a = sift.detectAndCompute(images[0], None)
    kp_b, desc_b = sift.detectAndCompute(images[1], None)
    if desc_a is None or desc_b is None:
        raise RuntimeError("Fixture has no SIFT descriptors; check the OpenCV installation.")
    return dict(a=np.array([k.pt for k in kp_a]), b=np.array([k.pt for k in kp_b]),
                desc_a=desc_a.astype(float), desc_b=desc_b.astype(float))


def show_matches(packet, features, pairs, inliers=None):
    canvas = np.concatenate([packet["view_a"], packet["view_b"]], axis=1)
    fig, ax = plt.subplots(figsize=(12, 4))
    ax.imshow(canvas)
    for i, (a, b) in enumerate(pairs[:60]):
        p, q = features["a"][a], features["b"][b] + [packet["view_a"].shape[1], 0]
        colour = "lime" if inliers is None or inliers[i] else "tomato"
        ax.plot([p[0], q[0]], [p[1], q[1]], color=colour, alpha=.5, linewidth=.6)
    ax.set_title("Green = retained; red = rejected (first 60 matches)")
    ax.axis("off")
    plt.show()


def panorama(packet, matrix, warp, blend):
    """Canvas bookkeeping supplied, inverse coordinate mapping and blending yours."""
    h, w = packet["view_a"].shape[:2]
    corners = np.array([[0, 0, 1], [w-1, 0, 1], [0, h-1, 1], [w-1, h-1, 1]])
    moved = corners @ matrix.T
    bounds = np.vstack([moved, corners[:, :2]])
    low, high = np.floor(bounds.min(0)), np.ceil(bounds.max(0))
    shape = tuple((high-low+1).astype(int)[::-1])
    if not np.isfinite(bounds).all() or min(shape) <= 0 or max(shape) > 2000:
        raise ValueError("Implausible teaching-rig canvas. Check affine direction and coordinate units.")
    offset = np.array([[1., 0., -low[0]], [0., 1., -low[1]], [0., 0., 1.]])
    a, ma = warp(packet["view_a"], (offset @ np.vstack([matrix, [0, 0, 1]]))[:2], shape)
    b, mb = warp(packet["view_b"], offset[:2], shape)
    wa = ndimage.distance_transform_edt(np.pad(ma, 1))[1:-1, 1:-1]
    wb = ndimage.distance_transform_edt(np.pad(mb, 1))[1:-1, 1:-1]
    result = blend(a, b, wa, wb)
    gallery([a, b, result], ["Camera A in common canvas", "Camera B", "Your feathered panorama"])
    return result


def make_loaders(domain="source", batch_size=32):
    """Independent object instances in each split; no augmented sibling leakage."""
    loaders = {}
    for split, count, base in [("train", 60, 10000), ("val", 18, 20000), ("test", 19, 30000)]:
        xs, ys = [], []
        for label in range(3):
            for i in range(count):
                image = tile(label, base + label*1000+i)
                if domain == "route":
                    image = np.clip(image*np.array([.75, 1.15, 1.05]), 0, 1)
                xs.append(image.transpose(2, 0, 1))
                ys.append(int(label != 1) if domain == "route" else label)
        dataset = TensorDataset(torch.tensor(np.asarray(xs), dtype=torch.float32), torch.tensor(ys))
        generator = torch.Generator().manual_seed(SEED)
        loaders[split] = DataLoader(dataset, batch_size=batch_size, shuffle=split == "train", generator=generator)
    return loaders


def fit(model, loaders, step, evaluate, optimizer="adam", lr=.01, epochs=8):
    opt_class = torch.optim.Adam if optimizer == "adam" else torch.optim.SGD
    opt = opt_class([p for p in model.parameters() if p.requires_grad], lr=lr)
    history = []
    start = time.perf_counter()
    for epoch in range(epochs):
        loss_sum, examples = 0., 0
        for x, y in loaders["train"]:
            loss_sum += step(model, opt, x, y)*len(y)
            examples += len(y)
        validation = evaluate(model, loaders["val"])
        history.append((loss_sum/examples, validation["accuracy"]))
    print(f"{epochs} epochs, {time.perf_counter()-start:.1f}s on CPU. Validation accuracy: {history[-1][1]:.3f}")
    model._cv1_fitted = True
    return np.array(history)


def compare_training(model_class, step, evaluate):
    """Shared data/order/budget; optimizer cases share weights, init cases change them."""
    seed_all()
    state = copy.deepcopy(model_class().state_dict())
    runs = {}
    for name, optimizer, lr, initialization in [("Adam .01", "adam", .01, "same"),
                                       ("Adam .00001", "adam", .00001, "same"),
                                       ("SGD .05", "sgd", .05, "same"),
                                       ("Zero init", "adam", .01, "zero"),
                                       ("Gaussian .02", "adam", .01, "gaussian"),
                                       ("He conv init", "adam", .01, "he")]:
        seed_all()
        model = model_class()
        model.load_state_dict(state)
        if initialization == "zero":
            for parameter in model.parameters():
                nn.init.zeros_(parameter)
        elif initialization in ("gaussian", "he"):
            for layer in model.modules():
                if isinstance(layer, nn.Conv2d):
                    if initialization == "he":
                        nn.init.kaiming_normal_(layer.weight, nonlinearity="relu")
                    else:
                        nn.init.normal_(layer.weight, std=.02)
                    nn.init.zeros_(layer.bias)
        print(name)
        hist = fit(model, make_loaders(), step, evaluate, optimizer, lr, epochs=20)
        runs[name] = hist
    fig, axes = plt.subplots(1, 2, figsize=(10, 3))
    for name, hist in runs.items():
        axes[0].plot(hist[:, 0], label=name)
        axes[1].plot(hist[:, 1], label=name)
    axes[0].set_title("Training CE (equal data/budget)")
    axes[1].set_title("Validation accuracy; NOT test data")
    axes[1].legend(fontsize=8)
    plt.show()
    return runs


def capture_cam(model, image, class_index=None):
    """Provide real activations/gradients from the trained toy model, not a fake CAM."""
    model.eval()
    with torch.enable_grad():
        features = model.features(image)
        # Frozen backbones can otherwise produce a non-differentiable tensor.
        if not features.requires_grad:
            features = features.detach().requires_grad_(True)
        logits = model.classifier(features.mean(dim=(2, 3)))
        target = int(logits.argmax(1)[0]) if class_index is None else int(class_index)
        grads = torch.autograd.grad(logits[0, target], features)[0]
    return features.detach(), grads.detach(), target


def close(actual, expected, atol=1e-6):
    np.testing.assert_allclose(actual, expected, atol=atol, rtol=1e-5)


class Mission:
    names = {
        "01": "Repair colour", "02": "Recolour without repainting shadows", "03": "Recover surface normals",
        "04": "Recover height", "05": "Build Gaussian filters", "06": "Measure edges", "07": "Compare LoG/DoG",
        "08": "Choose trackable features", "09": "Measure belt motion", "10": "Match local evidence",
        "11": "Reject bad correspondences", "12": "Build the belt map", "13": "Build the sorter",
        "14": "Train and audit", "15": "Reuse the backbone", "16": "Inspect attention",
    }

    def __init__(self):
        seed_all()
        self.packet = make_packet()
        self.states, self.results = {}, {}

    def run(self, key, solver):
        """Failures remain visible but don't prevent unrelated chapters from running."""
        self.results.pop(key, None)
        try:
            result = getattr(self, f"check_{key}")(solver)
        except NotImplementedError:
            self.states[key] = "TODO"
            print(f"[{key}] TODO: implement {self.names[key]}. Later chapters use supplied independent inputs.")
            return None
        except Exception as exc:
            self.states[key] = "CHECK FAILED"
            print(f"[{key}] CHECK FAILED — {type(exc).__name__}: {exc}")
            return None
        self.states[key] = "PASS"
        self.results[key] = result
        print(f"[{key}] PASS — {self.names[key]}")
        return result

    def status(self):
        for key, title in self.names.items():
            print(f"{key} {self.states.get(key, 'NOT RUN'):13} {title}")
        print(f"\n{sum(v == 'PASS' for v in self.states.values())}/16 code checkpoints passed.")

    def check_01(self, fn):
        toy = np.array([[[0., 0., 0.], [.4, .2, .2]]])
        out = fn(toy)
        close(out["lightness"], [[0, .3]])
        close(out["nrgb"], [[[0, 0, 0], [.5, .25, .25]]])
        close(out["opponent"][0, 1], [.2/np.sqrt(2), .2/np.sqrt(6), .8/np.sqrt(3)])
        close(out["balanced"].mean((0, 1)), [toy.mean()]*3)
        black = fn(np.zeros((2, 2, 3)))
        assert np.isfinite(black["nrgb"]).all() and np.isfinite(black["balanced"]).all()
        return fn(self.packet["raw"])

    def check_02(self, fn):
        a = np.array([[[.2, .3, .4], [.1, .2, .3]]])
        s = np.array([[.5, .8]])
        close(fn(a, s, np.array([[True, False]]), np.array([1., 0., 0.])),
              [[[.5, 0, 0], [.08, .16, .24]]])
        return fn(self.packet["albedo"], self.packet["shading"], self.packet["mask"], np.array([.9, .1, .1]))

    def check_03(self, fn):
        rho, n = fn(self.packet["burst"], self.packet["lights"])
        close(rho, self.packet["rho"])
        close(n, self.packet["normals"])
        rho0, n0 = fn(np.zeros((7, 1, 1)), self.packet["lights"])
        close(rho0, [[0]])
        close(n0, np.zeros((1, 1, 3)))
        obs = np.array([.5, .3, 0, .4, .5, .4, .3])
        L = self.packet["lights"]
        expected = np.linalg.lstsq(obs[:, None]*L, obs*obs, rcond=None)[0]
        rw, nw = fn(obs[:, None, None], L, weighted=True)
        close(rw[..., None]*nw, expected[None, None, :])
        return rho, n

    def check_04(self, fn):
        n = np.broadcast_to(np.array([-1., .5, 1.])/1.5, (4, 5, 3))
        out = fn(n)
        y, x = np.indices((4, 5))
        close(out["height"], x-.5*y)
        close(out["curl"], np.zeros((4, 5)))
        return fn(self.packet["normals"])

    def check_05(self, fn):
        g, d, dd = fn(1.2, 4)
        x = np.arange(-4, 5)
        assert g.shape == (9,) and (g > 0).all()
        close(g.sum(), 1)
        close(g, g[::-1])
        close(d, -x/1.2**2*g)
        close(dd, (x*x/1.2**4-1/1.2**2)*g)
        assert np.linalg.matrix_rank(np.outer(g, g)) == 1
        return g, d, dd

    def check_06(self, fn):
        y, x = np.indices((9, 9))
        gx, gy, mag, theta = fn(x+2*y)
        close(gx[2:-2, 2:-2], np.ones((5, 5)))
        close(gy[2:-2, 2:-2], np.full((5, 5), 2))
        close(mag[2:-2, 2:-2], np.full((5, 5), np.sqrt(5)))
        close(theta[2:-2, 2:-2], np.full((5, 5), np.arctan2(2, 1)))
        return fn(self.packet["noisy"])

    def check_07(self, fn):
        impulse = np.zeros((31, 31)); impulse[15, 15] = 1
        out = fn(impulse)
        assert set(out) == {"sequential", "direct", "dog"}
        for value in out.values():
            assert value.shape == impulse.shape and np.isfinite(value).all()
            assert np.max(np.abs(value)) > 1e-5
        const = fn(np.ones((31, 31)))
        for value in const.values():
            close(value[10:-10, 10:-10], np.zeros((11, 11)), atol=1e-5)
        # Direct sampled LoG must have a negative centre under our sign convention.
        assert out["direct"][15, 15] < 0
        return fn(self.packet["noisy"])

    def check_08(self, fn):
        out = fn(np.ones((9, 9)), np.zeros((9, 9)))
        close(out["shi"], np.zeros((9, 9)))
        close(out["harris"], np.full((9, 9), -.04*25**2))
        gx = np.zeros((9, 9)); gy = np.zeros_like(gx)
        gx[4, 3] = 3; gy[3, 4] = 4
        out = fn(gx, gy)
        close(out["shi"][4, 4], 9)
        close(out["harris"][4, 4], 9*16-.04*25**2)
        return fn(self.packet["gx"], self.packet["gy"])

    def check_09(self, fn):
        close(fn(np.array([[2., 0.]]), np.array([[0., 3.]]), np.array([[-4., 3.]])), [2, -1])
        bad = fn(np.ones((3, 3)), np.zeros((3, 3)), np.ones((3, 3)))
        assert np.isnan(bad).all(), "An edge must be rejected, not confidently assigned 2D flow."
        region = np.s_[38:55, 38:55]
        return fn(self.packet["gx"][region], self.packet["gy"][region], self.packet["it"][region])

    def check_10(self, fn):
        a = np.array([[0., 0.], [1., 1.]])
        b = np.array([[.01, 0.], [1.01, 1.], [9., 9.]])
        close(fn(a, b, .75), [[0, 0], [1, 1]])
        assert len(fn(np.array([[0., 0.]]), np.zeros((2, 2)), .75)) == 0, "Reject equal zero-distance alternatives."
        assert len(fn(np.array([[0.]]), np.array([[.8], [1.]]), .75)) == 0, "Squared distances need threshold squared."
        features = sift_pair(self.packet)
        pairs = np.asarray(fn(features["desc_a"], features["desc_b"], .75))
        assert len(pairs) >= 6, "Too few matches; check L2 vs squared ratio, ordering and threshold."
        assert pairs.ndim == 2 and pairs.shape[1] == 2 and np.issubdtype(pairs.dtype, np.integer), "Return integer index pairs, shape (N,2)."
        assert (pairs >= 0).all() and (pairs[:, 0] < len(features["a"])).all() and (pairs[:, 1] < len(features["b"])).all()
        return features, pairs

    def check_11(self, solvers):
        fit, robust = solvers
        rng = np.random.default_rng(4)
        src = rng.uniform(-10, 10, (45, 2))
        truth = np.array([[1.02, .03, 2.], [-.02, .98, -1.]])
        dst = np.c_[src, np.ones(len(src))] @ truth.T
        close(fit(src[:8], dst[:8]), truth)
        corrupt = dst.copy(); corrupt[:12] = rng.uniform(-30, 30, (12, 2))
        matrix, inliers = robust(src, corrupt, threshold=.1, trials=120, seed=8)
        close(matrix, truth)
        assert np.asarray(inliers).dtype == bool and inliers.sum() == 33
        features, pairs = self.results.get("10", (None, None))
        if features is None:
            print("Toy RANSAC checks passed; complete 10 to align the actual camera pair.")
            return matrix, inliers
        matrix, inliers = robust(features["a"][pairs[:, 0]], features["b"][pairs[:, 1]],
                                  threshold=2., trials=200, seed=8)
        assert inliers.sum() >= 5
        probes = np.array([[30, 30, 1], [220, 30, 1], [30, 110, 1], [220, 110, 1]])
        assert np.median(np.linalg.norm(probes@(matrix-self.packet["true_affine"]).T, axis=1)) < 2.
        return matrix, inliers

    def check_12(self, solvers):
        warp, blend = solvers
        image = np.arange(12., dtype=float).reshape(3, 4)
        output, valid = warp(image, np.array([[1., 0., 1.], [0., 1., 0.]]), (3, 5))
        close(output[:, 1:], image)
        assert valid[:, 1:].all() and not valid[:, 0].any()
        a = np.array([[[0., 0., 0.], [.2, .4, .6]]])
        b = np.ones_like(a)
        close(blend(a, b, np.array([[1., 1.]]), np.array([[1., 0.]])),
              [[[.5, .5, .5], [.2, .4, .6]]])
        close(blend(a, b, np.zeros((1, 2)), np.zeros((1, 2))), np.zeros_like(a))
        return True

    def check_13(self, cls):
        model = cls()
        assert model(torch.zeros(2, 3, 32, 32)).shape == (2, 3)
        assert sum(p.numel() for p in model.parameters()) == 1443, "Check kernels/channels, GAP and biases."
        assert len([m for m in model.modules() if isinstance(m, nn.Conv2d)]) == 2
        assert not any(isinstance(m, nn.Softmax) for m in model.modules()), "Return logits, not softmax."
        return model

    def check_14(self, solvers):
        step, evaluate = solvers
        seed_all()
        model = nn.Linear(2, 3)
        x = torch.tensor([[1., 2.], [2., 1.], [1., 1.]])
        y = torch.tensor([0, 1, 2])
        opt = torch.optim.SGD(model.parameters(), lr=.1)
        before = copy.deepcopy(model.state_dict())
        a = step(model, opt, x, y)
        assert np.isfinite(a) and any(not torch.equal(before[k], model.state_dict()[k]) for k in before)
        # Stale gradients must not contaminate a second, otherwise identical run.
        model2 = nn.Linear(2, 3); model2.load_state_dict(before)
        for p in model2.parameters():
            p.grad = torch.ones_like(p)*100
        step(model2, torch.optim.SGD(model2.parameters(), lr=.1), x, y)
        for p, q in zip(model.parameters(), model2.parameters()):
            torch.testing.assert_close(p, q)
        fixed = nn.Sequential(nn.Dropout(.8), nn.Linear(2, 2, bias=False))
        with torch.no_grad():
            fixed[1].weight.copy_(torch.eye(2))
        data = TensorDataset(torch.tensor([[2., 0.]]*4+[[0., 2.]]), torch.zeros(5, dtype=torch.long))
        grad_states = []
        handle = fixed.register_forward_pre_hook(lambda *_: grad_states.append(torch.is_grad_enabled()))
        result = evaluate(fixed, DataLoader(data, batch_size=4))
        handle.remove()
        assert grad_states and not any(grad_states), "Evaluation must disable gradient recording, not just set eval mode."
        close(result["accuracy"], .8)
        close(result["confusion"], [[4, 1], [0, 0]])
        assert not fixed.training and all(p.grad is None for p in fixed.parameters())
        close(result["loss"], nn.functional.cross_entropy(fixed(data.tensors[0]), data.tensors[1]).item())
        return True

    def check_15(self, fn):
        model = self.results.get("13")
        if model is None:
            raise NotImplementedError("Complete the model checkpoint first.")
        old_state = copy.deepcopy(model.state_dict())
        adapted = fn(model)
        assert adapted is not model, "Copy the source model; preserve your three-class sorter."
        assert adapted(torch.zeros(2, 3, 32, 32)).shape == (2, 2)
        assert all(not p.requires_grad for p in adapted.features.parameters())
        assert sum(p.numel() for p in adapted.parameters() if p.requires_grad) == 34
        for name, value in model.features.state_dict().items():
            torch.testing.assert_close(adapted.features.state_dict()[name], value)
        for name, value in old_state.items():
            torch.testing.assert_close(model.state_dict()[name], value)
        return adapted

    def check_16(self, fn):
        features = torch.tensor([[[[1., 2.], [3., 4.]], [[4., 3.], [2., 1.]]]])
        grads = torch.tensor([[[[1., 1.], [1., 1.]], [[-1., -1.], [-1., -1.]]]])
        close(fn(features, grads), [[0., 0.], [1/3, 1.]])
        close(fn(features, torch.zeros_like(grads)), np.zeros((2, 2)))
        return True


def final_replay(mission, colour_fn, photo_fn, height_fn, gaussian_fn, gradient_fn, frequency_fn,
                 score_fn, flow_fn, ratio_fn, robust_fn, warp_fn, blend_fn,
                 model, evaluate_fn, cam_fn):
    """Fresh calls through the visible pipeline, not just a cached PASS counter."""
    if any(mission.states.get(k) != "PASS" for k in mission.names):
        print("Final replay is locked until all 16 code checkpoints pass. No reference solution is substituted.")
        return None
    if model is None or not getattr(model, "_cv1_fitted", False):
        print("Code checks passed, but run the checkpoint 14 training cell before the final replay.")
        return None
    packet = mission.packet
    balanced = colour_fn(packet["raw"])["balanced"]
    rho, normals = photo_fn(packet["shadow"], packet["lights"], weighted=True)
    surface = height_fn(normals)
    g, _, _ = gaussian_fn(1.2, 4)
    cleaned = ndimage.correlate1d(ndimage.correlate1d(gray(balanced), g, axis=0), g, axis=1)
    gx, gy, magnitude, _ = gradient_fn(cleaned[:112, :200])
    frequency = frequency_fn(cleaned)
    gallery([balanced, rho, surface["height"], magnitude, frequency["direct"], frequency["dog"]],
            ["Your colour repair", "Your recovered albedo", "Your integrated surface",
             "Your gradient magnitude", "Your direct LoG", "Your DoG"], columns=3)
    scores = score_fn(gx, gy)
    motion = tracks(packet, scores, flow_fn)
    features = sift_pair(packet)
    pairs = ratio_fn(features["desc_a"], features["desc_b"], .75)
    matrix, inliers = robust_fn(features["a"][pairs[:, 0]], features["b"][pairs[:, 1]],
                               threshold=2., trials=200, seed=8)
    pano = panorama(packet, matrix, warp_fn, blend_fn)
    # Inspect the actual belt objects: the dataset generator also made these scene patches.
    crop_starts = [x for x in range(20, 380, 45) if x+32 <= balanced.shape[1]]
    objects = torch.tensor(np.stack([balanced[18+(i % 3)*35:50+(i % 3)*35,
                                      x:x+32].transpose(2, 0, 1)
                                     for i, x in enumerate(crop_starts)]), dtype=torch.float32)
    model.eval()
    with torch.no_grad():
        predictions = model(objects).argmax(1).numpy()
    gallery([a.permute(1, 2, 0).numpy() for a in objects],
            [f"#{i}: {LABELS[p]}" for i, p in enumerate(predictions)], columns=4, size=2)
    report = evaluate_fn(model, make_loaders()["test"])
    f, g, target = capture_cam(model, objects[:1])
    cam = cam_fn(f, g)
    gallery([objects[0].permute(1, 2, 0), cam], ["Live belt crop", f"Your CAM: {LABELS[target]}"], columns=2)
    print("Toy held-out test accuracy (final evaluation only):", round(report["accuracy"], 3))
    print("Camera-pair consensus:", int(inliers.sum()), "/", len(pairs), " | panorama:", pano.shape)
    print("Ship decision is YOURS: are calibration, motion, appearance and validation evidence adequate?")
    return dict(motion=motion, consensus=int(inliers.sum()), test=report, predictions=predictions)
