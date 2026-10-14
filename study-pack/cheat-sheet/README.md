# Computer Vision 1 — six-page cheat sheet

**[Printable PDF](cv1-cheat-sheet.pdf) · [Standalone LaTeX source](cv1-cheat-sheet.tex)**

Exactly **six portrait A4 pages**, for three double-sided sheets. Three columns per page, **6.45–7-point body text** (only expanded columns are smaller), 6.25-point code, compact native LaTeX equations and matrices, and nominal 5 mm margins. No cover or bibliography consumes a permitted side.

## Print

- Print **only `cv1-cheat-sheet.pdf`**, A4, portrait, **Actual size / 100%**.
- Use duplex printing, **flip on the long edge**. Page pairs are 1–2, 3–4 and 5–6.
- Do not use multiple pages per side or booklet mode. Automatic “Fit” can make the text smaller.
- Use a high-quality setting. Check one printed side before printing all three sheets. Some punctuation extends less than 0.5 mm into the nominal margins; the printer must support at least a 4.5 mm printable margin.
- The original 7-point version printed successfully, according to your report. The revised, smaller columns were checked in rendered images but **were not physically test-printed here**. Check one revised side before printing the full set.

## 14 October revision — requested additions

- **Side 1:** exact sine/cosine values for 0°, 30°, 45°, 60° and 90°, plus degree/radian conversion.
- **Side 2:** histogram equalization in six explicit steps; S1 Q5c's complete count/mapping table; Q5d–e's histogram, lookup, merged counts and first-row pixel remapping; Q5f's HSV/V-channel procedure. Named low/high/band-pass examples, the gradient-magnitude definition and calculation, and central-difference/Sobel/Prewitt/Gaussian-derivative choices are explicit.
- **Side 3:** raw weighted and unweighted HoG formulas, ordered vectors and code; the actual S3 Q2d vectors, including its flat-pixel counting convention. SIFT is organized around **S3 Q3a–c**: feature location/scale, illumination/scale/rotation mechanisms, and the 16 groups of eight descriptor values, with vote interpolation and normalization.
- **Side 4:** numbered stitching steps with descriptions and example algorithms: detect/describe, match, estimate alignment, warp to a common canvas, blend.
- **Side 6:** S4 Q4c's explicit locations × aspect ratios × scales × classes formula and **540 evaluations / 108 candidate boxes**. Larger stride and segmentation/proposals reduce sliding-window search, with their cost/recall trade-offs stated.

## Page map

| Side | Contents |
|---|---|
| 1 | Pinhole projection; intrinsic/extrinsic matrices; camera centre, rays and rotations; crop/resize; digital images and colour spaces; colour constancy and invariants; Lambertian/Phong/BRDF; intrinsic images; photometric stereo, weighting and height integration |
| 2 | Histograms, contrast/gamma/equalization; connectivity and component labelling; morphology and boundary rules; convolution/correlation, smoothing and derivative kernels; Gaussian separability, scale and LoG/DoG; Fourier, sampling and FFT recipes; NumPy axes, shapes and types |
| 3 | Canny; Harris/Shi–Tomasi and the structure tensor; HOG; scale selection, SIFT and matching; least squares, total least squares and Hough voting; RANSAC; Lucas–Kanade, pyramids and aperture problem; template/detection/mean-shift tracking |
| 4 | Transform families/invariants, affine fitting and homography DLT; warping/interpolation/stitching; calibration/distortion; F/E and epipolar geometry; rectification, disparity, depth and uncertainty; triangulation, SfM/PnP/bundle adjustment/MVS; Shape from X |
| 5 | Task definitions; k-means/mean shift; BoVW; k-NN/linear models/SVM; train/validation/test; confusion matrices, precision/recall/F1 and aggregation; retrieval/detection AP variants and mAP; IoU; activations/losses/backprop; SGD/Adam, initialization, generalization and train/eval code |
| 6 | CNN output shapes, parameters, compute, FC equivalence, 1×1/3D kernels, pooling, BatchNorm, receptive fields and backprop; sliding windows, Selective Search and NMS; R-CNN family/RoI/RPN; original YOLO and later-version distinctions; architectures, ResNet, encoder–decoder/U-Net/SegNet, segmentation, autoencoders, transfer and Grad-CAM; names |

