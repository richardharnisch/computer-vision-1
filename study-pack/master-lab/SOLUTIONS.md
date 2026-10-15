# Night Shift — conceptual debrief (spoilers)

Use this **after** attempting a checkpoint. Complete reference functions are in [solutions.py](solutions.py).
They are authored examples, not official lab solutions. Your output plots and training results can vary;
do not memorize one accuracy value as a universal result.

## 1. Booth: colour, intrinsic layers, normals and height

- **01:** Spatial means reduce H,W while retaining channels. Normalized RGB removes a common positive
  gain per pixel, not additive or channel-dependent changes. Grey-World assumes neutral average material;
  a mostly-cardboard view can violate that assumption. HSV separates hue/saturation from value; OpenCV
  uint8 hue is 0–179, while its float hue uses degrees. YCrCb stores Cr before Cb.
- **02:** Recolour the albedo layer and multiply by unchanged shading. Doubling shading doubles reconstructed
  linear intensities before clipping. The explicit mask preserves genuine black material and the background.
- **03:** `lstsq(L,i)` recovers g, then rho=norm(g), n=g/rho. Three independent lights are necessary for this
  unconstrained fit; merely adding dependent images is not enough. Multiplying each row and observation by i
  squares its weight in the LS objective. This suppresses the simulated zero-valued shadow equations but
  emphasizes bright specular contamination. It is not a general robust estimator. In RGB a black channel
  gives g=0, so its direction is undefined; valid channels can still constrain the shared normal.
- **04:** For the declared graph convention, p=-nx/nz, q=-ny/nz. The plane example changes height by
  `4*1+2*(-.5)=3`. Noisy p,q may violate dp/dy=dq/dx, so paths disagree. An anchor fixes the otherwise
  arbitrary additive height constant. Near-zero nz is a height-graph/masking problem, not a reason to
  divide by a tiny epsilon and call the result accurate.

## 2. Signal: smoothing and differentiation are different jobs

- **05:** A normalized Gaussian preserves a constant interior. The outer product is separable, giving two
  K-tap passes instead of a K×K pass. First derivatives are odd, second derivatives even. Differentiation
  amplifies noise; finite truncation changes exact continuous identities.
- **06:** On I=x+2y, the normalized Sobel correlation gives gx=1, gy=2, magnitude=sqrt(5), angle=atan2(2,1).
  Gradient is normal to an intensity edge and points toward increasing brightness in this sign convention.
  Reversing both derivative signs preserves magnitude and unsigned HOG, but reverses signed direction.
- **07:** Gaussian is low-pass; a Laplacian suppresses DC and emphasizes rapid change; DoG is band-pass.
  Sequential discrete filtering, a sampled continuous LoG and a finite-scale DoG need not agree numerically.
  DoG approximates `(k-1)*sigma²*LoG` for nearby scales. Its sign depends on subtraction order. A median
  comparison is useful for impulse noise, not a proof it beats Gaussian on every noise distribution.

## 3. Motion: a number is not necessarily an observable quantity

- **08:** The tensor sums gradient products. Flat patches have two small eigenvalues; straight edges have
  one weak eigenvalue; corners have evidence in two directions. Trace alone cannot distinguish them.
  Shi–Tomasi uses the smaller eigenvalue; Harris uses determinant minus k*trace².
- **09:** Stack `[gx,gy]` rows and solve against `-it`. One patch assumes small motion, brightness constancy,
  sufficient texture and common local motion. An edge cannot determine its tangential displacement.
  Larger windows can combine different motions. Quarter-resolution (2,-1) becomes (8,-4) full-resolution
  pixels, not simply a resized array. Pixels/frame needs frame rate and scene calibration to become m/s.

### RAFT reading debrief

1. A flow colour encodes motion direction and magnitude according to the visualization's key/normalization,
   not object identity. Different motions or changed magnitude normalization can change the same ball's
   colour. Inspect the numeric flow and scale; colour intensity conventions depend on the renderer.
