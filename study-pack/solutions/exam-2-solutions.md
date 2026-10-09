# Exam 2 — Answers and explanations
Questions: [Exam 2](../exams/exam-2.md). Source aliases: [coverage map](../COVERAGE.md). Convention warnings: [source notes](../SOURCE_NOTES.md).
## Quick key

| Question | Answer | Question | Answer |
|---|---|---|---|
| 01 | C | 26 | B |
| 02 | C | 27 | B |
| 03 | B | 28 | D |
| 04 | B | 29 | B |
| 05 | D | 30 | B |
| 06 | B | 31 | 3.74 |
| 07 | C | 32 | 35.00 |
| 08 | A | 33 | 0.63 |
| 09 | D | 34 | 0.45 |
| 10 | A | 35 | 51.00 |
| 11 | C | 36 | 6 |
| 12 | A | 37 | 8 |
| 13 | B | 38 | 10.00 |
| 14 | C | 39 | -126.87 |
| 15 | A | 40 | 1.34 |
| 16 | A | 41 | 1 |
| 17 | C | 42 | 10.25 |
| 18 | A | 43 | 3 |
| 19 | C | 44 | 1.67 |
| 20 | A | 45 | 0.68 |
| 21 | D | 46 | 2 |
| 22 | D | 47 | -6.00 |
| 23 | D | 48 | 45 |
| 24 | D | 49 | 686 |
| 25 | A | 50 | 6.00 |

## Worked solutions

### Q01 — C

**C. The inverse of R2 @ R1 is R1.T @ R2.T; rotation order generally matters.**

For a product, inverse order reverses. Orthogonality gives R^(-1)=R.T. A proper 3D rotation has 3 degrees of freedom, not 9.

*Topic: camera. Sources: HC1b pp.41–45; HC4a pp.11–19.*

### Q02 — C

**C. Subtract 40 from cx and 20 from cy; keep focal lengths and skew unchanged.**

The new pixel origin changes the principal-point coordinates. Cropping does not change the pose or the pixel scale.

*Topic: camera. Sources: HC1b pp.35–45; S1.*

### Q03 — B

**B. A lightness-based grayscale image of shape (H,W).**

The reduction is per pixel across channels. It is (max RGB + min RGB)/2, a grayscale lightness definition, not weighted luminance or white balance.

*Topic: colour. Sources: Lab1; Coding examples Q2.*

### Q04 — B

**B. I.mean(axis=(0,1), keepdims=True)**

Reducing the two spatial axes retains the channel dimension: shape (1,1,3). Reducing every axis instead gives the same scalar for all channels and defeats Grey-World correction.

*Topic: colour. Sources: Lab1; Coding examples Q3,Q4.*

### Q05 — D

**D. The normal is unchanged; the albedo estimate is doubled.**

i = 2 Lused gtrue, so ghat = 2 gtrue. Its magnitude doubles but its normalized direction remains the same. Calibrated strengths are needed for absolute albedo.

*Topic: photometric. Sources: HC2a pp.19–20,34–39; Lab1.*

### Q06 — B

**B. Change the object's albedo A and multiply the changed A by the original S.**

Albedo represents material colour; shading represents illumination and geometry. Recolour the material layer and reconstruct with the existing shading layer, while respecting the object mask.

*Topic: reflectance. Sources: HC2a pp.47–48; Lab1; Coding examples Q6.*

### Q07 — C

**C. Its surface normals and therefore light–normal dot products can vary.**

Constant material reflectance does not imply constant shading. Geometry and illumination influence intensity independently of the albedo value.

*Topic: reflectance. Sources: HC2a pp.12–23,47.*

### Q08 — A

**A. Which red, green and blue values occur together at the same pixels.**

Marginal distributions lose cross-channel associations. A joint histogram retains colour combinations but still loses spatial arrangement.

*Topic: histogram. Sources: HC2a pp.54–56.*

### Q09 — D

**D. Ignore those positions; require foreground only at active element positions.**

The structuring element specifies the tested support. Inactive positions impose no requirement. Treating their literal zeros as operands in the final AND is a common implementation error.

*Topic: morphology. Sources: HC2b pp.14–29; S2.*

### Q10 — A

**A. Semantic segmentation; no, touching people can merge into one connected component.**

Semantic labels distinguish classes, not individual instances. A connected component of the person-class mask can contain multiple touching people, so plain component labelling is not guaranteed instance segmentation.

