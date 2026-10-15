# /// script
# dependencies = ["numpy"]
# ///
"""Execute the sheet's NumPy recipes on synthetic data; check worked arithmetic.

No course notebook, dataset, training loop, or model download is run.
The two PyTorch listings receive syntax checks only.
"""

from __future__ import annotations

import ast
import math
from pathlib import Path
import re

import numpy as np
from numpy.lib.stride_tricks import sliding_window_view


SOURCE = Path(__file__).with_name("cv1-cheat-sheet.tex")


def close(actual, expected, *, atol=1e-9):
    np.testing.assert_allclose(actual, expected, atol=atol, rtol=1e-9)


def full_convolution(image, kernel):
    """Independent spatial reference, without FFT or sliding windows."""
    output = np.zeros(np.array(image.shape) + np.array(kernel.shape) - 1)
    for y, x in np.ndindex(image.shape):
        for a, b in np.ndindex(kernel.shape):
            output[y + a, x + b] += image[y, x] * kernel[a, b]
    return output


def iou(a, b):
    width = max(0, min(a[2], b[2]) - max(a[0], b[0]))
    height = max(0, min(a[3], b[3]) - max(a[1], b[1]))
    intersection = width * height
    aa = (a[2] - a[0]) * (a[3] - a[1])
    ab = (b[2] - b[0]) * (b[3] - b[1])
    return intersection / (aa + ab - intersection)


