# Exam 1 — Foundations under pressure
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

A camera uses the world-to-camera convention Xc = R Xw + t. Which expression gives its optical centre C in world coordinates?

- **A.** C = -R @ t

- **B.** C = -R.T @ t

- **C.** C = R.T @ t

- **D.** C = t

### Q02 — Multiple choice

An image is resized to half its original width and height, with no crop. Use the ideal continuous-coordinate model, with no pixel-centre offset. Which change is correct?

- **A.** Halve fx, fy, skew, cx and cy; keep R and t unchanged.

- **B.** Halve only fx and fy; leave the principal point unchanged.

- **C.** Halve R and t; leave K unchanged.

- **D.** Halve every entry of K, including K[2,2], without renormalizing it.

### Q03 — Multiple choice

Under an ideal pinhole model, two distinct visible 3D points have exactly the same image coordinates. What must hold?

- **A.** They lie on the same viewing ray from the optical centre.

- **B.** They have the same physical size.

- **C.** They have the same world X and Y coordinates, regardless of camera pose.

- **D.** They have the same depth.

### Q04 — Multiple choice

Keep illumination, material and surface orientation fixed. For an ideal Lambertian patch, what is independent of viewing direction?

- **A.** Its outgoing radiance, apart from visibility and camera effects.

- **B.** Its total projected area in the image.

- **C.** Its brightness under any change of light direction.

- **D.** Its surface normal in every coordinate frame.

### Q05 — Multiple choice

Twenty calibrated light vectors all lie in one plane through the origin. In the linear photometric-stereo model i = Lg, which claim is correct?

- **A.** Only the albedo is ambiguous; the normal is always unique.

- **B.** Twenty images guarantee a unique g.

- **C.** The component of g perpendicular to that plane is unobservable.

- **D.** Normalizing every light vector makes L full rank.

### Q06 — Multiple choice

A photometric-stereo estimate has g = [0,0,0]. What is the correct interpretation of n = g / ||g||?

- **A.** The normal must be [0,0,1].

- **B.** The surface must be infinitely far away.

- **C.** The division produces a valid zero unit normal.

- **D.** The normal is undefined; mask or otherwise handle the zero-reflectance/invalid pixel.

### Q07 — Multiple choice

For normalized intensity 0 < r < 1, apply s = r^gamma with 0 < gamma < 1. What happens?

- **A.** Every output intensity becomes 1.

- **B.** The result is a linear contrast stretch.

- **C.** Interior intensities increase; 0 and 1 remain fixed.

- **D.** Interior intensities decrease; 0 and 1 remain fixed.

### Q08 — Multiple choice

Why does a two-pass connected-component labelling algorithm store equivalences between provisional labels?

- **A.** It estimates the intensity histogram before labelling.

- **B.** Different provisional labels can later be found to belong to one connected region.

- **C.** It needs to assign a different label to every foreground pixel.

- **D.** It changes 4-connectivity into 8-connectivity automatically.

### Q09 — Multiple choice

Foreground objects contain tiny isolated foreground specks and small background holes. Which sequence directly targets the two defects, assuming suitable structuring elements?

- **A.** Closing, then another dilation.

- **B.** Dilation, then another dilation.

- **C.** Opening, then closing.

- **D.** Erosion, then another erosion.

### Q10 — Multiple choice

You implement a sliding dot product with an asymmetric 2D kernel K. What change converts this cross-correlation to mathematical convolution?

- **A.** Flip K horizontally and vertically before the sliding dot product.

- **B.** Divide K by its sum.

- **C.** Negate K without changing its positions.

- **D.** Transpose K only.

### Q11 — Multiple choice

Two ideal Gaussian smoothing filters with standard deviations 3 and 4 are applied successively. Ignore sampling and truncation. What is the equivalent standard deviation?

- **A.** 25

- **B.** 12

- **C.** 5

- **D.** 7

### Q12 — Multiple choice

A nonzero Fourier coefficient is a + i b. In NumPy's argument convention, which pair gives its magnitude and phase?

- **A.** a + b, arctan2(a, b)

- **B.** sqrt(a\*a + b\*b), arctan2(b, a)

- **C.** a\*a + b\*b, arctan(b/a) for every a and b

- **D.** sqrt(a\*a + b\*b), arctan2(a, b)

### Q13 — Multiple choice

Under valid continuous-domain differentiation and convolution, which operation is equivalent to differentiating a Gaussian-smoothed image?

- **A.** Convolve the image with the corresponding derivative of the Gaussian.

- **B.** Threshold the image and then take a histogram.

- **C.** Convolve the image with the square of the Gaussian.

