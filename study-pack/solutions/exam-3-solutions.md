# Exam 3 — Answers and explanations
Questions: [Exam 3](../exams/exam-3.md). Source aliases: [coverage map](../COVERAGE.md). Convention warnings: [source notes](../SOURCE_NOTES.md).
## Quick key

| Question | Answer | Question | Answer |
|---|---|---|---|
| 01 | C | 26 | D |
| 02 | C | 27 | A |
| 03 | B | 28 | D |
| 04 | B | 29 | A |
| 05 | A | 30 | B |
| 06 | B | 31 | 260.00 |
| 07 | D | 32 | 0.26 |
| 08 | A | 33 | 6.00 |
| 09 | C | 34 | 0.25 |
| 10 | D | 35 | 9 |
| 11 | B | 36 | 10 |
| 12 | D | 37 | 3 |
| 13 | A | 38 | 5 |
| 14 | B | 39 | 4.38 |
| 15 | B | 40 | 14.62 |
| 16 | C | 41 | 105 |
| 17 | A | 42 | 2.33 |
| 18 | D | 43 | 2.00 |
| 19 | B | 44 | 0.50 |
| 20 | A | 45 | 0.57 |
| 21 | A | 46 | 0.45 |
| 22 | C | 47 | 4448 |
| 23 | C | 48 | 275 |
| 24 | C | 49 | 0.36 |
| 25 | D | 50 | 0.31 |

## Worked solutions

### Q01 — C

**C. n\_w = R.T @ n\_c; translation does not act on a direction vector.**

Normals between rigid coordinate frames transform by rotation only. R maps world directions to camera directions; its transpose maps back. A general non-rigid affine transform would require a different normal rule, which is not asked here.

*Topic: camera. Sources: HC1b pp.35–45; HC2a surface normals; prerequisite linear algebra.*

### Q02 — C

**C. High spatial frequencies can otherwise alias into false lower-frequency patterns.**

Subsampling reduces the representable frequency range. Filtering first suppresses frequencies that the coarse grid cannot represent; smoothing after aliasing does not undo it.

*Topic: filtering. Sources: HC2b pp.93–105; HC5b pp.38–39; Szeliski §3.4.*

### Q03 — B

**B. No; multiple albedo/shading combinations can produce the same image.**

For positive scale c, A'=cA and S'=S/c preserve I, and further spatial ambiguities exist. Priors or extra observations are required.

*Topic: reflectance. Sources: HC2a pp.4–6,21–23,47–48; Lab1.*

### Q04 — B

**B. The model assumes a linear relation between measured intensity and radiance; the response must be linearized or modelled.**

If recorded value is a nonlinear function of radiance, the original linear dot-product equations no longer describe the observations. Camera-response calibration or suitable raw data is needed.

*Topic: photometric. Sources: HC2a pp.19–20,61–62; Lab1.*

### Q05 — A

**A. The interaction of source spectrum, surface spectral reflectance and that channel's spectral sensitivity.**

A channel integrates wavelength-dependent contributions. Material colour alone does not fix measured RGB; illumination and sensor response matter.

*Topic: colour. Sources: HC1b pp.67–71,80–86; Lab1.*

### Q06 — B

**B. An additive constant in height.**

Derivatives determine relative height, not the reference height. Fixing a height such as z(0,0)=0 removes this additive ambiguity on a connected region.

*Topic: photometric. Sources: HC2a pp.41–43; Lab1; Forsyth–Ponce §2.2.*

### Q07 — D

**D. Interior outputs remain constant, but outputs near boundaries can be darker.**

Interior samples see a full constant patch and weights sum to 1. At a zero-padded boundary some weighted values are 0. Padding is part of the filter's actual behaviour.

*Topic: filtering. Sources: HC2b pp.47–87; Lab2.*

### Q08 — A

**A. It can fill sufficiently small gaps/holes relative to the element's shape, but need not fill a large cavity.**

Closing is scale- and shape-dependent. It is dilation followed by erosion, not general topological hole filling.

*Topic: morphology. Sources: HC2b pp.39–45; S2.*

### Q09 — C

**C. Its outermost pixel border is removed.**

For a border pixel, part of the tested support lies outside the image and encounters 0. Interior pixels whose entire support is inside survive.

*Topic: morphology. Sources: HC2b pp.27–38; S2.*

### Q10 — D

**D. Each coefficient is multiplied by a frequency-dependent phase factor of unit magnitude; its magnitude is unchanged.**

The translated spectrum is the original spectrum times a unit-magnitude complex exponential. This is exact for a circular shift; cropping/zero-filled shifts can also change magnitude through boundaries. A particular coefficient can have an unchanged phase when its factor is 1.

