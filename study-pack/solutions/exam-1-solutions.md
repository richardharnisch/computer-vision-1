# Exam 1 — Answers and explanations
Questions: [Exam 1](../exams/exam-1.md). Source aliases: [coverage map](../COVERAGE.md). Convention warnings: [source notes](../SOURCE_NOTES.md).
## Quick key

| Question | Answer | Question | Answer |
|---|---|---|---|
| 01 | B | 26 | A |
| 02 | A | 27 | D |
| 03 | A | 28 | C |
| 04 | A | 29 | A |
| 05 | C | 30 | B |
| 06 | D | 31 | -270.00 |
| 07 | C | 32 | 0.75 |
| 08 | B | 33 | 4.00 |
| 09 | C | 34 | 1 |
| 10 | A | 35 | 8 |
| 11 | C | 36 | 8 |
| 12 | B | 37 | 2.83 |
| 13 | A | 38 | 59.04 |
| 14 | D | 39 | 2.36 |
| 15 | B | 40 | 34 |
| 16 | D | 41 | 7.33 |
| 17 | C | 42 | 48.75 |
| 18 | A | 43 | 0.63 |
| 19 | D | 44 | 0.57 |
| 20 | D | 45 | 0.33 |
| 21 | C | 46 | 1680 |
| 22 | B | 47 | 368 |
| 23 | B | 48 | 7850 |
| 24 | B | 49 | 8 |
| 25 | D | 50 | 2.00 |

## Worked solutions

### Q01 — B

**B. C = -R.T @ t**

At the optical centre Xc = 0. Thus R C + t = 0 and C = -R^(-1)t = -R.T t. The translation column is not generally the camera position.

*Topic: camera. Sources: HC1b pp.35–45; S1.*

### Q02 — A

**A. Halve fx, fy, skew, cx and cy; keep R and t unchanged.**

Pixel coordinates change, not the camera pose. The first two rows of K scale by 1/2 and its last row stays [0,0,1]. Scaling the entire K only changes homogeneous scale.

*Topic: camera. Sources: HC1b pp.35–45; S1.*

### Q03 — A

**A. They lie on the same viewing ray from the optical centre.**

Projection retains the direction of a camera-centred ray but loses distance along it. This is a fundamental single-view depth ambiguity.

*Topic: camera. Sources: HC1a; HC1b pp.24–34.*

### Q04 — A

**A. Its outgoing radiance, apart from visibility and camera effects.**

Lambertian radiance is view-independent. Projected area changes with viewpoint, and brightness still depends on the light–normal angle. Do not confuse radiance with the amount of energy collected from a fixed surface area.

*Topic: reflectance. Sources: HC2a pp.12–20.*

### Q05 — C

**C. The component of g perpendicular to that plane is unobservable.**

L has rank at most 2. Any vector in its nullspace can be added to g without changing Lg. More dependent observations cannot supply the missing component.

*Topic: photometric. Sources: HC2a pp.34–39; Lab1.*

### Q06 — D

**D. The normal is undefined; mask or otherwise handle the zero-reflectance/invalid pixel.**

A zero vector has no direction. Adding a small denominator can prevent a numerical exception, but does not recover a physically supported normal.

*Topic: photometric. Sources: Lab1; HC2a pp.35–45.*

### Q07 — C

**C. Interior intensities increase; 0 and 1 remain fixed.**

For r in (0,1), reducing a positive exponent below 1 makes r^gamma larger than r. Always state the power-law convention; some software uses its reciprocal.

*Topic: histogram. Sources: HC2a pp.59–63; S1.*

### Q08 — B

**B. Different provisional labels can later be found to belong to one connected region.**

The first pass can encounter separate branches before their connecting pixels. The second pass resolves recorded label equivalences.

*Topic: morphology. Sources: HC2b pp.7–12.*

### Q09 — C

**C. Opening, then closing.**

Opening removes small foreground structures. Closing fills small background gaps/holes. Either can alter genuine features, so choose element size and shape with care.

*Topic: morphology. Sources: HC2b pp.13–45; S2.*

### Q10 — A

**A. Flip K horizontally and vertically before the sliding dot product.**

Convolution reverses both spatial offsets. Symmetric kernels conceal this distinction; asymmetric derivative or shift kernels do not.