- **D.** Differentiate the Gaussian's standard deviation instead of a spatial coordinate.

### Q14 — Multiple choice

After Canny non-maximum suppression, a chain of weak pixels connects to a strong pixel; another weak chain is disconnected from all strong pixels. Hysteresis should do what?

- **A.** Keep every weak pixel because it exceeds the low threshold.

- **B.** Discard every weak pixel because it is below the high threshold.

- **C.** Keep whichever chain has the greatest number of pixels, regardless of connection.

- **D.** Keep the connected weak chain and discard the disconnected chain.

### Q15 — Multiple choice

A local structure tensor has two large eigenvalues. What does this indicate?

- **A.** A guaranteed scale-invariant feature at every resolution.

- **B.** Strong intensity variation in two independent directions: a good corner-like feature.

- **C.** A flat patch.

- **D.** A single straight edge with unconstrained tangential motion.

### Q16 — Multiple choice

Why is y = mx + b with vertical-residual ordinary least squares unsuitable for an exactly vertical line?

- **A.** It requires equal x and y measurement variances; unequal variances are the reason a vertical line is unrepresentable.

- **B.** The model becomes valid once both coordinate columns are centred, because centring makes the slope finite.

- **C.** Orthogonal-distance fitting handles vertical lines by forcing m = 0 in the same y = mx + b representation.

- **D.** A vertical line cannot be represented by a finite m; an orthogonal-distance line model avoids this problem.

### Q17 — Multiple choice

For fixed desired success probability and model sample size, what happens to the required RANSAC iteration count when the inlier fraction decreases?

- **A.** It decreases because more points are rejected.

- **B.** RANSAC becomes mathematically impossible as soon as inliers are below 50%.

- **C.** It increases, often sharply.

- **D.** It is unchanged because RANSAC is robust.

### Q18 — Multiple choice

In Lucas–Kanade, A has rows [Ix, Iy]. Which matrix also appears in corner analysis?

- **A.** A.T @ A: the local second-moment/structure tensor.

- **B.** A @ A.T, always a 2 by 2 matrix.

- **C.** The intrinsic calibration matrix K.

- **D.** The homography's last row.

### Q19 — Multiple choice

A Lucas–Kanade window crosses the boundary between two independently moving objects. Which assumption is most directly violated?

- **A.** The image contains any gradients at all.

- **B.** The image has more than one colour channel.

- **C.** The camera has a finite focal length.

- **D.** A single common flow vector for all pixels in the window.

### Q20 — Multiple choice

Which property is preserved by every nonsingular affine image transformation, but not by every projective transformation?

- **A.** All Euclidean lengths.

- **B.** All angles.

- **C.** The location of the origin.

- **D.** Parallelism of lines.

### Q21 — Multiple choice

Two views of a static scene are taken by rotating a camera about exactly the same optical centre. The scene is not planar. Which model still relates the ideal undistorted images?

- **A.** A unique depth-dependent map recovered by inverting the fundamental matrix.

- **B.** No global model can exist unless the scene is planar.

- **C.** One homography, independent of scene depth.

- **D.** A 2D affine map for every possible rotation angle and calibration, without a projective denominator.

### Q22 — Multiple choice

Why impose ||h|| = 1 when solving the homogeneous DLT problem min ||A h||^2 for a homography?

- **A.** Because all nine entries of H must equal 1.

- **B.** Without a scale constraint, h = 0 is a trivial minimizer and does not define a homography.

- **C.** Because every image point must have unit Euclidean norm.

- **D.** Because this fixes lens distortion.

### Q23 — Multiple choice

A descriptor's nearest and second-nearest match distances are almost equal. Why does Lowe's ratio test tend to reject it?

- **A.** Similar distances establish a reliable nearest match; the ratio test should therefore always keep it.

- **B.** The match is ambiguous even if the nearest absolute distance is small.

- **C.** The ratio test rejects it only because the nearest absolute distance must exceed a fixed universal cutoff.

- **D.** It has already been proven to be a geometric outlier; descriptor distances directly establish reprojection error.

### Q24 — Multiple choice

Two images have identical counts of visual words but different arrangements of those words. A plain Bag-of-Visual-Words histogram will do what?

- **A.** Recover their exact layout from the counts.

- **B.** Represent them identically, because it discards spatial arrangement.

- **C.** Require a different number of histogram bins for each image.

- **D.** Use the image labels as its histogram bin values.

### Q25 — Multiple choice

You want a clean estimate of generalization for a BoVW classifier. Which protocol is best?

- **A.** Choose k and vocabulary size using test accuracy, then report that accuracy.