*Topic: fourier. Sources: HC2b pp.97–104; Szeliski §3.4.*

### Q11 — B

**B. They are complex conjugates, with indices interpreted modulo the image size.**

Real-valued signals have Hermitian symmetry F[-k]=conj(F[k]). Thus magnitudes are symmetric and phases have opposite signs modulo a full turn, where defined.

*Topic: fourier. Sources: HC2b pp.99–104; Szeliski §3.4.*

### Q12 — D

**D. Reflectance or illumination changes can also cause an intensity edge.**

Image derivatives measure appearance changes. Material boundaries, shadows, highlights and orientation changes can create edges without a depth break.

*Topic: features. Sources: HC3a; S3 introduction; HC2a.*

### Q13 — A

**A. To locate distinctive structures at their characteristic scales; DoG approximates a scale-normalized LoG response.**

Scale selection allows corresponding structures to be detected after resizing. DoG is an efficient approximation, not a guarantee of unlimited viewpoint invariance.

*Topic: matching. Sources: HC4a pp.36–42; S4; Szeliski §7.1.*

### Q14 — B

**B. Gradients remove the constant offset b, and descriptor normalization reduces the common gain a.**

The derivative of aI+b is a times the derivative of I. Orientation and normalized magnitudes are relatively stable, provided clipping, quantization and nonlinear response do not disrupt the assumption.

*Topic: matching. Sources: HC4a pp.41–44; Szeliski §7.1.2 pp.434–436.*

### Q15 — B

**B. It is geometrically degenerate and does not uniquely constrain a general 2D affine transform.**

All-inlier probability alone is not enough. A minimal sample must also have the geometry required to determine the model. For affine transforms, the [x,y,1] design rows must have rank 3.

*Topic: fitting. Sources: HC4a pp.17–22,45–55; Lab4.*

### Q16 — C

**C. The larger threshold can admit poor matches and outliers as inliers.**

A threshold controls what residual is accepted. Compare fit quality using meaningful units and tolerances, rather than maximizing a count under arbitrarily relaxed criteria.

*Topic: fitting. Sources: HC4a pp.46–48; HC3a pp.99–109.*

### Q17 — A

**A. The appearance-constancy assumption for a physical surface point is violated; apparent image motion need not equal physical surface motion.**

Optical flow describes apparent image change and relies on assumptions. Lighting changes can mimic motion even with stationary geometry. A moving shadow pattern may itself have a consistent image displacement; that is not the underlying surface's displacement.

*Topic: flow. Sources: HC3b pp.8–47,57–58; Lab3.*

### Q18 — D

**D. The object can disappear or become indistinct at coarse levels, so its motion is not initialized correctly.**

Pyramids reduce displacement but also reduce detail. Coarse estimation can miss thin or small structures, and later refinement may remain in the wrong solution basin.

*Topic: flow. Sources: HC3b pp.52–58.*

### Q19 — B

**B. Incorrect predictions can contaminate the model and cause tracking drift.**

Self-labelled updates can learn the occluder or background. Controlled updates and re-detection can help, but no method is universally immune.

*Topic: tracking. Sources: HC3b pp.89–106; Lab3.*

### Q20 — A

**A. Depth-dependent parallax; one global homography need not align the nonplanar scene.**

Translation makes image displacement depend on depth. Blending can hide seams but cannot generally correct incompatible geometric alignments or double images.

*Topic: geometry. Sources: HC4a pp.33–35,60–64; S4; Lab4.*

### Q21 — A

**A. T @ H**

Matrix composition applies the rightmost transformation first: source -> H -> reference -> T -> canvas. Transform direction and multiplication order must be explicit.

*Topic: geometry. Sources: HC4a pp.19,24–35; Lab4.*

### Q22 — C

**C. Unweighted 3-nearest-neighbour majority voting predicts class 0, although the closest example has class 1.**

Squared distances are [.02,.82,.82,16.82]. The three nearest labels are [1,0,0], in an irrelevant tie order for the two zero labels. Their sum is 1, so the comparison is false and prediction=0. k-NN uses labelled examples; it does not update cluster centres. With k=1 the prediction would instead be 1.

*Topic: classification. Sources: HC4b pp.37–53; Lab0.*

### Q23 — C

**C. Spatial terms encourage location coherence, and alpha sets their relative importance against colour differences.**

K-means uses the metric in the supplied feature space. Scaling positions changes distances and can trade colour similarity against spatial compactness; it does not guarantee semantics or connectivity.

*Topic: clustering. Sources: HC5a pp.91–118.*

### Q24 — C

**C. It permits margin violations while balancing fit against regularization.**

