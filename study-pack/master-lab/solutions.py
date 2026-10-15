"""SPOILERS: reference implementations for the 16 notebook checkpoints.

Not imported by the learner notebook. Try each checkpoint before opening this.
These are authored teaching solutions, not official course-lab answers.
"""
import copy

import numpy as np
from scipy import ndimage, signal
import torch
from torch import nn

from mission_support import sample_bilinear


def colour_tools(rgb):
    rgb = np.asarray(rgb, dtype=float)
    total = rgb.sum(axis=-1, keepdims=True)
    nrgb = np.divide(rgb, total, out=np.zeros_like(rgb), where=total > 0)
    means = rgb.mean(axis=(0, 1), keepdims=True)
    gains = np.divide(means.mean(), means, out=np.zeros_like(means), where=means > 0)
    r, g, b = np.moveaxis(rgb, -1, 0)
    return dict(lightness=(rgb.max(-1)+rgb.min(-1))/2, nrgb=nrgb,
                opponent=np.stack([(r-g)/np.sqrt(2), (r+g-2*b)/np.sqrt(6), (r+g+b)/np.sqrt(3)], -1),
                balanced=rgb*gains)


def recolour(albedo, shading, mask, target):
    changed = np.asarray(albedo, float).copy()
    changed[mask] = target
    return changed*np.asarray(shading)[..., None]


def photometric(images, lights, weighted=False):
    images = np.asarray(images, float)
    m, h, w = images.shape
    observed = images.reshape(m, -1)
    if weighted:
        g = np.column_stack([np.linalg.lstsq(i[:, None]*lights, i*i, rcond=None)[0]
                             for i in observed.T])
    else:
        g = np.linalg.lstsq(lights, observed, rcond=None)[0]
    rho = np.linalg.norm(g, axis=0)
    n = np.divide(g, rho[None, :], out=np.zeros_like(g), where=rho[None, :] > 0)
    return rho.reshape(h, w), n.T.reshape(h, w, 3)


def integrate(normals):
    nz = normals[..., 2]
    if np.any(np.abs(nz) < 1e-8):
        raise ValueError("Height graph fails near vertical/invalid normals; mask these first.")
    p, q = -normals[..., 0]/nz, -normals[..., 1]/nz
    z = np.zeros_like(p)
    z[0, 1:] = np.cumsum(p[0, :-1])
    for y in range(1, len(z)):
        z[y] = z[y-1] + q[y-1]
    curl = np.gradient(p, axis=0)-np.gradient(q, axis=1)
    return dict(height=z, curl=curl)


def gaussian1d(sigma=1.2, radius=4):
    x = np.arange(-radius, radius+1, dtype=float)
    g = np.exp(-x*x/(2*sigma*sigma))
    g /= g.sum()
    return g, -x/sigma**2*g, (x*x/sigma**4-1/sigma**2)*g


def gradients(image):
    image = np.asarray(image, dtype=float)
    sx = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]], dtype=float)/8
    gx = signal.correlate2d(image, sx, mode="same", boundary="symm")
    gy = signal.correlate2d(image, sx.T, mode="same", boundary="symm")
    return gx, gy, np.hypot(gx, gy), np.arctan2(gy, gx)


def frequency_maps(image, sigma=1.2, k=1.6, radius=4):
    g, _, _ = gaussian1d(sigma, radius)
    G = np.outer(g, g)
    correlate = lambda a, b: signal.correlate2d(a, b, mode="same", boundary="symm")
    laplacian = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
    sequential = correlate(correlate(image, G), laplacian)
    y, x = np.mgrid[-radius:radius+1, -radius:radius+1]
    log_kernel = (x*x+y*y-2*sigma*sigma)/sigma**4*G
    log_kernel -= log_kernel.mean()  # remove finite-truncation DC response
    direct = correlate(image, log_kernel)
    wide, _, _ = gaussian1d(k*sigma, radius)
    dog = correlate(image, np.outer(wide, wide))-correlate(image, G)
    return dict(sequential=sequential, direct=direct, dog=dog)


def structure_scores(gx, gy, window=5, k=.04):
    aggregate = lambda a: ndimage.uniform_filter(a, size=window, mode="reflect")*window**2
    a, b, c = aggregate(gx*gx), aggregate(gx*gy), aggregate(gy*gy)
    trace, determinant = a+c, a*c-b*b
    small = (trace-np.sqrt(np.maximum((a-c)**2+4*b*b, 0)))/2
    return dict(shi=small, harris=determinant-k*trace**2)


