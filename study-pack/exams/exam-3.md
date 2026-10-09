# Exam 3 — Synthesis and transfer
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

A unit normal n\_c is expressed in the camera frame. The camera uses Xc=R@Xw+t. Which expression converts the normal to the world frame?

- **A.** n\_w = R.T @ (n\_c-t)

- **B.** n\_w = K @ n\_c, followed by perspective division

- **C.** n\_w = R.T @ n\_c; translation does not act on a direction vector.

- **D.** n\_w = R @ n\_c+t

### Q02 — Multiple choice

You resize an image to one quarter of each spatial dimension by keeping every fourth pixel. Why should a suitable low-pass filter normally be applied BEFORE subsampling?

- **A.** Keeping every fourth pixel is itself an ideal low-pass filter, so preprocessing cannot influence aliasing.

- **B.** It guarantees exact recovery of every original sample, even when the image has frequencies above the coarse-grid limit.

- **C.** High spatial frequencies can otherwise alias into false lower-frequency patterns.

- **D.** Low-pass filtering after subsampling removes aliasing just as reliably as filtering before subsampling.

### Q03 — Multiple choice

A single image is modelled as I=A\*S. Without further constraints, can it uniquely determine both albedo and shading?

- **A.** No, but dividing every pixel by 255 always resolves the ambiguity.

- **B.** No; multiple albedo/shading combinations can produce the same image.

- **C.** Yes, because one RGB pixel always supplies all geometry and material parameters.

- **D.** Yes, if the image has a high enough resolution, regardless of assumptions.

### Q04 — Multiple choice

Why can directly fitting the linear photometric-stereo model to strongly gamma-compressed pixel values be wrong?

- **A.** Normalizing the fitted g removes all gamma effects, so only albedo can be affected by a nonlinear response.

- **B.** The model assumes a linear relation between measured intensity and radiance; the response must be linearized or modelled.

- **C.** Gamma can always be absorbed into one constant camera gain, independent of intensity and light direction.

- **D.** No correction is needed: any common gamma exponent preserves the linear equations exactly under a change of albedo alone.

### Q05 — Multiple choice

What determines a sensor channel's response to an illuminated coloured surface?

- **A.** The interaction of source spectrum, surface spectral reflectance and that channel's spectral sensitivity.

- **B.** Only the surface's colour name, independent of light and sensor.

- **C.** Only the maximum channel value in a different pixel.

- **D.** Only the camera's extrinsic translation.

### Q06 — Multiple choice

An integrable normal-derived gradient field is reconstructed on a connected image domain with known x/y spacing and at least one nonzero slope. Which ambiguity remains without an anchor or boundary height?

- **A.** No height ambiguity remains, because unit-normal normalization already fixes the absolute reference height.

- **B.** An additive constant in height.

- **C.** An arbitrary multiplicative height scale, even though p and q and the x/y spacing are fixed.

- **D.** An independent additive height constant for every pixel, even while all neighbouring derivatives stay fixed.

### Q07 — Multiple choice

Apply a normalized averaging kernel to a constant positive image with zero padding. What is correct?

- **A.** All outputs become zero because averaging removes the DC component.

- **B.** Every output must be identical, including boundaries, for any padding rule.

- **C.** Only corners become brighter because there are fewer neighbours.

- **D.** Interior outputs remain constant, but outputs near boundaries can be darker.

### Q08 — Multiple choice

A closing operation uses a small structuring element. Which statement is safest?

- **A.** It can fill sufficiently small gaps/holes relative to the element's shape, but need not fill a large cavity.

- **B.** Closing removes every isolated foreground component without changing holes.

- **C.** Closing means erosion followed by dilation.

- **D.** One closing always fills every hole in every binary object.

### Q09 — Multiple choice

Erode an all-ones finite image using a centred 3 by 3 all-ones element with outside-image values defined as zero. What happens?

- **A.** Its foreground expands by one pixel outside the image.

- **B.** It remains all ones because every stored pixel is one.

- **C.** Its outermost pixel border is removed.

- **D.** Every interior pixel becomes zero while the border stays one.

### Q10 — Multiple choice

Circularly translate a discrete image by an integer offset. How does the DFT transform under the standard shift theorem?

- **A.** Only magnitude changes; phase is fixed.

- **B.** The spectrum is only reordered by fftshift; individual frequency coefficients never change.

