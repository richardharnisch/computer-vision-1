# Exam 2 — Implementation and failure diagnosis
## Conditions
- 50 questions: 30 single-answer multiple choice and 20 numerical. Each is worth 1 raw practice point.
- Suggested training limit: **150 minutes**. This is not a claim about the actual exam duration or question count.
- Use up to three double-sided A4 sheets, prepared by you, and a local Jupyter notebook. No internet, AI assistance or answer key during the attempt.
- Use Python/NumPy for computation; SciPy is also allowed. You do not need executable OpenCV or PyTorch. Specialized routines are provided when needed.
- For multiple choice, select exactly one of A–D. Attempt every question.
- Unless an exact integer is requested, round the final numerical answer to **two decimal places**. Keep full precision in intermediate steps. Use fractions rather than percentages unless specified.
- Numerical practice grading uses the syllabus rule: within ±0.01 of the unrounded reference, inclusive. Counts require the exact integer; no partial credit.
- Conventions stated in a question override defaults. Arrays use [row,column] = [y,x]; geometric vectors are columns; image-plane projection is virtual/front-facing; foreground is 1.
- This is original, challenging training material based on the supplied course files, not a lecturer-issued mock or a prediction of the exam.

Use [the blank answer sheet](../answer-sheet.md). Solutions are in a separate folder; do not open them until you finish.
## Part A — Single-answer multiple choice

### Q01 — Multiple choice

R1 and R2 are proper 3D rotation matrices. Which statement is correct?

- **A.** The inverse is always R2.T @ R1.T.

- **B.** A rotation matrix has 9 independent degrees of freedom.

- **C.** The inverse of R2 @ R1 is R1.T @ R2.T; rotation order generally matters.

- **D.** R1 @ R2 always equals R2 @ R1.

### Q02 — Multiple choice

Crop an image by removing 40 pixels from the left and 20 from the top, with no resize. In the continuous-coordinate model, how does K change?

- **A.** Subtract 40 from fx and 20 from fy.

- **B.** Keep K unchanged and add [40,20,0] to camera translation.

- **C.** Subtract 40 from cx and 20 from cy; keep focal lengths and skew unchanged.

- **D.** Multiply both focal lengths by the crop's remaining image area.

### Q03 — Multiple choice

For floating-point RGB image I of shape (H,W,3), what does this code compute?

```python
out = (I.max(axis=2) + I.min(axis=2)) / 2
```

- **A.** One scalar containing the midpoint of the global intensity range.

- **B.** A lightness-based grayscale image of shape (H,W).

- **C.** An RGB image with corrected white balance.

- **D.** A hue map obtained by averaging the red and blue channels.

### Q04 — Multiple choice

Which expression computes per-channel image means that broadcast correctly onto an array of shape (H,W,3)?

- **A.** I.mean(axis=0, keepdims=True), which always has shape (1,1,3)

- **B.** I.mean(axis=(0,1), keepdims=True)

- **C.** I.mean(axis=(0,1,2), keepdims=True)

- **D.** I.mean(axis=2, keepdims=True)

### Q05 — Multiple choice

Suppose the true lighting matrix is Ltrue = 2 \* Lused, with no shadows or noise. You solve i = Lused ghat. How do the estimated normal and albedo relate to the true ones?

- **A.** The normal doubles in length after normalization; albedo is unchanged.

- **B.** Both normal direction and albedo are unchanged.

- **C.** The normal reverses and albedo is halved.

- **D.** The normal is unchanged; the albedo estimate is doubled.

### Q06 — Multiple choice

For the intrinsic-image model I = A \* S, where multiplication is elementwise, which recolouring operation preserves the estimated shading?

- **A.** Divide the target albedo by S.

- **B.** Change the object's albedo A and multiply the changed A by the original S.

- **C.** Change S to the target RGB colour and discard A.

- **D.** Replace every RGB pixel in I by the same target colour, including shadows.

### Q07 — Multiple choice

A uniformly painted matte object has spatially constant albedo. Why can its image still contain a brightness gradient?

- **A.** Lambertian reflection requires all pixels to have the same intensity.

- **B.** Constant albedo forces constant depth.

- **C.** Its surface normals and therefore light–normal dot products can vary.

- **D.** Its intrinsic albedo must contain every shadow.