All **24 study-pack topic groups** and every topic on the **9 October 2026 preparation checklist** have a location in this map. Lower-priority material is compressed; this is not every lecture illustration, historical example, or chapter of either textbook, and it cannot guarantee every possible exam question.

Sources are the supplied HC1a–HC6b lecture decks, Seminars 1–5 with solutions, Labs 0–5, current preparation documents, and relevant textbook support already reviewed for the study pack. See [the exact source paths and review limits](../COVERAGE.md). The sheet also includes **Hough calculations from Seminar 2** and **diffuse/glossy colour invariants from Seminar 1**, not just a shortened flashcard deck. Standard supporting formulas provide compact calculation recipes; they are not predictions of what will be asked.

Guest Lecture 13 and optional-only advanced implementations are excluded. No training notebook, dataset download, official ANS question or real model training was run.

## Conventions and source conflicts

Follow a question's stated convention first. The sheet makes these distinctions explicit:

- World-to-camera pose; camera translation versus centre; image-array axes.
- HC2a's negative normal-to-height ratios versus Lab1's positive printed ratios.
- Correct NumPy phase argument order: `atan2(imag, real)`.
- Convolution versus cross-correlation and derivative signs; raw versus normalized HOG.
- Probabilistic RANSAC versus exhaustive no-repeat guarantees.
- F's rank constraint versus homogeneous scale; declared stereo disparity sign.
- Raw, interpolated and sampled AP; retrieval queries versus detection classes.
- **YOLO v1** `5*B+C` output and confidence versus later per-anchor variants.
- Parameters, weights, activations and MACs; gradients, train/eval modes and frozen weights.

More explanation is in [SOURCE_NOTES.md](../SOURCE_NOTES.md). Two-stage feature sharing, unequal-batch accuracy averaging, and other source qualifications are retained.

## Rebuild and verify

From `/home/richard/Documents/academics/1/computer-vision-1`:

```bash
uv run --no-project study-pack/cheat-sheet/build.py
```

Requires pdfLaTeX, `latexmk`, `pdftotext`, and the standard LaTeX packages named in the source, including `newtxtext`, `newtxmath`, `microtype` and `listings`. `uv` manages the NumPy dependency used for checks. The `.tex` itself is standalone and does not require Python to compile.

The build executes the **23 NumPy listings on dedicated synthetic inputs**, syntax-checks the **two PyTorch listings without running them**, independently checks worked arithmetic and finite-difference CNN gradients, then compiles and checks the actual PDF. It also recomputes the requested seminar examples: both equalization histograms and the 8×8 patch, gradient kernels/magnitudes, weighted/unweighted HoG, SIFT normalization/vote arithmetic, trigonometric values, box evaluations and stride counts. These are software/arithmetic checks, not execution of a full SIFT implementation or physical experiments.

It requires six A4 pages, all 18 columns within the height budget, at least 96% column-height use, the expected topic markers (including the requested additions), text inside a 4.5 mm safety boundary, and no overflow or missing-glyph warnings. It copies the PDF here only after the checks pass. Logs stay under `/tmp/opencode/`.

For calculation checks alone:

```bash
uv run --no-project study-pack/cheat-sheet/verify_math.py
```

Current column-height use is **97.1–99.9%, averaging 99.2%**. This measures occupied vertical layout, not black-ink coverage. All six final pages were checked visually from rendered images. Automated checks cannot prove every conceptual statement or replace a physical print check; PDF text extraction is not a proof of correct mathematical rendering.