- **C.** Both magnitude and phase must stay unchanged because the image content is the same.

- **D.** Each coefficient is multiplied by a frequency-dependent phase factor of unit magnitude; its magnitude is unchanged.

### Q11 — Multiple choice

For a real-valued image, what relationship holds between opposite-frequency DFT coefficients?

- **A.** Their imaginary components must all be zero, because the original image contains only real values.

- **B.** They are complex conjugates, with indices interpreted modulo the image size.

- **C.** They are always identical in both real and imaginary components, so their phases must also be identical.

- **D.** They are always negatives of each other, so the spectrum is antisymmetric at every opposite-frequency pair.

### Q12 — Multiple choice

A detected intensity edge does not necessarily mark a depth discontinuity. Why?

- **A.** Canny hysteresis guarantees that only physical depth boundaries survive its high threshold.

- **B.** A material boundary cannot affect intensity, so every strong edge must be a depth discontinuity.

- **C.** Increasing Gaussian sigma makes intensity edges uniquely attributable to changes in depth.

- **D.** Reflectance or illumination changes can also cause an intensity edge.

### Q13 — Multiple choice

Why does SIFT search across a Gaussian scale space and use Difference-of-Gaussians extrema?

- **A.** To locate distinctive structures at their characteristic scales; DoG approximates a scale-normalized LoG response.

- **B.** To recover absolute object size in metres from one image.

- **C.** To guarantee invariance to arbitrary projective deformation of every patch.

- **D.** To force all keypoints to have identical pixel scale.

### Q14 — Multiple choice

For positive affine brightness changes I'=aI+b with a>0, why can a normalized gradient-based SIFT descriptor be relatively robust?

- **A.** Dividing pixel coordinates by the focal length removes b.

- **B.** Gradients remove the constant offset b, and descriptor normalization reduces the common gain a.

- **C.** The descriptor stores the original unnormalized RGB values exactly.

- **D.** SIFT estimates and removes every spatially varying shadow without assumptions.

### Q15 — Multiple choice

An affine RANSAC sample contains three correct correspondences, but the three source points are collinear. Why should the sample be rejected?

- **A.** Three pairs supply six scalar equations, so the transform is necessarily unique despite collinearity.

- **B.** It is geometrically degenerate and does not uniquely constrain a general 2D affine transform.

- **C.** An all-inlier sample is always sufficient; degeneracy can occur only when at least one correspondence is wrong.

- **D.** Repeated least-squares refitting of the same three pairs automatically restores the missing rank.

### Q16 — Multiple choice

Increasing the RANSAC inlier threshold gives a model many more counted inliers. Why is this not automatically evidence of a better geometric model?

- **A.** A larger threshold always improves localization accuracy.

- **B.** A threshold has no influence on consensus size.

- **C.** The larger threshold can admit poor matches and outliers as inliers.

- **D.** Every counted inlier has exactly zero residual by definition.

### Q17 — Multiple choice

A stationary scene undergoes a moving cast shadow. A brightness-constancy flow method reports motion in the shadow region. Which interpretation is correct?

- **A.** The appearance-constancy assumption for a physical surface point is violated; apparent image motion need not equal physical surface motion.

- **B.** Increasing the window size always establishes that reported image motion corresponds to physical surface motion.

- **C.** The reported vector must be a sign error, because a static scene guarantees zero estimated flow regardless of illumination.

- **D.** Every measured optical flow vector necessarily equals a 3D object's velocity.

### Q18 — Multiple choice

Why can a coarse-to-fine flow method still fail on a tiny fast-moving object?

- **A.** Small objects always have zero displacement at full resolution.

- **B.** The coarse-level flow already gives exact depth in metres.

- **C.** Pyramids make every flow observable regardless of texture or visibility.

- **D.** The object can disappear or become indistinct at coarse levels, so its motion is not initialized correctly.

### Q19 — Multiple choice

An online tracker updates its appearance model from its own predicted box. What is a major risk during occlusion?

- **A.** Any online update guarantees improved test accuracy.

- **B.** Incorrect predictions can contaminate the model and cause tracking drift.

- **C.** Occlusion automatically provides perfect new positive labels.

- **D.** The model can never change because the initial template is fixed by definition.

### Q20 — Multiple choice

A camera translates while observing a scene with nearby and distant objects. One fitted panorama homography aligns the distant background but not the foreground. What is the main cause?