*Topic: filtering. Sources: HC2b pp.78–80; S2.*

### Q11 — C

**C. 5**

Variances add: sigma^2 = 3^2 + 4^2 = 25. Standard deviations do not add directly.

*Topic: filtering. Sources: HC2b pp.82–87; S2.*

### Q12 — B

**B. sqrt(a\*a + b\*b), arctan2(b, a)**

Magnitude is distance from the origin. Phase is the quadrant-aware angle measured from the positive real axis; NumPy takes (imaginary, real). See SOURCE\_NOTES.md for the slide argument-order issue.

*Topic: fourier. Sources: HC2b pp.97–100; SOURCE\_NOTES.*

### Q13 — A

**A. Convolve the image with the corresponding derivative of the Gaussian.**

d(I\*G)/dx = I\*(dG/dx). Smoothing controls noise before measuring spatial changes.

*Topic: features. Sources: HC3a pp.20–54; S2; Lab2.*

### Q14 — D

**D. Keep the connected weak chain and discard the disconnected chain.**

Strong pixels seed edge following. Weak pixels survive only through a qualifying connection to a strong seed, under the declared neighbourhood rule.

*Topic: features. Sources: HC3a pp.58–65; S2.*

### Q15 — B

**B. Strong intensity variation in two independent directions: a good corner-like feature.**

Both displacement directions produce a large change. One large and one small eigenvalue instead indicates an edge; two small values indicate a flat patch.

*Topic: features. Sources: S3; Lab3 Sections 2–3.*

### Q16 — D

**D. A vertical line cannot be represented by a finite m; an orthogonal-distance line model avoids this problem.**

The slope-intercept model privileges y as the dependent variable. Total least squares uses perpendicular distances and a line representation that admits vertical lines.

*Topic: fitting. Sources: HC3a pp.76–79; S3.*

### Q17 — C

**C. It increases, often sharply.**

The all-inlier sample probability is w^s. A lower w makes such samples rarer. RANSAC can work below 50% inliers, but the required budget can be large.

*Topic: fitting. Sources: HC3a pp.91–109; S3.*

### Q18 — A

**A. A.T @ A: the local second-moment/structure tensor.**

A.T A contains sums of Ix^2, Ix Iy and Iy^2. Its eigenvalues determine whether the local flow estimate is well constrained in both directions.

*Topic: flow. Sources: HC3b p.47; S3; Lab3.*

### Q19 — D

**D. A single common flow vector for all pixels in the window.**

A larger window adds equations but can mix incompatible motions. Local motion consistency, not simply pixel count, matters.

*Topic: flow. Sources: HC3b pp.39–47; Lab3.*

### Q20 — D

**D. Parallelism of lines.**

Affine transforms preserve parallelism and ratios along a line, not general angles or lengths. General homographies preserve straight lines but can map parallel lines to intersecting ones.

*Topic: geometry. Sources: HC4a pp.17–22; S4.*

### Q21 — C

**C. One homography, independent of scene depth.**

Pure rotation makes the image mapping depend on ray direction rather than depth: H = K2 R21 K1^(-1). A planar scene is the other important homography case.

*Topic: geometry. Sources: HC4a pp.33–35; S4.*

### Q22 — B

**B. Without a scale constraint, h = 0 is a trivial minimizer and does not define a homography.**

A homography is defined only up to nonzero scale. The constrained solution is the smallest-eigenvalue eigenvector of A.T A, equivalently the appropriate right singular vector of A.

*Topic: geometry. Sources: HC4a pp.51–55.*

### Q23 — B

**B. The match is ambiguous even if the nearest absolute distance is small.**

Repeated or weakly distinctive patterns can have several nearly equally plausible matches. The ratio compares distinctiveness relative to the next alternative.

*Topic: matching. Sources: HC4a pp.41–44; S4; Lab4.*

### Q24 — B

**B. Represent them identically, because it discards spatial arrangement.**

The vocabulary gives fixed-length count vectors. Plain BoVW is orderless; a spatial extension would be needed to retain layout.

*Topic: classification. Sources: HC4b pp.23–28; S4.*

### Q25 — D

**D. Fit the vocabulary on training descriptors; select settings on validation data; evaluate once on untouched test data.**

Unsupervised preprocessing can still leak information. The validation set selects hyperparameters; the test set measures the final chosen pipeline.