### Q08 — Multiple choice

What information can a joint RGB histogram retain that three separate channel histograms lose?

- **A.** Which red, green and blue values occur together at the same pixels.

- **B.** The scene's illumination-independent albedo distribution, regardless of camera response.

- **C.** The order of coloured regions across image rows, rather than just their colour counts.

- **D.** The exact spatial location of each pixel having a particular colour.

### Q09 — Multiple choice

A binary erosion uses a cross-shaped 3 by 3 structuring element with zeros at its corners. How should the zeros be treated?

- **A.** Require the image's corner positions to be zero.

- **B.** Replace the operation by an average over all nine pixels.

- **C.** Include the mask zeros in a logical AND, forcing every output to zero.

- **D.** Ignore those positions; require foreground only at active element positions.

### Q10 — Multiple choice

A system labels every pixel by semantic class, including pixels of several touching people, but gives no person-instance IDs. What does its output provide, and can connected-component labelling alone reliably supply the missing instance separation?

- **A.** Semantic segmentation; no, touching people can merge into one connected component.

- **B.** Instance segmentation; a semantic class label automatically identifies which individual person owns each pixel.

- **C.** Object detection only; connected-component labels are already separate bounding-box detections.

- **D.** Panoptic segmentation; instance IDs are unnecessary as long as all pixels have semantic labels.

### Q11 — Multiple choice

Why is a median filter often preferable to averaging for sparse salt-and-pepper noise?

- **A.** It is a linear filter with a fixed kernel of average weights.

- **B.** It increases the magnitude of all high-frequency components.

- **C.** It is less affected by extreme isolated values and can preserve edges better.

- **D.** It guarantees removal of every type of noise without information loss.

### Q12 — Multiple choice

A Gabor filter is best described as what?

- **A.** A sinusoidal pattern modulated by a Gaussian envelope, selective for local frequency and orientation.

- **B.** An unwindowed global sinusoid that has no spatial localization.

- **C.** A median of oriented derivative responses, making it a nonlinear rank filter.

- **D.** A Gaussian smoothing filter with no sinusoidal carrier and no orientation selectivity.

### Q13 — Multiple choice

You multiply two same-length unpadded DFTs and take the inverse DFT. What operation does this normally implement?

- **A.** Pointwise multiplication of the original spatial samples.

- **B.** Circular convolution, with wrap-around at the signal boundaries.

- **C.** Cross-correlation with no complex conjugation or reversal.

- **D.** Full linear convolution of length N+M-1 regardless of padding.

### Q14 — Multiple choice

A kernel measures the x derivative of an image. Which edge orientation usually gives a large response?

- **A.** Only a diagonal edge with exactly 45-degree slope.

- **B.** A horizontal edge: intensity changes only across y.

- **C.** A vertical edge: intensity changes across x.

- **D.** A perfectly constant patch.

### Q15 — Multiple choice

Compared with a small Gaussian sigma, what is a likely effect of increasing sigma in Canny?

- **A.** Suppress finer detail and noise, while potentially merging edges and reducing localization precision.

- **B.** Remove the need for non-maximum suppression.

- **C.** Make the operation exactly scale invariant.

- **D.** Guarantee detection of every weak edge with perfect localization.

### Q16 — Multiple choice

For a structure tensor at a pixel, which implementation follows the usual order of operations?

- **A.** Compute Ix\*Ix, Ix\*Iy and Iy\*Iy first, then aggregate or smooth those products over the neighbourhood.

- **B.** Use Ixx and Iyy as the diagonal entries and Ixy off diagonal, because the structure tensor is the image Hessian.

- **C.** Smooth Ix and Iy to one mean each, then use only the outer product of those two means.

- **D.** Aggregate only Ix and Iy and use their signed means as the diagonal entries, setting the off-diagonal entries to zero.

### Q17 — Multiple choice

Shi–Tomasi's corner score for structure-tensor eigenvalues lambda1 and lambda2 is which expression?

- **A.** max(lambda1, lambda2)

- **B.** lambda1 + lambda2, regardless of their relative sizes

- **C.** min(lambda1, lambda2)

- **D.** lambda1 - lambda2

### Q18 — Multiple choice

A Lucas–Kanade window contains 100 nonzero image-gradient vectors, all parallel. Is its two-component flow uniquely observable from those equations?