- **A.** Depth-dependent parallax; one global homography need not align the nonplanar scene.

- **B.** The foreground and background require opposite matrix multiplication orders, even when the transform direction is fixed.

- **C.** The blend ramp is too narrow; widening it guarantees correction of every geometric mismatch.

- **D.** H has the wrong homogeneous scale; multiplying all its entries by a different nonzero scalar corrects foreground without moving background.

### Q21 — Multiple choice

H maps source image coordinates to a reference image. A translation T then moves reference coordinates into a larger panorama canvas. With column vectors, which matrix maps source directly to the canvas?

- **A.** T @ H

- **B.** H @ T

- **C.** H + T

- **D.** H.T @ T, regardless of the coordinate convention

### Q22 — Multiple choice

Which classifier and prediction does this code implement for binary class labels? Squared distances preserve Euclidean neighbour order. Provided routine: `np.argsort(d2)` returns indices sorted by increasing d2.

```python
import numpy as np
X = np.array([[0,0], [0,1], [1,0], [3,3]], dtype=float)
y = np.array([1,0,0,1])
query = np.array([.1,.1])
d2 = ((X-query)**2).sum(axis=1)
nearest = np.argsort(d2)[:3]
prediction = int(y[nearest].sum() > 1)
```

- **A.** K-means predicts class 0 after moving three learned centres; the array y is used only as an initialization seed.

- **B.** Unweighted 3-nearest-neighbour voting predicts class 1 because the closest example's label outweighs both others.

- **C.** Unweighted 3-nearest-neighbour majority voting predicts class 0, although the closest example has class 1.

- **D.** 1-nearest-neighbour classification predicts class 1; the two other selected labels never contribute.

### Q23 — Multiple choice

For pixel clustering, why might features [R,G,B,alpha\*x,alpha\*y] give different segments from [R,G,B]?

- **A.** K-means always returns connected regions even with colour-only features.

- **B.** Adding x,y guarantees the true semantic labels without supervision.

- **C.** Spatial terms encourage location coherence, and alpha sets their relative importance against colour differences.

- **D.** Feature scaling cannot affect Euclidean distances.

### Q24 — Multiple choice

A training set contains label noise and is not linearly separable. Why use a soft-margin rather than a hard-margin linear SVM?

- **A.** It removes every mislabeled point with certainty.

- **B.** It guarantees infinite margin for nonseparable data.

- **C.** It permits margin violations while balancing fit against regularization.

- **D.** It ignores the weight norm entirely and only memorizes pixels.

### Q25 — Multiple choice

A CNN outputs softmax class scores that sum to one. Which conclusion is NOT guaranteed merely by applying softmax?

- **A.** Increasing one logit relative to the others increases its softmax probability.

- **B.** Each output is nonnegative.

- **C.** The outputs sum to one, up to numerical precision.

- **D.** The probabilities are well calibrated to actual correctness frequencies.

### Q26 — Multiple choice

Consider this training sequence from the kind of loop taught in Lab5. What is the purpose of the first line? No executable PyTorch code is required.

```python
optimizer.zero_grad()
loss.backward()
optimizer.step()
```

- **A.** Disable gradient recording for this batch while retaining earlier batches' stored gradients.

- **B.** Reset learned model parameters to zero, ensuring that each batch starts from the same initialized network.

- **C.** Normalize every stored gradient to unit norm, so the learning rate becomes irrelevant to the next update.

- **D.** Prevent unintended accumulation of earlier batches' gradients before this batch's update.

### Q27 — Multiple choice

A residual branch changes feature shape from H x W x C to H/2 x W/2 x 2C. What is required for an additive shortcut?

- **A.** A compatible shortcut, such as a stride-2 projection, so the tensors have matching shapes.

- **B.** Remove all nonlinearities from the entire network.

- **C.** Add the mismatched tensors with no mapping; addition always changes the channel count automatically.

- **D.** Concatenate them and call the result an identity addition.

### Q28 — Multiple choice

Multiply both a predicted box and its ground-truth box coordinates by the same positive scale. Which property is correct?

- **A.** Both losses must be identical for every pair of boxes.

- **B.** IoU doubles whenever object area doubles.

- **C.** Coordinate error becomes scale invariant just by summing its four components.