*Topic: classification. Sources: HC4b pp.25–28,55–58; Lab5.*

### Q26 — A

**A. 0**

It finds none of the minority examples: TP = 0 and FN is the minority count. Accuracy alone can hide complete failure on a rare class.

*Topic: metrics. Sources: HC4b pp.80–86.*

### Q27 — D

**D. Translation equivariance: shifting the input shifts the feature map.**

Shared local operations follow translations. Invariance would mean unchanged output; pooling and aggregation can provide limited or additional invariance, not the same property.

*Topic: cnn. Sources: HC5b pp.22–24,64; S5.*

### Q28 — C

**C. Faster R-CNN uses a learned Region Proposal Network; Fast R-CNN normally relies on external proposals such as Selective Search.**

Fast R-CNN shares a full-image convolutional feature map but retains external proposals. Faster R-CNN also learns proposals through an RPN sharing backbone features.

*Topic: detection. Sources: HC5b pp.125–133; HC6a pp.18–38.*

### Q29 — A

**A. ResNet adds compatible activations; U-Net concatenates encoder and decoder features across matching scales.**

Residual addition supports identity-like mappings and gradient paths. U-Net concatenation transfers high-resolution spatial information to the decoder.

*Topic: architectures. Sources: HC6a pp.99–112,122–137.*

### Q30 — B

**B. An epipolar line on which the corresponding point must lie.**

Epipolar geometry reduces correspondence search from 2D to 1D. It does not select a unique point along the line. The nonzero condition excludes the epipole's degenerate zero output.

*Topic: stereo. Sources: HC6b pp.50–65.*

### Q31 — -270.00

**Submit -270.00.** Unrounded reference: `-270.0`.

Xw-C = [2,3,4], Xc = [-3,2,4]. q[0] = 800\*(-3) + 20\*2 + 320\*4 = -1080. Divide by 4: u = -270. A negative pixel coordinate can simply be outside the field of view.

*Topic: camera. Sources: HC1b pp.24–45; S1.*

### Q32 — 0.75

**Submit 0.75.** Unrounded reference: `0.7452154112317649`.

L.T L = diag(1.28,1.28,2.44) and L.T i = [0.384,0.064,1.66]. Thus g = [0.3,0.05,1.66/2.44]. Its norm is about 0.7452, so submit 0.75. Do not normalize g before taking its magnitude.

*Topic: photometric. Sources: HC2a pp.34–39; Lab1; Coding examples Q1,Q5.*

### Q33 — 4.00

**Submit 4.00.** Unrounded reference: `4.0`.

p = -2/2 = -1 and q = -(-1)/2 = 0.5. z(3,4) = 5 + 3\*(-1) + 4\*0.5 = 4. The declared sign convention is essential.

*Topic: photometric. Sources: HC2a pp.41–43; Lab1; SOURCE\_NOTES.*

### Q34 — 1

**Submit 1.** Unrounded reference: `1`.

CDF(1) = (1+3)/8 = 0.5; floor(3\*0.5) = 1. Other equalization conventions can differ, which is why the mapping is specified.

*Topic: histogram. Sources: HC2a pp.51–63; S1.*

### Q35 — 8

**Submit 8.** Unrounded reference: `8`.

Dilation gives [1,1,1,1,1,1,1,1,1,1,0]. Erosion of that fixed-length result gives [0,1,1,1,1,1,1,1,1,0,0], which has 8 foreground entries.

*Topic: morphology. Sources: HC2b pp.13–45; S2.*

### Q36 — 8

**Submit 8.** Unrounded reference: `8`.

The flipped kernel is [[-2,0,3],[0,-1,0],[2,0,1]]. The dot product is -2 + 1 + 4 + 5 = 8. The unflipped result would be different.

*Topic: filtering. Sources: HC2b pp.78–80; S2; Lab2.*

### Q37 — 2.83

**Submit 2.83.** Unrounded reference: `2.8284271247461903`.

F[1] = 1 - 2i - 3 + 4i = -2 + 2i. Its magnitude is sqrt(4+4) = sqrt(8), so submit 2.83.

*Topic: fourier. Sources: HC2b pp.95–104.*

### Q38 — 59.04

**Submit 59.04.** Unrounded reference: `59.04`.

