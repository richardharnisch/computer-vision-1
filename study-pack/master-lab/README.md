# CV1 master lab — Night Shift

**[Open the master notebook](master-lab.ipynb)**

Recover a recycling-line inspection system: repair colour and lighting, estimate surface shape,
clean images, track belt motion, stitch camera views, train a sorter, adapt it to a new routing task,
and inspect its attention.

**One notebook, five stations, 16 coding checkpoints.** The learner notebook has 68 cells, compared
with 537 cells across the supplied Labs 1–4 and the three Lab5 tutorial/assignment notebooks.
The reduction removes setup, repetitions and large experiment grids, not just explanatory text.
Allow extra reading time if these topics are new; the original **2½–3½ hour** estimate assumes familiarity.

Each checkpoint now includes a teaching section before the implementation contract: context and
assumptions, TeX equations with explained symbols, array/tensor shapes, and the steps that connect
the mathematics to NumPy/PyTorch. The coding tasks, checks and separate solutions are unchanged.

## Start

From `/home/richard/Documents/academics/1/computer-vision-1`:

```bash
uv sync --project study-pack/master-lab
uv run --project study-pack/master-lab jupyter lab study-pack/master-lab/master-lab.ipynb
```

Save a copy as **`my-master-lab.ipynb`** before editing. In VS Code, use the Python interpreter at
`study-pack/master-lab/.venv/bin/python` as the notebook kernel. All required packages are local
to this component. `uv.lock` records the tested environment; PyTorch uses its **CPU-only** wheel index.
Initial package installation needs the internet. The main notebook subsequently needs **no network,
model weights, downloaded datasets or GPU**.

Work through the exercise cells; each check cell reports **PASS**, **TODO**, or **CHECK FAILED**.
Running the unfinished notebook from top to bottom is safe: it does not silently solve tasks or run
training on an unimplemented model. Independent stations use labelled supplied captures to prevent
one unfinished function from blocking every later topic. The final replay requires all 16 checkpoints
and an actual training run, then calls your functions again through the connected system.

Reference answers stay **outside** the notebook: [conceptual debrief](SOLUTIONS.md) and
[reference code](solutions.py). Do not open these until you have tried the relevant task.

## What you actually implement

| Station | Checkpoints | Work |
|---|---|---|
| Inspection booth | 01–04 | Grey-World, normalized/opponent colour and lightness; intrinsic recolouring; plain/weighted calibrated photometric stereo; normals to height and integrability |
| Signal processing | 05–07 | Sampled Gaussian and two derivatives; signed Sobel gradients/magnitude/angle; sequential LoG, direct sampled LoG, DoG |
| Motion | 08–09 + short reading | Harris/Shi–Tomasi second moments; observable Lucas–Kanade flow; tracking, units and lighting failure; RAFT architecture/correlation/colour interpretation |
| Camera map | 10–12 | Descriptor ratio matching; affine LS and RANSAC; inverse coordinates, interpolation coverage, feather blending |
| Sorter | 13–16 | Small CNN and parameter arithmetic; training/evaluation with correct modes/weighting; frozen-backbone transfer; Grad-CAM channel weights and map |

Each task has a specific output contract, small checks, a visual result or experiment, and a short
prediction/decision. No long essays are required. A final five-decision shift report checks the ideas
that numerical tests cannot assess. **16/16 is code-check completion, not proof of conceptual mastery.**

### Supplied rather than reimplemented

- Deterministic image/lighting/sequence generation, plotting, loaders, training drivers and canvas bounds.
- SciPy correlation and window aggregation, OpenCV SIFT detection/description, and bilinear sampling.
  You still implement the filters, matching, model fit, RANSAC, inverse coordinates and blending.
- HSV/YCbCr conversion is a short display/axis/range interpretation, not another conversion-library task.
- RAFT is **model/API reading**, not executed inference. Its five lab questions are condensed into
  three prompts covering visualization, its three components, correlation pyramid, fixed-grid updates,
  failure assumptions and domain shift. No RAFT prediction is fabricated or substituted.

## Course-source map and deliberate omissions