A hard-margin separator is infeasible for nonseparable labels. Soft margin penalizes violations and controls model complexity; it does not know which labels are wrong.

*Topic: classification. Sources: HC4b pp.69–78.*

### Q25 — D

**D. The probabilities are well calibrated to actual correctness frequencies.**

Softmax produces a normalized score distribution, but calibration is a separate empirical property. A high score alone is not proof that its stated frequency matches reality.

*Topic: metrics. Sources: HC5a p.5; HC5b p.78; prerequisite probability.*

### Q26 — D

**D. Prevent unintended accumulation of earlier batches' gradients before this batch's update.**

PyTorch gradient buffers accumulate unless cleared. Clearing gradients does not reset parameter values or disable gradient recording. Deliberate gradient accumulation is possible, but would need a different specified training schedule.

*Topic: optimization. Sources: Lab5 tutorial and training code.*

### Q27 — A

**A. A compatible shortcut, such as a stride-2 projection, so the tensors have matching shapes.**

Elementwise residual addition requires compatible dimensions. Identity shortcuts work only when the required shape matches; otherwise use an appropriate projection/downsampling path.

*Topic: architectures. Sources: HC6a pp.99–111.*

### Q28 — D

**D. IoU is unchanged, while an unnormalized squared coordinate-error loss generally scales by the square of that factor.**

Intersection and union areas both scale by the square factor, so their ratio stays fixed. Squared coordinate errors also scale by the square factor, without cancellation.

*Topic: detection. Sources: S5 Exercise 4; YOLOv4 §2.2.*

### Q29 — A

**A. The epipoles are at infinity in the horizontal baseline direction.**

The other camera centre projects to a point at infinity when the baseline is parallel to the image plane. Corresponding points lie on horizontal scanlines after rectification.

*Topic: stereo. Sources: HC6b pp.50–90.*

### Q30 — B

**B. SfM estimates camera poses and sparse structure; bundle adjustment refines poses and points jointly; MVS can densify using estimated cameras.**

SfM recovers geometry from correspondences and motion. Ordinary monocular reconstruction retains a global scale ambiguity without a metric reference. MVS and bundle adjustment have different roles.

*Topic: stereo. Sources: HC6b pp.108–149.*

### Q31 — 260.00

**Submit 260.00.** Unrounded reference: `260.0`.

After crop and resize: fy'=300 and cy'=(240-20)/2=110. v'=300\*(1/2)+110=260. Extrinsics do not change.

*Topic: camera. Sources: HC1b pp.24–45; S1.*

### Q32 — 0.26

**Submit 0.26.** Unrounded reference: `0.2625`.

The per-pixel sums are [[10,10],[0,4]], with the zero denominator replaced by 1. Normalized red values are [[.6,.2],[0,.25]]. Their mean is 1.05/4=.2625; submit .26. Normalizing a spatially averaged RGB vector would be a different calculation.

*Topic: colour. Sources: Lab1 Section 1; Lab0 array axes.*

### Q33 — 6.00

**Submit 6.00.** Unrounded reference: `6.0`.

Path A: p=0 along y=0, then q=4 along x=2, giving z\_A=12. Path B: q=0 along x=0, then p=3 along y=3, giving z\_B=6. Difference=6. The field is not integrable because dp/dy=1 differs from dq/dx=2.

*Topic: photometric. Sources: HC2a pp.41–43; Lab1.*

### Q34 — 0.25

**Submit 0.25.** Unrounded reference: `0.25`.

n dot l = (-1/3)\*.6+(2/3)\*.8=1/3. It is positive, so I=.75/3=.25.

*Topic: reflectance. Sources: HC2a pp.12–20; S1; Lab1.*

### Q35 — 9

**Submit 9.** Unrounded reference: `9`.

Erosion leaves only the central pixel (4,4); the isolated corner pixel disappears. Dilation restores the central 3 by 3 block, giving 9 pixels. It does not restore the isolated noise.

*Topic: morphology. Sources: HC2b pp.39–42; S2.*

### Q36 — 10

**Submit 10.** Unrounded reference: `10`.

a+b=[0,10,10], whose median is 10. Both original medians are 0. The difference is 10, a concrete failure of additivity proving that median filtering is nonlinear.

*Topic: filtering. Sources: HC2b pp.47,89–91; Lab2.*

### Q37 — 3

**Submit 3.** Unrounded reference: `3`.

c[3]=1\*h[3]+0\*h[2]+2\*h[1]+0\*h[0]=1+2=3. Wrap-around is part of the defined operation.

*Topic: fourier. Sources: HC2b pp.101–103; Szeliski §3.4.*

### Q38 — 5

**Submit 5.** Unrounded reference: `5`.