- **B.** Fit the vocabulary on all images, including the test set, to make evaluation easier.

- **C.** Choose every setting using training accuracy alone.

- **D.** Fit the vocabulary on training descriptors; select settings on validation data; evaluate once on untouched test data.

### Q26 — Multiple choice

A classifier predicts the majority class for every example and achieves 99% accuracy on a 99:1 class split. What can its minority-class recall be?

- **A.** 0

- **B.** 1

- **C.** 0.99

- **D.** It must equal minority-class precision and be positive.

### Q27 — Multiple choice

Ignoring boundaries, a stride-1 convolution with shared weights most directly provides which property?

- **A.** Exact translation invariance: the whole feature map never changes after a shift.

- **B.** A separate learned kernel for each image location.

- **C.** Exact invariance to every rotation and scale change.

- **D.** Translation equivariance: shifting the input shifts the feature map.

### Q28 — Multiple choice

What is the main proposal-generation difference between Fast R-CNN and Faster R-CNN?

- **A.** Fast R-CNN predicts pixel masks instead of boxes.

- **B.** Fast R-CNN has an RPN and Faster R-CNN removes it.

- **C.** Faster R-CNN uses a learned Region Proposal Network; Fast R-CNN normally relies on external proposals such as Selective Search.

- **D.** Faster R-CNN runs a separate backbone independently on every raw crop.

### Q29 — Multiple choice

Which statement correctly distinguishes the usual skip operations of ResNet and U-Net?

- **A.** ResNet adds compatible activations; U-Net concatenates encoder and decoder features across matching scales.

- **B.** Both use elementwise addition with mismatched channel counts; the addition automatically supplies the missing channels.

- **C.** Both normally concatenate along the channel axis, so every skip doubles the number of channels.

- **D.** ResNet concatenates encoder/decoder features; U-Net adds an identity tensor to each residual branch.

### Q30 — Multiple choice

Given a homogeneous image point x in image 1 and fundamental matrix F, with F x nonzero, what does F x specify in image 2?

- **A.** The unique matching point, including its depth.

- **B.** An epipolar line on which the corresponding point must lie.

- **C.** A viewing-ray depth that becomes metric once F is normalized to unit Frobenius norm.

- **D.** The matching image point after dehomogenizing F x as if it were a homography output.

## Part B — Numerical values

### Q31 — Numerical

Use column vectors and the virtual image plane in front of the camera. The camera centre is C = [1,2,0], Xw = [3,5,4], and Xc = R @ (Xw-C).

```python
import numpy as np
C = np.array([1,2,0])
Xw = np.array([3,5,4])
R = np.array([[0,-1,0], [1,0,0], [0,0,1]])
K = np.array([[800,20,320], [0,600,240], [0,0,1]])
```

Projection is q = K @ Xc, followed by u = q[0]/q[2]. Report u in pixels.

**Answer:** ____________________

### Q32 — Numerical

For one pixel, use i = Lg, where light strength and camera gain are already absorbed into L. Compute the least-squares estimate, then report albedo rho = ||g||.

```python
import numpy as np
L = np.array([[0,0,1], [.8,0,.6], [-.8,0,.6],
              [0,.8,.6], [0,-.8,.6]])
i = np.array([.70,.64,.16,.44,.36])
```

Provided routine: `g = np.linalg.lstsq(L, i, rcond=None)[0]` minimizes the sum of squared residuals. `np.linalg.norm(g)` returns the Euclidean norm.

**Answer:** ____________________

### Q33 — Numerical

Use the height-field convention n proportional to [-p,-q,1], where p = dz/dx and q = dz/dy. A plane has constant normal proportional to [2,-1,2] and z(0,0) = 5. Report z(3,4), using unit spatial spacing.

**Answer:** ____________________

### Q34 — Numerical

A 2-bit image has histogram counts [1,3,2,2] for levels [0,1,2,3]. Use this specific equalization rule: T(r) = floor(3 \* CDF(r)), with no subtraction of CDF\_min. Report T(1) as an exact integer.

**Answer:** ____________________

### Q35 — Numerical

Close the following 1D binary row with the centred structuring element [1,1,1]. Closing means dilation followed by erosion. At each stage retain exactly 11 entries and treat all out-of-range values as 0. Report the number of foreground entries after closing.

```text
[0,1,1,0,1,1,0,0,1,0,0]
```

**Answer:** ____________________

### Q36 — Numerical

For the 3 by 3 patch I and kernel K below, report the single valid output of mathematical convolution, not cross-correlation. The kernel is flipped on both axes. Report an exact integer.