def verify():
    text = SOURCE.read_text()
    listings = re.findall(r"\\begin\{lstlisting\}\n(.*?)\\end\{lstlisting\}", text, re.S)
    assert len(listings) == 25, "Listing count changed; update the execution fixtures."
    for number, code in enumerate(listings, 1):
        ast.parse(code, filename=f"sheet-listing-{number}")

    executed = set()

    def run(number, **variables):
        env = {"np": np, "sliding_window_view": sliding_window_view, **variables}
        exec(compile(listings[number - 1], f"sheet-listing-{number}", "exec"), env)
        executed.add(number)
        return env

    # 1: world-to-camera projection, row-vector storage, centre and ray.
    env = run(1, Xw=np.array([[5., 1., 10.], [2., 0., 4.]]), R=np.eye(3),
              t=np.array([-2., 0., 0.]), K=np.diag([100., 100., 1.]), u=30., v=10.)
    close(env["uv"], [[30, 10], [0, 0]])
    close(env["C"], [2, 0, 0])
    close(env["ray_c"], [.3, .1, 1])
    close(env["ray_w"], [.3, .1, 1])
    assert 5 / .01 == 500

    # 2--4: channel axes, white balance, black pixels, normal and recolouring.
    image = np.array([[[4, 2, 2], [4, 2, 2]]], dtype=np.uint8)
    env = run(2, I=image, bgr=np.array([[[1, 2, 3]]]))
    close(env["mc"], [[[4, 2, 2]]])
    close(env["out"], [[[2, 2, 2], [2, 2, 2]]])
    close(env["gray"], [[3, 3]])
    close(env["rgb"], [[[3, 2, 1]]])
    close(np.array([4., 2., 2.]) * np.array([2/3, 4/3, 4/3]), [8/3]*3)
    image = np.array([[[0., 0., 0.], [1., 2., 3.]]])
    env = run(3, I=image, a=[1, 0, 0], b=[0, 1, 0], rho=.4, J=200,
              light=[math.sin(math.pi/3), 0, math.cos(math.pi/3)])
    close(env["rgbn"], [[[0, 0, 0], [1/6, 2/6, 3/6]]])
    close(env["Id"], 40)
    env = run(4, albedo=image, shading=np.array([[[.2], [.8]]]))
    close(env["recolored"], [[[0, 0, 0], [.8, 0, 0]]])

    # Section 6: explicit intensity factors, cosine clamp and light-row strengths.
    section = text.split(r"\Topic{6. Calibrated photometric stereo (Lab1)}", 1)[1]
    section = section.split(r"\Topic{7.", 1)[0]
    assert r"I_j=\rho J_j\max(0,n\trans\ell_j)" in section
    assert r"L_j=J_j\ell_j\trans" in section
    directions = np.array([[0., 0., 1.], [math.sqrt(3)/2, 0., .5],
                           [0., 1., 0.], [0., 0., -1.]])
    strengths = np.array([100., 100., 80., 40.])
    intensities = []
    for strength, direction, expected in zip(strengths, directions, [50., 25., 0., 0.]):
        env = run(3, I=image, a=[1, 0, 0], b=[0, 1, 0],
                  rho=.5, J=strength, light=direction)
        close(env["Id"], expected)
        intensities.append(env["Id"])
    light_rows = strengths[:, None] * directions
    g_pixel = np.array([0., 0., .5])
    close(light_rows[:3] @ g_pixel, intensities[:3])
    close(np.linalg.lstsq(light_rows[:3], intensities[:3], rcond=None)[0], g_pixel)
    assert light_rows[-1] @ g_pixel < 0  # back-facing clamp is not a linear equation

    # 5--7: lights-as-rows, intensity row weighting and integrable height.
    lights = np.array([[0, 0, 1], [.8, 0, .6], [0, .8, .6],
                       [-.8, 0, .6], [0, -.8, .6]])
    g = np.array([40., -60., 100.])
    observations = lights @ np.column_stack([g, [10, 20, 50]])
    env = run(5, L=lights, i=lights @ g, obs=observations)
    close(env["g"], g)
    close(env["G"], np.column_stack([g, [10, 20, 50]]))
    close(np.linalg.norm(env["normals"], axis=0), [1, 1])
    env = run(6, L=lights, i=lights @ g)
    close(env["gw"], g)
    noisy = lights @ g + np.array([1, -2, 3, -1, 2])
    weighted = run(6, L=lights, i=noisy)["gw"]
    weights = np.diag(noisy**2)
    close(lights.T @ weights @ (lights @ weighted - noisy), np.zeros(3), atol=1e-6)
    env = run(7, p=np.ones((3, 4)), q=np.full((3, 4), -.5))
    y, x = np.indices((3, 4))
    close(env["z"], x - y/2)
    close(env["curl_error"], np.zeros((3, 4)))
    n = np.array([-2., 1., 2.]) / 3
    close(np.linalg.norm(n), 1)
    close([-n[0]/n[2], -n[1]/n[2]], [1, -.5])
    close(4*1 + 2*(-.5), 3)

    # 8--10: round/floor distinction, boundary-sensitive morphology, filtering.
    env = run(8, I=np.array([[0, 0], [1, 2]]), L=4)
    close(env["cdf"], [.5, .75, 1, 1])
    close(env["lut"], [2, 2, 3, 3])  # rint and floor are distinct conventions
    close(env["h_new"], [0, 0, 3, 1])
    close(np.floor(3*env["cdf"]), [1, 2, 3, 3])
    close(np.bincount(np.array([1, 1, 2, 3]), minlength=4), [0, 2, 1, 1])
    element = np.ones((3, 3), dtype=bool)
    env = run(9, B=np.ones((5, 5), dtype=bool), K=element)
    assert env["dilated"].sum() == 25 and env["eroded"].sum() == 9
    assert run(9, B=env["eroded"], K=element)["dilated"].sum() == 25
    assert run(9, B=env["dilated"], K=element)["eroded"].sum() == 9
    env = run(10, I=np.arange(16.).reshape(4, 4), r=1, sigma=1.)
    close(env["G"].sum(), 1)
    close(env["gx"].sum(), 0)
    close(env["Jcorr"], env["Jconv"])
    ref = full_convolution(np.arange(16.).reshape(4, 4), env["G"])
    close(env["Jconv"], ref[1:5, 1:5])
    close(16*4 - .04*(16+4)**2, 48)
    close(0 - .04*25**2, -25)

    # 11--14: Fourier, broadcasting, full convolution and raw unsigned HOG.
    image = np.arange(6.).reshape(2, 3)
    env = run(11, I=image, Hc=np.ones_like(image))
    close(env["out"], image)
    close(np.fft.fft([0, 1, 0, 0]), [1, -1j, -1, 1j])
    close(np.fft.fft([2, 2, 2, 2]), [8, 0, 0, 0])
    close(np.arctan2(1, 1), math.pi/4)
    env = run(12, V=np.array([[3., 0., 4.], [0., 0., 0.], [1., 2., 2.]]),
              hwc=np.arange(18).reshape(2, 3, 3), A=np.array([[8, 1], [0, 8], [1, 2]]),
              I=np.arange(25).reshape(5, 5), y=2, x=2, r=1)
    close(env["Vunit"], [[.6, 0, .8], [0, 0, 0], [1/3, 2/3, 2/3]])
    assert env["chw"].shape == (3, 2, 3) and env["patch"].shape == (3, 3)
    close(env["rows"], [[8, 1], [0, 8]])
    kernel = np.array([[1, 2, 0], [0, -1, 1], [2, 0, 3]])
    env = run(13, I=image, K=kernel)
    ref = full_convolution(image, kernel)
    close(env["J"], ref)
    close(env["Jsame"], ref[1:3, 1:4])
    env = run(14, Ix=np.array([[3., -3.], [0., 0.]]),
              Iy=np.array([[4., -4.], [0., 0.]]))
    close(env["h"], [0, 0, 10, 0, 0, 0, 0, 0, 0])
    close(env["h_count"], [2, 0, 2, 0, 0, 0, 0, 0, 0])
    close(env["lam"], [0, 50])
    close(np.degrees(np.arctan2(4, 3)), 53.13010235415598)

    # 15--18: line TLS, RANSAC, full-SVD DLT, LK and bilinear weights.
    env = run(15, pts=np.array([[0., 1.], [1., 3.], [2., 5.], [3., 7.]]),
              p=.99, w=.5, s=4)
    close(np.array([env["a"], env["b"]]) @ np.array([[0, 1, 2, 3], [1, 3, 5, 7]])
          + env["c"], np.zeros(4))
    assert env["trials"] == 72
    assert 1-(1-.5**4)**71 < .99 <= 1-(1-.5**4)**72
    assert math.ceil(math.log1p(-.99)/math.log1p(-.5**2)) == 17
    assert math.comb(13, 3) - math.comb(10, 3) + 1 == 167
    env = run(16, Ix=np.array([[2., 0.]]), Iy=np.array([[0., 3.]]),
              It=np.array([[-4., 3.]]))
    close([env["u"], env["v"]], [2, -1])
    h_true = np.array([[1.2, .1, 2], [.2, .9, 1], [.01, .02, 1]])
    rows = []
    for x, y in [[0, 0], [1, 0], [1, 1], [0, 1]]:
        q = h_true @ [x, y, 1]
        u, v = q[:2]/q[2]
        rows.extend([[x, y, 1, 0, 0, 0, -u*x, -u*y, -u],
                     [0, 0, 0, x, y, 1, -v*x, -v*y, -v]])
    env = run(17, A=np.array(rows), x=.25, y=.5)
    close(env["H"]/env["H"][2, 2], h_true)
    q = h_true @ [.25, .5, 1]
    close(env["uv"], q[:2]/q[2])
    env = run(18, xs=np.array(.25), ys=np.array(.5), I=np.array([[0., 10.], [20., 30.]]))
    close(env["val"], 12.5)

    # 19--20: E/F convention, rectified depth/uncertainty and triangulation.
    k = np.array([[800., 0., 320.], [0., 800., 240.], [0., 0., 1.]])
    translation = np.array([-.1, 0., 0.])
    essential = np.array([[0., 0., 0.], [0., 0., .1], [0., -.1, 0.]])
    env = run(19, K1=k, K2=k, E=essential, u1=400., v1=260., u2=380., v2=260.,
              f=800., B=.1, disparity=20., sigma_d=.5)
    close(env["dist"], 0)
    close(env["Z"], 4)
    close(env["sigma_Z"], .1)
    assert np.linalg.matrix_rank(env["F"]) == 2
    close(np.linalg.svd(essential)[1], [.1, .1, 0])
    p1 = k @ np.column_stack([np.eye(3), np.zeros(3)])
    p2 = k @ np.column_stack([np.eye(3), translation])
    env = run(20, P1=p1, P2=p2, u1=400., v1=260., u2=380., v2=260.)
    close(env["X"], [.4, .1, 4])
    close(env["err"], 0)

    # 21--22 and 24: k-means empty-cluster policy, AP conventions, stable CE.
    env = run(21, X=np.array([[0., 0.], [.2, 0.], [2., 1.], [2., 3.]]),
              centres=np.array([[0., 0.], [2., 2.], [10., 10.]]))
    close(env["new"], [[.1, 0], [2, 2], [10, 10]])
    close(env["hist"], [2, 2, 0])
    env = run(22, tp=[0, 1, 1], G=2)
    close(env["ap_raw"], 7/12)
    close(env["ap_interp"], 2/3)
    close(run(22, tp=[1, 0, 1], G=3)["ap_raw"], 5/9)
    for offset in [0., 1000.]:
        env = run(24, logits=np.array([offset, offset]), y=0)
        close(env["ce"], math.log(2))
        close(env["dz"], [-.5, .5])
    assert executed == set(range(1, 26)) - {23, 25}

    # Independent finite differences for the tiny CNN backpropagation example.
    x = np.array([[0., -1., 3.], [2., .5, 1.]])
    w = np.array([[0., 1.], [1., .5]])

    def forward(xx, ww, bias=0.):
        return np.array([(xx[:, j:j+2] * ww).sum() + bias for j in range(2)])

    close(forward(x, w), [1.25, 4])
    gradients = []
    for variable in [x, w]:
        numerical = np.zeros_like(variable)
        for index in np.ndindex(variable.shape):
            original = variable[index]
            variable[index] = original + 1e-5
            plus = forward(x, w).sum()
            variable[index] = original - 1e-5
            minus = forward(x, w).sum()
            variable[index] = original
            numerical[index] = (plus-minus)/2e-5
        gradients.append(numerical)
    close(gradients[0], [[0, 1, 1], [1, 1.5, .5]], atol=1e-8)
    close(gradients[1], [[-1, 2], [2.5, 1.5]], atol=1e-8)
    close((forward(x, w, 1e-5).sum()-forward(x, w, -1e-5).sum())/2e-5, 2)

    # Parameter/shape/RF, detection geometry, box decoding and metric examples.
    assert (32-5)//1 + 1 == 28 and (32-5)//3 + 1 == 10
    assert 5*5*3*8 == 600 and (5*5*3+1)*8 == 608
    assert 28*28*8*5*5*3 == 470400 and (28*28*8+1)*10 == 62730
    assert (256+1)*(18+36) == 13878 and 20*20*9 == 3600
    assert 7*(512+1) == 3591 and 1000*(512+1) == 513000
    assert 32*(192+1) == 6176 and 7*7*(5*2+20) == 1470
    r, jump = 1, 1
    for kernel, stride in [(3, 1), (2, 2), (3, 1)]:
        r, jump = r + (kernel-1)*jump, jump*stride
    assert (r, jump) == (8, 2)
    boxes = [(0, 0, 4, 2), (1, 0, 5, 2), (2, 0, 6, 2)]
    close([iou(boxes[0], boxes[1]), iou(boxes[1], boxes[2]), iou(boxes[0], boxes[2])],
          [.6, .6, 1/3])
    kept = []
    for candidate in range(3):  # already descending score
        if all(iou(boxes[candidate], boxes[k]) <= .5 for k in kept):
            kept.append(candidate)
    assert kept == [0, 2]
    tp, fp, fn, tn = 6, 2, 4, 8
    close([tp/(tp+fp), tp/(tp+fn), 2*tp/(2*tp+fp+fn), (tp+tn)/20], [.75, .6, 2/3, .7])
    close((tp+tn+80)/100, .94)
    close([tp/(tp+fp+fn), 2*tp/(2*tp+fp+fn)], [.5, 2/3])

    # Requested revision: S1 Q5c--f, with the seminar's stated rounding rule.
    histogram = np.array([900, 800, 700, 600, 500, 400, 300, 200])
    env = run(8, I=np.repeat(np.arange(8), histogram), L=8)
    assert histogram.sum() == 4400
    close(7*env["cdf"], [1.431818181818, 2.704545454545, 3.818181818182,
                         4.772727272727, 5.568181818182, 6.204545454545,
                         6.681818181818, 7])
    close(env["lut"], [1, 3, 4, 5, 6, 6, 7, 7])
    close(env["h_new"], [0, 900, 0, 800, 700, 600, 900, 500])
    patch = np.array([
        [1, 1, 1, 3, 3, 4, 4, 1], [4, 0, 0, 5, 1, 2, 0, 1],
        [0, 1, 3, 1, 2, 0, 2, 0], [3, 1, 2, 2, 2, 1, 1, 2],
        [1, 4, 2, 2, 2, 3, 5, 3], [0, 2, 1, 0, 2, 1, 3, 0],
        [0, 2, 1, 1, 0, 0, 4, 1], [0, 4, 0, 0, 0, 2, 1, 1],
    ])
    env = run(8, I=patch, L=8)
    close(env["h"], [16, 19, 14, 7, 6, 2, 0, 0])
    close(env["lut"], [2, 4, 5, 6, 7, 7, 7, 7])
    close(env["h_new"], [0, 0, 16, 0, 19, 14, 7, 8])
    close(env["J"][0], [4, 4, 4, 6, 6, 7, 7, 4])
    assert env["h_new"].sum() == patch.size

    # S3 Q2a--d: independent correlation differences at the nine interior pixels.
    patch = np.array([[1, 1, 1, 1, 1], [1, 1, 1, 1, 0], [1, 1, 1, 0, 0],
                      [1, 1, 0, 0, 0], [1, 0, 0, 0, 0]], dtype=float)
    gx, gy = np.zeros((3, 3)), np.zeros((3, 3))
    for y, x in np.ndindex(3, 3):
        gx[y, x] = patch[y+1, x] - patch[y+1, x+2]
        gy[y, x] = patch[y, x+1] - patch[y+2, x+1]
    close(gx, [[0, 0, 1], [0, 1, 1], [1, 1, 0]])
    close(gy, gx)
    env = run(14, Ix=gx, Iy=gy)
    close(env["mag"], np.sqrt(2)*gx)
    close(env["h_count"], [4, 0, 5, 0, 0, 0, 0, 0, 0])
    close(env["h"], [0, 0, 5*np.sqrt(2), 0, 0, 0, 0, 0, 0])
    count_valid = np.histogram(env["ang"][env["mag"] > 0], env["bins"])[0]
    close(count_valid, [0, 0, 5, 0, 0, 0, 0, 0, 0])
    close(run(14, Ix=-gx, Iy=-gy)["h"], env["h"])
    close(run(14, Ix=2*gx, Iy=2*gy)["h"], 2*env["h"])
    close(run(14, Ix=2*gx, Iy=2*gy)["h_count"], env["h_count"])

    # Standard gradient kernels and low/high/band-pass examples.
    y, x = np.indices((5, 5))
    ramp = x + 2*y
    windows = sliding_window_view(ramp, (3, 3))
    sobel = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    prewitt = np.array([[-1, 0, 1]]*3)
    close(np.einsum("yxab,ab->yx", windows, sobel), np.full((3, 3), 8))
    close(np.einsum("yxab,ab->yx", windows, sobel.T), np.full((3, 3), 16))
    close(np.einsum("yxab,ab->yx", windows, prewitt), np.full((3, 3), 6))
    close(np.einsum("yxab,ab->yx", windows, prewitt.T), np.full((3, 3), 12))
    low = np.ones((3, 3))/9
    high = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
    close(low.sum(), 1)
    close(high.sum(), 0)
    omega = np.array([0., 1., 100.])
    band = np.exp(-omega**2/2) - np.exp(-4*omega**2/2)  # sigma1=1, sigma2=2
    close(band[[0, 2]], [0, 0])
    assert band[1] > 0

    # S3 Q3: arithmetic behind illumination invariance and descriptor votes.
    def gaussian(sigma):
        grid = np.arange(-2, 3, dtype=float)
        g = np.exp(-grid**2/(2*sigma**2))
        g /= g.sum()
        return np.outer(g, g)

    y, x = np.indices((15, 15))
    blob = np.exp(-((x-7)**2+(y-7)**2)/(2*1.1**2))
    dog = gaussian(1.3)-gaussian(.9)
    response = np.einsum("yxab,ab->yx", sliding_window_view(blob, (5, 5)), dog)
    transformed = np.einsum("yxab,ab->yx", sliding_window_view(3*blob+5, (5, 5)), dog)
    close(transformed, 3*response)
    assert np.argmin(transformed) == np.argmin(response)
    raw = np.r_[1000., np.ones(127)]

    def descriptor_normalization(vector):
        vector = vector/np.linalg.norm(vector)
        vector = np.minimum(vector, .2)
        return vector/np.linalg.norm(vector)

    close(descriptor_normalization(raw), descriptor_normalization(3*raw))
    assert 4*4*8 == 128
    fraction = (60-45)/(90-45)
    close([6*(1-fraction), 6*fraction], [4, 2])
    close((150-90) % 360, 60)

    # Exact trig table, S4 Q4c class--box counts, and stride speed-up counts.
    angles = np.deg2rad([0, 30, 45, 60, 90])
    close(np.sin(angles), [0, .5, np.sqrt(2)/2, np.sqrt(3)/2, 1])
    close(np.cos(angles), [1, np.sqrt(3)/2, np.sqrt(2)/2, .5, 0])
    assert 9*3*4 == 108 and 9*3*4*5 == 540
    assert ((28-14)//2+1)**2*5 == 320
    assert ((28+2*2-14)//2+1)**2*5 == 500
    assert ((28-14)//2+1)**2 < ((28-14)//1+1)**2
    print("Verified 23 NumPy listings, 2 syntax-only PyTorch listings, worked arithmetic, "
          "and the requested seminar examples.")


if __name__ == "__main__":
    verify()