The left group has one strong 10 and four connected weak 6s, so all 5 survive. The three 5s on the right have no connection to a strong seed and are discarded.

*Topic: features. Sources: HC3a pp.58–65; S2.*

### Q39 — 4.38

**Submit 4.38.** Unrounded reference: `4.381966011250105`.

M=[[6,1],[1,5]]. lambda\_min=(11-sqrt(5))/2=4.381966. Submit 4.38. The score tests the least constrained direction.

*Topic: features. Sources: S3; Lab3 Sections 2–3.*

### Q40 — 14.62

**Submit 14.62.** Unrounded reference: `14.615915982243466`.

Scale coarse displacement by 8: [14,-4]. Add the residual: [14.25,-3.25]. Magnitude=sqrt(14.25^2+3.25^2)=about 14.62 pixels. Resizing the array alone is not enough.

*Topic: flow. Sources: HC3b pp.48–54; Lab3.*

### Q41 — 105

**Submit 105.** Unrounded reference: `105`.

w^3=.064. log(.001)/log(.936)=104.4417. Ceiling gives 105. A homography would require a different sample size and a larger budget.

*Topic: fitting. Sources: HC3a pp.104–105; Lab4.*

### Q42 — 2.33

**Submit 2.33.** Unrounded reference: `2.3333333333333335`.

The first pair gives c=1,f=2. The next pairs imply a=3g+2,d=2g,b=h,e=4h+2. The last pair gives h=0,g=1. Thus H=[[5,0,1],[2,2,2],[1,0,1]]. At (.5,.5), x'=3.5/1.5=7/3; submit 2.33. Averaging target corner positions would not implement a projective map.

*Topic: geometry. Sources: HC4a pp.47–55; S4.*

### Q43 — 2.00

**Submit 2.00.** Unrounded reference: `2.0`.

Ordinary ratios are [2/3,3/4,1/2,5/6,1/2]. Accepted nearest distances are [2,1,.5], whose maximum is 2. Comparing D1/D2 directly with .7 would use the wrong threshold.

*Topic: matching. Sources: HC4a pp.43–44; S4; Lab4.*

### Q44 — 0.50

**Submit 0.50.** Unrounded reference: `0.5`.

Assignments produce counts [1,2,3]. After normalization by 6, the final bin is 3/6=.5. The fixed vocabulary gives the same histogram length for every image.

*Topic: classification. Sources: HC4b pp.23–28; S4.*

### Q45 — 0.57

**Submit 0.57.** Unrounded reference: `0.5714285714285714`.

The first four predictions are positive. TP=2, FP=2, FN=1. F1=4/(4+2+1)=4/7=.5714286; submit .57. The score exactly at .6 is positive because the rule is inclusive.

*Topic: metrics. Sources: HC4b pp.80–86; S4.*

### Q46 — 0.45

**Submit 0.45.** Unrounded reference: `0.45`.

Cumulative precisions are [0,1/2,1/3,2/4,3/5], recalls [0,1/4,1/4,2/4,3/4]. The future-maximum precision at each TP is .6. Three increments of .25 contribute .25\*.6 each, so AP=.45. The missing final quarter of recall contributes zero; raw uninterpolated AP would instead be .40.

*Topic: metrics. Sources: HC5a pp.68–78; S4.*

### Q47 — 4448

**Submit 4448.** Unrounded reference: `4448`.

Counts are (64+1)\*16=1040, (3\*3\*16+1)\*16=2320, and (16+1)\*64=1088. Total=4448. The identity shortcut has no parameters.

*Topic: architectures. Sources: HC5b pp.70–73; HC6a pp.107–111; S5.*

### Q48 — 275

**Submit 275.** Unrounded reference: `275`.

Each filter has 3\*3\*3\*2=54 weights. Five filters and five biases give (54+1)\*5=275. Do not count frames as independent input channels for this 3D convolution.

*Topic: cnn. Sources: S5 Exercise 5.*

### Q49 — 0.36

**Submit 0.36.** Unrounded reference: `0.36`.

Box confidence=.75\*.6=.45. Class-specific score=.8\*.45=.36. The convention is explicitly given because different YOLO versions use different outputs and targets.

*Topic: detection. Sources: HC6a pp.66–72; SOURCE\_NOTES.*

### Q50 — 0.31

**Submit 0.31.** Unrounded reference: `0.3125`.

Sensitivity magnitude is 180/144=1.25 metres per pixel. Multiply by .25: .3125 metres, so submit .31. Depth becomes increasingly sensitive to disparity errors at small disparity/large depth.

*Topic: stereo. Sources: HC6b pp.84–90; Szeliski §12.1; prerequisite calculus.*