| Original source | Retained learning | Compression / omission |
|---|---|---|
| [Lab1](../../labs/cv1-lab-1/cv1-lab-1.ipynb), colour/constancy and intrinsic sections | Axes, types, grayscale, opponent/normalized RGB, HSV/YCbCr, Grey-World assumptions, albedo × shading, masked recolouring | Repeated channel-display functions and literature-search task removed |
| Lab1 photometric section | Calibrated LS, row shapes, albedo/unit normals, intensity-squared shadow weighting, specular failure, RGB zero-channel problem, height paths/curl/anchor | One controlled lighting burst replaces repeated sphere/monkey/face/apple loading, plotting and image-count sweeps. RGB uses the same solver per channel; no separate duplicated implementation |
| [Lab2](../../labs/cv1-lab-2/cv1-lab-2.ipynb), Gaussian and edge sections | Kernel normalization, separability/cost, first/second derivatives, correlation/convolution signs, magnitude/angle, three LoG/DoG routes | No optional advanced Gabor/filter-bank segmentation, PSNR sweeps or repeated denoising grids. A small median comparison remains illustrative |
| [Lab3](../../labs/cv1-lab-3/cv1-lab-3.ipynb), feature warm-up, LK and RAFT sections | Second moments/eigenvalues, LK conditioning/aperture, sparse tracks, pyramid-vector units, brightness failure, RAFT Q17–21 concepts | Feature warm-up compressed; no optional Horn–Schunck implementation, video encoding, RAFT download/inference or long sequence rendering |
| [Lab4](../../labs/cv1-lab-4/cv1-lab-4.ipynb) | SIFT descriptor use, ambiguity/ratio, affine constraints, robust estimation/refit, backward warping/interpolation/masks, panorama/blending, parallax limitations | SIFT library extraction and canvas setup provided; no repeated manual match plotting or optional many-image panorama system. Forward splatting is explained, not a second full warper |
| [Lab5 tutorial](../../labs/cv1-lab-5/docs/tutorial-image-data-notebook.ipynb), [CIFAR tutorial](../../labs/cv1-lab-5/docs/tutorial-cifar-image-data-notebook.ipynb), [assignment](../../labs/cv1-lab-5/docs/assignment-image-data-notebook.ipynb) | Layers/capacity, CE/logits, train/validation/test, data order, modes/no-grad, unequal batches, optimizers/rate/init, gradients, generalization/augmentation, last layer, transfer, Grad-CAM | Tiny generated CPU task replaces MNIST/CIFAR/garbage downloads, large networks and optional search grids. Transfer reuses a locally trained backbone, **not ImageNet pretraining**. VGG-specific API/history is not a new implementation exercise |

Lab0 indexing/broadcasting/type basics are used throughout, not repeated as a setup lab.
This is original study material, not lecturer-issued solutions or a replacement for assessed submissions.
The original course files are not changed. The photometric-normal sign discrepancy is stated explicitly.

## Data and experiment rules

- Main images are generated fixtures, not real photographs. Physical assumptions are declared:
  fixed-view/different-light captures for photometric stereo, separate moving-belt frames, and an affine
  camera pair. Belt speed uses a **given fictional calibration**, not a measurement of a real machine.
- The simulated object labels are **shape proxies**. Success cannot establish real material recognition,
  depth accuracy, safe robotics, production reliability, or robustness on real scenes.
- Train/validation/test object instances are disjoint. The routing domain preserves those same split IDs;
  recolouring a test object does not turn it into a training example. Use validation for choices and the
  held-out test only in the final replay. Final belt crops are a demonstration, not the held-out test.
- The optional six-run comparison fixes data, order and epoch budget. Rate/optimizer cases share initial
  weights; initialization cases deliberately differ. Scores are observations of this small exercise,
  not claims that one optimizer or initializer always wins.
- The optional reality check reads one existing local Lab5 metal photograph, if present, only for a
  gradient/appearance comparison. It does not download data or pretend the toy head predicts real materials.

## Rebuild and verification

```bash
uv run --project study-pack/master-lab python study-pack/master-lab/build_notebook.py
uv run --project study-pack/master-lab python study-pack/master-lab/verify_notebook.py
```

`build_notebook.py` is the notebook/stub authoring source; `instructional_notes.py` contains the expanded
teaching sections. `mission_support.py` contains fixtures, checks and
experiment drivers, and `solutions.py` contains separate authored answers. The delivered `.ipynb` is the
actual learner artifact. The generator **refuses to overwrite changed notebook text/code**; choose a new
`--output` path if you want a fresh template. Do not regenerate your working copy.

Verification validates the delivered notebook against its source, parses every code cell, checks
rendered navigation/expandable-hint formatting and overwrite protection, then runs **two fresh
Jupyter kernels** with this component's Python:

1. Unfinished notebook: completes with 16 honest TODOs and no hidden solutions/training.
2. Temporary solved copy: executes all 16 checkpoints, real SIFT on generated camera images, actual
   affine/RANSAC/warp/blend, small CPU training, six ablations, local transfer, real autograd Grad-CAM,
   and a fresh final pipeline. The optional local-photo branch is also exercised when available.

The verifier also rejects several plausible wrong answers (zero gradients, invented flow on edges,
black-as-missing-data blending, constant fake heatmaps). Executed copies/plots stay under
`/tmp/opencode/`; the learner notebook stays blank and solutions remain separate.
No original course notebook or pretrained model is executed. Automated checks are software evidence,
not proof that all conceptual answers or real-world assumptions are correct.