- **D.** IoU is unchanged, while an unnormalized squared coordinate-error loss generally scales by the square of that factor.

### Q29 — Multiple choice

For an ideal rectified stereo pair with parallel optical axes and a horizontal baseline, why are epipolar lines parallel?

- **A.** The epipoles are at infinity in the horizontal baseline direction.

- **B.** The fundamental matrix maps every point to the image's principal point.

- **C.** Both cameras have exactly the same optical centre.

- **D.** Every scene point has the same depth.

### Q30 — Multiple choice

Which description of a standard multi-view reconstruction pipeline is correct?

- **A.** Bundle adjustment modifies only colour histograms and never camera parameters.

- **B.** SfM estimates camera poses and sparse structure; bundle adjustment refines poses and points jointly; MVS can densify using estimated cameras.

- **C.** SfM requires only one camera image with no priors or known geometry.

- **D.** MVS always estimates metric scale from arbitrary uncalibrated image content alone.

## Part B — Numerical values

### Q31 — Numerical

An original camera has fx=800, fy=600, cx=320, cy=240 and zero skew. Crop away 40 pixels from the left and 20 from the top; then halve both spatial dimensions. Use continuous coordinates with no half-pixel offsets. A camera-frame point is [0.5,1,2]. Report its final image v coordinate, using the virtual image plane in front of the camera.

**Answer:** ____________________

### Q32 — Numerical

For the RGB image below, compute normalized RGB PER PIXEL, then report the spatial mean of its normalized red channel. For black pixels, define all normalized channels as zero.

```python
import numpy as np
I = np.array([[[6,1,3], [2,6,2]],
              [[0,0,0], [1,1,2]]], dtype=float)
s = I.sum(axis=2, keepdims=True)
safe = np.where(s == 0, 1, s)
normalized = I / safe
answer = normalized[:, :, 0].mean()
```

Provided function: `np.where(condition, a, b)` selects a where the condition is true and b elsewhere. Black pixels are included in the spatial mean.

**Answer:** ____________________

### Q33 — Numerical

Let estimated height gradients be p(x,y)=dz/dx=y and q(x,y)=dz/dy=2x. Start with z(0,0)=0. Integrate continuously to (2,3) along path A: x first then y; and path B: y first then x. Report the absolute difference between the two resulting heights.

**Answer:** ____________________

### Q34 — Numerical

Use calibrated Lambertian intensity I=rho\*max(n dot l,0), with unit vectors n=[2/3,-1/3,2/3] and l=[0,0.6,0.8], rho=0.75, and unit light strength/gain. Report I.

**Answer:** ____________________

### Q35 — Numerical

A 9 by 9 binary image is zero except for a 3 by 3 all-ones block at rows 3..5 and columns 3..5 (inclusive, zero-based), and a single foreground pixel at (0,0). Apply opening with a centred 3 by 3 all-ones element, zero outside the image, retaining the same shape after each stage. Report the final foreground-pixel count.

**Answer:** ____________________

### Q36 — Numerical

Use the median of three entries: `med(v)=sorted(v)[1]`. Let a=[0,0,10] and b=[0,10,0], with elementwise addition. Report med(a+b)-med(a)-med(b) as an exact integer.

**Answer:** ____________________

### Q37 — Numerical

For f=[1,0,2,0] and h=[0,1,0,1], use 4-point CIRCULAR convolution c[k]=sum(n=0..3) f[n]\*h[(k-n) modulo 4]. Report c[3] as an exact integer. This is the result of multiplying their unpadded 4-point DFTs and applying the inverse DFT.

**Answer:** ____________________

### Q38 — Numerical

The grid below contains gradient magnitudes AFTER non-maximum suppression. Use 8-neighbour Canny hysteresis: strong means >=9; weak means >=4 and <9; lower values are rejected. Retain every weak pixel connected through weak/strong pixels to a strong pixel. Report the retained pixel count.

```text
10 6 0 0 5 5 0
 0 6 0 0 0 5 0
 0 6 6 0 0 0 0
```

**Answer:** ____________________

### Q39 — Numerical

Use equal weights for a four-pixel window with Ix=[1,0,1,2] and Iy=[0,2,1,0]. Construct M=[[sum(Ix^2),sum(Ix\*Iy)],[sum(Ix\*Iy),sum(Iy^2)]]. Report the Shi–Tomasi score, the smaller eigenvalue. Provided formula for symmetric [[a,b],[b,d]]: lambda\_min=(a+d-sqrt((a-d)^2+4\*b\*b))/2.