*Topic: foundations. Sources: HC5a pp.81–89,120–122; HC2b pp.5–12.*

### Q11 — C

**C. It is less affected by extreme isolated values and can preserve edges better.**

An isolated extreme affects the mean strongly but may not alter the median. The median is nonlinear; its suitability depends on the noise and window.

*Topic: filtering. Sources: HC2b pp.89–91; S2; Lab2.*

### Q12 — A

**A. A sinusoidal pattern modulated by a Gaussian envelope, selective for local frequency and orientation.**

The Gaussian localizes the sinusoid. Varying orientation and frequency produces a useful texture-analysis filter bank.

*Topic: fourier. Sources: HC2b pp.106–107; Lab2.*

### Q13 — B

**B. Circular convolution, with wrap-around at the signal boundaries.**

DFT signals are periodic. To obtain full linear convolution, pad to at least the combined length minus one in each relevant dimension. Otherwise boundary terms wrap around.

*Topic: fourier. Sources: HC2b pp.101–103; Szeliski §3.4.*

### Q14 — C

**C. A vertical edge: intensity changes across x.**

Derivative direction is perpendicular to the edge's tangent. The sign depends on the stated kernel orientation and whether the implementation uses convolution or correlation.

*Topic: features. Sources: HC2b pp.74–80; HC3a; Lab2.*

### Q15 — A

**A. Suppress finer detail and noise, while potentially merging edges and reducing localization precision.**

Smoothing changes the analysis scale. Larger scales emphasize broader structure but can remove or shift fine structures.

*Topic: features. Sources: HC3a pp.20–66.*

### Q16 — A

**A. Compute Ix\*Ix, Ix\*Iy and Iy\*Iy first, then aggregate or smooth those products over the neighbourhood.**

The tensor aggregates the local outer products of gradient vectors. The outer product of the mean gradient is generally different and can cancel gradients of opposite sign. The image Hessian is a different second-derivative matrix.

*Topic: features. Sources: S3; Lab3.*

### Q17 — C

**C. min(lambda1, lambda2)**

Both directions must be constrained. The minimum eigenvalue prevents a strong straight edge from scoring highly just because one direction has a large gradient.

*Topic: features. Sources: Lab3 Section 2; S3.*

### Q18 — A

**A. No; the design matrix has rank 1 and tangential motion remains ambiguous.**

Number of equations does not guarantee independent constraints. Parallel gradients constrain only the normal component of flow: the aperture problem.

*Topic: flow. Sources: HC3b pp.39–47; S3; Lab3.*

### Q19 — C

**C. Multiply displacement components by 2, then warp and refine at the finer level.**

A coarse pixel spans two finer pixels. Vector units must scale with the grid, not just the array's dimensions.

*Topic: flow. Sources: HC3b pp.48–54; Lab3.*

### Q20 — A

**A. SSD can increase even for the true match; a mean-normalized comparison can handle an additive offset better.**

SSD compares raw values. Subtracting patch means before comparison removes a constant offset; zero-mean normalized correlation can additionally address positive gain when variance is nonzero.

*Topic: tracking. Sources: HC3b pp.75–87; HC6b p.103; Szeliski §9.1.*

### Q21 — D

**D. It seeks density modes; kernel bandwidth influences how many modes and clusters are found.**

Mean shift repeatedly moves to a local kernel-weighted mean. It does not need a preset K, but bandwidth and mode-merging rules strongly influence the result.

*Topic: clustering. Sources: HC3b pp.110–122.*

### Q22 — D

**D. Match visible local descriptors and verify a consistent homography; the occluded parts need not match.**

Local descriptors allow the visible part of an instance to support retrieval despite partial occlusion. Ambiguity rejection and geometric verification reduce false matches. The explicitly planar facade permits a homography between ideal undistorted views; not every arbitrary nonplanar scene does.

*Topic: matching. Sources: HC5a pp.14–24; HC4a pp.33–48; S4; Szeliski §7.1.4.*

### Q23 — D

**D. Three point pairs whose source points are noncollinear.**

There are 6 affine parameters and two scalar equations per pair. Three noncollinear source points make the affine design matrix full rank.

*Topic: geometry. Sources: HC4a pp.17–22,50; S4; Lab4.*

### Q24 — D

**D. For each destination pixel, inverse-map its coordinate and sample/interpolate the source; out-of-domain samples still need a boundary rule.**

Backward warping avoids discretization holes within covered regions, but does not create unseen content or automatically prevent sampling artifacts.