det(M) = 81-9 = 72; trace(M) = 18. R = 72 - 0.04\*324 = 59.04. A positive response alone still needs thresholding and spatial non-maximum suppression.

*Topic: features. Sources: S3; Lab3.*

### Q39 — 2.36

**Submit 2.36.** Unrounded reference: `2.3636363636363638`.

A.T A = [[6,1],[1,2]], A.T(-It) = [13,0]. Solve 6u+v=13 and u+2v=0: u=26/11, v=-13/11. Submit 2.36; forgetting the minus sign reverses the estimate.

*Topic: flow. Sources: HC3b pp.39–47; S3; Lab3.*

### Q40 — 34

**Submit 34.** Unrounded reference: `34`.

The all-inlier probability is 0.6^4 = 0.1296. The ratio of logarithms is approximately 33.18; round upwards, not to the nearest integer. N = 34.

*Topic: fitting. Sources: HC3a pp.104–105; HC4a pp.45–48.*

### Q41 — 7.33

**Submit 7.33.** Unrounded reference: `7.333333333333333`.

H @ [5,4,1] = [11,2,1.5]. Dehomogenize: x' = 11/1.5 = 7.3333, so submit 7.33. The third coordinate is not generally 1.

*Topic: geometry. Sources: HC4a pp.20–22,51; S4.*

### Q42 — 48.75

**Submit 48.75.** Unrounded reference: `48.75`.

Weights are 0.1875, 0.0625, 0.5625 and 0.1875. The weighted sum is 1.875 + 1.875 + 28.125 + 16.875 = 48.75. Do not interchange x and y.

*Topic: geometry. Sources: HC4a pp.24–31; Lab4.*

### Q43 — 0.63

**Submit 0.63.** Unrounded reference: `0.631578947368421`.

TP=12, FP=2+4=6, FN=3+5=8. F1 = 2TP/(2TP+FP+FN) = 24/38 = 0.6315789. Submit 0.63.

*Topic: metrics. Sources: HC4b pp.80–86; S4.*

### Q44 — 0.57

**Submit 0.57.** Unrounded reference: `0.5666666666666667`.

AP = (1/1 + 2/3 + 3/5)/4 = 17/30. The missing relevant image contributes zero, so the denominator is 4, not 3. Submit 0.57.

*Topic: metrics. Sources: HC5a pp.19–24,68–78; S4.*

### Q45 — 0.33

**Submit 0.33.** Unrounded reference: `0.3333333333333333`.

Each area is 24. The intersection is width 4 times height 3 = 12. Union = 24+24-12 = 36. IoU = 12/36 = 1/3; submit 0.33.

*Topic: detection. Sources: HC5a p.62; S4.*

### Q46 — 1680

**Submit 1680.** Unrounded reference: `1680`.

Hout = floor((31+2-5)/2)+1 = 15; Wout = floor((29-3)/2)+1 = 14. Total = 15\*14\*8 = 1680. Count output positions, not input positions.

*Topic: cnn. Sources: HC5b pp.25–43,66–68; S5.*

### Q47 — 368

**Submit 368.** Unrounded reference: `368`.

Each output channel has 5\*3\*3 = 45 weights and one bias. There are 8 output channels, so 8\*(45+1) = 368. Spatial resolution and stride do not change this count.

*Topic: cnn. Sources: HC5b pp.66–73; S5.*

### Q48 — 7850

**Submit 7850.** Unrounded reference: `7850`.

The flattened input has 7\*7\*16 = 784 values. Count 784\*10 weights plus 10 biases = 7850.

*Topic: cnn. Sources: HC5b pp.16–24; S5.*

### Q49 — 8

**Submit 8.** Unrounded reference: `8`.

After conv: r=3,j=1. After pool: r=4,j=2. After second conv: r=4+2\*2=8,j=2. Pooling changes the spacing used by later layers.

*Topic: cnn. Sources: HC5b pp.80–85; HC6a pp.6–9.*

### Q50 — 2.00

**Submit 2.00.** Unrounded reference: `2.0`.

l2=[0,-1,7], so the line is y=7. The candidate has y=9, giving distance | -9+7 | / 1 = 2. This tests the line constraint, not whether the candidate is the true appearance match.

*Topic: stereo. Sources: HC6b pp.50–65.*
