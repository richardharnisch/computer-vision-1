"""Explanations placed before each notebook implementation task, without solved code."""
from textwrap import dedent

NOTES = {
    "01": r"""
#### Why colour needs more than one representation

The camera measures light reflected by the material **and** modified by the illuminant. A channel gain
can therefore change the apparent colour without changing the object. We will compare representations
that answer different questions, then apply one simple colour-constancy assumption.

For a pixel with channels R,G,B, lightness is
$$\ell=\frac{\max(R,G,B)+\min(R,G,B)}{2}.$$
This is not the weighted grayscale/luma conversion used elsewhere. Normalized RGB instead records
relative channel proportions:
$$r=\frac{R}{R+G+B},\quad g=\frac{G}{R+G+B},\quad b=\frac{B}{R+G+B}.$$
A common positive brightness multiplier cancels, but different channel gains do not. At a black pixel
the denominator is zero; the task defines the output as zero rather than inventing a colour.
Opponent channels compare red with green, yellow with blue, and total brightness. Unlike RGB,
the first two opponent channels can legitimately be negative.

Grey-World assumes the **average material colour in the view is neutral**. Let
$$\mu_c=\frac{1}{HW}\sum_{y,x}I_{yxc},\qquad
\bar\mu=\frac{\mu_R+\mu_G+\mu_B}{3},\qquad
I'_{yxc}=I_{yxc}\frac{\bar\mu}{\mu_c}.$$
This estimates three global gains, not a different correction for every pixel. A neutral strip lets
you inspect the result, but this algorithm does not locate or explicitly use that strip.

**Translate to arrays.** Start with `(H,W,3)`. A per-pixel channel reduction removes the last axis;
a spatial channel mean reduces axes `(0,1)`. Retain singleton dimensions when a denominator or gain
must broadcast back over the image. For example, `(H,W,1)` broadcasts per pixel, whereas `(1,1,3)`
broadcasts per channel. Convert to float before arithmetic. Do not stretch negative opponent values
or clip corrected RGB until preparing a display: that would change the quantities you are computing.
""",
    "02": r"""
#### Separate what the object is from how it is lit

An intrinsic-image model writes a linear RGB observation as
$$I(x,y,c)=A(x,y,c)S(x,y).$$
Here A is material reflectance (albedo), and S is a scalar shading field. The simplified model assumes
the same shading factor affects all three channels. It ignores coloured interreflection and specular
highlights. In real images, recovering A and S from I alone is ambiguous; **this task supplies them**.
You are implementing reconstruction and a material edit, not solving intrinsic decomposition.

Painting the displayed image directly would replace shadowed pixels and bright pixels alike, making
the result look flat. Instead, change the material and render it again under the original shading:
$$A'(x,y,:)=\begin{cases}t,&M(x,y)=1,\\A(x,y,:),&M(x,y)=0,\end{cases}
\qquad I'=A'S.$$
The target t is an RGB albedo, not the final observed RGB. A red material can still look dark in shadow.

**Translate to arrays.** Albedo has shape `(H,W,3)`, shading and mask have shape `(H,W)`, and the
target has shape `(3,)`. Boolean selection with the mask selects complete RGB pixels. Make a copy
before replacement so later experiments still have the original albedo. Multiplication needs shading
with shape `(H,W,1)`; otherwise NumPy tries to align W with the colour axis. The mask defines which
material changes; a zero pixel is not a substitute for a mask. Outside the mask, reconstruct the
original material under its shading rather than copying an unshaded albedo value to the output.
""",
    "03": r"""
#### Recover geometry by changing the lights, not the viewpoint

The booth holds the object and camera fixed. Under a diffuse Lambertian model, one pixel observed
under light j satisfies
$$i_j=\rho\,\mathbf l_j^T\mathbf n=\mathbf l_j^T\mathbf g,
\qquad \mathbf g=\rho\mathbf n.$$
The light vector includes the calibrated light direction/intensity convention; the supplied vectors
are normalized. Stacking m exposures gives
$$\underbrace{\mathbf i}_{m\times1}=
\underbrace{L}_{m\times3}\underbrace{\mathbf g}_{3\times1},\qquad
\hat{\mathbf g}=\arg\min_{\mathbf g}\|L\mathbf g-\mathbf i\|_2^2.$$
Three independent light directions are needed to constrain three unknown components. More exposures
make an overdetermined fit, not a guarantee against shadows or highlights. Prefer a least-squares
solver to explicitly forming and inverting the normal equations.

**Translate to arrays.** Reshape `(m,H,W)` into `(m,P)`, where `P=H*W`. Each column now represents
one pixel across all exposures. A multi-right-hand-side least-squares solve returns `(3,P)`.
Recover albedo and normals by
$$\rho_p=\sqrt{g_{1p}^2+g_{2p}^2+g_{3p}^2},\qquad
\mathbf n_p=\mathbf g_p/\rho_p.$$
Reduce the component axis, not the pixel axis. Transpose the normal array to `(P,3)` **before**
reshaping it to `(H,W,3)`; a direct reshape of `(3,P)` mixes channels and pixels. Zero albedo means
no observable normal, and the defined zero output is a validity convention, not a physical direction.

**Why the weighted version is different.** For each pixel, form `D=diag(i)` and solve
$$\min_{\mathbf g}\|DL\mathbf g-D\mathbf i\|_2^2
=\min_{\mathbf g}\sum_j i_j^2(\mathbf l_j^T\mathbf g-i_j)^2.$$
Thus each row of L is multiplied by its corresponding intensity, and the right-hand side contains
intensity squared. A length-m vector must gain a column axis to scale rows of an `(m,3)` array.
Do not use one pixel's D for the entire image: its shadow pattern varies spatially. Zero observations
drop out, but unusually bright specular observations receive **more** influence. The comparison table
tests this limitation rather than assuming weighting is always better.
""",
    "04": r"""
#### Surface orientation tells you a slope, not an absolute height

Represent the surface as a height graph z(x,y), with slopes p and q. Its tangent vectors are
`(1,0,p)` and `(0,1,q)`, whose cross product gives a normal proportional to `(-p,-q,1)`:
$$\mathbf n=\frac{(-p,-q,1)}{\sqrt{1+p^2+q^2}},\qquad
p=\frac{\partial z}{\partial x}=-\frac{n_x}{n_z},\quad
q=\frac{\partial z}{\partial y}=-\frac{n_y}{n_z}.$$
This explains the signs; do not choose them by whether a plot looks like a bump. Our y coordinate
increases down the array, and the surface convention is declared consistently with that coordinate.

Integration adds local height increments along a path. For horizontal spacing Δx and vertical
spacing Δy, an increment is approximately pΔx or qΔy. This exercise sets both spacings to one.
To reach `(y,x)`, first move across row zero, then down column x:
$$z(y,x)=\sum_{a=0}^{x-1}p(0,a)+\sum_{b=0}^{y-1}q(b,x).$$
Empty sums are zero, which fixes the top-left anchor. A cumulative sum must therefore be shifted
into positions starting at index one; including the current pixel's outgoing slope is an off-by-one error.

**Translate to arrays.** Extract the three normal components from the final axis. p and q are HW
arrays. Fill the first row from horizontal increments, then propagate each later row from the row
above using q. This is a deliberately simple path integrator, not a global least-squares reconstruction.
Compute the diagnostic
$$C=\frac{\partial p}{\partial y}-\frac{\partial q}{\partial x}.$$
In NumPy, the y derivative is axis 0 and x derivative is axis 1. For a smooth, integrable field C
should be near zero. Noise can make different paths disagree; discrete differentiation/integration
also introduces approximation error. Adding any constant to z leaves the normals unchanged.
""",
    "05": r"""
#### Smooth nearby pixels without moving the whole image

A Gaussian uses large weights near the centre and smaller weights farther away. Sigma controls its
spread in pixels; radius controls where we truncate its infinite support. They are different parameters.
On integer positions `-r,...,r`, construct
$$\tilde g(x)=e^{-x^2/(2\sigma^2)},\qquad
g(x)=\frac{\tilde g(x)}{\sum_{a=-r}^{r}\tilde g(a)}.$$
Normalize the **actual sampled vector**, rather than assuming the continuous normalization constant
makes a truncated discrete sum exactly one. A unit-sum smoothing kernel preserves a constant image.

Differentiate the Gaussian to obtain filters that respond to change:
$$g'(x)=-\frac{x}{\sigma^2}g(x),\qquad
g''(x)=\left(\frac{x^2}{\sigma^4}-\frac1{\sigma^2}\right)g(x).$$
The first derivative is odd; the second is even. These are sampled analytic derivatives using the
normalized g above, not finite differences of the vector. An odd derivative should have zero sum
up to roundoff. The truncated second derivative can have a small nonzero sum. Neither should be
normalized to unit sum: doing so destroys its meaning or divides by nearly zero.

**Translate to arrays.** x, g, dg and ddg are all length `K=2*radius+1`; powers and products are
elementwise. Forming `outer(g,g)` produces a `(K,K)` kernel. A 2D isotropic Gaussian separates:
$$G(x,y)=g(x)g(y).$$
One horizontal pass and one vertical pass therefore reproduce the 2D filtering with matching boundary
rules, at roughly 2K rather than K² multiply-adds per output pixel. The provided comparison checks
that claim numerically. Symmetric reflection limits artificial borders; it does not make image edges
equivalent to observations outside the camera. When applying **odd** derivative kernels later,
remember that convolution flips a kernel whereas cross-correlation does not.
""",
    "06": r"""
#### Make the direction and strength of an edge measurable

An image gradient consists of two directional derivatives:
$$\nabla I=(I_x,I_y),\qquad
\|\nabla I\|=\sqrt{I_x^2+I_y^2},\qquad
\theta=\operatorname{atan2}(I_y,I_x).$$
The gradient points toward increasing intensity, perpendicular to a local intensity contour. It is
not the direction along the edge. An orientation is not meaningful where both derivatives are zero,
even though a numeric implementation may return zero there.

Our horizontal Sobel operator combines a left/right difference with vertical smoothing:
$$S_x=\frac18\begin{bmatrix}-1&0&1\\-2&0&2\\-1&0&1\end{bmatrix},\qquad S_y=S_x^T.$$
The factor 1/8 makes the interior response to a unit x-ramp equal to one. Here we use **correlation**:
the kernel is used in the written order, so brighter pixels on the right give positive gx. A convolution
with the same written kernel reverses that sign.

**Translate to arrays.** Cast the HW input to float before filtering: unsigned arithmetic cannot
represent negative derivatives. Correlate with each 3×3 kernel using `mode='same'` and
`boundary='symm'`; both results stay HW. Magnitude and angle then use elementwise operations.
An unrestricted matrix norm would collapse the whole image to one number. `atan(gy/gx)` both
divides by zero and loses quadrant information; `atan2` accepts the two arrays directly.
Its argument order is **y component first, x component second**. Keep signed derivatives for later
calculations. Scaling each derivative independently for display would change the recovered angles.
""",
    "07": r"""
#### Find changes at a chosen spatial scale

The Laplacian adds second derivatives in x and y. It responds to rapid spatial changes, but applying
it directly to a noisy image also amplifies noise. Gaussian smoothing selects a scale before measuring
curvature. The continuous identity is
$$\nabla^2(G_\sigma*I)=(\nabla^2G_\sigma)*I.$$
This motivates the first two routes, but their discrete constructions differ. Route one uses a sampled
Gaussian followed by a small finite-difference Laplacian. Route two samples the analytic LoG:
$$\nabla^2G_\sigma(x,y)=
\frac{x^2+y^2-2\sigma^2}{\sigma^4}G_\sigma(x,y).$$
Its centre is negative with this convention, surrounded by positive weights. A constant image should
have zero second derivative. Truncation can leave the sampled kernel with nonzero sum, so subtract
its **mean** to remove that unwanted DC response. This is not unit-sum normalization.

The third route subtracts two smoothing scales:
$$D=G_{k\sigma}*I-G_\sigma*I,\qquad k>1.$$
Broad structures survive both smoothings and largely cancel; very fine structures are suppressed by
both. Intermediate scales remain. For nearby scales,
$$D\approx(k-1)\sigma^2(\nabla^2G_\sigma)*I.$$
Thus matching the location of structures is different from matching their numerical amplitudes.

**Translate to arrays.** Create x and y coordinate grids of shape `(K,K)` on the same support as
`outer(g,g)`, not image-sized grids. Apply every filter with the same output size and boundary mode.
For DoG, construct and normalize a new Gaussian at k*sigma; multiplying the narrow kernel's
values by k does not make it wider. Keep the subtraction signed. Taking an absolute value too early
removes polarity and hides zero crossings. The three maps should resemble related scale-selective
responses, but finite sampling, truncation and different discrete Laplacians prevent exact equality.
""",
    "08": r"""
#### A useful feature constrains motion in two directions

An edge can slide along itself without much appearance change. A corner or textured patch has
intensity variation in more than one direction. Summarize that evidence in a local second-moment matrix:
$$M=\sum_{(x,y)\in W}\begin{bmatrix}I_x^2&I_xI_y\\I_xI_y&I_y^2\end{bmatrix}
=\begin{bmatrix}a&b\\b&c\end{bmatrix}.$$
This is a 2×2 matrix **at every image location**, not one covariance matrix for the entire picture.
Its eigenvalues measure gradient evidence along two principal directions. Both small means flat;
one small means an edge; both large means a promising trackable patch.

Shi–Tomasi uses the smaller eigenvalue, whereas Harris avoids an explicit eigenvalue decomposition:
$$\lambda_{\min}=\frac{a+c-\sqrt{(a-c)^2+4b^2}}2,\qquad
R=ac-b^2-k(a+c)^2.$$
Harris scores can be negative at edges; that is expected. Positive definiteness comes from gradient
information, not from replacing every negative score by zero.

**Translate to arrays.** First form the three HW product images, **then** aggregate each spatially.
Squaring an averaged gradient is not the same operation as averaging squared gradients: opposing
gradients could cancel before their evidence is counted. `uniform_filter` computes a mean, so multiply
by the window area to obtain the sums required here. The window parameter is a side length, making
the area `window**2`. Combining the resulting a,b,c arrays elementwise yields full-image score maps.
The helper performs thresholding, local-maximum selection and border exclusion afterwards. Your
function should return scores, not an already-thresholded list of coordinates.
""",
    "09": r"""
#### Turn brightness constancy into a solvable local system

If a visible point moves by (u,v) between nearby frames without changing brightness,
$$I(x+u,y+v,t+1)\approx I(x,y,t).$$
A first-order Taylor expansion gives the optical-flow constraint
$$I_xu+I_yv+I_t=0.$$
One pixel provides one equation for two unknowns: this is the aperture problem. Lucas–Kanade adds
the assumption that all pixels in a small patch share the same flow. For P pixels, stack
$$A=\begin{bmatrix}I_x(1)&I_y(1)\\\vdots&\vdots\\I_x(P)&I_y(P)\end{bmatrix},
\quad b=-\begin{bmatrix}I_t(1)\\\vdots\\I_t(P)\end{bmatrix},
\quad \hat{\mathbf v}=\arg\min_{\mathbf v}\|A\mathbf v-b\|^2.$$
The solution has just two components, regardless of patch size. The matrix `A.T@A` is the same
gradient-product structure studied in checkpoint 08. Its smaller eigenvalue tells us whether there
is enough evidence for motion in **both** directions. A numerical least-squares solver can return a
minimum-norm vector for a rank-deficient edge, but that does not make the missing component observable.

**Translate to arrays.** Flatten gx,gy,it in the same order so each row describes the same pixel.
Stack gx and gy as **columns**, producing `(P,2)`, not `(2,P)`. Negate it because the supplied temporal
difference is second frame minus first frame. Test conditioning before solving; return the specified
NaNs when the patch cannot support a two-dimensional estimate. The result is `(u,v)`, not `(row,column)`.

The small displacement is essential to the linear approximation. Repeated warping or image pyramids
can extend the useful range, but this task implements one local solve. A brightness jump breaks the
model even when motion has not changed. The helper's long arrows are display scaling only; never
multiply the returned flow by that factor when converting pixels/frame into physical speed.
""",
    "10": r"""
#### A descriptor is local evidence, not a unique identity

SIFT detects stable locations across scale, assigns a dominant orientation, and describes a normalized
neighbourhood using gradient histograms. Its usual descriptor contains 4×4 spatial cells with eight
orientation bins each: 128 values. The provided extractor does this work. You implement the decision
about which descriptors correspond across cameras.

For descriptors a_i and b_j, use Euclidean distance
$$d_{ij}=\|a_i-b_j\|_2.$$
For each a_i, let d₁ and d₂ be its smallest and second-smallest distances to **different candidates**
in camera B. Keep the nearest neighbour only when `d1 < threshold*d2`. This tests distinctiveness:
a small best distance is less convincing if another candidate is almost equally good. It does not
enforce mutual matching or geometric agreement; those are separate tests.

**Translate to arrays.** For N source and M target descriptors, the distance table is `(N,M)`.
Search/sort along its target axis, independently for each source row. You need both target indices
and distance values: the returned pair is `(source_index, nearest_target_index)`, not two distances.
Avoid taking square roots by using
$$\|a-b\|^2=\|a\|^2+\|b\|^2-2a^Tb,$$
but then the retention test is `d1_squared < threshold**2*d2_squared`. Floating-point subtraction
can produce tiny negative squared distances; clamp those to zero before interpreting them. Equal
zero-distance alternatives remain ambiguous and must be rejected. Return an integer `(0,2)` array
when no matches survive, so downstream column indexing still has a defined shape.
""",
    "11": r"""
#### Separate transformation estimation from outlier rejection

An affine map can translate, rotate, scale and shear a plane:
$$\begin{bmatrix}x'\\y'\end{bmatrix}=
\underbrace{\begin{bmatrix}a&b&t_x\\c&d&t_y\end{bmatrix}}_{M}
\begin{bmatrix}x\\y\\1\end{bmatrix}.$$
There are six unknowns; each matched pair supplies two equations. With source points as N×2 rows,
append ones to form X of shape N×3. Solve `X@C ≈ dst` for the two right-hand sides together;
C is 3×2, so the requested transform M is its transpose. Three source points must be noncollinear
for X to have rank three. More pairs allow a least-squares fit, but ordinary LS gives outliers influence.

RANSAC treats matches as competing evidence. For each trial: sample three distinct pairs, fit a
candidate, predict **all** target points, and measure target-plane residuals
$$r_i=\|M[x_i,y_i,1]^T-[x'_i,y'_i]^T\|_2.$$
An inlier has residual at most the threshold in pixels. Keep the largest consensus, then fit again
using every pair in that consensus. The final LS fit uses more evidence than the winning minimal
sample. Recompute the reported mask against that final model. Degenerate samples should be skipped,
not terminate the whole search; failure to find any usable consensus should be reported.

**Translate to arrays.** Use one index sample to select corresponding rows in both arrays. Generate
predictions with the same source→target convention as your fitter, and reduce the two-coordinate
residual along axis 1. Keep the boolean mask separately from its integer count. Seed the generator
once outside the loop; resetting it each trial would repeat the same sample. If the inlier fraction is w
and sample size s, an idealized all-inlier sample has probability w^s; for desired success p,
$$T\geq\frac{\log(1-p)}{\log(1-w^s)}.$$
This estimate assumes independent trials and usable geometry; the fixed trial budget is not certainty.
""",
    "12": r"""
#### Estimate geometry first, then resample appearance

An affine transform maps continuous coordinates, but images store samples on integer grids. Forward
mapping source pixels and rounding their destinations can leave holes or place several samples at
one location. Inverse warping instead visits every destination pixel and asks where it came from:
$$\begin{bmatrix}x_s\\y_s\\1\end{bmatrix}=
\begin{bmatrix}M_{00}&M_{01}&M_{02}\\M_{10}&M_{11}&M_{12}\\0&0&1\end{bmatrix}^{-1}
\begin{bmatrix}x_d\\y_d\\1\end{bmatrix}.$$
The forward matrix remains source→destination; only the **sampling query** uses its inverse.
For an affine transform, the last homogeneous coordinate stays one. A projective transform would
also require division by that coordinate, but is not the model used here.

**Translate to arrays.** `np.indices((H,W))` returns y then x. Flatten those grids, stack x,y,ones
as a 3×(H*W) coordinate matrix, transform it, then reshape source x and y to the output HW shape.
Pass those arrays to the supplied sampler in **x,y order**. It uses bilinear interpolation: the four
neighbouring source samples contribute according to fractional horizontal/vertical position. It also
returns a geometric validity mask. Out-of-bounds zeros are padding; in-bounds black pixels are real data.

After both cameras occupy the same canvas, feathering combines them with nonnegative coverage weights:
$$I=\frac{w_AI_A+w_BI_B}{w_A+w_B}.$$
The supplied distance-to-boundary weights favour view interiors. In a region covered only by A,
normalization returns A unchanged. Where neither view contributes, define zero explicitly rather than
divide by zero. For RGB, give HW weights a singleton channel axis so the **same weight** applies to all
channels. Feathering smooths intensity seams; it cannot correct a wrong transform or parallax.
""",
    "13": r"""
#### Learn useful features instead of hand-designing the last decision

The earlier stations use specified filters and geometric models. The sorter instead learns convolution
weights from labelled examples. Each convolution shares its weights across image positions, ReLU
introduces a nonlinearity, and pooling reduces spatial resolution. This task classifies already-provided
object crops; it does not learn to locate objects on a whole belt.

For one spatial axis, a convolution's output size is
$$H_{out}=\left\lfloor\frac{H_{in}+2P-D(K-1)-1}{S}\right\rfloor+1.$$
Here dilation D=1, kernel K=3, stride S=1 and padding P=1 preserve height/width. A 2×2 max pool
with default stride two halves them. Keep a shape trace on paper: batch size N stays unchanged,
convolutions change channel count, and pooling changes spatial dimensions.

Global average pooling converts the final feature maps A into one number per feature channel:
$$f_{nk}=\frac1{H_fW_f}\sum_{y,x}A_{nkyx},\qquad z_n=Wf_n+b.$$
The three entries of z are logits: unnormalized class scores. The next task's cross-entropy handles
their conversion into log probabilities; a softmax layer here would apply the wrong input contract.

**Translate to tensors.** Input is `(N,3,32,32)`, not HWC. Put the two convolution/ReLU/pool blocks
in `self.features`, and the final linear layer in `self.classifier` so transfer and CAM can access them.
Average only spatial dimensions `(2,3)`, retaining batch and feature axes. Do not flatten all 8×8
positions into the classifier: that defines a different architecture and parameter count. Learnable
parameter counts are `(K*K*Cin+1)*Cout` for each biased convolution and `(Din+1)*Dout` for the
linear layer. Pooling, ReLU and spatial averaging add no learned parameters in this architecture.
""",
    "14": r"""
#### Optimizing weights and measuring performance are separate operations

For logits z and correct class y, multiclass cross-entropy is
$$\mathcal L(z,y)=-\log\frac{e^{z_y}}{\sum_c e^{z_c}}
=-z_y+\log\sum_c e^{z_c}.$$
Use PyTorch's stable implementation rather than manually exponentiating scores. Targets are integer
class indices of shape `(N,)`, not one-hot RGB masks. Training computes gradients of the mean batch
loss and lets the optimizer update the parameters.

**Implement the sequence deliberately.** Set training mode first. Clear previous parameter gradients;
PyTorch accumulates them by default. Run the model, compute scalar loss, call backward to populate
gradients, then call the optimizer step to change weights. Backward alone does not train the model.
Detach the returned reporting value so history does not retain computation graphs. Do not detach
the logits or loss **before** backward, because that disconnects the learning path.

Evaluation has two separate controls: `eval()` selects inference behaviour for layers such as dropout
and BatchNorm, while `no_grad()` disables recording derivative computations. Neither replaces the
other. Predict each sample by the largest logit along the class axis. There is no need to compute
softmax first because it preserves score ordering.

**Aggregate by examples, not by batches.** If batch b has n_b examples and mean loss L_b,
$$L_{dataset}=\frac{\sum_b n_bL_b}{\sum_b n_b},\qquad
accuracy=\frac{\sum_b correct_b}{\sum_b n_b}.$$
Alternatively accumulate sum-reduced batch losses. Averaging batch means directly overweights a
short final batch. Confusion entry `(i,j)` counts true class i predicted as j; increment every example,
including repeated pairs. Derive the number of classes from the logit width, since the later routing
head has two outputs rather than three. Use validation to make choices; reserve the test split for
the final run, not repeated learning-rate selection.
""",
    "15": r"""
#### Reuse a representation while changing what its outputs mean

The trained sorter can be viewed as two functions:
$$z=h_\phi(f_\theta(x)).$$
The feature extractor f has learned spatial responses to this small source task. The head h maps
those responses to the original three classes. The new routing task has two meanings, so the old
head is not reusable simply by keeping its first two output columns. Replace it with a new two-output
head and learn that mapping using route-labelled data.

Freezing the backbone means optimizing only the new head parameters φ, while preserving θ. The
inputs now also have a changed channel gain, providing a small domain shift. Whether frozen features
remain useful is an empirical validation question, not a guarantee of transfer learning. Large real
domain shifts can require fine-tuning some feature layers and more representative data.

**Translate to model operations.** Deep-copy the whole source before changing anything. An assignment
like `adapted=source` creates an alias, so replacing its head would also destroy the three-class sorter.
Disable gradients for the copied feature parameters, then install a newly initialized linear head with
the same 16 input features and two outputs. Its weights and biases must remain trainable. The existing
training driver builds an optimizer from parameters that require gradients.

Freezing, evaluation mode and no-grad do different jobs. A frozen feature extractor can still run in
training mode; dropout/BatchNorm behaviour would matter in a more complex backbone. Conversely,
wrapping the **entire** adapted forward pass in no-grad would prevent learning the new head. This
particular backbone has no dropout or BatchNorm, but keep the distinctions clear for other networks.
Only the head's `16*2+2` parameters should update; frozen weights still occupy memory and compute.
""",
    "16": r"""
#### Ask which feature locations support a class score

A correct classification does not reveal whether the model used the intended object or a background
shortcut. Grad-CAM builds a coarse class-specific map from feature activations and their influence
on a selected class **logit**. It is a diagnostic, not a segmentation target or proof of causality.

For activation channel k at spatial location (i,j), and selected score s_c, define
$$\alpha_k^c=\frac1{H_fW_f}\sum_{i,j}\frac{\partial s_c}{\partial A_{kij}},
\qquad L^c_{ij}=\operatorname{ReLU}\left(\sum_k\alpha_k^c A_{kij}\right).$$
First average gradients spatially to measure each channel's contribution. Then combine the **spatial
activation maps** using those channel weights. ReLU keeps positive support under this method's
convention. Do not average away the activation locations themselves: that would leave no map to inspect.

**Translate to tensors.** Both inputs have shape `(1,K,Hf,Wf)`. Average gradient axes `(2,3)`, keeping
them as singleton dimensions, to obtain `(1,K,1,1)`. Broadcasting those weights over activations,
then summing channel axis 1, gives `(1,Hf,Wf)`. Select the one batch element to return HW. These
operations stay in PyTorch until you detach and convert the final map to NumPy. The helper already
computes real class-score gradients for you; your task is their correct spatial/channel reduction.

For display, normalize this single map by
$$\hat L=\frac{L-\min L}{\max L-\min L}.$$
If the denominator is zero, return zeros rather than NaNs. This normalization expresses **relative
strength within one map**; it does not make magnitudes comparable across classes or images. The map
is at feature resolution, so it can look blocky beside the input. An empty positive-support map is
possible and does not automatically mean your code is broken. Evaluation mode may be enabled while
autograd remains active: explanations need gradients even when we are not updating weights.
""",
}

NOTES = {key: dedent(value).strip() for key, value in NOTES.items()}