- **A.** No; the design matrix has rank 1 and tangential motion remains ambiguous.

- **B.** Yes, because there are more equations than unknowns.

- **C.** No, because least squares works only for exactly two pixels.

- **D.** Yes, because every gradient is nonzero.

### Q19 — Multiple choice

Move a flow estimate from a half-resolution pyramid level to full resolution. After spatially resizing the flow arrays, what else is required?

- **A.** Keep the vector magnitudes unchanged because the arrays were resized.

- **B.** Divide both displacement components by 2.

- **C.** Multiply displacement components by 2, then warp and refine at the finer level.

- **D.** Set every displacement to zero before the finer solve.

### Q20 — Multiple choice

A fixed image template is tracked with SSD. The target's shape and position remain the same but all intensities gain a constant positive offset. Which claim is correct?

- **A.** SSD can increase even for the true match; a mean-normalized comparison can handle an additive offset better.

- **B.** Unnormalized correlation always removes additive and multiplicative brightness changes.

- **C.** Only the target's geometric rotation can change SSD.

- **D.** SSD is exactly invariant to every additive intensity change.

### Q21 — Multiple choice

Which statement about mean-shift clustering is correct?

- **A.** It always requires the desired number of clusters K as its central input.

- **B.** It minimizes the same fixed-K objective as k-means using identical updates.

- **C.** Its result cannot depend on the bandwidth.

- **D.** It seeks density modes; kernel bandwidth influences how many modes and clusters are found.

### Q22 — Multiple choice

Retrieve images of the same planar building facade using a query in which part of the facade is occluded by a tree. Assuming enough distinctive features remain visible, which local-keypoint approach is appropriate?

- **A.** Reject every database image unless every query descriptor has a correct facade match, including descriptors on the tree.

- **B.** Accept every nearest descriptor match as geometrically correct, because SIFT's scale robustness guarantees the same scene point.

- **C.** Rank only by each database image's total keypoint count; descriptor appearance and geometric consistency are unnecessary.

- **D.** Match visible local descriptors and verify a consistent homography; the occluded parts need not match.

### Q23 — Multiple choice

What is the generic minimum data requirement for an unconstrained 2D affine transformation?

- **A.** Two point pairs because an affine transformation is only rotation plus translation.

- **B.** Four collinear point pairs always uniquely determine it.

- **C.** One point pair because affine transforms have two parameters.

- **D.** Three point pairs whose source points are noncollinear.

### Q24 — Multiple choice

Which statement accurately describes backward image warping?

- **A.** It guarantees valid source data for every destination pixel, even outside source coverage.

- **B.** It forward-maps each source pixel without interpolation.

- **C.** It always avoids aliasing during downsampling, even without a low-pass filter.

- **D.** For each destination pixel, inverse-map its coordinate and sample/interpolate the source; out-of-domain samples still need a boundary rule.

### Q25 — Multiple choice

What does the SVM kernel trick allow?

- **A.** Evaluate inner products in a transformed feature space without explicitly constructing all transformed features.

- **B.** Make every nonlinear decision boundary linear in the original coordinates.

- **C.** Change the distance metric only after fitting a linear SVM, without changing any training computation.

- **D.** Automatically eliminate every mislabeled training example, making soft-margin penalties unnecessary.

### Q26 — Multiple choice

At a fixed detection IoU threshold, two same-class detections both overlap the same ground-truth object sufficiently. In score-ordered, one-to-one matching, how are they counted?

- **A.** Both are TPs but each receives half a recall increment, making this identical to a single detection.

- **B.** The first can be a TP; the second is a duplicate FP unless it can validly match another unmatched object.

- **C.** The first is a TP and the second is ignored automatically in AP, so duplicate boxes cannot reduce precision.

- **D.** Both are TPs because their IoUs are high, even though they claim the same object.

### Q27 — Multiple choice

Three same-class boxes have descending scores A>B>C. IoU(A,B)>threshold, IoU(B,C)>threshold, but IoU(A,C)<threshold. What does greedy hard NMS keep?

- **A.** A only, because overlap is transitively inherited through B.

- **B.** A and C.

- **C.** B and C.

- **D.** All three, because A and C do not overlap strongly.

### Q28 — Multiple choice