**Answer:** ____________________

### Q40 — Numerical

A flow at one-eighth spatial resolution is [u,v]=[1.75,-0.5] in COARSE pixels. Upsample to full resolution with the correct vector-unit scaling, then add a full-resolution residual flow [0.25,0.75]. Report the Euclidean magnitude of the resulting full-resolution vector.

**Answer:** ____________________

### Q41 — Numerical

An affine RANSAC uses minimal samples of 3 point pairs and independently sampled inlier fraction w=0.4. Assume all-inlier samples are nondegenerate. Use N=ceil(log(1-p)/log(1-w^3)). Report the minimum integer N for p=0.999.

**Answer:** ____________________

### Q42 — Numerical

A nonsingular homography maps these four source points to targets:

```text
(0,0) -> (1,2)
(1,0) -> (3,2)
(0,1) -> (1,4)
(1,1) -> (3,3)
```

Use H=[[a,b,c],[d,e,f],[g,h,1]], so x'=(a\*x+b\*y+c)/(g\*x+h\*y+1), y'=(d\*x+e\*y+f)/(g\*x+h\*y+1). Rearrange the eight scalar equations into a linear system. You may use the provided least-squares routine `np.linalg.lstsq(A, rhs, rcond=None)[0]` to solve a full-rank system. Report the target x coordinate for source (0.5,0.5).

**Answer:** ____________________

### Q43 — Numerical

A matcher returns SQUARED Euclidean distances [D1,D2], nearest first. Apply Lowe's test to the ordinary distances: sqrt(D1)/sqrt(D2)<0.7. For the rows below, report the largest ordinary nearest distance among accepted matches.

```text
[[4,9], [9,16], [1,4], [25,36], [.25,1]]
```

**Answer:** ____________________

### Q44 — Numerical

A 1D visual vocabulary has centres [0,4,8]. Quantize descriptors [1,3,5,7,8,9] to their nearest centre using Euclidean distance. Build counts, then L1-normalize by the number of descriptors. Report the normalized bin value for centre 8.

**Answer:** ____________________

### Q45 — Numerical

A binary classifier predicts positive iff score>=0.6. True labels are [1,0,1,0,1,0] and scores are [.9,.8,.7,.6,.5,.4], in the same order. Report F1 for the positive class as a fraction.

**Answer:** ____________________

### Q46 — Numerical

One class has 4 ground-truth objects. After score-ordered, one-to-one matching, ranked detections are [FP,TP,FP,TP,TP]. Use ALL-POINTS INTERPOLATED AP: sum each positive recall increment times the maximum precision at that recall or any later recall. Precision beyond maximum achieved recall is zero. Report AP as a fraction. This is NOT 11-point AP or raw uninterpolated AP.

**Answer:** ____________________

### Q47 — Numerical

A residual block has an identity shortcut and this dense bottleneck branch: 1 x 1 convolution 64->16 channels; 3 x 3 convolution 16->16; 1 x 1 convolution 16->64. Include one bias per output channel in EACH convolution. There is no normalization layer or trainable shortcut. Report total trainable parameters.

**Answer:** ____________________

### Q48 — Numerical

A standard 3D convolution processes a video tensor with 2 input channels and uses 5 output channels. Each filter has temporal x height x width size 3 x 3 x 3. Include one bias per output channel. No groups. Report the trainable parameter count; the video length and spatial image size do not enter this count.

**Answer:** ____________________

### Q49 — Numerical

Use the ORIGINAL YOLO v1 confidence convention: box\_confidence=Pr(object)\*IoU(predicted\_box,GT); class\_specific\_score=Pr(class|object)\*box\_confidence. Given Pr(object)=0.75, IoU=0.6 and Pr(class|object)=0.8, report the class-specific score.

**Answer:** ____________________

### Q50 — Numerical

For rectified stereo, Z=f\*B/d. Let f=900 pixels, B=0.2 metres, d=12 pixels, and small disparity-error magnitude delta\_d=0.25 pixel. Use FIRST-ORDER error propagation |delta\_Z| approximately (f\*B/d^2)\*|delta\_d|. Report the estimated depth-error magnitude in metres, not the exact finite-difference error.

**Answer:** ____________________
