# Source and convention notes

Use these notes to avoid learning incompatible formulas or copying a simplified statement as a universal rule. The course files themselves were not changed. If the lecturer states a convention in an exam question, follow it.

## 1. Camera frames and image axes

This pack uses column vectors and **world-to-camera** `Xc=R@Xw+t`, so `C=-R.T@t`. Projection uses a virtual image plane in front of the pinhole, with positive visible depth. A physical plane behind it gives the familiar inversion/sign change.

Array indexing is `I[y,x]`. Cartesian rotation diagrams can use y-up while image arrays use y-down; an apparent clockwise/counterclockwise change can be a coordinate change rather than a different rotation formula. Crop/resize questions explicitly ignore half-pixel resampling offsets.

Sources: HC1b PDF pp.24–45; Seminar 1; Lab0.

## 2. Normal-to-height signs really differ in the supplied materials

- HC2a **PDF p.42**, visually checked, gives `p=-nx/nz`, `q=-ny/nz`, for the upward graph normal proportional to `[-p,-q,1]`.
- Lab1 **Q19 / notebook cell 57** writes `p=nx/nz`, `q=ny/nz` without those minus signs.

Do not switch formulas halfway through a solve. This pack declares the upward graph convention when a numerical question needs it. For the physical reason, tangent `[1,0,p]` must be perpendicular to normal `[-p,-q,1]`. Reversing the entire normal alone does **not** reverse the ratios; axes/height conventions or an inconsistent formula must be considered. The local sources do not resolve the discrepancy further.

For Lab1-specific code, follow its stated definition if the question asks what that code computes. For an abstract geometry question, follow the declared graph/coordinate convention.

## 3. Photometric-stereo shapes and scale

This pack stacks lights as rows: `i=L@g`, `L.shape=(m,3)`. Some slide equations instead stack light columns or solve for rows of pixels. Check dimensions rather than memorizing a transpose position.

The simple course model absorbs light strength/gain constants as stated. A physically calibrated Lambertian BRDF uses `rho/pi`; that does not make the simplified `I=rho*J*(n dot l)` equation wrong when its coefficient includes those factors.

Lab1's shadow trick solves `diag(i)@L@g=diag(i)@i`. Squaring those scaled residuals gives weights `i_j^2`, not `i_j`. It can reduce dark-observation influence but can emphasize bright specular outliers. Absolute albedo depends on calibrated light strength and camera gain.

Sources: HC2a PDF pp.19–20,34–43; Lab1 Q18.

## 4. Fourier phase: the NumPy argument order

HC2b **PDF p.100**, visually checked, prints `atan2(Real, Imag)`. For NumPy, phase is instead:

```python
phase = np.arctan2(F.imag, F.real)
# equivalent to np.angle(F), for nonzero F
```

NumPy takes `atan2(y,x)`. For `F=1+0j`, the correct phase is zero, whereas the reversed call returns pi/2. This provides a direct check without relying on extracted PDF text. At zero magnitude, phase is physically undefined even if a function returns a placeholder.

The practice DFT convention is unnormalized forward, inverse divided by sample count, matching NumPy's default. Other textbook normalizations change coefficient scale, not the core frequency interpretation.

## 5. Correlation, convolution, and gradient sign

Mathematical convolution flips spatial kernel offsets; cross-correlation does not. CNN libraries normally call cross-correlation “convolution.” Questions that need the distinction say which rule to apply.

Seminar 3 Q2a says changing correlation/convolution is only a sign flip for its antisymmetric derivative and that results remain the same. The important qualification is:

- gradient **magnitude** stays the same if both derivatives reverse;
- **unsigned** HoG angles modulo 180 stay the same;
- signed gradient directions change by 180 degrees and are not identical.

Also distinguish **derivative of Gaussian** from **Difference of Gaussians**. The latter is SIFT's two-scale approximation to LoG; it is not simply an x derivative. HC3a's short “DoG” labels can otherwise be confusing.

## 6. Raw HoG and normalized descriptors

Seminar 3 uses a **raw magnitude-weighted** HoG example. Doubling image intensities doubles its nonzero histogram entries. More complete normalized HoG variants can reduce common-gain sensitivity. Therefore the seminar's answer and a normalized-descriptor explanation are not contradictions.

The practice HoG question states unsigned orientation, exact bin edges, hard assignment, no interpolation and no normalization. Never infer these settings merely from “9 bins.” SIFT's standard descriptor is 4×4×8=128 values with its own orientation/normalization rules.

Sources: Seminar 3 Exercise 2; HC4a pp.41–44; Forsyth–Ponce §5.4.

## 7. AP is not one unstated arithmetic rule

HC5a pp.20–22 and Seminar 4 give a retrieval ranking average of precision at relevant ranks. The examples normalize by their counted relevant results; they do not clearly establish every missing-relevant-item convention for a truncated ranking. HC5a pp.68–78 describes detection AP as precision–recall area.

This pack states the rule in each numerical AP question:

- **Raw ranking AP:** average precision at relevant ranks, divided by the specified total relevant count; unreturned relevant items contribute zero.
- **All-points interpolated AP:** use the future-maximum precision envelope and integrate positive recall increments; unreached recall contributes zero.