2. Feature/context encoders build representations; all-pairs correlation measures feature similarity;
   recurrent updates use local lookups in a correlation pyramid to refine one working-resolution flow.
   Pooling matching evidence provides larger search ranges without requiring a succession of coarse flow
   solutions. This can help small structures, not guarantee their recovery. RAFT still uses downsampled
   features internally and upsamples its output.
3. Learned features/training can make a network less sensitive to some appearance changes than raw LK.
   Occlusion can still remove a correspondence, and unfamiliar lighting/texture can be out of distribution.
   Do not infer infallibility from learned rather than hand-specified assumptions. This notebook does not
   execute RAFT or establish a RAFT accuracy result.

## 4. Map: descriptor agreement is not geometric agreement

- **10:** Lowe's test compares nearest with second-nearest distance. Ambiguous equal alternatives fail;
  passing is not proof of a physically correct match. A threshold on squared distances must be squared too.
  SIFT's descriptor is 128 values: sixteen magnitude-weighted eight-bin orientation histograms.
- **11:** Three noncollinear pairs constrain an affine transform. Minimal samples are noisy: sample,
  fit, score, retain consensus and refit. Ordinary LS is easily moved by outliers. A larger inlier threshold
  can accept wrong matches. Required random trials rise when inlier fraction decreases or sample size
  increases. Random resampling has probability, not a finite worst-case certainty guarantee.
- **12:** Backward warping visits every destination grid point and asks where to sample the source.
  Forward rounding/splatting can leave unfilled pixels. Coverage is geometric; black is valid image data.
  Feather weights smooth seams but cannot repair parallax, a wrong transform or independent object motion.
  This fixture is affine; arbitrary perspective views require a compatible projective model, not blind reuse.

## 5. Sorter: evaluate what was actually learned

- **13:** Spatial sizes: N×3×32×32 → N×8×32×32 → N×8×16×16 → N×16×16×16 →
  N×16×8×8 → N×16 → N×3. Parameter counts: 224 + 1168 + 51 = **1443**. Stride/pooling change
  activation positions and compute, not the shared convolution weight count.
- **14:** `zero_grad` clears gradients, not weights; backward accumulates gradients, step updates parameters.
  CE consumes logits. Eval mode controls dropout/BatchNorm; no-grad controls derivative recording.
  Four correct examples plus one wrong example give accuracy .8, not the unweighted batch mean .5.
  Aggregate loss by example count too. Low train and validation performance may be underfitting or failed
  optimization; a train/validation gap suggests a generalization problem. Diagnose rather than memorize
  an optimizer ranking. Zero ReLU weights block useful feature learning while output biases may still move.
- **Initialization/gradients:** Random weights break symmetry. He scales for rectifiers; Xavier uses
  fan-in/fan-out under different assumptions. Saturating activations and products of Jacobians can reduce
  gradients; excessive gains can explode them. Clipping addresses excessive magnitude, not missing signal.
  Appropriate augmentation, regularization and early stopping can improve generalization; validate them.
- **15:** Frozen feature weights are reused; a new head maps features to new meanings. The two-route head
  has `2*(16+1)=34` trainable parameters; total stored parameters are larger. Copying preserves the old task.
  A severe domain shift can make frozen features inadequate; validation can justify fine-tuning more layers.
  This small local transfer experiment is not equivalent to broad ImageNet pretraining.
- **16:** Grad-CAM averages class-score gradients per channel, weights activations, sums and applies ReLU.
  It is a coarse class-related influence visualization. A plausible heatmap is not a causal proof or an exact
  instance mask; a zero map is possible. Background attention motivates controlled checks for shortcuts.

## Final shift report

A defensible report separates implementation checks, observed synthetic outcomes, assumptions and gaps.
You can demonstrate an internally consistent simulated pipeline, but you cannot approve a physical sorter
from that evidence alone. Require real camera/light calibration, representative object instances and
lighting/motion/occlusion tests, an untouched real evaluation set, correct labels and measured runtime,
plus a safe failure/abstention policy. The optional metal photo is an appearance example, not that evaluation.
