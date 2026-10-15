"""Authoring source. Rebuild only an unchanged template, never a learner's edits."""
from __future__ import annotations

import argparse
import ast
import hashlib
import json
from pathlib import Path
import textwrap

import nbformat as nbf
from instructional_notes import NOTES

HERE = Path(__file__).resolve().parent


def digest(notebook):
    content = [(c.cell_type, c.source, c.metadata.get("exercise_id")) for c in notebook.cells]
    return hashlib.sha256(json.dumps(content, ensure_ascii=False).encode()).hexdigest()


def make_notebook():
    cells = []

    def md(source):
        cells.append(nbf.v4.new_markdown_cell(textwrap.dedent(source).strip()))

    def code(source, **metadata):
        source = textwrap.dedent(source).strip()
        ast.parse(source)  # Catch template escaping/indentation errors before writing a notebook.
        cells.append(nbf.v4.new_code_cell(source, metadata=metadata))

    def exercise(key, text, stub, check):
        heading, body = textwrap.dedent(text).strip().split("\n", 1)
        md(heading + "\n\n" + NOTES[key] + "\n\n#### Your implementation\n\n" + body.strip())
        code(stub, exercise_id=key, tags=["exercise", f"checkpoint-{key}"])
        code(check, tags=["check", f"checkpoint-{key}"])

    md("""
    # Night Shift: get the recycling line moving again
    **One notebook · five labs · 16 short checkpoints · CPU only**

    The lights have changed, one inspection camera is noisy, the belt-speed sensor is down,
    and the sorter needs a new routing rule. You have one shift to recover the inspection pipeline.

    **Your deliverable:** corrected images → surface inspection → motion estimate → stitched belt map
    → a trained three-class sorter → a two-route adapted model → an attention audit.

    This is a **generated teaching simulator**, not photographs or a physically validated robot.
    Objects are geometric proxies for cardboard tiles, caps and cans. Main data, labels and lighting
    are created locally; no model weights, videos or datasets are downloaded. A final optional cell
    can open one existing course photograph to expose the domain gap.

    | Station | You build | Original lab | Suggested active time |
    |---|---|---|---|
    | [1. Fix the inspection booth](#booth) | Colour, intrinsic layers, normals, height | Lab1 | 30–40 min |
    | [2. Clean the signal](#signal) | Gaussian derivatives, gradients, LoG/DoG | Lab2 | 25–35 min |
    | [3. Recover belt motion](#motion) | Features, Lucas–Kanade; RAFT reading | Lab3 | 20–30 min |
    | [4. Build a common map](#map) | SIFT matches, affine RANSAC, warping, blending | Lab4 | 30–40 min |
    | [5. Teach and audit the sorter](#sorter) | CNN, training, transfer, Grad-CAM | Lab5 | 35–45 min |

    Times are estimates, not a deadline. Skip the optional ablations on a first pass.
    No installation essays, video codecs, long training runs or repeated plotting boilerplate.
    """)
    md("""
    ## Start here
    Launch instructions and coverage details are in `README.md` beside this notebook. Save a copy as
    `my-master-lab.ipynb` before working. **Edit only the exercise cells and your short answers.**
    Run a challenge's check cell after editing. `TODO` or `CHECK FAILED` is not a pass; it does not
    prevent you trying another station. Later stations start from clearly labelled supplied captures,
    not silently inserted solutions. The final replay uses your implementations and stays locked
    until all 16 code checkpoints pass. Restart and Run All before trusting the final score.

    Allowed: NumPy, the named SciPy operations, PyTorch and the supplied plotting/interpolation helpers.
    Implement the requested algorithm; don't replace it with a high-level solver that bypasses it.
    Mathematical `lstsq` is allowed. Reference answers are **separate** in `solutions.py` and
    `SOLUTIONS.md`; this notebook never imports them.

    **Conventions:** RGB float `[0,1]`, HWC arrays; gray images HW; tensor images NCHW.
    Arrays use `I[y,x]`; coordinates and flows are `(x,y)` and `(u,v)` with y down.
    The height graph uses `n ∝ [-p,-q,1]`, hence `p=-nx/nz`, `q=-ny/nz`.
    Lab1's printed positive ratios conflict with HC2a; do not mix the two conventions.
    """)
    code("""
    from pathlib import Path
    import copy
    import sys
    import numpy as np
    import matplotlib.pyplot as plt
    import cv2
    from scipy import ndimage, signal
    import torch
    from torch import nn
    from torch.utils.data import DataLoader, TensorDataset

    get_ipython().run_line_magic('matplotlib', 'inline')
    candidates = [Path.cwd(), Path.cwd() / 'study-pack' / 'master-lab']
    LAB_DIR = next((p for p in candidates if (p / 'mission_support.py').is_file()), None)
    if LAB_DIR is None:
        raise RuntimeError('Open from the course root or study-pack/master-lab; see README.md.')
    sys.path.insert(0, str(LAB_DIR.resolve()))
    import mission_support as support
    from mission_support import sample_bilinear
    mission = support.Mission()
    packet = mission.packet
    print(f'CPU | NumPy {np.__version__} | OpenCV {cv2.__version__} | PyTorch {torch.__version__}')
    print('No course files are changed. All main captures are generated locally.')
    support.gallery([packet['raw'], packet['view_a'], packet['view_b']],
                    ['Colour-cast inspection feed', 'Belt camera A', 'Belt camera B'])
    """)
    md("""
    <a id="booth"></a>
    ## 1 — Fix the inspection booth
    The surface-inspection booth stops the belt and takes seven fixed-view images under calibrated lights.
    The later motion/camera-pair captures are **different acquisitions**, not moving photometric-stereo inputs.
    """)
    exercise("01", r"""
    ### 01 · The magenta mystery [Lab1 colour/constancy]
    Write `colour_tools(rgb)`, returning a dict:
    - `lightness`: `(max(R,G,B)+min(R,G,B))/2`, shape HW.
    - `nrgb`: each pixel divided by its channel sum; black pixels stay zero.
    - `opponent`: `(R-G)/sqrt(2)`, `(R+G-2B)/sqrt(6)`, `(R+G+B)/sqrt(3)`, stacked HWC.
    - `balanced`: Grey-World correction; spatial channel means to their common mean. Zero-mean channels stay zero.

    Work in float, **do not clip or quantize intermediate results**. Clip only for display if necessary.
    The calibration strip is neutral gray in the generator.
    **Your call:** would Grey-World still be a good assumption if the whole view were brown cardboard?
    <details><summary>Hint</summary>

    Channel means use axes `(0,1)`, per-pixel channel sums use `-1`.
    `keepdims=True` keeps broadcasting honest. Use `np.divide(..., where=...)` for zeros.

    </details>
    """, """
    def colour_tools(rgb):
        # Return dict(lightness=..., nrgb=..., opponent=..., balanced=...).
        raise NotImplementedError('01: channel axes and colour correction')
    """, """
    colour = mission.run('01', colour_tools)
    if colour is not None:
        support.gallery([packet['raw'], np.clip(colour['balanced'],0,1), colour['nrgb']],
                        ['Before', 'Your Grey-World correction', 'Your normalized RGB'])
        support.colour_views(np.clip(colour['balanced'],0,1))
    """)
    exercise("02", """
    ### 02 · Repaint the material, not the shadows [Lab1 intrinsic images]
    The simulator supplies material RGB `albedo`, gray `shading` and an explicit object `mask`.
    Implement `recolour`: copy albedo, replace it by `target` **only inside the mask**, then reconstruct
    with `I=A*S` (broadcast shading to HWC). Do not infer a mask from black pixels.
    **Predict first:** if shading doubles, what happens to every nonzero reconstructed channel?
    """, """
    def recolour(albedo, shading, mask, target):
        raise NotImplementedError('02: preserve shading and outside-mask material')
    """, """
    recoloured = mission.run('02', recolour)
    if recoloured is not None:
        support.gallery([packet['albedo']*packet['shading'][...,None], packet['shading'], recoloured],
                        ['Original rendering', 'Unchanged shading', 'Your recoloured object'])
    """)
    exercise("03", r"""
    ### 03 · Is that can dented? [Lab1 photometric stereo]
    `images` is `(m,H,W)`, lights `L` is `(m,3)`. Solve `i=L@g`, `g=rho*n` per pixel.
    Return `(rho, normals)` of shapes HW and HWC. For zero rho return a zero normal, not NaN.
    Unweighted mode can solve all pixels at once with `lstsq`.

    Also implement Lab1's shadow weighting: solve `diag(i) @ L @ g = diag(i) @ i` per pixel.
    It minimizes residuals with weights **i²**, not i. Loops over pixels are fine for weighted mode.
    This rig uses linear radiometry and rank-3 lights; valid clean dot products are positive.
    **Your call:** the table compares shadow and specular corruption. Why can weighting help one and hurt the other?
    For RGB, repeat the fit per channel. A zero-reflectance channel cannot supply a normal direction:
    mask it or use a valid shared-geometry estimate, rather than divide by zero.
    <details><summary>Hint</summary>

    Reshape observations to `(m,H*W)`. Normalize g along its 3-vector axis,
    not by one norm of the entire image. Extra images cannot fix rank-deficient lighting.

    </details>
    """, """
    def photometric(images, lights, weighted=False):
        raise NotImplementedError('03: least squares, albedo, unit normals and weights')
    """, """
    surface = mission.run('03', photometric)
    if surface is not None:
        rho, normals = surface
        support.gallery([rho, (normals+1)/2, packet['shadow'][1]],
                        ['Your albedo', 'Your normals encoded as RGB', 'One damaged exposure'])
        support.photo_summary(packet, photometric)
        rgb_burst = packet['burst'][...,None]*np.array([.7,.4,0.])
        rgb_fits = [photometric(rgb_burst[...,c],packet['lights']) for c in range(3)]
        print('RGB channel mean albedos (blue is deliberately black):',[round(r.mean(),3) for r,n in rgb_fits])
        print('Blue-channel normal is invalid, even though other channels observe the surface.')
    """)
    exercise("04", r"""
    ### 04 · Normals are not a height map [Lab1 integration]
    Use `p=-nx/nz`, `q=-ny/nz`, unit grid spacing, anchor `z[0,0]=0`.
    Integrate **across the top row**, then **down each column** using outgoing/left differences:
    `z[0,x+1]=z[0,x]+p[0,x]`; `z[y+1,:]=z[y,:]+q[y,:]`.
    Return `dict(height=z, curl=dp/dy-dq/dx)`. Use `np.gradient(..., axis=...)` for the curl diagnostic.
    The supplied normals have nonzero nz; a real vertical/invalid normal needs masking.
    Central-difference slopes and this one-sided sum use different discretizations: even clean height is approximate.
    **Predict first:** a plane with p=1,q=-.5 rises by how much over dx=4,dy=2?
    **Your call:** why can the opposite integration path disagree on a noisy field? Which height ambiguity remains?
    """, """
    def integrate(normals):
        raise NotImplementedError('04: slopes, path and mixed derivatives')
    """, """
    relief = mission.run('04', integrate)
    if relief is not None:
        support.gallery([packet['height']-packet['height'][0,0], relief['height'], relief['curl']],
                        ['Generated height, same anchor', 'Your path integral', 'Integrability residual'])
    """)
    md("""
    <a id="signal"></a>
    ## 2 — Clean the signal, keep the edges
    A supplied noisy belt capture lets you continue even if the booth is unfinished. You will build the
    filters, not write another plotting framework. Noise-removal comparisons here are a short supporting
    experiment; the original lab's long optional noise/PSNR/Gabor sweeps are omitted.
    """)
    exercise("05", r"""
    ### 05 · Build one useful filter family [Lab2 Gaussian construction]
    For `x=-radius..radius`, sample `g=exp(-x**2/(2*sigma**2))` and normalize its actual sum.
    Return `(g, dg, ddg)` with `dg=-(x/sigma**2)*g`, `ddg=(x**2/sigma**4-1/sigma**2)*g`.
    These derivatives use the sampled normalized g; do **not** normalize derivatives to sum 1.
    **Your call:** why do two 1D passes equal an outer-product 2D filter? Compare K² and 2K work/pixel.
    """, """
    def gaussian1d(sigma=1.2, radius=4):
        raise NotImplementedError('05: normalized Gaussian and its derivatives')
    """, """
    kernels = mission.run('05', gaussian1d)
    if kernels is not None:
        g, dg, ddg = kernels
        image = packet['noisy']
        smooth = ndimage.correlate1d(ndimage.correlate1d(image,g,axis=0),g,axis=1)
        direct = signal.correlate2d(image,np.outer(g,g),mode='same',boundary='symm')
        print('Largest direct/separable difference:', np.max(np.abs(smooth-direct)))
        support.gallery([packet['clean'], image, smooth, ndimage.median_filter(image,3)],
                        ['Clean teaching target', 'Noisy', 'Your Gaussian', 'Supplied median comparison'], columns=4)
        plt.figure(figsize=(7,2)); plt.plot(g,label='g'); plt.plot(dg,label="g′"); plt.plot(ddg,label="g″")
        plt.legend(); plt.show()
    """)
    exercise("06", r"""
    ### 06 · How strong is the edge? [Lab2 gradients]
    Return `(gx, gy, magnitude, angle_radians)`. Use **cross-correlation** with
    `sx=[[-1,0,1],[-2,0,2],[-1,0,1]]/8`, `sy=sx.T`, same output, symmetric boundaries.
    `signal.correlate2d` is allowed; a built-in Sobel/gradient routine is not the implementation here.
    Cast to float first. Magnitude is `sqrt(gx**2+gy**2)` **per pixel**; angle is `atan2(gy,gx)`.
    Do not min-max normalize derivatives used in calculations; normalize only visualizations.
    **Predict:** on `I=x+2y`, what are gx,gy away from the boundary? Is gradient direction along or across an edge?
    """, """
    def gradients(image):
        raise NotImplementedError('06: signed derivatives, magnitude and quadrant-safe angle')
    """, """
    edges = mission.run('06', gradients)
    if edges is not None:
        gx, gy, magnitude, angle = edges
        support.gallery([gx,gy,magnitude,angle],['gx','gy','Gradient magnitude','Angle (radians)'],columns=4)
    """)
    exercise("07", r"""
    ### 07 · Same edge, three routes [Lab2 LoG/DoG]
    Return `dict(sequential=..., direct=..., dog=...)`, all HW, same symmetric boundaries.
    Reuse your `gaussian1d`; use `signal.correlate2d`, not a built-in LoG.
    1. Gaussian smooth, then correlate with `[[0,1,0],[1,-4,1],[0,1,0]]`.
    2. Make `G=outer(g,g)`, then sampled LoG `((x**2+y**2-2*sigma**2)/sigma**4)*G`.
       Subtract the sampled kernel's mean to correct its finite-support DC leakage; correlate directly.
    3. Smooth at sigma and k*sigma on the same support, then **wide minus narrow**.
    **Your call:** which is low-/high-/band-pass? Why aren't these three sampled responses exactly equal?
    For k close to 1, divide DoG by `(k-1)*sigma**2` to compare with LoG; don't compare unscaled amplitudes.
    """, """
    def frequency_maps(image, sigma=1.2, k=1.6, radius=4):
        raise NotImplementedError('07: sequential/direct LoG and two-scale DoG')
    """, """
    frequency = mission.run('07', frequency_maps)
    if frequency is not None:
        support.gallery(list(frequency.values()), list(frequency.keys()))
    """)
    md("""
    <a id="motion"></a>
    ## 3 — The speed sensor is down
    Two supplied gray frames move the same belt by a small displacement. Derivatives for the LK
    equations are supplied from smoothed frames so filtering mistakes do not block this station.
    Station 2 still builds and checks your own gradient implementation.
    """)
    exercise("08", r"""
    ### 08 · Pick a point that can actually be tracked [Lab3 features]
    Form local **sums** `a=sum(gx²), b=sum(gx*gy), c=sum(gy²)` in a window.
    Allowed aggregation: `ndimage.uniform_filter(...,window,mode='reflect')*window**2`.
    Return `dict(shi=lambda_min, harris=det(M)-k*trace(M)**2)` over the full image,
    where `M=[[a,b],[b,c]]` and `lambda_min=(a+c-sqrt((a-c)**2+4*b**2))/2`.
    **Predict:** flat region, straight edge, textured corner—which has two useful eigenvalues?
    This compresses the original optional feature warm-up into a dependency for mandatory LK.
    """, """
    def structure_scores(gx, gy, window=5, k=.04):
        raise NotImplementedError('08: second moments and corner scores')
    """, """
    corners = mission.run('08', structure_scores)
    if corners is not None:
        support.gallery([packet['frame0'],corners['shi'],corners['harris']],
                        ['Choose reliable points', 'Shi–Tomasi', 'Harris'])
    """)
    exercise("09", r"""
    ### 09 · Recover belt speed [Lab3 Lucas–Kanade]
    Assume constant local flow. Flatten the patch; A has rows `[gx,gy]`, b=`-it`.
    If `eigvalsh(A.T@A)[0] < min_eigenvalue`, return `[nan,nan]`: reject unobservable motion.
    Otherwise return least-squares `(u,v)` in **pixels/frame**, no visualization scale factor.
    `it` is second-minus-first intensity, not the other sign.
    **Your call:** larger windows add equations, but what can go wrong at a motion boundary?
    A quarter-resolution `(u,v)=(2,-1)` is what displacement at original resolution?
    """, """
    def lk_patch(gx, gy, it, min_eigenvalue=1e-5):
        raise NotImplementedError('09: observable 2D flow, correct temporal sign')
    """, """
    motion = mission.run('09', lk_patch)
    if motion is not None and corners is not None:
        tracked_motion = support.tracks(packet, corners, lk_patch)
        # A deliberate lighting failure; no geometry has changed.
        region = np.s_[38:55,38:55]
        print('Same patch with a brightness jump:',
              lk_patch(packet['gx'][region],packet['gy'][region],packet['it'][region]+.1))
    """)
    md("""
    ### RAFT pit stop — five lab questions in one model-reading challenge [Lab3 Q17–21]
    **No RAFT weights or inference are run here.** This retains the taught concepts without the
    original video decoding/download setup. RAFT = Recurrent All-Pairs Field Transforms.

    Three parts: (1) learned feature/context encoders; (2) all-pairs feature correlations with a pooled
    **correlation pyramid**; (3) recurrent updates that repeatedly refine one flow estimate.
    The flow stays at a fixed working grid (commonly 1/8 input resolution) and is upsampled for output;
    it does **not** mean the feature extractor never downsamples. Unlike coarse-to-fine LK, the
    correlation pyramid pools matching evidence, not a succession of resized flow fields.

    Read the essential API shape, not executable setup:
    ```python
    model = raft_small(weights=weights).eval()
    with torch.no_grad():
        flow_iterations = model(frame1_batch, frame2_batch)
    final_flow = flow_iterations[-1]  # N,2,H,W; components u,v in input-pixel units
    display = flow_to_image(final_flow)  # visualization, NOT class labels
    ```
    **Write three short answers below:**
    1. Why can the same ball have different flow colours in two frame pairs? Which quantities do colour/direction
       and intensity/magnitude represent, and why must you inspect the visualization scale?
    2. How do correlation lookup and recurrent updates help both small/large displacements without discarding
       a small feature at a coarse flow level? Name the three components in your explanation.
    3. Lighting change broke your LK estimate. Does a trained network guarantee the right answer under
       occlusion or unfamiliar lighting? Distinguish learned robustness from a valid visible correspondence.
    """)
    code("""
    raft_answers = {
        'colours_and_units': 'YOUR ANSWER',
        'architecture_and_correlation_pyramid': 'YOUR ANSWER',
        'failure_and_domain_shift': 'YOUR ANSWER',
    }
    """, tags=["reflection"])
    md("""
    <a id="map"></a>
    ## 4 — Two cameras, one belt map
    You get overlapping views with a small affine change. OpenCV supplies **only SIFT detection/descriptors**.
    You supply matching, robust fitting, inverse coordinate mapping and mask-aware blending.
    This rig is affine by construction; a general perspective panorama would need a homography.
    """)
    exercise("10", r"""
    ### 10 · Find evidence, not lookalikes [Lab4 SIFT matching]
    `a` and `b` are descriptor matrices N×D and M×D. Return integer `(N_kept,2)` index pairs.
    Compute the closest and second closest **L2 distances** per row of a; retain if `d1/d2 < threshold`.
    Reject d2=0 ties; if fewer than 2 candidates, return an empty `(0,2)` array.
    Using squared distances? Compare their ratio to **threshold²**.
    **Your call:** can a ratio test prove the two points belong to the same physical location?
    <details><summary>Hint</summary>

    Squared distance can be formed without an N×M×D tensor:
    `sum(a*a)[:,None] + sum(b*b)[None,:] - 2*a@b.T`. Clamp tiny negative roundoff to zero.

    </details>
    """, """
    def ratio_matches(a, b, threshold=.75):
        raise NotImplementedError('10: distances, ambiguity and index pairs')
    """, """
    matching = mission.run('10', ratio_matches)
    if matching is not None:
        features, pairs = matching
        print(len(pairs),'ratio-test matches. Descriptor width:',features['desc_a'].shape[1])
        support.show_matches(packet,features,pairs)
    """)
    exercise("11", r"""
    ### 11 · Ignore the convincing wrong matches [Lab4 affine RANSAC]
    `fit_affine(src,dst)` returns M of shape 2×3, with `dst ≈ [src,1] @ M.T`.
    Fit by LS; reject rank<3 (collinear source points). At least three point pairs are needed.
    `ransac_affine` uses a seeded RNG, samples 3 distinct pairs, rejects degeneracy, counts residuals
    `<=threshold` in target pixels, keeps the largest consensus, then **refits all its inliers**.
    Return `(matrix, boolean_inlier_mask)`; reject fewer than 3 input pairs/no usable consensus.
    Use your `fit_affine`, not OpenCV's RANSAC implementation.
    **Predict:** which needs more trials: w=.8 or w=.4, same sample size and success probability?
    <details><summary>Hint</summary>

    Use `np.random.default_rng(seed)`, `choice(...,replace=False)`.
    An all-inlier sample still needs nondegenerate geometry. A finite budget is not a certainty guarantee.

    </details>
    """, """
    def fit_affine(src, dst):
        raise NotImplementedError('11a: affine least squares')

    def ransac_affine(src, dst, threshold=2., trials=200, seed=8):
        raise NotImplementedError('11b: sample, score, retain, refit')
    """, """
    alignment = mission.run('11', (fit_affine,ransac_affine))
    if alignment is not None and matching is not None:
        matrix,inliers = alignment
        print('Inliers:',inliers.sum(),'/',len(pairs),'| Your A→B affine:')
        print(matrix)
        support.show_matches(packet,features,pairs,inliers)
    """)
    exercise("12", r"""
    ### 12 · Build the map without holes or black-pixel bugs [Lab4 warping/stitching]
    Implement two short functions:
    - `inverse_warp(image,matrix,output_shape)`: output_shape is `(H,W)`. Matrix maps **source→destination**.
      Build the destination grid, apply the inverse 3×3 homogeneous matrix, then call the supplied
      `sample_bilinear(image,xs,ys)`; it returns `(warped,valid_mask)`. You compute the coordinates.
    - `feather_blend(a,b,wa,wb)`: return `(a*wa+b*wb)/(wa+wb)` with channel broadcasting and zero
      where both weights are zero. Weights are coverage-aware, not `image != 0`.

    The helper supplies corner bounds/canvas translation and distance-to-boundary weights.
    **Your call:** why does forward pixel splatting leave holes? Why is real black not a reliable missing-data marker?
    """, """
    def inverse_warp(image, matrix, output_shape):
        raise NotImplementedError('12a: backward coordinates and valid coverage')

    def feather_blend(a, b, wa, wb):
        raise NotImplementedError('12b: weighted combination, including valid black')
    """, """
    mapped = mission.run('12', (inverse_warp,feather_blend))
    if mapped is not None and alignment is not None and matching is not None:
        belt_map = support.panorama(packet,alignment[0],inverse_warp,feather_blend)
    """)
    md("""
    <a id="sorter"></a>
    ## 5 — Teach, adapt, and audit the sorter
    You are building a **classifier, not an object detector**: object crops are provided.
    Training/validation/test contain independent generated object instances. Colours vary independently
    of labels; shapes still make this much easier than real material recognition. No MNIST/CIFAR/ImageNet download.
    Use validation for choices. Open the held-out test score only in the final replay.
    """)
    code("""
    loaders = support.make_loaders()
    sample_x,sample_y = next(iter(loaders['train']))
    support.gallery([a.permute(1,2,0).numpy() for a in sample_x[:6]],
                    [support.LABELS[int(y)] for y in sample_y[:6]],columns=6,size=1.7)
    print('Batch:',sample_x.shape,'| train/val/test:',[len(loaders[k].dataset) for k in ['train','val','test']])
    """)
    exercise("13", r"""
    ### 13 · Small network, real tensor arithmetic [Lab5 CNN mechanics]
    Build `Sorter` with attributes `features` and `classifier`:
    `Conv(3→8,3×3,pad1) → ReLU → MaxPool(2) → Conv(8→16,3×3,pad1) → ReLU → MaxPool(2)`.
    Then **global spatial mean** (N,16,8,8→N,16), then `Linear(16,3)`. Include ordinary biases.
    Return **logits**, not softmax; cross-entropy includes log-softmax.
    Use ordinary PyTorch layers, not an imported pretrained network.
    **Predict before running:** trainable parameters? Feature-map shape after each stage? Does stride change weights?
    <details><summary>Hint</summary>

    Conv params `(Kh*Kw*Cin+1)*Cout`; FC `(Din+1)*Dout`.
    GAP, ReLU and pooling have no ordinary learned weights. Forward must use the two named attributes.

    </details>
    """, """
    class Sorter(nn.Module):
        def __init__(self):
            super().__init__()
            raise NotImplementedError('13: features and classifier')

        def forward(self, x):
            raise NotImplementedError('13: spatial mean and logits')
    """, """
    model = mission.run('13', Sorter)
    if model is not None:
        print(model)
        print('Trainable parameters:',sum(p.numel() for p in model.parameters() if p.requires_grad))
    """)
    exercise("14", r"""
    ### 14 · The training loop is part of the model [Lab5 learning/evaluation]
    `train_step`: train mode → clear gradients → logits → CE → backward → optimizer.step;
    return detached **mean batch loss** as a Python float. Clearing gradients must work even if stale gradients exist.
    `evaluate`: eval mode **and** no_grad; return dict `accuracy`, `loss` (dataset mean CE), and integer
    `confusion` (rows true, columns predicted). Use example-weighted totals, not a mean of batch accuracies.
    Derive class count from output width; this must also work on the two-route model later.
    Batches are CPU tensors; no device boilerplate is needed.
    **Your call:** a smaller last batch exposes what averaging bug? Does `no_grad` turn off dropout?
    """, """
    def train_step(model, optimizer, x, y):
        raise NotImplementedError('14a: complete training update')

    def evaluate(model, loader):
        raise NotImplementedError('14b: modes, sample weights and confusion counts')
    """, """
    learning = mission.run('14', (train_step,evaluate))
    if learning is not None and model is not None:
        history = support.fit(model,loaders,train_step,evaluate,epochs=24)
        print('VALIDATION confusion (rows=true):')
        print(evaluate(model,loaders['val'])['confusion'])
    """)
    md("""
    ### Optional 3-minute failure lab — change one thing, not five
    Same architecture, object instances, batch order and twenty-epoch budget. Rate/optimizer comparisons
    share initial weights; initialization comparisons deliberately change them.
    Compare Adam, tiny learning rate, SGD, zero/Gaussian/He convolution initialization. These are small training
    demonstrations, **not universal optimizer rankings**. A fixed epoch budget is not equal wall-clock cost.
    Inspect training loss as well as validation: is the problem underfit, overfit or optimization?
    Zero-initialized ReLU branches can fail while the output bias still updates.

    **Diagnosis card:** He/ReLU weight variance is about `2/fan_in`; Xavier/Glorot about
    `2/(fan_in+fan_out)` under their usual assumptions. Repeated derivative magnitudes below 1 can vanish,
    above 1 can explode. Initialization, non-saturating activations, normalization and residual paths
    help; clipping limits exploding gradients, not vanished ones. A deeper model with higher **training**
    error can have optimization trouble, not overfitting. High train/low validation performance suggests
    checking capacity, augmentation, regularization and data leakage. Augmentation must preserve labels.
    """)
    code("""
    RUN_ABLATIONS = False  # switch to True after checkpoint 14
    if RUN_ABLATIONS and learning is not None and model is not None:
        comparisons = support.compare_training(Sorter,train_step,evaluate)
    """, tags=["optional"])
    exercise("15", r"""
    ### 15 · New job, same backbone [Lab5 transfer learning]
    New output meaning: **0=bypass caps, 1=press cardboard/cans**, under a different channel gain.
    `transfer_head(source)` must deep-copy the trained model, freeze **features only**, replace the
    classifier with `Linear(16,2)` (new head trainable), and return the adapted model.
    Never reset the feature weights or mutate your three-class source.
    This is **local toy pretraining/domain adaptation**, not an ImageNet/VGG experiment.
    Split membership stays by object ID across domains: no test object's recoloured sibling enters training.
    **Predict:** how many parameters now update? Explain freezing versus eval mode versus no_grad.
    """, """
    def transfer_head(source):
        raise NotImplementedError('15: reuse learned weights, change output semantics')
    """, """
    router = mission.run('15', transfer_head)
    if router is not None and learning is not None:
        routes = support.make_loaders(domain='route')
        route_history = support.fit(router,routes,train_step,evaluate,epochs=30)
        print('New-head trainable parameters:',sum(p.numel() for p in router.parameters() if p.requires_grad))
        print('ROUTE VALIDATION confusion:')
        print(evaluate(router,routes['val'])['confusion'])
    """)
    exercise("16", r"""
    ### 16 · Is it looking at the object? [Lab5 Grad-CAM]
    The helper computes actual activations A and class-score gradients from your trained model.
    `cam_map(features,gradients)` receives NCHW **PyTorch tensors**, N=1.
    Average gradients over H,W → channel weights; weighted sum of A over channels → ReLU → HW NumPy.
    Min-max scale this one map to `[0,1]`; return zeros if constant.
    **Your call:** would a belt-background highlight be a warning? Does a plausible heatmap prove causal reasoning?
    Do not run a gradient-based explanation inside no_grad. Eval and gradient recording are separate controls.
    """, """
    def cam_map(features, gradients):
        raise NotImplementedError('16: gradient weights, channel sum and positive map')
    """, """
    attention = mission.run('16', cam_map)
    if attention is not None and model is not None:
        probe = sample_x[:1]
        activations,gradient_values,target = support.capture_cam(model,probe)
        heatmap = cam_map(activations,gradient_values)
        support.gallery([probe[0].permute(1,2,0).numpy(),heatmap],
                        ['Validation not used here: one TRAIN probe',f'Grad-CAM for {support.LABELS[target]}'],columns=2)
    """)
    md("""
    ## Final replay — the line must work as a system
    This is not a sequence of reference answers: the replay calls your colour correction, shadow-weighted
    photometric stereo, height integration, Gaussian/gradient/LoG routines, feature score, LK, ratio test,
    affine RANSAC, inverse warp, feathering, trained sorter, evaluation and CAM functions.
    Fixed-view shape inspection and moving-belt inspection remain physically separate branches.
    Belt crops are supplied at known positions; they are **not independent test examples** or detections.
    The untouched generated test split is evaluated here, after your validation-based choices.
    """)
    code("""
    mission.status()
    final_report = support.final_replay(
        mission, colour_tools, photometric, integrate, gaussian1d, gradients, frequency_maps,
        structure_scores, lk_patch, ratio_matches, ransac_affine, inverse_warp, feather_blend,
        model, evaluate, cam_map,
    )
    if final_report is not None and router is not None:
        print('Final ROUTE test accuracy:',round(evaluate(router,support.make_loaders('route')['test'])['accuracy'],3))
    """, tags=["integration"])
    md("""
    ### Your shift report — five decisions, not five essays
    Write one or two sentences each. Code checks cannot assess these explanations.
    1. **Lighting/shape:** where did shadow weighting help, where did it fail, and what height reference is missing?
    2. **Signal:** which filter would you deploy and what relevant detail did it remove?
    3. **Motion:** which assumptions failed under the brightness jump; would larger windows or RAFT guarantee a repair?
    4. **Map:** which matches were rejected, why use inverse warping, and what can't blending fix?
    5. **Sorter:** what do validation/confusion/CAM show, what remains untested, and would you ship or hold this system?
    Include a real-world test you would require before deployment. Toy accuracy is not that test.
    """)
    code("""
    shift_report = {
        'lighting_and_shape': 'YOUR ANSWER',
        'signal': 'YOUR ANSWER',
        'motion': 'YOUR ANSWER',
        'map': 'YOUR ANSWER',
        'sorter_and_ship_or_hold': 'YOUR ANSWER',
    }
    """, tags=["reflection"])
    md("""
    ### Optional 2-minute reality check — one local course photograph
    If you have the original Lab5 image folder, inspect one metal photo with your edge pipeline.
    This does not download anything or evaluate a material classifier. Our toy shape labels do **not**
    match the real six-material label set. Do not present the toy classifier's output as a material prediction.
    **Your call:** which gaps—texture, pose, clutter, lighting, labels, data size—make a real deployment harder?
    """)
    code("""
    RUN_REAL_PHOTO = False
    if RUN_REAL_PHOTO and edges is not None:
        photo_dir = LAB_DIR.resolve().parents[1] / 'labs/cv1-lab-5/docs/garbage-classification-dataset/garbage-classification-images/metal'
        photos = sorted(photo_dir.glob('*.jpg'))
        if photos:
            real_rgb = cv2.cvtColor(cv2.imread(str(photos[0])),cv2.COLOR_BGR2RGB)/255.
            real_mag = gradients(support.gray(real_rgb))[2]
            support.gallery([real_rgb,real_mag],['Provided Lab5 photograph','Your gradients on real appearance'],columns=2)
        else:
            print('Local course photograph not found; the core notebook needs no course data.')
    """, tags=["optional"])
    md("""
    **Done.** If you can write the small functions and defend the decisions, you have rehearsed the
    main computational ideas of Labs 1–5 without repeating their setup or large experiment grids.
    See `README.md` for the exact coverage/omission map and `SOLUTIONS.md` after your attempt.
    This is original revision material, not an official replacement for assessed lab submissions.
    """)
    # Stable IDs make generated-source diffs and preserved learner edits easy to inspect.
    for index, cell in enumerate(cells):
        cell.id = f"cv1-master-{index:03}"
    notebook = nbf.v4.new_notebook(cells=cells, metadata={
        "kernelspec": {"display_name": "Python 3 (CV1 master lab)", "language": "python", "name": "python3"},
        "language_info": {"name": "python", "version": "3.12"},
        "cv1_master_lab": {"version": 1, "checkpoints": 16},
    })
    notebook.metadata.cv1_master_lab.generated_digest = digest(notebook)
    return notebook


def write_notebook(path, notebook):
    path = Path(path)
    if path.exists():
        old = nbf.read(path, as_version=4)
        baseline = old.metadata.get("cv1_master_lab", {}).get("generated_digest")
        if not baseline or digest(old) != baseline:
            raise SystemExit("Learner edits detected. Nothing overwritten; use --output with a NEW filename.")
    nbf.validate(notebook)
    nbf.write(notebook, path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=HERE / "master-lab.ipynb")
    args = parser.parse_args()
    notebook = make_notebook()
    write_notebook(args.output, notebook)
    print(f"Wrote {args.output}: {len(notebook.cells)} cells, 16 exercise checkpoints.")