These can differ. Neither should silently be replaced by 11-point AP or COCO's sampled-recall implementation. Retrieval mAP averages queries; detection mAP averages class APs, and COCO-style summaries also average IoU thresholds.

## 8. YOLO output/confidence equations are version-specific

HC6a pp.64–72 describes **original YOLO v1**. Its output uses one shared class vector per grid cell: `S*S*(5*B+C)`. It defines box confidence as `Pr(object)*IoU`, then multiplies by conditional class probability for a class-specific score. The confidence slide, PDF p.69, was checked visually.

Other single-shot/per-anchor diagrams and later YOLO versions can use `B*(5+C)` channels per cell and different objectness targets. Do not combine these conventions. The practice questions explicitly say “original YOLO v1” when using its equations.

## 9. RANSAC probability is not a finite worst-case guarantee

The usual `w^s` formula models independent draws and assumes nondegenerate all-inlier samples. Sampling s distinct points from a finite set instead has exact all-inlier probability `choose(I,s)/choose(N,s)`.

Seminar 4 Q1e counts distinct bad subsets before a good one. Its finite worst-case count needs a **no-repeated-subset/exhaustive** interpretation. Ordinary random resampling can repeat bad subsets indefinitely, so a fixed finite budget gives a probability, not certainty. The numerical questions use the explicit independent approximation and ceiling formula.

There is no universal 50%-inlier requirement. Competing models, degeneracy, residual threshold and the sample budget matter.

## 10. Fundamental-matrix rank and scale

HC6b PDF p.55 says rank deficiency is “due to scale ambiguity.” These are different facts:

- `F` is defined up to nonzero scale, removing one degree of freedom.
- Nondegenerate epipolar geometry gives rank 2 and an epipole null direction; the essential form `[t]_x R` illustrates the rank constraint.

Scale ambiguity alone does not imply rank deficiency: every nonzero scalar multiple of the identity still has rank 3. The pack uses the standard rank-2, 7-DoF F and calibrated 5-DoF E distinctions.

HC6b PDF p.85 defines a disparity using `x2-x1`. The practice depth questions explicitly define `d=uL-uR` with a compatible positive baseline and equal principal points, so `Z=f*B/d`. Do not copy a sign without the camera convention.

## 11. CNN parameter counts: a checked textbook typo and important qualifications

In the supplied Szeliski draft, **Figure 5.35 caption, printed p.293 / PDF p.319**, the total-weight expression is printed as `Kw*Kh*Cin*Cin`. The page was checked visually: this is not an extraction error. Its own diagram has axes `Cout*Cin*Kw*Kh`, which gives the correct count:

```text
weights = Kh*Kw*Cin*Cout
parameters_with_bias = (Kh*Kw*Cin + 1)*Cout
```

The pack derives these counts independently. Further safeguards:

- “Weights” and “parameters including bias” differ.
- Stride changes output positions and work, not shared kernel parameters.
- Dense convolution work uses **output** positions. Seminar 5 Q5d's input-volume expression applies only to the shape-preserving case it specifies.
- Seminar 5 Q5e's statement that (2+1)D convolution has fewer parameters needs channel dimensions: factorization is not automatically smaller for every intermediate width.

## 12. Two-stage detectors share features too

Seminar 5 Q4a broadly contrasts one-stage whole-image processing with two-stage region processing. Do not interpret this as “every two-stage detector runs its backbone separately on each raw crop.” That describes original R-CNN. Fast/Faster R-CNN share full-image convolutional features; Faster adds the learned RPN.

The pack follows the explicit HC5b/HC6a architecture comparisons. No new advanced detector implementation is required.

## 13. Training examples are not universal optimizer rankings

Lab5's small experiments are useful illustrations, not laws that Adam always wins, SGD always wins on noisy/shallow data, or deeper always means better. Adam still has a base learning rate. Compare settings on validation data and separate optimization failure from overfitting.

Constant initialization can keep interchangeable hidden units symmetric. All-zero ReLU weights can also stop useful gradients, but an output bias can still change: “all parameters can never update” is too strong.

Two implementation details are particularly useful for code interpretation:

- The CIFAR tutorial's `evaluate()` uses `torch.no_grad()` without a `model.eval()` call. These do different things; gradient recording and layer train/eval behaviour are separate.
- The garbage assignment averages batch accuracies equally. With a smaller last batch, this need not equal `total_correct/total_examples`; use batch-size weighting for the latter metric.

Neither notebook was altered or retrained to establish a performance claim.

## 14. Names, editions and study priorities

VGG is associated with **Karen Simonyan and Andrew Zisserman**; the early HC6a overview has an inconsistent spelling. Learn the canonical names, not the typo. The artificial-neuron/perceptron history also uses inconsistent dates, so those cards prioritize the associated names and concepts.

Lab1 refers to an older Forsyth–Ponce chapter location for photometric stereo. In the supplied **second edition**, that material is in §2.2; §5.4 instead covers SIFT/HoG. Use the supplied edition's headings.

Cards tagged `breadth` still include taught supporting material; they are not a promise of exam questions. The pack excludes optional-only advanced code. Hough appears in an outline, so only a short method definition is kept. The three practice exams intentionally overtrain computations without claiming the lecturer's exact weighting.