def lk_patch(gx, gy, it, min_eigenvalue=1e-5):
    A = np.column_stack([gx.ravel(), gy.ravel()])
    if np.linalg.eigvalsh(A.T@A)[0] < min_eigenvalue:
        return np.full(2, np.nan)
    return np.linalg.lstsq(A, -it.ravel(), rcond=None)[0]


def ratio_matches(a, b, threshold=.75):
    if len(b) < 2:
        return np.empty((0, 2), dtype=int)
    distance2 = np.maximum((a*a).sum(1)[:, None]+(b*b).sum(1)[None, :]-2*a@b.T, 0)
    order = np.argsort(distance2, axis=1)[:, :2]
    first = distance2[np.arange(len(a)), order[:, 0]]
    second = distance2[np.arange(len(a)), order[:, 1]]
    keep = (second > 0) & (first < threshold**2*second)
    return np.column_stack([np.flatnonzero(keep), order[keep, 0]])


def fit_affine(src, dst):
    design = np.column_stack([src, np.ones(len(src))])
    if np.linalg.matrix_rank(design) < 3:
        raise ValueError("Need three noncollinear source points.")
    return np.linalg.lstsq(design, dst, rcond=None)[0].T


def ransac_affine(src, dst, threshold=2., trials=200, seed=8):
    rng = np.random.default_rng(seed)
    design = np.column_stack([src, np.ones(len(src))])
    best = np.zeros(len(src), dtype=bool)
    if len(src) < 3:
        raise ValueError("Need at least three correspondences.")
    for _ in range(trials):
        indices = rng.choice(len(src), 3, replace=False)
        try:
            matrix = fit_affine(src[indices], dst[indices])
        except ValueError:
            continue
        inliers = np.linalg.norm(design@matrix.T-dst, axis=1) <= threshold
        if inliers.sum() > best.sum():
            best = inliers
    if best.sum() < 3:
        raise ValueError("No usable consensus.")
    matrix = fit_affine(src[best], dst[best])
    inliers = np.linalg.norm(design@matrix.T-dst, axis=1) <= threshold
    return matrix, inliers


def inverse_warp(image, matrix, output_shape):
    y, x = np.indices(output_shape)
    destination = np.stack([x.ravel(), y.ravel(), np.ones(x.size)])
    source = np.linalg.inv(np.vstack([matrix, [0, 0, 1]]))@destination
    xs, ys = source[0].reshape(output_shape), source[1].reshape(output_shape)
    return sample_bilinear(np.asarray(image, float), xs, ys)


def feather_blend(a, b, wa, wb):
    total = wa+wb
    if a.ndim == 3:
        wa, wb, total = wa[..., None], wb[..., None], total[..., None]
    return np.divide(a*wa+b*wb, total, out=np.zeros_like(a, dtype=float), where=total > 0)


class Sorter(nn.Module):
    def __init__(self):
        super().__init__()
        self.features = nn.Sequential(nn.Conv2d(3, 8, 3, padding=1), nn.ReLU(), nn.MaxPool2d(2),
                                      nn.Conv2d(8, 16, 3, padding=1), nn.ReLU(), nn.MaxPool2d(2))
        self.classifier = nn.Linear(16, 3)

    def forward(self, x):
        return self.classifier(self.features(x).mean(dim=(2, 3)))


def train_step(model, optimizer, x, y):
    model.train()
    optimizer.zero_grad()
    loss = nn.functional.cross_entropy(model(x), y)
    loss.backward()
    optimizer.step()
    return float(loss.detach())


def evaluate(model, loader):
    model.eval()
    total, correct, loss_sum, confusion = 0, 0, 0., None
    with torch.no_grad():
        for x, y in loader:
            logits = model(x)
            pred = logits.argmax(1)
            if confusion is None:
                confusion = np.zeros((logits.shape[1], logits.shape[1]), dtype=int)
            np.add.at(confusion, (y.numpy(), pred.numpy()), 1)
            total += len(y)
            correct += int((pred == y).sum())
            loss_sum += float(nn.functional.cross_entropy(logits, y, reduction="sum"))
    return dict(accuracy=correct/total, loss=loss_sum/total, confusion=confusion)


def transfer_head(source):
    adapted = copy.deepcopy(source)
    for parameter in adapted.features.parameters():
        parameter.requires_grad_(False)
    adapted.classifier = nn.Linear(16, 2)
    return adapted


def cam_map(features, gradients):
    weights = gradients.mean(dim=(2, 3), keepdim=True)
    cam = torch.relu((weights*features).sum(dim=1))[0].detach().numpy()
    scale = cam.max()-cam.min()
    return (cam-cam.min())/scale if scale > 0 else np.zeros_like(cam)