*Topic: geometry. Sources: HC4a pp.24–31; Lab4.*

### Q25 — A

**A. Evaluate inner products in a transformed feature space without explicitly constructing all transformed features.**

The classifier can be linear in the implicit feature space while nonlinear in the original space. A valid kernel computes the required feature-space inner products.

*Topic: classification. Sources: HC4b pp.69–78.*

### Q26 — B

**B. The first can be a TP; the second is a duplicate FP unless it can validly match another unmatched object.**

Each ground-truth object can be claimed once. Duplicate detections inflate precision errors even when both boxes localize the same object well.

*Topic: metrics. Sources: HC5a pp.68–78; S4.*

### Q27 — B

**B. A and C.**

Keep A and suppress B. The suppressed B does not itself suppress C; C is compared with retained boxes and survives its low overlap with A.

*Topic: detection. Sources: HC5a pp.63–67.*

### Q28 — D

**D. Symmetric units can receive identical activations and gradients, so they fail to learn distinct features.**

Random weight initialization breaks symmetry. Zero biases are often acceptable with randomized weights. Initializing all weights to zero can introduce further dead-gradient problems, especially with ReLU.

*Topic: optimization. Sources: S5; Lab5 assignment Tasks 5 and 8.*

### Q29 — B

**B. Adam uses gradient-moment estimates to adapt parameter updates, but still has a base learning-rate hyperparameter.**

Adaptation does not remove the need to tune the base step size or other settings. Performance depends on task, initialization, data and optimization settings.

*Topic: optimization. Sources: Lab5 assignment Tasks 3–5; S5.*

### Q30 — B

**B. There is no translation baseline and no depth-dependent parallax.**

Rays can be aligned by rotation, but points at different distances on the same ray are still indistinguishable. SfM initialization normally needs adequate non-panoramic views and parallax.

*Topic: stereo. Sources: HC4a p.34; HC6b pp.114–124.*

### Q31 — 3.74

**Submit 3.74.** Unrounded reference: `3.7416573867739413`.

R.T t = [-1,2,-3], so C=[1,-2,3]. Distance = sqrt(1+4+9)=sqrt(14). Submit 3.74 metres. Rotation preserves length, so ||t|| gives the same distance, but t is still not the world-frame centre C.

*Topic: camera. Sources: HC1b pp.35–45; S1.*

### Q32 — 35.00

**Submit 35.00.** Unrounded reference: `35.0`.

target = 140/3. The green value is (30/40)\*(140/3)=35. Means come from the full image, not this one pixel.

*Topic: colour. Sources: Lab1; Coding examples Q3,Q4.*

### Q33 — 0.63

**Submit 0.63.** Unrounded reference: `0.6307692307692307`.

The fourth row has residual weight squared 4. Relative to [.2,.3,.6], all three components gain the same delta. Solve delta=4\*(.1-3\*delta), giving delta=.4/13. g[2]=.6+.4/13=.6307692; submit 0.63.

*Topic: photometric. Sources: Lab1; HC2a pp.34–39.*

### Q34 — 0.45

**Submit 0.45.** Unrounded reference: `0.45`.

Diffuse = .6\*.5=.3; specular = .8\*(.5^4)=.05. I=.1+.3+.05=.45. The specular exponent acts on the dot product, not on the entire intensity.

*Topic: reflectance. Sources: HC2a p.33.*

### Q35 — 51.00

**Submit 51.00.** Unrounded reference: `51.0`.

The fractional position is (70-50)/(150-50)=.2. Output=.2\*255=51.

*Topic: histogram. Sources: HC2a pp.59–60; S1.*

### Q36 — 6

**Submit 6.** Unrounded reference: `6`.

There are 8 four-connected foreground components. Under 8-connectivity, the diagonal chain, the top (0,2) pixel and the right-hand pair are linked into one component; the bottom-left pixel is the other. Thus 8-2=6.

*Topic: morphology. Sources: HC2b pp.7–12; S2.*

### Q37 — 8

**Submit 8.** Unrounded reference: `8`.

Sorted values: [0,0,7,8,8,9,10,11,255]. The fifth value is 8. The impulse 255 does not dominate the median.

*Topic: filtering. Sources: HC2b pp.89–91; S2; Lab2.*

### Q38 — 10.00

**Submit 10.00.** Unrounded reference: `10.0`.