Why is identical constant initialization of all interchangeable hidden units problematic?

- **A.** Random initialization guarantees no overfitting.

- **B.** Every nonzero constant necessarily causes exploding gradients on the first step.

- **C.** Biases must always be random for any network to learn at all.

- **D.** Symmetric units can receive identical activations and gradients, so they fail to learn distinct features.

### Q29 — Multiple choice

Which statement about Adam and learning rate is correct?

- **A.** Adam eliminates base learning-rate tuning because its moment estimates guarantee stable convergence for any chosen step size.

- **B.** Adam uses gradient-moment estimates to adapt parameter updates, but still has a base learning-rate hyperparameter.

- **C.** Adam uses only a running mean of gradients, so it is exactly SGD with momentum and has no second-moment adaptation.

- **D.** Increasing Adam's base learning rate cannot destabilize training because all adaptive updates are independent of that rate.

### Q30 — Multiple choice

A camera only rotates about its optical centre while viewing a static scene. Why is this unsuitable as the sole initialization for ordinary depth triangulation?

- **A.** The pure-rotation homography is invertible, so its inverse already provides each point's unique metric depth.

- **B.** There is no translation baseline and no depth-dependent parallax.

- **C.** Higher image resolution creates a metric translation baseline even when the optical centre stays fixed.

- **D.** A pure rotation makes all otherwise visible feature correspondences invalid.

## Part B — Numerical values

### Q31 — Numerical

A world-to-camera extrinsic transform is Xc=R@Xw+t, with R=[[0,0,1],[0,1,0],[-1,0,0]] and t=[-3,2,1] metres. Report the Euclidean distance of the camera centre from the world origin. Use C=-R.T@t.

**Answer:** ____________________

### Q32 — Numerical

An RGB image has per-channel means [80,40,20]. A pixel has RGB value [100,30,10]. Grey-World correction uses target=(80+40+20)/3, then corrected = pixel/channel\_means\*target. Ignore clipping and quantization. Report the corrected green value.

**Answer:** ____________________

### Q33 — Numerical

Weighted photometric stereo minimizes sum\_j (w[j]\*(L[j]@g-i[j]))^2. The last light vector's magnitude also encodes its strength. Report g[2].

```python
import numpy as np
L = np.array([[1,0,0],[0,1,0],[0,0,1],[1,1,1]], dtype=float)
i = np.array([.2,.3,.6,1.2])
w = np.array([1,1,1,2], dtype=float)
```

Provided routine: `np.linalg.lstsq(L*w[:,None], i*w, rcond=None)[0]` minimizes the stated weighted residuals.

**Answer:** ____________________

### Q34 — Numerical

Use the simplified Phong model I = Ia + kd\*max(n dot l,0) + ks\*max(v dot r,0)^s. Let Ia=0.1, kd=0.6, n dot l=0.5, ks=0.8, v dot r=0.5, and s=4. Report I.

**Answer:** ____________________

### Q35 — Numerical

Linearly stretch intensities from input range [50,150] to [0,255]. Report the output for input intensity 70. No clipping is needed for this value.

**Answer:** ____________________

### Q36 — Numerical

For the binary image below, compute the number of foreground components under 4-connectivity and under 8-connectivity. Report count4-count8 as one exact integer. Background is not counted.

```text
1 0 1 0 0
0 1 0 0 1
0 0 1 0 1
0 0 0 1 0
1 0 0 0 1
```

**Answer:** ____________________

### Q37 — Numerical

Report the centre output of a 3 by 3 median filter on this patch. Use all nine entries and report an exact integer.

```text
[[0, 7,8],
 [8,255,9],
 [10,11,0]]
```

**Answer:** ____________________

### Q38 — Numerical

Construct a magnitude-weighted UNSIGNED HoG histogram from Gx=[3,-3,0,2] and Gy=[4,-4,5,0]. Use angles theta=degrees(atan2(Gy,Gx)) modulo 180. Use nine HARD bins [0,20),[20,40),...,[160,180), numbered 0..8; no interpolation and no histogram normalization. Report the value of bin 2, which covers [40,60) degrees.

Provided functions: `np.arctan2(y,x)` gives quadrant-aware angles in radians; `np.degrees(angle)` converts radians to degrees. Magnitude is `np.sqrt(Gx*Gx+Gy*Gy)`.