```text
I = [[1, 2, 0], [3,-1,4], [2,1,5]]
K = [[1, 0, 2], [0,-1,0], [3,0,-2]]
```

**Answer:** ____________________

### Q37 — Numerical

Use the unnormalized DFT F[k] = sum(n=0..3) f[n] exp(-2\*pi\*i\*k\*n/4). For f = [1,2,3,4], report the magnitude of F[1]. You can use exp(-i\*pi/2) = -i and exp(-i\*pi) = -1.

**Answer:** ____________________

### Q38 — Numerical

A patch has structure tensor M = [[9,3],[3,9]]. The Harris response is R = det(M) - k \* trace(M)^2, with k = 0.04. Report R.

**Answer:** ____________________

### Q39 — Numerical

Use Ix\*u + Iy\*v = -It and one constant flow in the window. Compute the least-squares flow and report u.

```python
import numpy as np
A = np.array([[1,0], [0,1], [1,1], [2,0]], dtype=float)
It = np.array([-2,1,-1,-5], dtype=float)
```

Provided routine: `np.linalg.lstsq(A, -It, rcond=None)[0]` minimizes squared residuals.

**Answer:** ____________________

### Q40 — Numerical

A homography RANSAC uses samples of 4 correspondences, each independently an inlier with probability w = 0.6. Report the minimum integer iteration count for success probability at least p = 0.99. Use N = ceil(log(1-p) / log(1-w^4)). Assume all-inlier samples are nondegenerate.

**Answer:** ____________________

### Q41 — Numerical

A homography maps source to target with H = [[2,0,1],[0,1,-2],[0.1,0,1]]. Use column-vector homogeneous coordinates. Report the target x coordinate of source point (5,4).

**Answer:** ____________________

### Q42 — Numerical

Backward warping maps a target pixel to source coordinates (x,y) = (0.25,0.75). Source intensities are I[0,0]=10, I[0,1]=30, I[1,0]=50, I[1,1]=90. Arrays use I[y,x]. Report the bilinear interpolated intensity. The weights are (1-x)(1-y), x(1-y), (1-x)y and xy, respectively.

**Answer:** ____________________

### Q43 — Numerical

Rows of the following confusion matrix are actual classes A,B,C; columns are predicted classes A,B,C. Report the F1 score for class B as a fraction, not a percentage.

```text
[[18, 2, 0],
 [ 3,12, 5],
 [ 1, 4,15]]
```

**Answer:** ____________________

### Q44 — Numerical

A retrieval query has 4 relevant database images in total. In its returned ranking, relevant images occur at ranks 1,3,5; the fourth is not returned. Use uninterpolated AP = (sum of precision at each relevant rank) / total relevant images. Report AP as a fraction.

**Answer:** ____________________

### Q45 — Numerical

Boxes use continuous coordinates [xmin,ymin,xmax,ymax], so width = xmax-xmin, without a +1 correction. Report IoU for A=[0,0,6,4] and B=[2,1,8,5].

**Answer:** ____________________

### Q46 — Numerical

A standard 2D convolution takes an H x W x Cin input of 31 x 29 x 3. Kernel height/width = 5 x 3, stride = 2 x 2, padding = 1 x 0 on EACH side, and Cout = 8. No dilation. Report the total number of scalar outputs, excluding the batch dimension. Use out = floor((in + 2\*pad - kernel)/stride)+1 per axis.

**Answer:** ____________________

### Q47 — Numerical

For the convolution in Q46, report the number of trainable parameters INCLUDING one bias per output channel. It is a dense convolution across all 3 input channels; no groups.

**Answer:** ____________________

### Q48 — Numerical

Flatten a 7 x 7 x 16 feature map and feed it to a fully connected layer with 10 output units. Include one bias per output unit. Report its trainable parameter count.

**Answer:** ____________________

### Q49 — Numerical

A network applies: a 3 x 3 convolution with stride 1; a 2 x 2 pooling layer with stride 2; a 3 x 3 convolution with stride 1. Report the side length of one final unit's theoretical receptive field in original input pixels. Ignore boundaries. Provided recurrence: r\_new = r\_old + (kernel-1)\*j\_old; j\_new = j\_old\*stride; start r=j=1.

**Answer:** ____________________

### Q50 — Numerical

For x2.T @ F @ x1 = 0, let F=[[0,0,0],[0,0,-1],[0,1,0]], x1=[12,7,1] and candidate x2=[9,9,1]. Report the perpendicular distance in pixels from x2 to its epipolar line l2=F@x1. Provided formula: distance = abs(a\*x+b\*y+c)/sqrt(a\*a+b\*b), for line [a,b,c].

**Answer:** ____________________