Magnitudes are [5,5,5,2]. The first two unsigned angles are both about 53.13 degrees; reversing a gradient by 180 degrees preserves unsigned orientation. Both vote into bin 2, so its value is 5+5=10. The other angles are 90 and 0 degrees and go to other bins.

*Topic: features. Sources: S3 Exercise 2; HC3a gradients.*

### Q39 — -126.87

**Submit -126.87.** Unrounded reference: `-126.86989764584402`.

The point is in the third quadrant. Its principal angle is -180 + atan(4/3) = -126.8699 degrees; submit -126.87. atan(4/3) alone gives the wrong quadrant.

*Topic: fourier. Sources: HC2b pp.97–100; SOURCE\_NOTES.*

### Q40 — 1.34

**Submit 1.34.** Unrounded reference: `1.3373493975903614`.

A.T A=[[14,1],[1,6]], A.T(-It)=[29,10]. The determinant is 83; v=(-29+140)/83=111/83. Submit 1.34.

*Topic: flow. Sources: HC3b pp.39–47; S3; Lab3.*

### Q41 — 1

**Submit 1.** Unrounded reference: `1`.

The three costs are [4,2,2]. The first minimum occurs at index 1, not index 2. Broadcasting subtracts T independently from each candidate patch.

*Topic: tracking. Sources: HC3b pp.75–87; Lab0.*

### Q42 — 10.25

**Submit 10.25.** Unrounded reference: `10.25`.

The target-y least-squares coefficients are [.5,3.5,-1.25]. Predicted y=.5\*2+3.5\*3-1.25=10.25. The x and y output coordinates use separate columns of P.

*Topic: geometry. Sources: HC4a pp.17–22,50; Lab4.*

### Q43 — 3

**Submit 3.** Unrounded reference: `3`.

Ratios are [.6,.8,.6,20/21,.25]. Rows 0,2,4 pass, giving 3 matches. These are descriptor candidates, not guaranteed geometric inliers.

*Topic: matching. Sources: HC4a pp.43–48; S4; Lab4.*

### Q44 — 1.67

**Submit 1.67.** Unrounded reference: `1.6666666666666667`.

The first centre gets [0,2,3] and updates to 5/3. The other gets [9,11] and updates to 10. Submit 1.67. Do not average the initial centre itself into its assigned data.

*Topic: clustering. Sources: HC5a pp.91–118.*

### Q45 — 0.68

**Submit 0.68.** Unrounded reference: `0.6833333333333332`.

Class recalls are 30/40=.75, 10/20=.5, 8/10=.8. Macro recall=(.75+.5+.8)/3=.6833333. Submit .68; averaging classes differs from weighting by class frequency.

*Topic: metrics. Sources: HC4b pp.80–86; S4.*

### Q46 — 2

**Submit 2.** Unrounded reference: `2`.

Keep A and suppress B because 3/5>.5. C survives its comparison with A (1/3), so keep C and suppress D (3/5). Retained boxes are A,C; B's overlap with C is irrelevant after B is suppressed. The table can arise from rectangles [0,0,4,2], [1,0,5,2], [2,0,6,2], [3,0,7,2] in continuous corner format.

*Topic: detection. Sources: HC5a pp.63–67.*

### Q47 — -6.00

**Submit -6.00.** Unrounded reference: `-6.0`.

W[1,1] multiplies I[1,1]=-1 in the first patch and I[1,2]=4 in the second. Gradient=2\*(-1)+(-1)\*4=-6. Shared weights accumulate contributions across output positions.

*Topic: cnn. Sources: S5 Exercise 3; HC5b pp.24–33.*

### Q48 — 45

**Submit 45.** Unrounded reference: `45`.

Global pooling produces 8 features. The head has 8\*5 weights plus 5 biases = 45. The parameter-free pooling removes spatial dimensions before the linear layer.

*Topic: cnn. Sources: HC5b pp.64–78; HC6a network architectures; Lab5.*

### Q49 — 686

**Submit 686.** Unrounded reference: `686`.

Each cell has 2\*5+4=14 outputs. There are 7\*7=49 cells, giving 49\*14=686. Do not use B\*(5+C), which is a different per-anchor convention.

*Topic: detection. Sources: HC6a pp.66–72.*

### Q50 — 6.00

**Submit 6.00.** Unrounded reference: `6.0`.

d=24 pixels. Z=1200\*.12/24=6 metres. Use focal length in pixels with pixel disparity; the baseline sets metric units.

*Topic: stereo. Sources: HC6b pp.79–90; Szeliski §12.1.*