**Answer:** ____________________

### Q39 — Numerical

A complex Fourier coefficient is F=-3-4i. Report its principal phase in degrees in the range (-180,180]. Provided function: `np.degrees(np.arctan2(F.imag, F.real))` uses quadrant-aware atan2(y,x).

**Answer:** ____________________

### Q40 — Numerical

In Lucas–Kanade, solve A@[u,v] = -It by least squares and report v.

```python
import numpy as np
A = np.array([[2,1],[1,-1],[0,2],[3,0]], dtype=float)
It = np.array([-5,-1,-3,-6], dtype=float)
```

Provided routine: `np.linalg.lstsq(A, -It, rcond=None)[0]` returns [u,v].

**Answer:** ____________________

### Q41 — Numerical

Report the zero-based index returned by this SSD matching code. NumPy's argmin returns the FIRST minimum in a tie.

```python
import numpy as np
T = np.array([[1,2],[3,4]])
P = np.array([[[2,3],[4,5]],
              [[1,1],[3,5]],
              [[2,2],[2,4]]])
costs = ((P-T)**2).sum(axis=(1,2))
answer = int(np.argmin(costs))
```

**Answer:** ____________________

### Q42 — Numerical

Fit a 2D affine transform by least squares. Source rows are [[0,0],[1,0],[0,1],[1,1]]; target rows are [[2,-1],[4,-1],[3,2],[5,3]]. Build A with rows [x,y,1] and solve A@P=targets. Report the predicted target y coordinate for source (2,3).

Provided routine: `P=np.linalg.lstsq(A, targets, rcond=None)[0]`; prediction is `np.array([2,3,1])@P`.

**Answer:** ____________________

### Q43 — Numerical

Rows contain [nearest\_distance, second\_nearest\_distance] from descriptor matching. Keep a match iff d1/d2 < 0.75 (strict inequality). Report the count kept.

```text
[[.30,.50], [.40,.50], [.60,1.00], [.20,.21], [.10,.40]]
```

**Answer:** ____________________

### Q44 — Numerical

Run ONE assignment/update iteration of 1D k-means with initial centres [0,10] and data [0,2,3,9,11]. Use squared Euclidean distance. Report the updated smaller centre.

**Answer:** ____________________

### Q45 — Numerical

Rows are actual classes; columns are predicted classes. Report MACRO recall as a fraction for this matrix.

```text
[[30,10,0],
 [ 5,10,5],
 [ 0, 2,8]]
```

**Answer:** ____________________

### Q46 — Numerical

Greedy hard NMS processes one class in score order A,B,C,D (all scores distinct). Exact pairwise IoUs are below; fractions mean ordinary division. Suppress a lower-scoring box only when its IoU with a KEPT box is strictly greater than 0.5. Report the number kept.

```text
      A    B    C    D
A     1   3/5  1/3  1/7
B    3/5   1   3/5  1/3
C    1/3  3/5   1   3/5
D    1/7  1/3  3/5   1
```

**Answer:** ____________________

### Q47 — Numerical

A CNN layer uses a valid stride-1 CROSS-CORRELATION, no bias, I=[[1,3,5],[2,-1,4]] and W=[[1,0],[-1,2]]. Its two output positions receive upstream loss gradients [2,-1]. Report dLoss/dW[1,1], with zero-based indices. The derivative sums upstream\_gradient \* the corresponding input value over BOTH output positions.

**Answer:** ____________________

### Q48 — Numerical

A final feature map has shape 9 x 9 x 8. Global average pooling replaces each channel by its spatial mean. A fully connected 5-class head then uses one bias per class. Report the head's trainable parameter count; exclude the backbone.

**Answer:** ____________________

### Q49 — Numerical

Use ORIGINAL YOLO v1, whose output shape is S x S x (5\*B+C): B boxes with 5 values each, and ONE shared C-class probability vector per cell. Let S=7, B=2 and C=4. Report the total number of scalar outputs.

**Answer:** ____________________

### Q50 — Numerical

An ideal rectified stereo pair has focal length f=1200 pixels, baseline B=0.12 metres, and matching horizontal coordinates uL=414, uR=390. Both principal points are equal. Use disparity d=uL-uR and depth Z=f\*B/d. Report Z in metres.

**Answer:** ____________________
