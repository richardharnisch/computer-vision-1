# CV1 flashcards — 673 cards

Each prompt tests one main fact or distinction. Try to answer before opening the back. Formulas use ordinary text, not rendered mathematics.

**core** = direct emphasis in the lecturer checklist or a closely related calculation/failure mode. **breadth** = other taught content, supporting names and details. These labels are study priorities, not predictions.

Import version: [Anki TSV](flashcards-anki.tsv). Source aliases: [coverage](COVERAGE.md). Conventions and source issues: [notes](SOURCE_NOTES.md).

## Topics

- [foundations](#foundations) — 19 cards
- [camera](#camera) — 47 cards
- [colour](#colour) — 35 cards
- [reflectance](#reflectance) — 27 cards
- [photometric](#photometric) — 29 cards
- [histogram](#histogram) — 14 cards
- [morphology](#morphology) — 26 cards
- [filtering](#filtering) — 37 cards
- [fourier](#fourier) — 23 cards
- [features](#features) — 37 cards
- [fitting](#fitting) — 24 cards
- [flow](#flow) — 23 cards
- [tracking](#tracking) — 11 cards
- [geometry](#geometry) — 32 cards
- [matching](#matching) — 20 cards
- [clustering](#clustering) — 12 cards
- [classification](#classification) — 29 cards
- [metrics](#metrics) — 24 cards
- [cnn](#cnn) — 45 cards
- [optimization](#optimization) — 33 cards
- [detection](#detection) — 38 cards
- [architectures](#architectures) — 26 cards
- [stereo](#stereo) — 42 cards
- [coding](#coding) — 20 cards

## foundations

### CV1-001 · breadth

**What is computer vision?**

<details>
<summary>Show answer</summary>

Obtaining useful information about a scene or task from images, videos or other visual measurements. It is not just displaying or enhancing images.

*Sources: HC1a pp.3–5.*

</details>

### CV1-002 · breadth

**Why is recovering a 3D scene from one 2D image generally ill-posed?**

<details>
<summary>Show answer</summary>

Different shapes, materials, lighting and depths can produce the same image. Extra observations or prior assumptions are needed to select a solution.

*Sources: HC1a; HC2a pp.4–5.*

</details>

### CV1-003 · core

**What is image classification?**

<details>
<summary>Show answer</summary>

Assign an image to a category or categories. In the single-label setting, output one label for the whole image.

*Sources: HC4b pp.5–9.*

</details>

### CV1-004 · core

**What is object detection?**

<details>
<summary>Show answer</summary>

Identify object instances, assign class labels and locate them, usually with bounding boxes.

*Sources: HC5a pp.25–35.*

</details>

### CV1-005 · core

**What is semantic segmentation?**

<details>
<summary>Show answer</summary>

Assign a semantic class to each pixel, without distinguishing different instances of the same class.

*Sources: HC5a pp.81–89,120.*

</details>

### CV1-006 · core

**What is instance segmentation?**

<details>
<summary>Show answer</summary>

Predict a separate pixel mask and class for each object instance, including multiple objects of the same class.

*Sources: HC5a pp.120–122.*

</details>

### CV1-007 · breadth

**What is panoptic segmentation?**

<details>
<summary>Show answer</summary>

Combine semantic labels for all pixels with separate instance IDs for countable objects; include non-instance stuff such as sky or road.

*Sources: HC5a p.122.*

</details>

### CV1-008 · core

**What is image retrieval?**

<details>
<summary>Show answer</summary>

Rank database images by relevance or similarity to a query, using representations and a similarity measure.

*Sources: HC5a pp.13–24.*

</details>

### CV1-009 · breadth

**What is the semantic gap in image classification?**

<details>
<summary>Show answer</summary>

The gap between low-level pixel values or features and high-level object or scene meanings.

*Sources: HC4b p.8.*

</details>

### CV1-010 · breadth

**Name common sources of variation that make recognition difficult.**

<details>
<summary>Show answer</summary>

Viewpoint, scale, lighting, deformation, occlusion, clutter, intraclass variation and fine-grained differences between classes.

*Sources: HC1a; HC4b pp.9–16.*

</details>

### CV1-011 · breadth

**What is the difference between intraclass variation and interclass similarity?**

<details>
<summary>Show answer</summary>

Intraclass variation: examples of one class look different. Interclass similarity: examples of different classes look alike. Both can confuse recognition.

*Sources: HC4b pp.10–11.*

</details>

### CV1-012 · core

**What does the syllabus say about concepts found only in the textbook?**

<details>
<summary>Show answer</summary>

They are not exam content if absent from the lectures, seminars and labs. Textbook readings support concepts taught in those materials.

*Sources: Syllabus pp.7–8.*

</details>

### CV1-572 · breadth

**What are examples of low-, mid- and high-level vision in the introduction?**

<details>
<summary>Show answer</summary>

Low: colour, contrast, edges. Mid: depth, 3D reconstruction, motion. High: object/activity recognition and instance segmentation. The categories describe task abstraction, not strict isolated modules.

*Sources: HC1a pp.26–28.*

</details>

### CV1-573 · breadth

**What does SLAM stand for?**

<details>
<summary>Show answer</summary>

Simultaneous Localization and Mapping: estimate a sensor's pose while building a map. It is introduced as an application, not an advanced implementation topic here.

*Sources: HC1a p.39.*

</details>

### CV1-574 · breadth

**What does SAM stand for in the introductory segmentation example?**

<details>
<summary>Show answer</summary>

Segment Anything Model, a promptable segmentation model. The introduction gives an application example, not a requirement to implement its architecture.

*Sources: HC1a p.31.*

</details>

### CV1-575 · breadth

**What does CCD stand for and what does it measure?**

<details>
<summary>Show answer</summary>

Charge-Coupled Device. Its sensor elements convert incident photons to accumulated charge for digital image formation.

*Sources: HC1b pp.69–70.*

</details>

### CV1-576 · breadth

**What is a perceptron and who is associated with it?**

<details>
<summary>Show answer</summary>

A weighted-input threshold classifier, associated with Frank Rosenblatt. The slide history gives late-1950s dates; learn the model/name rather than treating the slide dates as consistent.

*Sources: HC5b pp.10,15.*

</details>

### CV1-577 · breadth

**What does MLP stand for?**

<details>
<summary>Show answer</summary>

Multi-Layer Perceptron: a feed-forward network of fully connected layers with nonlinear hidden activations.

*Sources: HC5b pp.16–18.*

</details>

### CV1-578 · breadth

**Which names are associated with the 1943 artificial-neuron model?**

<details>
<summary>Show answer</summary>

Warren McCulloch and Walter Pitts.

*Sources: HC5b pp.10,15.*

</details>

## camera

### CV1-013 · core

**Where is the origin of the pinhole camera coordinate frame?**

<details>
<summary>Show answer</summary>

At the optical centre, also called the pinhole or centre of projection.

*Sources: HC1b p.24; S1.*

</details>

### CV1-014 · core

**What is focal length in the ideal pinhole projection model?**

<details>
<summary>Show answer</summary>

The distance from the optical centre to the model's image plane, expressed in physical units or converted to pixels in K.

*Sources: HC1b pp.21–26.*

</details>

### CV1-015 · core

**What is the virtual-image-plane pinhole projection formula?**

<details>
<summary>Show answer</summary>

For camera point [X,Y,Z] with Z>0: x=f\*X/Z and y=f\*Y/Z. The virtual image plane is in front of the pinhole at Z=f.

*Sources: HC1b pp.24–26; S1.*

</details>

### CV1-016 · core

**How do projection signs differ for the physical image plane behind the pinhole?**

<details>
<summary>Show answer</summary>

With the same axes and a plane at Z=-f, x=-f\*X/Z and y=-f\*Y/Z. The physical image is inverted. Always check the convention.

*Sources: HC1b p.24; S1.*

</details>

### CV1-017 · core

**What determines apparent size in perspective projection?**

<details>
<summary>Show answer</summary>

Projected size is proportional to focal length and physical size, and inversely proportional to distance/depth for a fronto-parallel object.

*Sources: HC1b pp.25–27.*

</details>

### CV1-018 · core

**What happens to apparent object size if depth doubles and focal length stays fixed?**

<details>
<summary>Show answer</summary>

It halves for the ideal fronto-parallel pinhole setting. The image alone does not distinguish size from distance.

*Sources: HC1b pp.25–27.*

</details>

### CV1-019 · breadth

**What happens to field of view when focal length increases for a fixed sensor?**

<details>
<summary>Show answer</summary>

Field of view decreases; projected object size increases.

*Sources: HC1b pp.21–22.*

</details>

### CV1-020 · breadth

**Give the field-of-view formula for a centred pinhole sensor of width W.**

<details>
<summary>Show answer</summary>

Horizontal FOV=2\*atan(W/(2\*f)), with W and f in matching units. A corresponding vertical formula uses sensor height.

*Sources: S1; Forsyth–Ponce camera chapter.*

</details>

### CV1-021 · breadth

**What is the aperture-size trade-off in a simple pinhole camera?**

<details>
<summary>Show answer</summary>

A larger hole admits more light but increases geometric blur. A very small hole admits little light and eventually suffers diffraction.

*Sources: HC1b pp.7–20.*

</details>

### CV1-022 · breadth

**How does lens aperture size affect depth of field?**

<details>
<summary>Show answer</summary>

A smaller aperture generally increases depth of field; a larger aperture decreases it, with other camera settings fixed.

*Sources: HC1b pp.16–20.*

</details>

### CV1-023 · breadth

**What is depth of field?**

<details>
<summary>Show answer</summary>

The range of scene depths that appear acceptably sharp for a given focus and camera setting.

*Sources: HC1b pp.16–18.*

</details>

### CV1-024 · core

**How is a 2D Cartesian point converted to homogeneous coordinates?**

<details>
<summary>Show answer</summary>

[x,y] -> [x,y,1]. Any nonzero common scale represents the same finite point.

*Sources: HC1b pp.32–34; S1.*

</details>

### CV1-025 · core

**How is a finite homogeneous point [a,b,w] converted to Cartesian coordinates?**

<details>
<summary>Show answer</summary>

[a/w,b/w], provided w is nonzero. Do not discard the third coordinate without dividing.

*Sources: HC1b pp.33–34.*

</details>

### CV1-026 · core

**What does homogeneous-coordinate scale invariance mean?**

<details>
<summary>Show answer</summary>

x and alpha\*x represent the same projective point for any nonzero alpha. This removes one effective degree of freedom.

*Sources: HC1b p.34; HC4a p.22.*

</details>

### CV1-027 · breadth

**What does a homogeneous point with last coordinate zero represent?**

<details>
<summary>Show answer</summary>

A point at infinity, encoding a direction rather than a finite Cartesian location. It cannot be dehomogenized by ordinary division.

*Sources: HC1b pp.28–34; Szeliski §2.1.*

</details>

### CV1-028 · core

**Why use homogeneous coordinates for geometric transformations?**

<details>
<summary>Show answer</summary>

They express translation and projective mappings by matrix multiplication and allow transformations to be composed consistently.

*Sources: HC1b pp.32–45; HC4a.*

</details>

### CV1-029 · core

**Write the general 3 by 3 intrinsic matrix K.**

<details>
<summary>Show answer</summary>

K=[[fx,s,cx],[0,fy,cy],[0,0,1]]. fx,fy are focal scales in pixels; s is skew; cx,cy are principal-point coordinates. For orthogonal sensor axes with physical pixel pitches px,py, fx=f/px and fy=f/py in consistent units.

*Sources: HC1b pp.35–45; Szeliski §2.1.4.*

</details>

### CV1-030 · core

**What is the principal point?**

<details>
<summary>Show answer</summary>

The image location at which the optical axis meets the image plane; represented by [cx,cy] in K. It need not equal the image centre.

*Sources: HC1b pp.39–63.*

</details>

### CV1-031 · core

**What does skew in K model?**

<details>
<summary>Show answer</summary>

Non-orthogonality of image coordinate axes; in the usual convention s is K[0,1]. It is usually assumed zero for modern cameras.

*Sources: HC1b pp.39,62–65.*

</details>

### CV1-032 · core

**How many free parameters does the usual general K have?**

<details>
<summary>Show answer</summary>

Five: fx, fy, skew, cx and cy, after choosing K[2,2]=1. Additional distortion parameters are not entries of this K.

*Sources: HC1b pp.39–45.*

</details>

### CV1-033 · core

**What do camera extrinsics describe?**

<details>
<summary>Show answer</summary>

Camera orientation and position relative to a world frame, through a rigid coordinate transformation.

*Sources: HC1b pp.35–45; S1.*

</details>

### CV1-034 · core

**What does Xc=R\*Xw+t mean?**

<details>
<summary>Show answer</summary>

R and t map a world-coordinate point into camera coordinates. This is the world-to-camera convention, not its inverse.

*Sources: HC1b pp.35–45.*

</details>

### CV1-035 · core

**What is the full homogeneous camera projection equation?**

<details>
<summary>Show answer</summary>

x is proportional to P\*Xw\_h, where P=K\*[R|t] is 3 by 4 and Xw\_h=[X,Y,Z,1]. Dehomogenize the resulting image vector.

*Sources: HC1b pp.35–45; HC6b p.27.*

</details>

### CV1-036 · core

**What are the shapes of K, R, t and [R|t]?**

<details>
<summary>Show answer</summary>

K: 3x3; R: 3x3; t: 3x1; [R|t]: 3x4. Their product P=K\*[R|t] is 3x4.

*Sources: HC1b pp.35–45.*

</details>

### CV1-037 · core

**What is the camera centre C when Xc=R\*Xw+t?**

<details>
<summary>Show answer</summary>

C=-R.T\*t for a rotation matrix. Equivalently t=-R\*C. Translation t is not generally the world-frame camera position.

*Sources: HC1b pp.35–45; S1.*

</details>

### CV1-038 · core

**What constraints define a proper rotation matrix?**

<details>
<summary>Show answer</summary>

R.T\*R=I and det(R)=+1. Its inverse is R.T; a proper 3D rotation has 3 degrees of freedom.

*Sources: HC1b pp.41–45; S1.*

</details>

### CV1-039 · core

**Does the order of 3D rotations matter?**

<details>
<summary>Show answer</summary>

Generally yes: R1\*R2 is not R2\*R1. With column vectors, the rightmost matrix acts first.

*Sources: HC1b pp.41–42.*

</details>

### CV1-040 · core

**Give the 2D counterclockwise rotation matrix in Cartesian x-right, y-up coordinates.**

<details>
<summary>Show answer</summary>

R(theta)=[[cos(theta),-sin(theta)],[sin(theta),cos(theta)]]. Displayed image rotation can look reversed when y points down.

*Sources: HC4a pp.11–13; S1.*

</details>

### CV1-041 · core

**What is perspective division?**

<details>
<summary>Show answer</summary>

Divide the first two entries of a projected homogeneous image vector by its third entry to obtain pixel coordinates.

*Sources: HC1b pp.24–45.*

</details>

### CV1-042 · core

**Can one image pixel determine unique depth?**

<details>
<summary>Show answer</summary>

No. Without further constraints it specifies a viewing ray; many depths along that ray produce the same pixel.

*Sources: HC1a; HC1b pp.24–34.*

</details>

### CV1-043 · core

**What is orthographic projection?**

<details>
<summary>Show answer</summary>

Projection along parallel viewing rays; in its simplest form [X,Y,Z] maps to [X,Y], so image scale does not vary with Z.

*Sources: HC2a p.23; Forsyth–Ponce photometric-stereo section.*

</details>

### CV1-044 · core

**How do perspective and orthographic models differ in their dependence on depth?**

<details>
<summary>Show answer</summary>

Perspective divides camera X and Y by Z, making scale depth-dependent. Orthographic projection ignores Z in its basic image-position mapping and uses parallel rays.

*Sources: HC1b pp.24–26; HC2a p.23.*

</details>

### CV1-045 · core

**What does resizing both image axes by factor a do to K in a continuous-coordinate model?**

<details>
<summary>Show answer</summary>

Scale the first two rows by a: focal scales, skew and principal-point coordinates scale. Keep the last row [0,0,1] and extrinsics unchanged.

*Sources: HC1b projection model; S1.*

</details>

### CV1-046 · core

**What does cropping an image at top-left offset (x0,y0) do to K?**

<details>
<summary>Show answer</summary>

cx becomes cx-x0 and cy becomes cy-y0. Focal scales and skew stay unchanged if there is no resize.

*Sources: HC1b projection model; S1.*

</details>

### CV1-047 · breadth

**How are radial and tangential lens distortion different?**

<details>
<summary>Show answer</summary>

Radial distortion depends on distance from the image's distortion centre, usually near the principal point, causing barrel/pincushion effects. Tangential distortion relates to lens/sensor misalignment.

*Sources: HC1b pp.46–53; HC6b pp.35–37.*

</details>

### CV1-048 · core

**Why undistort images before using an ideal homography or epipolar model?**

<details>
<summary>Show answer</summary>

Lens distortion is nonlinear and is not included in the simple pinhole K[R|t] model; correcting it makes the ideal geometric relations applicable.

*Sources: HC1b pp.46–65; HC6b pp.35–37.*

</details>

### CV1-049 · breadth

**What is camera calibration?**

<details>
<summary>Show answer</summary>

Estimate camera parameters, such as intrinsics, distortion and/or extrinsics, from suitable known geometry and observations.

*Sources: HC6b pp.26–47.*

</details>

### CV1-050 · breadth

**How many degrees of freedom has a general pinhole projection matrix?**

<details>
<summary>Show answer</summary>

Eleven up to scale: 5 intrinsic plus 6 rigid extrinsic parameters. Additional distortion is outside that count.

*Sources: HC1b p.43.*

</details>

### CV1-051 · breadth

**What are vanishing points?**

<details>
<summary>Show answer</summary>

Image locations where projections of parallel scene lines meet, possibly outside the image or at infinity. They encode scene directions.

*Sources: HC1b pp.28–31; HC3a pp.70–73.*

</details>

### CV1-052 · breadth

**What is a vanishing line or horizon for a scene plane?**

<details>
<summary>Show answer</summary>

The line containing vanishing points of directions lying in that plane. For a level ground plane it forms its geometric horizon.

*Sources: HC1b pp.28–31; S1.*

</details>

### CV1-579 · core

**Give the active right-handed column-vector rotation matrix about the x axis.**

<details>
<summary>Show answer</summary>

Rx(theta)=[[1,0,0],[0,cos(theta),-sin(theta)],[0,sin(theta),cos(theta)]]. State frame and active/passive conventions before composing rotations.

*Sources: HC1b pp.41–42; S1.*

</details>

### CV1-580 · core

**Give the active right-handed column-vector rotation matrix about the y axis.**

<details>
<summary>Show answer</summary>

Ry(theta)=[[cos(theta),0,sin(theta)],[0,1,0],[-sin(theta),0,cos(theta)]].

*Sources: HC1b pp.41–42; S1.*

</details>

### CV1-581 · core

**Give the active right-handed column-vector rotation matrix about the z axis.**

<details>
<summary>Show answer</summary>

Rz(theta)=[[cos(theta),-sin(theta),0],[sin(theta),cos(theta),0],[0,0,1]].

*Sources: HC1b pp.41–42; S1.*

</details>

### CV1-582 · core

**Write the 4x4 homogeneous world-to-camera rigid transform.**

<details>
<summary>Show answer</summary>

[[R,t],[0,0,0,1]], meaning a top 3x4 block [R|t] and bottom row [0,0,0,1]. It maps [Xw,Yw,Zw,1] to camera coordinates before projection.

*Sources: HC1b pp.35–45; HC6b pp.29–41.*

</details>

### CV1-583 · core

**What is the inverse of the homogeneous rigid transform [R|t]?**

<details>
<summary>Show answer</summary>

The inverse has top block [R.T|-R.T\*t] and bottom row [0,0,0,1], for an orthogonal R. Do not only negate t.

*Sources: HC1b pp.35–45; prerequisite linear algebra.*

</details>

### CV1-584 · core

**How do you obtain a camera-frame viewing-ray direction from pixel (u,v)?**

<details>
<summary>Show answer</summary>

Solve K\*d=[u,v,1]. The ray is Xc=lambda\*d for positive depth scale under the front-facing convention; calibration gives direction, not unique lambda.

*Sources: HC1b projection; HC6b p.28.*

</details>

### CV1-585 · core

**How are a normal and point transformed differently by a rigid camera pose?**

<details>
<summary>Show answer</summary>

Points use rotation and translation. Direction/unit-normal vectors use rotation only; for Xc=R\*Xw+t, n\_w=R.T\*n\_c.

*Sources: HC1b extrinsics; HC2a normals; prerequisite linear algebra.*

</details>

## colour

### CV1-053 · core

**How are ordinary image arrays indexed in NumPy?**

<details>
<summary>Show answer</summary>

I[row,column]=I[y,x]; an RGB array usually has shape (H,W,3), with channels on the last axis.

*Sources: HC1b pp.75–78; Lab0; Lab1.*

</details>

### CV1-054 · breadth

**What is sampling in digital image formation?**

<details>
<summary>Show answer</summary>

Measuring a continuous image at discrete spatial locations, usually a regular grid of sensor elements.

*Sources: HC1b pp.69–78.*

</details>

### CV1-055 · breadth

**What is quantization in digital image formation?**

<details>
<summary>Show answer</summary>

Representing continuous measurement values with a finite set of discrete levels, such as integers 0..255.

*Sources: HC1b pp.69–78.*

</details>

### CV1-056 · core

**How many intensity levels can an unsigned b-bit channel represent?**

<details>
<summary>Show answer</summary>

2^b levels, normally 0 through 2^b-1. For 8 bits: 256 levels, not 255 levels.

*Sources: HC1b pp.77–78; S3 4-bit examples.*

</details>

### CV1-057 · core

**What are usual normalized-float and uint8 image ranges?**

<details>
<summary>Show answer</summary>

Float images often use [0,1]; uint8 images use integers [0,255]. A float type alone does not guarantee normalization.

*Sources: HC1b pp.77–78; Lab0; Lab1.*

</details>

### CV1-058 · core

**What colour-channel order does OpenCV commonly use for loaded colour images?**

<details>
<summary>Show answer</summary>

BGR, not RGB. Convert or reverse channels when an RGB-based display or calculation requires it.

*Sources: HC1b p.87; Lab0; Lab1.*

</details>

### CV1-059 · core

**What is the average-method RGB grayscale value?**

<details>
<summary>Show answer</summary>

(R+G+B)/3. It treats all channels equally and is not a perceptual luminance weighting.

*Sources: Lab1 Section 1.*

</details>

### CV1-060 · core

**What is the lightness-method RGB grayscale value?**

<details>
<summary>Show answer</summary>

(max(R,G,B)+min(R,G,B))/2. This matches the coding-prep example, not the channel average.

*Sources: Lab1; Coding examples Q2.*

</details>

### CV1-061 · core

**What is a common weighted luminosity/luma grayscale approximation?**

<details>
<summary>Show answer</summary>

About 0.299\*R + 0.587\*G + 0.114\*B for RGB channel values. This is a conventional weighted approximation, not a universal physical luminance formula. Use supplied coefficients and channel order.

*Sources: Lab1 Section 1; Szeliski §2.3.*

</details>

### CV1-062 · breadth

**Why do RGB channels not uniquely specify a physical spectrum?**

<details>
<summary>Show answer</summary>

A sensor compresses the wavelength-dependent signal into three responses. Different spectra can give the same responses.

*Sources: HC1b pp.80–92; Szeliski §2.3.*

</details>

### CV1-063 · core

**What determines measured RGB for an illuminated surface?**

<details>
<summary>Show answer</summary>

Source spectral power, material spectral reflectance and sensor channel sensitivities, combined over wavelength, plus geometry and camera response.

*Sources: HC1b pp.67–71,80–86.*

</details>

### CV1-064 · breadth

**What does H mean in HSV?**

<details>
<summary>Show answer</summary>

Hue: the angular/cyclic colour type, such as red, green or blue. It is unstable or undefined when saturation is zero.

*Sources: HC1b pp.88–91; Lab1.*

</details>

### CV1-065 · breadth

**What does S mean in HSV?**

<details>
<summary>Show answer</summary>

Saturation: colour purity relative to gray. S=0 is achromatic in the standard definition.

*Sources: HC1b pp.88–91; Lab1.*

</details>

### CV1-066 · breadth

**What does V mean in HSV?**

<details>
<summary>Show answer</summary>

Value/brightness, commonly max(R,G,B) for normalized RGB. It is not the same quantity as HSL lightness.

*Sources: HC1b pp.88–91; Lab1.*

</details>

### CV1-067 · core

**What assumption does Grey-World white balance make?**

<details>
<summary>Show answer</summary>

Under neutral illumination, the scene's average colour is gray, so average R, G and B responses should be equal.

*Sources: Lab1; Coding examples Q3,Q4.*

</details>

### CV1-068 · core

**Write the Grey-World channel-scaling rule.**

<details>
<summary>Show answer</summary>

Compute spatial channel means m\_c, choose a neutral target such as their mean m, then I'\_c=I\_c\*m/m\_c. Handle zero means; clip/quantize only after correction.

*Sources: Lab1; Coding examples Q3,Q4.*

</details>

### CV1-069 · core

**What axes compute per-channel means for shape (H,W,3)?**

<details>
<summary>Show answer</summary>

axis=(0,1). With keepdims=True the result has shape (1,1,3), suitable for channel-wise broadcasting.

*Sources: Coding examples Q3.*

</details>

### CV1-070 · core

**Why does I.mean(axis=(0,1,2)) break the intended Grey-World correction?**

<details>
<summary>Show answer</summary>

It collapses channels to the same overall mean. Dividing and multiplying by that scalar cancels instead of correcting channel imbalance.

*Sources: Coding examples Q4.*

</details>

### CV1-071 · core

**When can Grey-World fail?**

<details>
<summary>Show answer</summary>

When the scene's average material colour is not gray, such as a strongly monochromatic scene, or when clipping and nonuniform illumination invalidate the model.

*Sources: Lab1.*

</details>

### CV1-072 · breadth

**What assumption does White-Patch white balance make, as one example for Lab1's open-choice prompt?**

<details>
<summary>Show answer</summary>

A brightest or reference patch is assumed to reflect the illuminant neutrally; channel responses there estimate colour cast. This is one possible additional colour-constancy method, not a named required algorithm in the notebook.

*Sources: Lab1 Q8 (chosen example); Forsyth–Ponce §2.2 brightest-patch assumption.*

</details>

### CV1-073 · core

**Why can unsigned-integer image subtraction be unsafe?**

<details>
<summary>Show answer</summary>

Unsigned arithmetic can wrap around on negative results. Convert to a suitable floating-point or signed type before difference/gradient computations.

*Sources: Lab0; Lab2.*

</details>

### CV1-074 · core

**Why convert to float before weighted sums or intensity correction?**

<details>
<summary>Show answer</summary>

It avoids integer overflow and preserves fractional values during calculation. Convert back only after required scaling and clipping.

*Sources: Lab0; Lab1; Lab2.*

</details>

### CV1-075 · breadth

**What is sensor dynamic range?**

<details>
<summary>Show answer</summary>

The range between the weakest usable signal and saturation, often limited by noise at the low end and clipping at the high end.

*Sources: HC1b p.71; Szeliski §2.3.*

</details>

### CV1-076 · breadth

**What is the rolling-shutter problem?**

<details>
<summary>Show answer</summary>

Different image rows are exposed at different times, so scene or camera motion can distort the captured geometry.

*Sources: HC1b p.71.*

</details>

### CV1-586 · core

**What is normalized RGB?**

<details>
<summary>Show answer</summary>

r=R/(R+G+B), g=G/(R+G+B), b=B/(R+G+B), per pixel for positive channel sum. Specify a fallback for black pixels.

*Sources: Lab1 Section 1.*

</details>

### CV1-587 · core

**Why does normalized RGB have only two independent components at a valid pixel?**

<details>
<summary>Show answer</summary>

r+g+b=1, so the third follows from the other two. The normalization removes overall intensity magnitude.

*Sources: Lab1 Section 1.*

</details>

### CV1-588 · core

**To what illumination change is normalized RGB invariant in the ideal arithmetic model?**

<details>
<summary>Show answer</summary>

A common positive multiplicative gain on all three channels at a pixel. Different channel gains, additive offsets and clipping generally break this invariance.

*Sources: Lab1 Section 1.*

</details>

### CV1-589 · core

**What are common opponent-colour coordinates in the lab's colour-space task?**

<details>
<summary>Show answer</summary>

O1=(R-G)/sqrt(2); O2=(R+G-2B)/sqrt(6); O3=(R+G+B)/sqrt(3). This is one standard convention; check signs and scaling if supplied.

*Sources: Lab1 Section 1; Szeliski §2.3.*

</details>

### CV1-590 · core

**What do the usual three opponent-colour coordinates represent?**

<details>
<summary>Show answer</summary>

O1: red–green difference; O2: yellow–blue difference; O3: an intensity-like sum. The chromatic axes can have negative values.

*Sources: Lab1 Section 1.*

</details>

### CV1-591 · breadth

**Why can an opponent-colour channel contain negative numbers?**

<details>
<summary>Show answer</summary>

It is a signed difference of channel responses, not an ordinary nonnegative intensity. Display scaling must not be confused with changing the representation.

*Sources: Lab1 Section 1.*

</details>

### CV1-592 · core

**What do Y, Cb and Cr represent in YCbCr?**

<details>
<summary>Show answer</summary>

Y is a luma/intensity-like component; Cb and Cr encode blue-difference and red-difference chroma. Exact coefficients and offsets depend on the standard/range.

*Sources: Lab1 Section 1.*

</details>

### CV1-593 · core

**Why separate intensity-like and chromatic channels?**

<details>
<summary>Show answer</summary>

It allows operations or representations to target brightness separately from colour differences, reducing their coupling compared with raw RGB. It does not guarantee total illumination invariance.

*Sources: HC1b p.87; Lab1 Section 1.*

</details>

### CV1-594 · core

**What ranges does Lab1 specify for uint8 OpenCV HSV?**

<details>
<summary>Show answer</summary>

H is 0..179; S and V are 0..255. Do not treat this H array as raw degrees or as a float hue in 0..1.

*Sources: Lab1 convert\_colour\_space docstring.*

</details>

### CV1-595 · core

**What is the main computational goal of colour constancy?**

<details>
<summary>Show answer</summary>

Estimate the illuminant/colour cast and compensate it so material colours are more consistent under a canonical illumination.

*Sources: Lab1 Section 2.*

</details>

### CV1-596 · core

**Why is averaging normalized RGB not generally the same as normalizing average RGB?**

<details>
<summary>Show answer</summary>

The per-pixel normalization is nonlinear and has different denominators at different pixels. Operation order matters.

*Sources: Lab1 Section 1; prerequisite aggregation.*

</details>

## reflectance

### CV1-077 · core

**What is a surface normal?**

<details>
<summary>Show answer</summary>

A direction perpendicular to the local tangent plane, usually represented as a unit outward vector. Its components depend on the coordinate frame.

*Sources: HC2a p.11.*

</details>

### CV1-078 · core

**What is albedo in the simplified diffuse model?**

<details>
<summary>Show answer</summary>

The material's diffuse reflectance factor, separated from lighting and orientation. Physical calibrated reflectance is normally in [0,1].

*Sources: HC2a pp.6,19–20.*

</details>

### CV1-079 · core

**What is irradiance?**

<details>
<summary>Show answer</summary>

Incoming radiant power per unit surface area, integrated over incoming directions. It describes illumination arriving at a surface.

*Sources: HC2a pp.11–12; Szeliski §2.2.*

</details>

### CV1-080 · core

**What is radiance?**

<details>
<summary>Show answer</summary>

Directional radiant power per unit projected area per unit solid angle. The camera measures a response related to incoming scene radiance.

*Sources: HC2a pp.11–20; Szeliski §2.2.*

</details>

### CV1-081 · core

**What is a directional light source?**

<details>
<summary>Show answer</summary>

A model with parallel rays and constant direction over the object, approximating an infinitely distant source. Strength can be absorbed into its vector magnitude.

*Sources: HC2a pp.7–8,19.*

</details>

### CV1-082 · core

**What does Lambert's cosine law say for illumination?**

<details>
<summary>Show answer</summary>

Received irradiance is proportional to the positive cosine of the angle between the surface normal and direction toward the light.

*Sources: HC2a pp.12–14.*

</details>

### CV1-083 · core

**Write the simplified calibrated Lambertian pixel-intensity model.**

<details>
<summary>Show answer</summary>

I=rho\*J\*max(n dot l,0), with unit n and l. Strength J and gain may instead be encoded in the light vector and effective diffuse coefficient.

*Sources: HC2a pp.12–20; Lab1.*

</details>

### CV1-084 · core

**In Lambertian lighting, what happens as the light–normal angle approaches 90 degrees?**

<details>
<summary>Show answer</summary>

The diffuse contribution approaches zero because cos(angle) approaches zero. Shadows and other effects may require more than this local model.

*Sources: HC2a pp.12–20.*

</details>

### CV1-085 · core

**Is ideal Lambertian radiance view-dependent?**

<details>
<summary>Show answer</summary>

No, for fixed material, illumination and normal. Projected surface area and visibility can still change with view.

*Sources: HC2a pp.13–18.*

</details>

### CV1-086 · core

**How do ideal diffuse and ideal specular reflection differ?**

<details>
<summary>Show answer</summary>

Diffuse reflection has view-independent radiance; ideal specular reflection directs light along the mirror-reflection direction.

*Sources: HC2a pp.9–10,25–27.*

</details>

### CV1-087 · breadth

**What is the distinction between body and surface reflection?**

<details>
<summary>Show answer</summary>

Body scattering often produces diffuse matte appearance; surface reflection produces specular/glossy highlights. Real materials can have both.

*Sources: HC2a p.26.*

</details>

### CV1-088 · core

**What is a BRDF?**

<details>
<summary>Show answer</summary>

Bidirectional Reflectance Distribution Function: relates incoming irradiance from a direction to outgoing radiance in another direction at a surface point.

*Sources: HC2a pp.28–32.*

</details>

### CV1-089 · breadth

**Why is the general BRDF a four-dimensional angular function?**

<details>
<summary>Show answer</summary>

Incoming direction needs two angles and outgoing direction needs two more, relative to the surface frame.

*Sources: HC2a pp.29–30.*

</details>

### CV1-090 · breadth

**What is Helmholtz reciprocity for an ordinary reciprocal BRDF?**

<details>
<summary>Show answer</summary>

Interchanging incoming and outgoing directions leaves the BRDF value unchanged. It is a material reciprocity property, not equality of all image intensities.

*Sources: HC2a p.30.*

</details>

### CV1-091 · breadth

**Why does a general BRDF complicate normal estimation?**

<details>
<summary>Show answer</summary>

The surface normal determines the local angular frame, so it enters both the cosine term and the BRDF's directional arguments. The resulting inverse problem is generally nonlinear.

*Sources: HC2a pp.28–32.*

</details>

### CV1-092 · core

**What are the three terms in the Phong illumination model?**

<details>
<summary>Show answer</summary>

Ambient, diffuse and specular contributions, added together.

*Sources: HC2a p.33.*

</details>

### CV1-093 · core

**Write the simplified Phong diffuse and specular terms.**

<details>
<summary>Show answer</summary>

Diffuse: kd\*max(n dot l,0). Specular: ks\*max(v dot r,0)^s, where r is the ideal reflection direction and s is shininess. Add an ambient term if specified.

*Sources: HC2a p.33.*

</details>

### CV1-094 · core

**What happens when the Phong shininess exponent increases?**

<details>
<summary>Show answer</summary>

The highlight becomes narrower and sharper, for the same coefficient and directions.

*Sources: HC2a p.33.*

</details>

### CV1-095 · core

**How can a mirror sphere help calibrate light direction?**

<details>
<summary>Show answer</summary>

Its known geometry gives the normal at the highlight, and the known viewing direction plus the law of reflection determines the light direction.

*Sources: HC2a p.27; Lab1.*

</details>

### CV1-096 · breadth

**With n and v pointing outward/toward the viewer, what is the reflected light-direction relation at a mirror highlight?**

<details>
<summary>Show answer</summary>

l=2\*(n dot v)\*n-v for unit vectors under this outward-direction convention. Other sign conventions require corresponding changes.

*Sources: HC2a p.27; Lab1.*

</details>

### CV1-097 · core

**What is intrinsic image decomposition?**

<details>
<summary>Show answer</summary>

Separate image appearance into material/albedo and illumination/shading, commonly using I=A\*S elementwise in a simplified model.

*Sources: HC2a pp.47–48; Lab1.*

</details>

### CV1-098 · core

**How do you recolour an object while keeping estimated shading?**

<details>
<summary>Show answer</summary>

Modify its albedo layer inside the object mask, keep shading fixed, and multiply the layers to reconstruct the image.

*Sources: Lab1; Coding examples Q6.*

</details>

### CV1-099 · core

**Why is shape from one shaded image ambiguous?**

<details>
<summary>Show answer</summary>

Intensity combines unknown material, lighting and geometry. Even with known albedo and light, one local intensity gives insufficient information for a unique normal.

*Sources: HC2a pp.4–5,21–23.*

</details>

### CV1-100 · breadth

**What simplifying assumptions are listed for classical shape from shading?**

<details>
<summary>Show answer</summary>

Diffuse material with constant albedo, known distant illumination and an orthographic/distant camera, with additional constraints needed to recover shape.

*Sources: HC2a pp.21–23.*

</details>

### CV1-597 · breadth

**How does physical Lambertian albedo relate to a BRDF coefficient?**

<details>
<summary>Show answer</summary>

A calibrated ideal Lambertian BRDF is rho/pi, while the simplified course intensity equation can absorb pi and camera/light factors into an effective coefficient. Do not mix conventions.

*Sources: HC2a pp.19–20,28–32; Szeliski §2.2.*

</details>

### CV1-598 · core

**Why are intrinsic-image ground truths often synthetic?**

<details>
<summary>Show answer</summary>

Rendering can expose exact albedo, shading and other components. Measuring separate, exact per-pixel components of a real scene is difficult; synthetic success is not proof of real-scene performance.

*Sources: Lab1 Q10.*

</details>

### CV1-599 · breadth

**What additional appearance component can be separated beyond diffuse albedo and shading?**

<details>
<summary>Show answer</summary>

A specular-reflection layer, among others, can model view-dependent highlights that the simple diffuse product does not explain.

*Sources: Lab1 Q9; HC2a pp.25–33.*

</details>

## photometric

### CV1-101 · core

**What observations does photometric stereo use?**

<details>
<summary>Show answer</summary>

Multiple images of the same fixed scene from the same viewpoint under different lighting conditions.

*Sources: HC2a pp.6,34–45; Lab1.*

</details>

### CV1-102 · core

**What does calibrated photometric stereo estimate at each pixel?**

<details>
<summary>Show answer</summary>

An effective albedo-scaled normal g, then albedo from its magnitude and the unit normal from its direction. A height map requires further integration.

*Sources: HC2a pp.34–43.*

</details>

### CV1-103 · core

**Write the per-pixel linear photometric-stereo system with lights as rows.**

<details>
<summary>Show answer</summary>

i=L\*g, where L has shape (number\_of\_lights,3), i has one intensity per image, and g=rho\*n when strength/gain are calibrated into L.

*Sources: HC2a pp.34–39; Lab1.*

</details>

### CV1-104 · core

**Why can photometric-stereo matrix orientation differ between sources?**

<details>
<summary>Show answer</summary>

Some stack light vectors as rows and use i=L\*g; others use columns and pixels as rows, giving I=G\*L. Check shapes before using a formula.

*Sources: HC2a pp.34–39; Lab1; SOURCE\_NOTES.*

</details>

### CV1-105 · core

**What is the theoretical minimum number of independent calibrated lights for unconstrained diffuse photometric stereo?**

<details>
<summary>Show answer</summary>

Three, with linearly independent light vectors and valid unshadowed linear measurements. Three images alone do not guarantee independence.

*Sources: HC2a pp.34–36; Lab1.*

</details>

### CV1-106 · core

**When is a 3 by 3 lighting matrix invertible?**

<details>
<summary>Show answer</summary>

When its light vectors span 3D, so rank(L)=3. Coplanar vectors through the origin do not meet this condition.

*Sources: HC2a p.36.*

</details>

### CV1-107 · core

**What is the least-squares solution for full-column-rank L?**

<details>
<summary>Show answer</summary>

g=(L.T\*L)^(-1)\*L.T\*i in exact algebra. In computation use a stable least-squares routine rather than explicitly inverting the normal equations.

*Sources: HC2a p.39; Coding examples Q1,Q5.*

</details>

### CV1-108 · core

**What does np.linalg.lstsq(L,i,rcond=None)[0] return?**

<details>
<summary>Show answer</summary>

A vector minimizing ||L\*g-i||\_2^2. It is not gradient descent and does not require a learning rate. A full-rank overdetermined system need not fit exactly.

*Sources: Coding examples Q1,Q5.*

</details>

### CV1-109 · core

**How is albedo recovered from a solved g?**

<details>
<summary>Show answer</summary>

rho=||g||\_2, under the calibrated effective-reflectance convention. Unknown light strength or gain changes its absolute scale.

*Sources: HC2a pp.35–39; Lab1.*

</details>

### CV1-110 · core

**How is the unit surface normal recovered from g?**

<details>
<summary>Show answer</summary>

n=g/||g||\_2, provided ||g|| is nonzero. Mask zero or invalid estimates rather than claiming a direction.

*Sources: HC2a pp.35–39; Lab1.*

</details>

### CV1-111 · core

**What does adding more independent photometric-stereo images provide?**

<details>
<summary>Show answer</summary>

An overdetermined fit that can reduce noise sensitivity and expose residual/model errors. It does not automatically eliminate systematic shadows or non-Lambertian effects.

*Sources: HC2a pp.39–45; Lab1.*

</details>

### CV1-112 · core

**What are major violations of the basic photometric-stereo model?**

<details>
<summary>Show answer</summary>

Shadows, specular highlights, interreflections, unknown/incorrect light calibration, nonlinear camera response, motion and changing viewpoint.

*Sources: HC2a pp.19–20,45; Lab1.*

</details>

### CV1-113 · core

**How can shadows affect a least-squares photometric-stereo fit?**

<details>
<summary>Show answer</summary>

A dark observation may reflect occlusion of the light rather than the linear dot product, so treating it as an ordinary equation can bias the normal.

*Sources: Lab1 shadow trick; HC2a p.45.*

</details>

### CV1-114 · core

**What does weighted least squares do in photometric stereo?**

<details>
<summary>Show answer</summary>

Reduce the influence of unreliable observations by minimizing a specified weighted residual sum. The chosen weighting rule is a heuristic/model choice, not a universal shadow solution.

*Sources: Lab1.*

</details>

### CV1-115 · core

**If rows and intensities are both multiplied by w\_j, what residual weight is minimized?**

<details>
<summary>Show answer</summary>

sum\_j w\_j^2\*(L\_j\*g-i\_j)^2. Multiplying the rows by w\_j gives squared weights, not w\_j alone.

*Sources: Lab1 weighted estimation; prerequisite linear algebra.*

</details>

### CV1-116 · core

**Can dependent lighting be repaired merely by collecting more images with the same dependent directions?**

<details>
<summary>Show answer</summary>

No. Additional observations can improve noise estimates but cannot recover directions in the lighting matrix's nullspace.

*Sources: HC2a pp.36–39.*

</details>

### CV1-117 · core

**What happens if every true light strength is a common factor a larger than the strengths used in the fit?**

<details>
<summary>Show answer</summary>

The fitted g and albedo scale by a; the normalized normal stays unchanged for a>0 in the ideal model.

*Sources: HC2a pp.19–20,34–39.*

</details>

### CV1-118 · core

**For a graph z(x,y), what upward normal convention is used in this pack?**

<details>
<summary>Show answer</summary>

n is proportional to [-dz/dx,-dz/dy,1]. Thus p=-nx/nz and q=-ny/nz. Lab1 prints positive ratios instead; the local sources do not resolve that discrepancy. Follow the explicitly declared convention.

*Sources: HC2a p.42; Lab1; SOURCE\_NOTES.*

</details>

### CV1-119 · core

**What is the integrability condition for height derivatives p and q?**

<details>
<summary>Show answer</summary>

dp/dy=dq/dx for a sufficiently smooth height field on a simply connected region. A violation means the estimated field need not be path-independent.

*Sources: HC2a pp.42–43; Lab1.*

</details>

### CV1-120 · core

**How does simple discrete normal integration recover height?**

<details>
<summary>Show answer</summary>

Starting from an anchor, accumulate p along x steps and q along y steps, using the specified spacing and path. Noise can accumulate.

*Sources: HC2a pp.41–43; Lab1.*

</details>

### CV1-121 · core

**Why can different integration paths give different reconstructed heights?**

<details>
<summary>Show answer</summary>

The estimated gradients can be non-integrable due to noise, calibration errors or model violations. Mixed-derivative differences reveal this inconsistency.

*Sources: Lab1; HC2a pp.42–43.*

</details>

### CV1-122 · core

**What ambiguity remains after integrating a valid gradient field without a height anchor?**

<details>
<summary>Show answer</summary>

An additive height constant. Relative height changes are constrained; absolute height is not.

*Sources: HC2a p.43; Lab1; Forsyth–Ponce §2.2.*

</details>

### CV1-123 · core

**Why is dividing by nz dangerous when nz is near zero?**

<details>
<summary>Show answer</summary>

The surface approaches a vertical tangent relative to the height-field model, so estimated slopes can become arbitrarily large and unstable.

*Sources: HC2a p.42; Lab1.*

</details>

### CV1-124 · core

**Why can solving colour channels separately produce invalid normals in a zero channel?**

<details>
<summary>Show answer</summary>

A channel with zero reflectance can have zero observations and g=0, so its normal cannot be normalized. Use a valid shared-geometry strategy or masking.

*Sources: Lab1 colour photometric stereo.*

</details>

### CV1-125 · breadth

**How can a global height least-squares system improve on one-path integration?**

<details>
<summary>Show answer</summary>

Solve neighbouring height differences to best fit all measured slopes, with a height anchor, distributing inconsistent/noisy errors rather than accumulating them along one path.

*Sources: HC2a p.43.*

</details>

### CV1-126 · breadth

**Who is associated with classical photometric stereo?**

<details>
<summary>Show answer</summary>

Robert Woodham. The essential idea is fixed-view images under different illumination, unlike geometric stereo with different viewpoints.

*Sources: HC2a p.41; Forsyth–Ponce notes.*

</details>

### CV1-600 · core

**What is the exact linear-system weighting used by Lab1's shadow trick?**

<details>
<summary>Show answer</summary>

Form diag(i) and solve diag(i)\*L\*g=diag(i)\*i. Its least-squares objective weights each residual by i\_j^2, so dark observations contribute less.

*Sources: Lab1 Q18.*

</details>

### CV1-601 · core

**Does Lab1's intensity-based shadow weighting solve specular contamination too?**

<details>
<summary>Show answer</summary>

Not reliably. Bright specular observations can receive large weights even though they violate the diffuse model. It is a shadow-oriented heuristic, not a general robust estimator.

*Sources: Lab1 Q18; HC2a p.45.*

</details>

### CV1-602 · core

**How do photometric stereo and geometric stereo differ?**

<details>
<summary>Show answer</summary>

Photometric: fixed camera/view, varying lights, estimating normals/albedo. Geometric: varying camera centres/views, using correspondence and triangulation for depth.

*Sources: HC2a; HC6b; Lab1.*

</details>

## histogram

### CV1-127 · core

**What is an image intensity histogram?**

<details>
<summary>Show answer</summary>

Counts of pixels in each intensity level or bin. It summarizes the intensity distribution, not the spatial arrangement.

*Sources: HC2a pp.51–57.*

</details>

### CV1-128 · core

**How is a normalized histogram formed?**

<details>
<summary>Show answer</summary>

Divide bin counts by the total number of counted pixels. Its entries sum to 1 if all pixels are included.

*Sources: HC2a p.54.*

</details>

### CV1-129 · core

**What is the cumulative distribution function of an image histogram?**

<details>
<summary>Show answer</summary>

CDF(r)=sum of normalized counts for levels <=r. It is nondecreasing and reaches 1 at the highest included level.

*Sources: HC2a p.54.*

</details>

### CV1-130 · breadth

**What is the effect of choosing too many or too few histogram bins?**

<details>
<summary>Show answer</summary>

Too many can give sparse/noisy estimates; too few merge distinct intensities or colours and lose detail.

*Sources: HC2a pp.52–53.*

</details>

### CV1-131 · core

**What spatial information does an ordinary histogram lose?**

<details>
<summary>Show answer</summary>

Pixel positions, arrangement, boundaries and connectivity. Different layouts can have identical histograms.

*Sources: HC2a pp.51–56.*

</details>

### CV1-132 · core

**What information do separate RGB channel histograms lose compared with a joint histogram?**

<details>
<summary>Show answer</summary>

Cross-channel associations: which R,G,B values occur together. Both ordinary forms still lose spatial layout.

*Sources: HC2a pp.55–56.*

</details>

### CV1-133 · core

**What is a point operator?**

<details>
<summary>Show answer</summary>

An operation whose output at a pixel depends on that pixel's value, not its neighbours. Its mapping can be fixed or estimated from global statistics.

*Sources: HC2a pp.58–63.*

</details>

### CV1-134 · core

**Write a linear contrast-stretch mapping from [a,b] to [c,d].**

<details>
<summary>Show answer</summary>

s=c+(r-a)\*(d-c)/(b-a), for b>a. Clip outside the input range if the stated rule requires it.

*Sources: HC2a pp.59–60; S1.*

</details>

### CV1-135 · core

**What is the power-law gamma mapping used in the slides?**

<details>
<summary>Show answer</summary>

s=c\*r^gamma. For normalized r in (0,1), gamma<1 brightens and gamma>1 darkens; gamma=1 is linear scaling.

*Sources: HC2a pp.61–62; S1.*

</details>

### CV1-136 · core

**What is the central idea of histogram equalization?**

<details>
<summary>Show answer</summary>

Map intensity through a scaled cumulative histogram/CDF to spread the output distribution across the available range.

*Sources: HC2a p.63; S1.*

</details>

### CV1-137 · core

**Does discrete histogram equalization guarantee a perfectly flat histogram?**

<details>
<summary>Show answer</summary>

No. Finite counts, quantization and merging levels can prevent exact uniformity. Equalization cannot split identical input levels using a single deterministic point mapping.

*Sources: HC2a p.63; S1.*

</details>

### CV1-138 · core

**Why must numerical histogram-equalization questions specify a mapping convention?**

<details>
<summary>Show answer</summary>

Choices such as CDF\_min subtraction, number of levels and rounding/flooring can produce different output levels. Follow the stated rule.

*Sources: HC2a p.63; S1.*

</details>

### CV1-139 · breadth

**Why can separately equalizing R, G and B alter image colours?**

<details>
<summary>Show answer</summary>

The three different mappings can change channel ratios, and therefore hue/chromaticity. An intensity-channel approach can limit this, but must use a suitable colour space and range handling.

*Sources: HC2a histograms; Lab1 colour spaces.*

</details>

### CV1-140 · breadth

**Why can global contrast enhancement be undesirable?**

<details>
<summary>Show answer</summary>

It can amplify noise, change intended appearance or fail to improve small regions whose local statistics differ from the overall image.

*Sources: HC2a pp.57–63; Szeliski §3.1.*

</details>

## morphology

### CV1-141 · core

**What is 4-connectivity in a 2D grid?**

<details>
<summary>Show answer</summary>

Neighbours share an edge: up, down, left and right. Diagonal contact alone does not connect foreground pixels.

*Sources: HC2b p.10; S2.*

</details>

### CV1-142 · core

**What is 8-connectivity in a 2D grid?**

<details>
<summary>Show answer</summary>

Include the four edge neighbours and four diagonal neighbours. Diagonal contact can connect foreground pixels.

*Sources: HC2b p.10; S2.*

</details>

### CV1-143 · core

**What is a connected foreground component?**

<details>
<summary>Show answer</summary>

A maximal set of foreground pixels joined by foreground paths under the specified neighbourhood rule.

*Sources: HC2b pp.7–10.*

</details>

### CV1-144 · core

**Does connected-component count necessarily equal physical object count?**

<details>
<summary>Show answer</summary>

No. Touching objects can merge; fragmented objects can split. Connectivity is a property of the binary representation.

*Sources: HC2b pp.5–12,38.*

</details>

### CV1-145 · core

**What does the first pass of two-pass connected-component labelling do?**

<details>
<summary>Show answer</summary>

Scan foreground pixels, assign provisional labels using already-seen neighbours, and record equivalences where labelled branches meet.

*Sources: HC2b p.11.*

</details>

### CV1-146 · core

**What does the second pass of connected-component labelling do?**

<details>
<summary>Show answer</summary>

Resolve label equivalences and relabel pixels consistently so each connected region has one final label.

*Sources: HC2b p.12.*

</details>

### CV1-147 · core

**What is a structuring element?**

<details>
<summary>Show answer</summary>

A spatial support mask with a defined origin, specifying which relative positions participate in a morphological operation.

*Sources: HC2b p.14.*

</details>

### CV1-148 · core

**For a symmetric binary structuring element, how is dilation computed locally?**

<details>
<summary>Show answer</summary>

The output is 1 if any active support position sees foreground; equivalently the maximum over active positions.

*Sources: HC2b pp.15–24; S2.*

</details>

### CV1-149 · core

**For a binary structuring element, how is erosion computed locally?**

<details>
<summary>Show answer</summary>

The output is 1 only if every active support position sees foreground; equivalently the minimum over active positions.

*Sources: HC2b pp.27–36; S2.*

</details>

### CV1-150 · core

**Are zero entries of a structuring-element mask required zeros in the image?**

<details>
<summary>Show answer</summary>

No. They are inactive positions for ordinary dilation/erosion. Only active support positions impose tests.

*Sources: HC2b pp.14–29; S2.*

</details>

### CV1-151 · core

**What effects can binary dilation have?**

<details>
<summary>Show answer</summary>

Grow foreground, join nearby components and reduce sufficiently small background gaps/holes, depending on element shape and size.

*Sources: HC2b pp.15–26.*

</details>

### CV1-152 · core

**What effects can binary erosion have?**

<details>
<summary>Show answer</summary>

Shrink foreground, remove small protrusions/bridges, split touching regions or eliminate small components.

*Sources: HC2b pp.27–38.*

</details>

### CV1-153 · core

**What is opening?**

<details>
<summary>Show answer</summary>

Erosion followed by dilation with the same structuring element: open(B)=(B eroded by K) dilated by K.

*Sources: HC2b pp.39–42; S2.*

</details>

### CV1-154 · core

**What is closing?**

<details>
<summary>Show answer</summary>

Dilation followed by erosion with the same structuring element: close(B)=(B dilated by K) eroded by K.

*Sources: HC2b pp.43–45; S2.*

</details>

### CV1-155 · core

**What is opening mainly used to remove?**

<details>
<summary>Show answer</summary>

Small foreground structures or narrow foreground connections that the structuring element cannot fit inside.

*Sources: HC2b pp.39–42.*

</details>

### CV1-156 · core

**What is closing mainly used to remove?**

<details>
<summary>Show answer</summary>

Small background gaps, cracks or holes relative to the structuring element; it can join nearby foreground regions.

*Sources: HC2b pp.43–45.*

</details>

### CV1-157 · core

**Is erosion followed by dilation generally an exact inverse operation?**

<details>
<summary>Show answer</summary>

No. Opening can permanently remove small foreground structures. Closing also need not restore the original image.

*Sources: HC2b pp.39–45; S2.*

</details>

### CV1-158 · breadth

**Are ideal opening and closing idempotent?**

<details>
<summary>Show answer</summary>

Yes under their consistent mathematical definitions: applying the same opening or closing again changes nothing. Finite-image boundary handling can alter practical behaviour.

*Sources: HC2b pp.39–45; Szeliski §3.3.*

</details>

### CV1-159 · core

**Why must a morphology question specify the image boundary rule?**

<details>
<summary>Show answer</summary>

Out-of-image samples can change erosion/dilation and counts near borders. Zero padding, reflection and other rules are not equivalent.

*Sources: S2; HC2b morphology.*

</details>

### CV1-160 · core

**What happens to the border of an all-ones image under 3x3 erosion with outside values zero?**

<details>
<summary>Show answer</summary>

Border pixels whose support leaves the image become zero; only the interior with complete foreground support survives.

*Sources: S2; HC2b pp.27–38.*

</details>

### CV1-161 · core

**How can morphology support counting touching objects?**

<details>
<summary>Show answer</summary>

Threshold to foreground, separate suitable narrow connections with erosion/opening, then label and count connected regions. This can damage true small objects.

*Sources: HC2b pp.38–42.*

</details>

### CV1-162 · breadth

**What is the binary component area?**

<details>
<summary>Show answer</summary>

The number of foreground pixels in the component; multiply by physical pixel area only when such calibration is given.

*Sources: HC2b p.9.*

</details>

### CV1-163 · breadth

**How is a binary component centroid calculated?**

<details>
<summary>Show answer</summary>

Mean the x and y coordinates of its foreground pixels, or equivalently divide first spatial moments by area.

*Sources: HC2b p.9; prerequisite aggregation.*

</details>

### CV1-164 · breadth

**How can dilation produce an outer foreground boundary?**

<details>
<summary>Show answer</summary>

Compute dilated(B)-B with the stated element and boundary rule. Erosion can similarly give an inner boundary B-eroded(B).

*Sources: HC2b p.26.*

</details>

### CV1-603 · breadth

**What extensivity properties hold for dilation and erosion when the origin belongs to the structuring element?**

<details>
<summary>Show answer</summary>

Dilation contains the original foreground; erosion is contained in it, under consistent domain definitions. Finite cropped intermediate images and boundary rules need care.

*Sources: HC2b pp.22,34.*

</details>

### CV1-604 · breadth

**What is the basic complement duality of dilation and erosion?**

<details>
<summary>Show answer</summary>

Complementing a dilation gives an erosion of the complement with the reflected element, and vice versa, under consistent whole-domain definitions. The reflection matters for asymmetric elements.

*Sources: HC2b pp.22,34; Szeliski §3.3.*

</details>

## filtering

### CV1-165 · core

**What makes an image operator linear?**

<details>
<summary>Show answer</summary>

Additivity and homogeneity: H(aI+bJ)=aH(I)+bH(J). Fixed weighted sums satisfy this; median, max and thresholding generally do not.

*Sources: HC2b pp.47–50.*

</details>

### CV1-166 · core

**Write 2D discrete mathematical convolution with offsets centred at the kernel origin.**

<details>
<summary>Show answer</summary>

(I\*K)[y,x]=sum over offsets (dy,dx) K[dy,dx]\*I[y-dy,x-dx]. The sign reversal is essential.

*Sources: HC2b pp.78–80.*

</details>

### CV1-167 · core

**Write a centred sliding cross-correlation operation.**

<details>
<summary>Show answer</summary>

C[y,x]=sum over offsets (dy,dx) K[dy,dx]\*I[y+dy,x+dx]. The kernel is not flipped.

*Sources: HC2b pp.78–80.*

</details>

### CV1-168 · core

**When do correlation and convolution with a kernel give the same values?**

<details>
<summary>Show answer</summary>

When the kernel is symmetric under reversal of both spatial axes, with compatible alignment and boundary rules.

*Sources: HC2b pp.78–80.*

</details>

### CV1-169 · core

**What operation is commonly called convolution in CNN libraries?**

<details>
<summary>Show answer</summary>

Sliding cross-correlation with learned kernels, usually without flipping them. It is a naming convention; compute using the specified forward rule.

*Sources: HC2b p.50; HC5b pp.25–33.*

</details>

### CV1-170 · core

**What is a normalized box filter?**

<details>
<summary>Show answer</summary>

Equal weights over a window, divided by the number of positions. It replaces each pixel with a local mean under the boundary rule.

*Sources: HC2b pp.51–72; S2.*

</details>

### CV1-171 · core

**Why normalize a smoothing kernel to sum to one?**

<details>
<summary>Show answer</summary>

To preserve the intensity of constant regions where the full support has valid constant samples. Zero-padded boundaries can still darken.

*Sources: HC2b pp.51–87; Lab2.*

</details>

### CV1-172 · core

**What is the isotropic 2D Gaussian kernel formula?**

<details>
<summary>Show answer</summary>

G(x,y)=1/(2\*pi\*sigma^2)\*exp(-(x^2+y^2)/(2\*sigma^2)) in the continuous form. A sampled truncated kernel is often renormalized.

*Sources: HC2b pp.82–87; S2.*

</details>

### CV1-173 · core

**What does increasing Gaussian sigma do?**

<details>
<summary>Show answer</summary>

Increase spatial smoothing scale, suppress more fine detail/noise and broaden features.

*Sources: HC2b pp.82–85.*

</details>

### CV1-174 · core

**What is Gaussian separability?**

<details>
<summary>Show answer</summary>

G(x,y)=g(x)\*g(y). A 2D Gaussian filter can be applied as two 1D filters along the two axes.

*Sources: HC2b pp.86–87; S2; Lab2.*

</details>

### CV1-175 · core

**What is the per-pixel cost advantage of a separable k by k kernel?**

<details>
<summary>Show answer</summary>

Roughly 2\*k multiplications instead of k^2, excluding implementation overhead. The benefit requires a separable kernel.

*Sources: HC2b pp.86–87; S2; Lab2.*

</details>

### CV1-176 · core

**How do standard deviations combine when convolving two ideal Gaussians?**

<details>
<summary>Show answer</summary>

sigma\_total=sqrt(sigma1^2+sigma2^2), because variances add. This is idealized before finite sampling/truncation.

*Sources: HC2b p.85; S2.*

</details>

### CV1-177 · core

**What extra Gaussian sigma is needed to reach sigma\_target from existing sigma\_current?**

<details>
<summary>Show answer</summary>

sqrt(sigma\_target^2-sigma\_current^2), provided target>=current and the ideal Gaussian model applies.

*Sources: HC2b p.85; S2.*

</details>

### CV1-178 · core

**What is a low-pass image filter?**

<details>
<summary>Show answer</summary>

Passes relatively slowly varying components and suppresses high spatial frequencies; common smoothing filters are low-pass.

*Sources: HC2b pp.93–105.*

</details>

### CV1-179 · core

**What is a high-pass image filter?**

<details>
<summary>Show answer</summary>

Suppresses slowly varying components and emphasizes rapid intensity changes such as fine texture or edges.

*Sources: HC2b pp.93–105.*

</details>

### CV1-180 · core

**What sum should an ordinary discrete derivative kernel have?**

<details>
<summary>Show answer</summary>

Zero, so a constant region gives zero derivative when the boundary rule does not introduce changes.

*Sources: HC2b pp.74–80; HC3a; Lab2.*

</details>

### CV1-181 · core

**What is the image gradient?**

<details>
<summary>Show answer</summary>

The vector [Ix,Iy] of spatial intensity derivatives, pointing toward the fastest intensity increase.

*Sources: HC3a; S2; Lab2.*

</details>

### CV1-182 · core

**What are gradient magnitude and orientation?**

<details>
<summary>Show answer</summary>

Magnitude=sqrt(Ix^2+Iy^2); orientation=atan2(Iy,Ix), using the stated coordinate axes.

*Sources: HC3a pp.20–57; S2.*

</details>

### CV1-183 · core

**How is gradient direction related to the edge direction?**

<details>
<summary>Show answer</summary>

The gradient is approximately perpendicular to the edge tangent. An x derivative detects intensity change across x, often at a vertical edge.

*Sources: HC2b pp.74–76; HC3a.*

</details>

### CV1-184 · core

**Why smooth before taking image derivatives?**

<details>
<summary>Show answer</summary>

Differentiation amplifies high-frequency noise. Smoothing limits noise while setting the spatial analysis scale.

*Sources: HC3a; S2; Lab2.*

</details>

### CV1-185 · core

**What is the derivative-of-convolution identity used for edge detection?**

<details>
<summary>Show answer</summary>

d(I\*G)/dx=I\*(dG/dx) under appropriate regularity/boundary assumptions. Smooth-and-differentiate can be combined in one derivative-of-Gaussian filter.

*Sources: HC3a; S2; Lab2.*

</details>

### CV1-186 · core

**What is a Sobel derivative kernel in one common cross-correlation x convention?**

<details>
<summary>Show answer</summary>

[[-1,0,1],[-2,0,2],[-1,0,1]], combining x differencing with y smoothing. Some slides/libraries use the opposite sign; convolution flips it.

*Sources: HC2b pp.75–80; Lab2; SOURCE\_NOTES.*

</details>

### CV1-187 · core

**What is a median filter?**

<details>
<summary>Show answer</summary>

Replace a pixel by the median of neighbourhood values under a specified window/boundary rule. It is nonlinear.

*Sources: HC2b pp.89–91; S2; Lab2.*

</details>

### CV1-188 · core

**Why can a median filter suppress sparse salt-and-pepper noise?**

<details>
<summary>Show answer</summary>

The middle-ranked value is less affected by isolated extreme outliers than an arithmetic mean, while preserving some sharp transitions.

*Sources: HC2b pp.89–91; S2.*

</details>

### CV1-189 · core

**Does a median filter guarantee preservation of every edge and thin structure?**

<details>
<summary>Show answer</summary>

No. Its window can remove thin structures or shift details; success depends on noise density and feature size.

*Sources: HC2b pp.89–91; Lab2.*

</details>

### CV1-190 · core

**What do valid, same and full convolution output modes mean at a high level?**

<details>
<summary>Show answer</summary>

Valid: only full-overlap positions. Same: output aligned to an input-sized grid under a stated boundary rule. Full: all partial-overlap positions. Check even-kernel alignment.

*Sources: Lab2; S2.*

</details>

### CV1-191 · core

**What is the full linear-convolution output size for lengths N and M?**

<details>
<summary>Show answer</summary>

N+M-1. In 2D use H+Kh-1 by W+Kw-1.

*Sources: HC2b convolution; Lab2; Szeliski §3.2.*

</details>

### CV1-192 · core

**What is aliasing during image downsampling?**

<details>
<summary>Show answer</summary>

Frequencies too high for the new grid become indistinguishable from lower-frequency patterns. Low-pass filtering before subsampling can reduce it.

*Sources: HC2b pp.93–105; HC5b p.39.*

</details>

### CV1-193 · breadth

**What is a Gabor filter?**

<details>
<summary>Show answer</summary>

A Gaussian envelope multiplied by a sinusoidal carrier. It analyzes local orientation and spatial frequency, often in a filter bank.

*Sources: HC2b pp.106–107; Lab2.*

</details>

### CV1-194 · breadth

**Why do padding choices affect convolution outputs?**

<details>
<summary>Show answer</summary>

The effective neighbourhood values near edges differ. Zero, reflected, replicated and periodic extensions can give different boundary responses.

*Sources: S2; Lab2.*

</details>

### CV1-605 · core

**Write the continuous 1D Gaussian kernel.**

<details>
<summary>Show answer</summary>

G\_sigma(x)=1/(sqrt(2\*pi)\*sigma)\*exp(-x^2/(2\*sigma^2)), for sigma>0. Normalize a finite sampled kernel by its actual sum.

*Sources: Lab2 Q3; S2.*

</details>

### CV1-606 · core

**Write the first spatial derivative of a 1D Gaussian.**

<details>
<summary>Show answer</summary>

G'\_sigma(x)=-(x/sigma^2)\*G\_sigma(x). It is odd-symmetric and integrates to zero in the ideal continuous domain.

*Sources: Lab2 Q7; HC3a.*

</details>

### CV1-607 · core

**Write the second spatial derivative of a 1D Gaussian.**

<details>
<summary>Show answer</summary>

G''\_sigma(x)=(x^2/sigma^4-1/sigma^2)\*G\_sigma(x). It is even-symmetric and can support zero-crossing/curvature analysis.

*Sources: Lab2 Q8; HC3a pp.42–45.*

</details>

### CV1-608 · core

**Write the continuous 2D isotropic Laplacian of Gaussian.**

<details>
<summary>Show answer</summary>

Laplacian(G\_sigma)=((x^2+y^2-2\*sigma^2)/sigma^4)\*G\_sigma(x,y). The Laplacian sums the x and y second derivatives.

*Sources: HC3a pp.42–47; Lab2 Q8.*

</details>

### CV1-609 · core

**What is a separable anisotropic Gaussian?**

<details>
<summary>Show answer</summary>

G(x,y)=G\_sigma\_x(x)\*G\_sigma\_y(y); horizontal and vertical smoothing scales can differ, while two-pass separability remains.

*Sources: Lab2 Q4.*

</details>

### CV1-610 · core

**What is the whole-image direct versus separable Gaussian-filter complexity for HxW and width K?**

<details>
<summary>Show answer</summary>

Direct: O(H\*W\*K^2). Two separable passes: O(H\*W\*K), ignoring boundary/implementation overhead.

*Sources: Lab2 Q6.*

</details>

### CV1-611 · core

**Is convolution plus a fixed nonzero bias a linear operator in the strict algebraic sense?**

<details>
<summary>Show answer</summary>

No. The unbiased fixed convolution is linear; adding a constant bias makes it affine. Course neural-network terminology often calls both a linear layer.

*Sources: HC5b pp.45–46; S5; prerequisite linearity.*

</details>

## fourier

### CV1-195 · core

**What does the Fourier transform represent?**

<details>
<summary>Show answer</summary>

A signal or image as weighted sinusoidal/complex-exponential components indexed by spatial frequency, with magnitude and phase.

*Sources: HC2b pp.93–104.*

</details>

### CV1-196 · core

**What does low spatial frequency describe?**

<details>
<summary>Show answer</summary>

Slowly varying intensity structure and broad patterns. Zero frequency is the constant/DC component.

*Sources: HC2b pp.93–105.*

</details>

### CV1-197 · core

**What does high spatial frequency describe?**

<details>
<summary>Show answer</summary>

Rapid changes over short spatial distances, such as fine texture and sharp transitions. Noise can also have high-frequency content.

*Sources: HC2b pp.93–105.*

</details>

### CV1-198 · core

**What is Euler's formula?**

<details>
<summary>Show answer</summary>

exp(i\*theta)=cos(theta)+i\*sin(theta); therefore exp(-i\*theta)=cos(theta)-i\*sin(theta).

*Sources: HC2b p.99; SOURCE\_NOTES.*

</details>

### CV1-199 · core

**How are sinusoid frequency u, angular frequency omega and period T related?**

<details>
<summary>Show answer</summary>

omega=2\*pi\*u and T=1/u for positive nonzero u. Use consistent spatial/time units.

*Sources: HC2b pp.96–99.*

</details>

### CV1-200 · core

**For A\*exp(i\*(omega\*x+phi)), what do A, omega and phi mean?**

<details>
<summary>Show answer</summary>

A is magnitude/radius, omega is angular rate, and phi is the starting phase angle. Real and imaginary parts are cosine and sine components.

*Sources: HC2b pp.97–100.*

</details>

### CV1-201 · core

**How are real and imaginary components recovered from magnitude A and phase phi?**

<details>
<summary>Show answer</summary>

real=A\*cos(phi), imaginary=A\*sin(phi).

*Sources: HC2b pp.97–100.*

</details>

### CV1-202 · core

**How is the magnitude of a+ib computed?**

<details>
<summary>Show answer</summary>

sqrt(a^2+b^2), equivalently abs(a+1j\*b). Magnitude squared is a^2+b^2, not the same quantity.

*Sources: HC2b p.100.*

</details>

### CV1-203 · core

**How is the phase of a+ib computed in NumPy?**

<details>
<summary>Show answer</summary>

np.arctan2(b,a): imaginary first, real second. It retains the correct quadrant.

*Sources: HC2b p.100; SOURCE\_NOTES.*

</details>

### CV1-204 · core

**Why use atan2 rather than atan(b/a) for phase?**

<details>
<summary>Show answer</summary>

atan2 handles quadrants and a=0 correctly. A plain ratio loses quadrant information and can divide by zero. Phase is undefined at zero magnitude.

*Sources: HC2b pp.97–100; Lab2.*

</details>

### CV1-205 · core

**Write the unnormalized N-point forward DFT convention used in the practice questions.**

<details>
<summary>Show answer</summary>

F[k]=sum(n=0..N-1) f[n]\*exp(-2\*pi\*i\*k\*n/N). The inverse has a positive exponent and a 1/N factor.

*Sources: HC2b pp.102–103; SOURCE\_NOTES.*

</details>

### CV1-206 · core

**What is F[0] in an unnormalized DFT?**

<details>
<summary>Show answer</summary>

The sum of all samples. Divide by sample count to obtain the mean. Other normalization conventions scale this value.

*Sources: HC2b pp.99–103.*

</details>

### CV1-207 · core

**Why can a real-valued image have a complex-valued Fourier transform?**

<details>
<summary>Show answer</summary>

Complex coefficients encode sinusoid magnitude and phase through two components. Real input does not mean every phase is zero.

*Sources: HC2b pp.97–104.*

</details>

### CV1-208 · core

**What symmetry does the DFT of a real signal have?**

<details>
<summary>Show answer</summary>

F[-k]=conjugate(F[k]) with indices modulo N; in images use the corresponding opposite frequency pair on both axes.

*Sources: HC2b pp.99–104; Szeliski §3.4.*

</details>

### CV1-209 · core

**State the convolution theorem under a compatible normalization.**

<details>
<summary>Show answer</summary>

Fourier transform of spatial convolution is pointwise multiplication of spectra. Spatial multiplication corresponds to frequency convolution, with convention-dependent scale factors.

*Sources: HC2b p.101; Szeliski §3.4.*

</details>

### CV1-210 · core

**What boundary assumption does an unpadded DFT convolution make?**

<details>
<summary>Show answer</summary>

Periodic/circular boundaries. Products of finite DFTs yield circular convolution, not automatically full linear convolution.

*Sources: HC2b pp.101–103; Szeliski §3.4.*

</details>

### CV1-211 · core

**How much zero padding is needed for 1D DFT-based full linear convolution?**

<details>
<summary>Show answer</summary>

At least N+M-1 transform samples for signals of lengths N and M. In 2D pad each axis to the corresponding summed size minus one.

*Sources: HC2b pp.101–103; Szeliski §3.4.*

</details>

### CV1-212 · core

**What does a spatial translation do to the Fourier spectrum in the ideal/circular case?**

<details>
<summary>Show answer</summary>

Multiply by a unit-magnitude phase factor exp(-i\*omega\*shift). Magnitude stays unchanged, while phase changes with frequency.

*Sources: HC2b Fourier; Szeliski §3.4.*

</details>

### CV1-213 · core

**Does Fourier magnitude alone determine a general image?**

<details>
<summary>Show answer</summary>

No. Phase contains essential spatial arrangement information; different images can share magnitudes.

*Sources: HC2b p.104; Szeliski §3.4.*

</details>

### CV1-214 · breadth

**What does fftshift do to a frequency-array visualization?**

<details>
<summary>Show answer</summary>

Reorders entries to put zero frequency near the centre. It does not itself filter or change coefficient values.

*Sources: HC2b p.104; Lab2.*

</details>

### CV1-215 · breadth

**Why plot log magnitude rather than raw Fourier magnitude?**

<details>
<summary>Show answer</summary>

Large dynamic range can hide weaker components. A transform such as log(1+abs(F)) makes them visible without defining a new frequency spectrum.

*Sources: HC2b p.104; Lab2.*

</details>

### CV1-216 · core

**Does discarding the imaginary part of each Fourier coefficient preserve phase information?**

<details>
<summary>Show answer</summary>

No. It generally changes the signal and can destroy the representation of translated/asymmetric structure.

*Sources: HC2b pp.97–104.*

</details>

### CV1-612 · core

**Write the unnormalized 2D DFT for an HxW image I[y,x].**

<details>
<summary>Show answer</summary>

F[v,u]=sum(y=0..H-1,x=0..W-1) I[y,x]\*exp(-2\*pi\*i\*(v\*y/H+u\*x/W)). NumPy's default inverse divides by H\*W.

*Sources: HC2b pp.102–104; Szeliski §3.4; SOURCE\_NOTES.*

</details>

## features

### CV1-217 · core

**What is an intensity edge?**

<details>
<summary>Show answer</summary>

A local rapid change in intensity, which can come from depth, surface orientation, material or illumination changes.

*Sources: HC3a; S3.*

</details>

### CV1-218 · core

**Why does edge detection alone not identify complete object boundaries?**

<details>
<summary>Show answer</summary>

Edges can be fragmented, noisy or caused by texture/shadows; their membership in objects or lines is not automatically known.

*Sources: HC3a pp.69–74.*

</details>

### CV1-219 · core

**What are the principal stages of the Canny detector?**

<details>
<summary>Show answer</summary>

Gaussian smoothing/derivative filtering; gradient magnitude and direction; directional non-maximum suppression; double-threshold hysteresis and edge linking.

*Sources: HC3a pp.55–66; S2.*

</details>

### CV1-220 · core

**What does Canny non-maximum suppression compare?**

<details>
<summary>Show answer</summary>

Gradient magnitude against neighbouring/interpolated magnitudes along the gradient direction, not simply along the edge tangent.

*Sources: HC3a pp.58–59.*

</details>

### CV1-221 · core

**What is the purpose of Canny non-maximum suppression?**

<details>
<summary>Show answer</summary>

Thin a broad gradient response to locally maximal edge locations before hysteresis.

*Sources: HC3a pp.58–65.*

</details>

### CV1-222 · core

**How does Canny hysteresis use its high and low thresholds?**

<details>
<summary>Show answer</summary>

High threshold seeds strong edges; weak pixels above the low threshold survive if connected to a strong edge through qualifying pixels.

*Sources: HC3a pp.60–65.*

</details>

### CV1-223 · core

**Can a weak Canny pixel survive through several other weak pixels?**

<details>
<summary>Show answer</summary>

Yes, if the weak/strong chain reaches a strong seed under the specified connectivity. It need not be directly adjacent to a strong pixel.

*Sources: HC3a pp.60–65.*

</details>

### CV1-224 · core

**Does a weak Canny component with no strong seed survive?**

<details>
<summary>Show answer</summary>

No, not under ordinary hysteresis. Exceeding the low threshold alone is insufficient.

*Sources: HC3a pp.60–65.*

</details>

### CV1-225 · core

**How does Gaussian scale influence detected edges?**

<details>
<summary>Show answer</summary>

Larger sigma reduces noise and fine detail but can merge or weaken closely spaced edges. Small sigma is more sensitive to fine structure and noise.

*Sources: HC3a p.66.*

</details>

### CV1-226 · breadth

**Who is associated with the Canny edge detector?**

<details>
<summary>Show answer</summary>

John Canny; his standard computational edge-detection work is from 1986.

*Sources: HC4b p.21; HC3a.*

</details>

### CV1-227 · core

**What distinguishes a corner from an edge in local intensity variation?**

<details>
<summary>Show answer</summary>

A corner has substantial variation in at least two independent spatial directions; an edge has strong variation mainly normal to one direction.

*Sources: S3; Lab3 Section 2.*

</details>

### CV1-228 · core

**Write the local structure/second-moment tensor M.**

<details>
<summary>Show answer</summary>

M=sum over the window of w\*[[Ix^2,Ix\*Iy],[Ix\*Iy,Iy^2]]. Aggregate gradient products, not just the mean gradient.

*Sources: S3; Lab3.*

</details>

### CV1-229 · core

**What do the eigenvalues of M measure?**

<details>
<summary>Show answer</summary>

Local intensity-change strength along its principal directions. Both small: flat; one large: edge; both large: corner-like structure.

*Sources: S3; Lab3.*

</details>

### CV1-230 · core

**Write the Harris corner response.**

<details>
<summary>Show answer</summary>

R=det(M)-k\*trace(M)^2=lambda1\*lambda2-k\*(lambda1+lambda2)^2. The value depends on scale and gradient magnitude.

*Sources: S3; Lab3.*

</details>

### CV1-231 · core

**What does a large negative Harris response usually indicate?**

<details>
<summary>Show answer</summary>

An edge: one large eigenvalue and one small eigenvalue. A large positive response often indicates a corner; near zero can indicate flat structure.

*Sources: S3; Lab3.*

</details>

### CV1-232 · core

**Write the Shi–Tomasi cornerness score.**

<details>
<summary>Show answer</summary>

min(lambda1,lambda2), the smaller structure-tensor eigenvalue. Use a threshold and spatial selection to choose features.

*Sources: Lab3 Section 2.*

</details>

### CV1-233 · core

**Why are corners useful for Lucas–Kanade tracking?**

<details>
<summary>Show answer</summary>

Their varied gradient directions make the local motion system well conditioned in both displacement directions. Flat patches and straight edges leave ambiguity.

*Sources: S3; Lab3 Sections 2–4.*

</details>

### CV1-234 · core

**Is the ideal Harris response rotation invariant?**

<details>
<summary>Show answer</summary>

Yes, with a suitable rotationally symmetric window: rotating coordinates changes M by a similarity transform, preserving eigenvalues, determinant and trace. Sampling and rectangular windows can affect implementations.

*Sources: S3; Lab3.*

</details>

### CV1-235 · core

**Is ordinary single-scale Harris detection scale invariant?**

<details>
<summary>Show answer</summary>

No. Changing object scale changes the window's relation to the structure; a scale-selection method is needed for comparable scale robustness.

*Sources: S3; Lab3; HC4a pp.36–42.*

</details>

### CV1-236 · core

**Why perform spatial non-maximum suppression on a corner-response map?**

<details>
<summary>Show answer</summary>

To avoid selecting many neighbouring pixels around the same local feature. It is distinct from Canny's directional thinning.

*Sources: Lab3.*

</details>

### CV1-237 · core

**What is the Laplacian of Gaussian (LoG)?**

<details>
<summary>Show answer</summary>

Apply the Laplacian, the sum of second spatial derivatives, to a Gaussian-smoothed image; used for blob/scale analysis and related edge cues.

*Sources: HC4a pp.37–41; Szeliski §7.1.*

</details>

### CV1-238 · core

**What is a feature's characteristic scale?**

<details>
<summary>Show answer</summary>

The scale at which a suitable scale-normalized detector gives an extremal response for that structure.

*Sources: HC4a pp.37–41.*

</details>

### CV1-239 · breadth

**What does a Hough transform do at a high level?**

<details>
<summary>Show answer</summary>

Let image features vote for model parameters; peaks in an accumulator indicate supported lines or other shapes. This pack does not add advanced Hough variants.

*Sources: HC3a outline; Szeliski §7.4.*

</details>

### CV1-240 · core

**What is a normal-form line representation that admits vertical lines?**

<details>
<summary>Show answer</summary>

a\*x+b\*y+c=0, with sqrt(a^2+b^2)=1 when measuring signed perpendicular distance. Unlike y=m\*x+b, it can represent x=constant with finite coefficients.

*Sources: HC3a pp.78–82.*

</details>

### CV1-613 · core

**How can second derivatives locate an ideal smoothed step edge?**

<details>
<summary>Show answer</summary>

A first-derivative extremum corresponds to a second-derivative zero crossing, with appropriate response-strength tests; not every noise zero crossing is a true edge.

*Sources: HC3a pp.41–45; Lab2 Q8.*

</details>

### CV1-614 · core

**How does derivative scale normalization work at a high level?**

<details>
<summary>Show answer</summary>

Multiply an m-th spatial derivative at Gaussian scale sigma by sigma^m under the standard normalization, so responses are more comparable across scale.

*Sources: HC3a pp.48–50.*

</details>

### CV1-615 · core

**What does Difference of Gaussians mean?**

<details>
<summary>Show answer</summary>

Subtract images/kernels smoothed at two nearby Gaussian scales. It is a band-pass response and approximates a scale-normalized LoG for suitable nearby scales.

*Sources: HC3a pp.47,51; HC4a p.41.*

</details>

### CV1-616 · core

**Why is the acronym DoG potentially confusing in edge/SIFT discussions?**

<details>
<summary>Show answer</summary>

Difference of Gaussians uses two smoothing scales; derivative of Gaussian takes a spatial derivative. They are related but not the same operation. Use the full name/formula.

*Sources: HC3a pp.47,51,56; Lab2.*

</details>

### CV1-617 · core

**What does HoG/HOG stand for?**

<details>
<summary>Show answer</summary>

Histogram of Oriented Gradients: aggregate local gradient directions, commonly weighted by magnitude.

*Sources: S3 Exercise 2.*

</details>

### CV1-618 · core

**How do you build the simplified HoG histogram in Seminar 3?**

<details>
<summary>Show answer</summary>

Compute gradient vectors, magnitudes and orientations; map orientations to the specified bins; sum magnitude votes. The seminar also compares unweighted counts.

*Sources: S3 Exercise 2.*

</details>

### CV1-619 · core

**What are unsigned gradient orientations in HoG?**

<details>
<summary>Show answer</summary>

Angles modulo 180 degrees: theta and theta+180 use the same orientation. Use an explicit binning/interpolation convention.

*Sources: S3 Q2d.*

</details>

### CV1-620 · core

**Why should zero-gradient pixels have no vote in magnitude-weighted HoG?**

<details>
<summary>Show answer</summary>

Their magnitude is zero, and their direction has no physical meaning. A stored placeholder angle must not create a nonzero vote.

*Sources: S3 Q2b–d.*

</details>

### CV1-621 · core

**Is the seminar's raw magnitude-weighted HoG invariant to I'=aI for a>0?**

<details>
<summary>Show answer</summary>

No. Gradient magnitudes and histogram entries scale by a. Normalizing a nonzero histogram can remove that common scale under ideal assumptions.

*Sources: S3 Q2e; SOURCE\_NOTES.*

</details>

### CV1-622 · core

**Is a derivative-based HoG invariant to I'=I+b for constant b?**

<details>
<summary>Show answer</summary>

In the interior under compatible boundary rules, derivatives remove the constant offset, so the descriptor is unchanged. Clipping or padding effects can break this.

*Sources: S3 Q2e.*

</details>

### CV1-623 · core

**Is ordinary HoG rotation invariant without orientation alignment?**

<details>
<summary>Show answer</summary>

No. Rotation changes which orientation bins receive votes and can change spatial cells. Unlike SIFT, basic HoG does not automatically align a dominant orientation.

*Sources: S3 Q2f; HC4a p.42.*

</details>

### CV1-624 · core

**Why can sign reversal of both derivatives leave unsigned HoG unchanged but change signed angles?**

<details>
<summary>Show answer</summary>

Reversal rotates the gradient by 180 degrees. Unsigned bins identify those directions, while signed 0..360 angles distinguish them. Magnitude stays the same.

*Sources: S3 Q2a–f; SOURCE\_NOTES.*

</details>

### CV1-625 · breadth

**Who are Harris corners named after?**

<details>
<summary>Show answer</summary>

Chris Harris and Mike Stephens, associated with the 1988 corner detector.

*Sources: HC5b p.10; S3.*

</details>

## fitting

### CV1-241 · core

**What does ordinary least squares minimize?**

<details>
<summary>Show answer</summary>

The sum of squared residuals under the chosen observation/model representation. For y=mx+b, these are vertical y residuals.

*Sources: HC3a pp.76–79.*

</details>

### CV1-242 · core

**Write the full-column-rank OLS solution for A\*p=y.**

<details>
<summary>Show answer</summary>

p=(A.T\*A)^(-1)\*A.T\*y. Numerically prefer a least-squares solver over forming an explicit inverse.

*Sources: HC3a p.77; Coding examples Q1,Q5.*

</details>

### CV1-243 · core

**Why can ordinary least squares be highly sensitive to outliers?**

<details>
<summary>Show answer</summary>

Squaring residuals gives extreme errors large influence, so a few outliers can substantially move the fitted model.

*Sources: HC3a pp.79–88.*

</details>

### CV1-244 · core

**What does total least squares change in 2D line fitting?**

<details>
<summary>Show answer</summary>

Use perpendicular distances and a symmetric line representation instead of choosing only vertical residuals in y=mx+b.

*Sources: HC3a pp.78–82.*

</details>

### CV1-245 · core

**What constant estimate minimizes summed squared scalar errors?**

<details>
<summary>Show answer</summary>

The arithmetic mean. Large outliers can strongly affect it.

*Sources: HC3a pp.83–85.*

</details>

### CV1-246 · core

**What constant estimate minimizes summed absolute scalar errors?**

<details>
<summary>Show answer</summary>

A median. For an even number of values, any value between the two central sorted values minimizes the absolute-error objective; their mean is a conventional median.

*Sources: HC3a pp.83–85.*

</details>

### CV1-247 · breadth

**What does Huber loss do at a high level?**

<details>
<summary>Show answer</summary>

Behaves quadratically for small residuals and linearly for large residuals, controlled by a transition parameter. It reduces outlier influence compared with pure squared loss.

*Sources: HC3a p.86.*

</details>

### CV1-248 · core

**What does RANSAC stand for?**

<details>
<summary>Show answer</summary>

RANdom SAmple Consensus. It estimates a model from small random subsets and evaluates their agreement with the full data.

*Sources: HC3a p.91.*

</details>

### CV1-249 · breadth

**Who introduced RANSAC?**

<details>
<summary>Show answer</summary>

Martin Fischler and Robert Bolles, 1981.

*Sources: HC3a pp.91,103.*

</details>

### CV1-250 · core

**What are the main RANSAC steps?**

<details>
<summary>Show answer</summary>

Sample a nondegenerate minimal subset; fit a candidate; compute residuals for all data; classify/count inliers; retain the best consensus; finally refit using its inliers.

*Sources: HC3a pp.91–101; HC4a pp.45–48.*

</details>

### CV1-251 · core

**What is an inlier in RANSAC?**

<details>
<summary>Show answer</summary>

A datum whose residual against the candidate model satisfies the stated threshold and residual definition. It is not necessarily a truly correct correspondence.

*Sources: HC3a; HC4a p.48.*

</details>

### CV1-252 · core

**Why reject a degenerate RANSAC sample?**

<details>
<summary>Show answer</summary>

Even if its points are correct, its geometry may not uniquely determine the requested model, such as collinear affine control points.

*Sources: HC4a pp.47–55; Lab4.*

</details>

### CV1-253 · core

**What are minimal sample sizes for a 2D line, circle, affine transform and homography?**

<details>
<summary>Show answer</summary>

Line: 2 distinct points. Circle: 3 noncollinear points. Affine: 3 noncollinear point pairs. Homography: 4 point pairs in general position.

*Sources: HC3a pp.92–97; HC4a pp.47–50; Lab4.*

</details>

### CV1-254 · core

**What is the all-inlier probability for an independent RANSAC sample of size s?**

<details>
<summary>Show answer</summary>

w^s, where w is the inlier fraction. Nondegeneracy is a separate requirement.

*Sources: HC3a pp.104–105.*

</details>

### CV1-255 · core

**What is the probability of at least one all-inlier sample after N independent RANSAC iterations?**

<details>
<summary>Show answer</summary>

p=1-(1-w^s)^N under the independent-sampling approximation.

*Sources: HC3a pp.104–105.*

</details>

### CV1-256 · core

**Give the minimum RANSAC iteration formula for desired success p.**

<details>
<summary>Show answer</summary>

N=ceil(log(1-p)/log(1-w^s)), for 0<w^s<1. Use the model's minimal sample size and round upwards.

*Sources: HC3a pp.104–105.*

</details>

### CV1-257 · core

**What increases the required RANSAC iteration count?**

<details>
<summary>Show answer</summary>

Lower inlier fraction, larger minimal sample size or higher desired success probability.

*Sources: HC3a pp.104–109.*

</details>

### CV1-258 · core

**Does RANSAC fail in principle whenever the inlier fraction is below 50%?**

<details>
<summary>Show answer</summary>

No. It can work with a minority of inliers, but may need a large iteration budget and careful model/threshold choice.

*Sources: HC3a pp.104–109.*

</details>

### CV1-259 · core

**Why refit the final RANSAC model on all selected inliers?**

<details>
<summary>Show answer</summary>

A minimal sample is noisy. Refitting uses more compatible data to improve precision after robust selection.

*Sources: HC3a p.101; HC4a pp.46–48.*

</details>

### CV1-260 · core

**Why does increasing the inlier threshold not necessarily improve RANSAC accuracy?**

<details>
<summary>Show answer</summary>

It can include erroneous correspondences and bias the refit. Thresholds must match the residual's units and expected noise.

*Sources: HC4a p.48; HC3a p.109.*

</details>

### CV1-261 · breadth

**Why is fitting several models harder than one basic RANSAC fit?**

<details>
<summary>Show answer</summary>

One consensus can dominate. Multiple structures need extra selection or repeated/multi-model procedures; one fit does not assign all scene lines.

*Sources: HC3a p.109.*

</details>

### CV1-626 · core

**What is the minimal RANSAC sample for a plane in 3D?**

<details>
<summary>Show answer</summary>

Three noncollinear 3D points. Three collinear points do not determine a unique plane.

*Sources: S4 Q1d.*

</details>

### CV1-627 · core

**If each sample draws s distinct points from N, with I known inliers, what is the exact all-inlier probability?**

<details>
<summary>Show answer</summary>

choose(I,s)/choose(N,s), for I>=s. The familiar (I/N)^s is an independent-draw approximation; distinguish within-sample sampling without replacement.

*Sources: S4 Q1e; HC3a iteration formula; prerequisite probability.*

</details>

### CV1-628 · core

**Does an ordinary randomized finite-budget RANSAC run guarantee finding an all-inlier sample?**

<details>
<summary>Show answer</summary>

No. It has a success probability under sampling assumptions. A deterministic exhaustive distinct-subset count is a different guarantee.

*Sources: HC3a pp.104–109; S4 Q1e; SOURCE\_NOTES.*

</details>

## flow

### CV1-262 · core

**What is optical flow?**

<details>
<summary>Show answer</summary>

The apparent 2D displacement or velocity field of image structure between frames, with units determined by frame/time spacing.

*Sources: HC3b pp.8–38.*

</details>

### CV1-263 · core

**How does optical flow differ from 3D scene motion?**

<details>
<summary>Show answer</summary>

It is an image-plane apparent motion field, affected by projection and appearance. It is not directly a metric 3D velocity and can reflect lighting changes.

*Sources: HC3b pp.8–38.*

</details>

### CV1-264 · core

**State brightness constancy for displacement (u,v) across one time step.**

<details>
<summary>Show answer</summary>

I(x+u,y+v,t+1)=I(x,y,t). It assumes the tracked appearance remains constant, apart from motion.

*Sources: HC3b p.39.*

</details>

### CV1-265 · core

**Derive the local optical-flow constraint at a high level.**

<details>
<summary>Show answer</summary>

First-order Taylor-expand brightness constancy for small motion; cancel I(x,y,t), giving Ix\*u+Iy\*v+It=0.

*Sources: HC3b p.40; S3.*

</details>

### CV1-266 · core

**Why does one optical-flow constraint not determine both u and v?**

<details>
<summary>Show answer</summary>

It gives one scalar equation for two unknown components. Only the gradient-normal motion component is constrained.

*Sources: HC3b pp.40–47.*

</details>

### CV1-267 · core

**What is the aperture problem?**

<details>
<summary>Show answer</summary>

Locally observing a straight edge cannot reveal motion along the edge; different tangential motions can produce the same local change.

*Sources: HC3b pp.41–47.*

</details>

### CV1-268 · core

**What extra assumption does local Lucas–Kanade make?**

<details>
<summary>Show answer</summary>

The pixels in a chosen neighbourhood share one approximately constant flow vector. Stack their constraints to estimate it.

*Sources: HC3b pp.42–47; Lab3.*

</details>

### CV1-269 · core

**Write the Lucas–Kanade least-squares system and solution convention.**

<details>
<summary>Show answer</summary>

Rows of A are [Ix,Iy], b=-It; solve A\*[u,v]=b in least squares. For full rank, flow=(A.T\*A)^(-1)\*A.T\*b.

*Sources: HC3b p.47; S3; Lab3.*

</details>

### CV1-270 · core

**When is a local Lucas–Kanade flow well constrained?**

<details>
<summary>Show answer</summary>

A has rank 2 and its structure tensor A.T\*A has two sufficiently large eigenvalues with manageable condition number.

*Sources: S3; Lab3.*

</details>

### CV1-271 · core

**What happens to Lucas–Kanade in a flat patch?**

<details>
<summary>Show answer</summary>

Spatial derivatives are near zero, so there is little information to determine either displacement component; estimates become unstable or unobservable.

*Sources: HC3b p.47; Lab3.*

</details>

### CV1-272 · core

**What happens to Lucas–Kanade on a straight edge?**

<details>
<summary>Show answer</summary>

Gradient directions are nearly parallel; tangential motion is poorly constrained because the system is close to rank 1.

*Sources: HC3b pp.41–47; S3.*

</details>

### CV1-273 · core

**Why can corners be better flow features than edges?**

<details>
<summary>Show answer</summary>

Independent local gradient directions constrain both u and v, matching the corner/structure-tensor criterion.

*Sources: S3; Lab3.*

</details>

### CV1-274 · core

**What are key assumptions/conditions behind the basic Lucas–Kanade estimate?**

<details>
<summary>Show answer</summary>

Brightness constancy, small displacement for linearization, common local motion, sufficient texture and valid visible correspondence.

*Sources: HC3b pp.39–47.*

</details>

### CV1-275 · core

**What violates brightness constancy?**

<details>
<summary>Show answer</summary>

Lighting changes, shadows, specular changes, nonlinear response changes or occlusion can change intensity without the assumed motion correspondence.

*Sources: HC3b pp.57–58; Lab3.*

</details>

### CV1-276 · core

**Why can a large Lucas–Kanade window hurt near a motion boundary?**

<details>
<summary>Show answer</summary>

It combines pixels with different motion vectors, violating the shared-flow assumption even while adding more equations.

*Sources: HC3b pp.42–47.*

</details>

### CV1-277 · core

**Why use a coarse-to-fine image pyramid for optical flow?**

<details>
<summary>Show answer</summary>

Large full-resolution motion becomes smaller in coarse pixels, making local linearization more plausible. Upsample, rescale, warp and refine.

*Sources: HC3b pp.48–54.*

</details>

### CV1-278 · core

**How must flow vectors scale when going from half resolution to full resolution?**

<details>
<summary>Show answer</summary>

Multiply displacement components by 2 after spatial upsampling. Vector units depend on pixel size.

*Sources: HC3b pp.52–54; Lab3.*

</details>

### CV1-279 · core

**What is warping's role in iterative flow estimation?**

<details>
<summary>Show answer</summary>

Use the current displacement to align frames, then estimate the smaller residual motion from the remaining mismatch.

*Sources: HC3b pp.53–56.*

</details>

### CV1-280 · core

**What limitation can a coarse-to-fine flow pyramid have?**

<details>
<summary>Show answer</summary>

Small/thin structures can disappear at coarse levels, or an incorrect coarse match can trap finer refinement. It does not guarantee recovery of all large motion.

*Sources: HC3b pp.52–58.*

</details>

### CV1-281 · core

**Why is occlusion a fundamental problem for flow correspondence?**

<details>
<summary>Show answer</summary>

A pixel's scene point may not be visible in the other frame, so its assumed matching observation does not exist.

*Sources: HC3b pp.45–58.*

</details>

### CV1-282 · breadth

**How do sparse and dense optical flow differ?**

<details>
<summary>Show answer</summary>

Sparse flow estimates displacements at selected features; dense flow estimates a vector for most or all image pixels.

*Sources: HC3b; Lab3.*

</details>

### CV1-283 · breadth

**How does Horn–Schunck differ from local Lucas–Kanade at a high level?**

<details>
<summary>Show answer</summary>

Horn–Schunck uses a global smoothness regularizer to encourage a dense smooth field; Lucas–Kanade uses local common-flow windows. Advanced Horn–Schunck details are optional in the lab.

*Sources: HC3b pp.57–59; Lab3 optional material.*

</details>

### CV1-284 · breadth

**Give uses of optical flow beyond tracking.**

<details>
<summary>Show answer</summary>

Video stabilization, interpolation, motion analysis, denoising/super-resolution, compression and photometric consistency for learning.

*Sources: HC3b pp.62–70.*

</details>

## tracking

### CV1-285 · core

**What is template-based tracking?**

<details>
<summary>Show answer</summary>

Search for the region in a new frame that best matches a fixed appearance template, often near the previous location.

*Sources: HC3b pp.75–87.*

</details>

### CV1-286 · core

**What is SSD in template matching?**

<details>
<summary>Show answer</summary>

Sum of squared differences: SSD(y)=sum\_x (I(x+y)-T(x))^2. Select the displacement with smallest cost.

*Sources: HC3b p.79.*

</details>

### CV1-287 · core

**What is unnormalized cross-correlation in template matching?**

<details>
<summary>Show answer</summary>

CC(y)=sum\_x I(x+y)\*T(x). Select the largest response, but raw correlation can favour brightness/energy changes.

*Sources: HC3b pp.79–87.*

</details>

### CV1-288 · core

**Is raw SSD invariant to additive brightness change?**

<details>
<summary>Show answer</summary>

No. A constant offset changes the squared differences even for a geometrically correct match. Mean-normalized comparisons can reduce this sensitivity.

*Sources: HC3b pp.75–87; Szeliski §9.1.*

</details>

### CV1-289 · breadth

**What makes zero-mean normalized cross-correlation relatively robust to brightness offset and positive gain?**

<details>
<summary>Show answer</summary>

Subtracting patch means removes a constant offset; dividing by centred patch norms removes positive scale, when variance is nonzero. Normalization without mean subtraction does not remove offsets.

*Sources: Szeliski §9.1; HC6b p.103.*

</details>

### CV1-290 · core

**Why restrict a tracker's search around its previous position?**

<details>
<summary>Show answer</summary>

A motion prior reduces computation and ambiguous matches, but can miss a target that moves farther than the allowed search region.

*Sources: HC3b pp.77,80,87.*

</details>

### CV1-291 · core

**What is tracking by detection?**

<details>
<summary>Show answer</summary>

Detect or classify candidate regions in each frame and associate/update the target using an appearance model and motion constraints.

*Sources: HC3b pp.89–106.*

</details>

### CV1-292 · core

**What is tracking drift?**

<details>
<summary>Show answer</summary>

Progressive loss of the true target, often because incorrect self-labelled updates learn background or an occluder.

*Sources: HC3b pp.89–106.*

</details>

### CV1-293 · core

**What representation does mean-shift tracking often compare?**

<details>
<summary>Show answer</summary>

Target and candidate-region colour histograms, using a similarity measure; local updates seek a more similar candidate position.

*Sources: HC3b p.122.*

</details>

### CV1-294 · breadth

**What can make colour-histogram tracking robust and what can make it fail?**

<details>
<summary>Show answer</summary>

It tolerates some pixel rearrangement but loses spatial layout; similarly coloured backgrounds, large appearance change and occlusion can confuse it.

*Sources: HC3b pp.78,122; Szeliski §9.4.4.*

</details>

### CV1-295 · breadth

**How can descriptor-based tracking tolerate some occlusion better than one raw template?**

<details>
<summary>Show answer</summary>

Visible local descriptors may still match even when part of the target is hidden; geometric and object/background consistency are still needed.

*Sources: HC3b pp.97–106.*

</details>

## geometry

### CV1-296 · core

**What is a global image transform?**

<details>
<summary>Show answer</summary>

One parameterized coordinate mapping is applied across the image domain; it is not independently chosen for each pixel.

*Sources: HC4a p.6.*

</details>

### CV1-297 · core

**Give a homogeneous 2D translation matrix for column vectors.**

<details>
<summary>Show answer</summary>

T=[[1,0,tx],[0,1,ty],[0,0,1]]. It sends [x,y,1] to [x+tx,y+ty,1].

*Sources: HC4a pp.14–16.*

</details>

### CV1-298 · core

**Give a homogeneous 2D scaling matrix.**

<details>
<summary>Show answer</summary>

S=diag(sx,sy,1). Uniform scaling has sx=sy; nonuniform scaling can change angles and shapes.

*Sources: HC4a pp.8–10,16.*

</details>

### CV1-299 · core

**What is a 2D affine transformation?**

<details>
<summary>Show answer</summary>

x'=A\*x+t. Its homogeneous matrix has last row [0,0,1] after normalization and 6 free parameters in general.

*Sources: HC4a pp.17–22.*

</details>

### CV1-300 · core

**What is a 2D similarity transformation?**

<details>
<summary>Show answer</summary>

Rotation plus translation plus one uniform scale; ordinarily 4 degrees of freedom: angle, two translations and scale.

*Sources: HC4a p.21.*

</details>

### CV1-301 · core

**What is a 2D rigid/Euclidean transformation?**

<details>
<summary>Show answer</summary>

Rotation plus translation, with 3 degrees of freedom. It preserves Euclidean distances and angles.

*Sources: HC4a p.21.*

</details>

### CV1-302 · core

**Which properties does a nonsingular affine transform preserve?**

<details>
<summary>Show answer</summary>

Lines, parallelism and ratios of distances along a common line. It does not generally preserve angles, lengths or areas unchanged.

*Sources: HC4a pp.17–18.*

</details>

### CV1-303 · core

**What is a planar projective transformation or homography?**

<details>
<summary>Show answer</summary>

A nonsingular 3x3 homogeneous mapping between projective image-plane points, defined up to a nonzero scale. Dehomogenization makes its Cartesian mapping projective.

*Sources: HC4a pp.20–22.*

</details>

### CV1-304 · core

**Why does a homography have 8 degrees of freedom?**

<details>
<summary>Show answer</summary>

Its 9 matrix entries are defined only up to one common nonzero scale, leaving 8 independent parameters.

*Sources: HC4a p.22.*

</details>

### CV1-305 · core

**What do general nonsingular homographies preserve?**

<details>
<summary>Show answer</summary>

Incidence and collinearity: straight lines map to straight lines. They do not generally preserve Euclidean lengths, angles, parallelism or ordinary distance ratios.

*Sources: HC1b p.28; HC4a pp.20–22.*

</details>

### CV1-306 · core

**How do you compose two transforms H followed by T with column-vector coordinates?**

<details>
<summary>Show answer</summary>

Use T\*H. The rightmost transform acts first; multiplication order generally matters.

*Sources: HC4a p.19.*

</details>

### CV1-307 · core

**What is forward image warping?**

<details>
<summary>Show answer</summary>

Iterate over source pixels, map their coordinates forward and place/splat their values in the destination. Discretization can leave holes or create collisions.

*Sources: HC4a pp.24–27.*

</details>

### CV1-308 · core

**What is backward/inverse image warping?**

<details>
<summary>Show answer</summary>

Iterate over destination pixels, inverse-map each location and sample/interpolate the source. Handle out-of-domain samples explicitly.

*Sources: HC4a pp.28–31.*

</details>

### CV1-309 · core

**Why is backward warping commonly used for raster images?**

<details>
<summary>Show answer</summary>

It determines a sample for each destination location within mapped source coverage, avoiding forward-mapping discretization holes. It does not create valid data outside coverage.

*Sources: HC4a pp.28–31.*

</details>

### CV1-310 · core

**What is nearest-neighbour interpolation?**

<details>
<summary>Show answer</summary>

Use the value of the nearest source grid location. It is simple but can look blocky and does not average neighbouring values.

*Sources: HC4a p.29; Lab4.*

</details>

### CV1-311 · core

**What is bilinear interpolation?**

<details>
<summary>Show answer</summary>

A weighted average of four surrounding source pixels, linear separately in x and y. Weights depend on fractional position and sum to one.

*Sources: HC4a p.30; Lab4.*

</details>

### CV1-312 · core

**Give bilinear interpolation weights for fractional offsets dx and dy.**

<details>
<summary>Show answer</summary>

Top-left:(1-dx)\*(1-dy); top-right:dx\*(1-dy); bottom-left:(1-dx)\*dy; bottom-right:dx\*dy, using I[y,x].

*Sources: HC4a p.30; Lab4.*

</details>

### CV1-313 · core

**Under what two major conditions can two ideal views share one homography?**

<details>
<summary>Show answer</summary>

The viewed points lie on one scene plane, or the camera rotates around the same optical centre with no translation.

*Sources: HC4a pp.34–35; S4.*

</details>

### CV1-314 · core

**Why does translating a camera through a nonplanar scene cause stitching problems?**

<details>
<summary>Show answer</summary>

Image shifts depend on depth (parallax), so one homography generally cannot align all depths simultaneously.

*Sources: HC4a pp.34–35; S4; Lab4.*

</details>

### CV1-315 · core

**How many generic point pairs minimally determine a homography?**

<details>
<summary>Show answer</summary>

Four in general position, with no degeneracy such as three collinear points in a minimal configuration. Each pair supplies two scalar equations.

*Sources: HC4a pp.46–55; S4.*

</details>

### CV1-316 · core

**How many generic point pairs minimally determine a general affine transform?**

<details>
<summary>Show answer</summary>

Three pairs with noncollinear source points. The 6 parameters need independent coordinate constraints.

*Sources: HC4a p.50; Lab4.*

</details>

### CV1-317 · core

**Write the coordinate formula for homography H at finite source (x,y).**

<details>
<summary>Show answer</summary>

x'=(h11\*x+h12\*y+h13)/(h31\*x+h32\*y+h33); y'=(h21\*x+h22\*y+h23)/(h31\*x+h32\*y+h33), when the denominator is nonzero.

*Sources: HC4a pp.47–52.*

</details>

### CV1-318 · core

**What is DLT's homogeneous system for homography fitting?**

<details>
<summary>Show answer</summary>

Stack two linear constraints per correspondence to form A\*h=0, where h contains the 9 entries of H. A has shape (2N,9).

*Sources: HC4a pp.51–53.*

</details>

### CV1-319 · core

**Why must homogeneous least squares constrain homography scale?**

<details>
<summary>Show answer</summary>

Otherwise h=0 trivially minimizes ||A\*h||^2 but defines no mapping. A common constraint is ||h||\_2=1.

*Sources: HC4a p.54.*

</details>

### CV1-320 · core

**Which eigenvector solves unit-norm homogeneous least squares for a homography?**

<details>
<summary>Show answer</summary>

The eigenvector of A.T\*A with the smallest eigenvalue; equivalently the corresponding right singular vector of A.

*Sources: HC4a p.55.*

</details>

### CV1-321 · core

**What is reprojection error in image alignment?**

<details>
<summary>Show answer</summary>

The distance between an observed target point and the dehomogenized prediction from the fitted transform; specify one-way or symmetric error and units.

*Sources: HC4a pp.46–55; Lab4.*

</details>

### CV1-322 · core

**What are the main steps of a feature-based stitching pipeline?**

<details>
<summary>Show answer</summary>

Detect/describe keypoints; match descriptors; reject ambiguity; robustly estimate a transform; warp to a common canvas; blend overlaps.

*Sources: HC4a pp.33–64; S4; Lab4.*

</details>

### CV1-323 · core

**What is weighted image blending in an overlap?**

<details>
<summary>Show answer</summary>

Combine aligned intensities with normalized weights, such as I=w\*I1+(1-w)\*I2 with 0<=w<=1. A ramp can reduce visible seams.

*Sources: HC4a pp.60–64; S4.*

</details>

### CV1-324 · core

**Can blending repair arbitrary geometric misalignment?**

<details>
<summary>Show answer</summary>

No. It can soften seams but may create ghosting/double images if content is not aligned, especially with parallax or moving objects.

*Sources: HC4a pp.60–64; Lab4.*

</details>

### CV1-325 · breadth

**Why must panorama canvas offset be included in the warp matrix?**

<details>
<summary>Show answer</summary>

Negative/reference-image coordinates may need translation into valid canvas coordinates. With column vectors, source-to-canvas is T\_canvas\*H\_source\_to\_reference.

*Sources: Lab4; HC4a p.19.*

</details>

### CV1-629 · core

**What is the pure-rotation image homography from view 1 to view 2?**

<details>
<summary>Show answer</summary>

H=K2\*R21\*K1^(-1), where R21 maps camera-1 ray directions into camera-2 coordinates and the optical centre is unchanged.

*Sources: HC4a p.34; S4; Szeliski §8.1.*

</details>

### CV1-630 · core

**Why keep a separate valid-pixel mask when blending warped images?**

<details>
<summary>Show answer</summary>

A zero intensity can be genuine black or an out-of-domain fill value. A mask identifies source coverage without confusing valid black pixels with missing data.

*Sources: Lab4 warping/blending.*

</details>

## matching

### CV1-326 · core

**What is the difference between keypoint detection and description?**

<details>
<summary>Show answer</summary>

Detection chooses repeatable locations and often scales/orientations; description encodes local appearance for comparisons.

*Sources: HC4a pp.36–44; S4; Lab4.*

</details>

### CV1-327 · core

**What does SIFT stand for?**

<details>
<summary>Show answer</summary>

Scale-Invariant Feature Transform. Its usual pipeline includes scale-space detection, orientation assignment and a local gradient descriptor.

*Sources: HC4a pp.41–44; S4.*

</details>

### CV1-328 · breadth

**Who is associated with SIFT and the commonly used ratio test?**

<details>
<summary>Show answer</summary>

David Lowe.

*Sources: HC4a p.44; Szeliski §7.1.2.*

</details>

### CV1-329 · core

**What are the main SIFT construction stages?**

<details>
<summary>Show answer</summary>

Detect DoG scale-space extrema; refine/reject unstable points; assign dominant orientation; form normalized local gradient-orientation histograms.

*Sources: HC4a pp.36–44; S4; Szeliski §7.1.*

</details>

### CV1-330 · core

**Why does SIFT use a scale-space detector?**

<details>
<summary>Show answer</summary>

To detect structures at corresponding characteristic scales after image/object rescaling, rather than using one fixed pixel-scale detector.

*Sources: HC4a pp.36–41.*

</details>

### CV1-331 · core

**How does SIFT gain rotation robustness?**

<details>
<summary>Show answer</summary>

Assign a dominant local gradient orientation and express the descriptor's spatial/orientation bins relative to it.

*Sources: HC4a p.42; S4.*

</details>

### CV1-332 · core

**How long is a standard SIFT descriptor and why?**

<details>
<summary>Show answer</summary>

128 values: a 4x4 grid of subregions, each with an 8-bin gradient-orientation histogram.

*Sources: S4; Szeliski §7.1.2 pp.434–436.*

</details>

### CV1-333 · core

**What weights contribute to the standard SIFT histogram entries?**

<details>
<summary>Show answer</summary>

Local gradient magnitudes with spatial Gaussian weighting, distributed into spatial/orientation bins rather than storing raw pixels.

*Sources: HC4a p.42; S4; Szeliski §7.1.2.*

</details>

### CV1-334 · core

**How does normalization improve SIFT's illumination robustness?**

<details>
<summary>Show answer</summary>

Gradients remove a constant additive offset; vector normalization reduces a common positive gain. Clipping and renormalization further reduce dominant responses.

*Sources: S4; Szeliski §7.1.2.*

</details>

### CV1-335 · breadth

**Is SIFT exactly invariant to every viewpoint, lighting or deformation change?**

<details>
<summary>Show answer</summary>

No. It is designed for scale/rotation robustness and some illumination/local deformation tolerance, not unlimited projective or nonuniform appearance invariance.

*Sources: HC4a pp.36–44; Szeliski §7.1.*

</details>

### CV1-336 · core

**How does brute-force descriptor matching work?**

<details>
<summary>Show answer</summary>

Compute distances between a query descriptor and candidate descriptors, then select nearest candidates under the chosen metric.

*Sources: Lab4; S4.*

</details>

### CV1-337 · core

**What is Lowe's nearest-neighbour ratio test?**

<details>
<summary>Show answer</summary>

Keep a proposed match when nearest distance d1 divided by second-nearest distance d2 is below a chosen threshold, with d2>0 and a declared strict/inclusive rule.

*Sources: HC4a p.44; S4; Lab4.*

</details>

### CV1-338 · core

**Why can nearest absolute distance alone be misleading?**

<details>
<summary>Show answer</summary>

Repeated patterns can offer multiple nearly equally good alternatives; a small nearest distance does not prove a distinctive or correct match.

*Sources: HC4a p.44.*

</details>

### CV1-339 · core

**What does a ratio d1/d2 close to one suggest?**

<details>
<summary>Show answer</summary>

Ambiguous descriptor matching: the best and next-best alternatives are similarly plausible.

*Sources: HC4a p.44; Lab4.*

</details>

### CV1-340 · core

**Does passing a descriptor ratio test guarantee geometric correctness?**

<details>
<summary>Show answer</summary>

No. Use geometric constraints and robust estimation, such as a homography/affine RANSAC, to reject inconsistent matches.

*Sources: HC4a pp.44–48; Lab4.*

</details>

### CV1-341 · core

**How must a ratio-test threshold change if distances are squared?**

<details>
<summary>Show answer</summary>

d1/d2<t is equivalent to D1/D2<t^2 for D=d^2. Comparing squared ratios to t itself changes the acceptance rule.

*Sources: HC4a ratio test; prerequisite algebra.*

</details>

### CV1-342 · breadth

**What is geometric verification in image retrieval?**

<details>
<summary>Show answer</summary>

Check whether local feature matches agree with a plausible transform or other scene geometry, rather than ranking only by aggregate appearance similarity.

*Sources: HC5a retrieval; HC4a; Szeliski §6.1.*

</details>

### CV1-343 · breadth

**Why are local descriptors useful under partial occlusion?**

<details>
<summary>Show answer</summary>

Some unoccluded regions can still provide matches even when the whole-image appearance changes. False matches and geometry still need checking.

*Sources: HC3b pp.97–106; HC5a retrieval.*

</details>

### CV1-631 · breadth

**What does SURF stand for?**

<details>
<summary>Show answer</summary>

Speeded-Up Robust Features, named as a local-feature alternative in Seminar 4. Advanced SURF implementation is not required by this pack.

*Sources: S4 Q1b,Q2b.*

</details>

### CV1-632 · breadth

**What does ORB stand for?**

<details>
<summary>Show answer</summary>

Oriented FAST and Rotated BRIEF, named as a keypoint/descriptor alternative in Seminar 4. Do not infer advanced ORB algorithm requirements from its name alone.

*Sources: S4 Q1b.*

</details>

## clustering

### CV1-344 · core

**What is k-means' usual objective?**

<details>
<summary>Show answer</summary>

Minimize the sum of squared Euclidean distances from data points to their assigned cluster centres for a chosen K.

*Sources: HC5a pp.91–118.*

</details>

### CV1-345 · core

**What are k-means' two alternating update steps?**

<details>
<summary>Show answer</summary>

Assign each point to its nearest centre, then replace each nonempty cluster's centre by the mean of its assigned points. Repeat until a stopping condition.

*Sources: HC5a p.93.*

</details>

### CV1-346 · core

**Why does k-means use the mean as each updated centre?**

<details>
<summary>Show answer</summary>

The arithmetic mean minimizes summed squared Euclidean distances within a fixed assigned cluster.

*Sources: HC5a p.93; HC3a pp.83–85.*

</details>

### CV1-347 · core

**Does k-means guarantee the global optimum?**

<details>
<summary>Show answer</summary>

No. It can converge to a local optimum and is sensitive to initialization; multiple starts can help.

*Sources: HC5a pp.110–111.*

</details>

### CV1-348 · core

**What choices strongly affect k-means results?**

<details>
<summary>Show answer</summary>

K, feature representation, feature scaling/metric, initialization and stopping/empty-cluster handling.

*Sources: HC5a pp.91–118.*

</details>

### CV1-349 · core

**What is the difference between k-means and k-nearest neighbours?**

<details>
<summary>Show answer</summary>

K-means is unsupervised clustering with K centres; k-NN is supervised prediction from the labels of nearby training examples.

*Sources: HC5a clustering; HC4b pp.37–58.*

</details>

### CV1-350 · core

**Why does adding pixel position to colour features change clustering?**

<details>
<summary>Show answer</summary>

It adds spatial distance to the metric, encouraging spatial compactness. Relative feature scales control its influence.

*Sources: HC5a pp.91–93.*

</details>

### CV1-351 · core

**Does colour-only k-means guarantee connected image regions?**

<details>
<summary>Show answer</summary>

No. Distant pixels with similar colour can get the same cluster label. Semantic regions and connected components are separate concepts.

*Sources: HC5a pp.91–118.*

</details>

### CV1-352 · core

**What is mean-shift clustering?**

<details>
<summary>Show answer</summary>

A mode-seeking density-based procedure that repeatedly moves a point/window to a local kernel-weighted mean until convergence.

*Sources: HC3b pp.110–119.*

</details>

### CV1-353 · core

**What is kernel bandwidth in mean shift?**

<details>
<summary>Show answer</summary>

The neighbourhood/scale over which density is estimated. It influences detail, attraction basins and the number of modes/clusters.

*Sources: HC3b pp.110–119.*

</details>

### CV1-354 · core

**Must mean shift specify a target number of clusters K?**

<details>
<summary>Show answer</summary>

Not in its basic form. Modes emerge from the data, kernel and bandwidth; a mode-merging rule can affect final grouping.

*Sources: HC3b p.119.*

</details>

### CV1-355 · breadth

**What is an attraction basin in mean shift?**

<details>
<summary>Show answer</summary>

The set of starting locations whose update trajectories converge to the same density mode.

*Sources: HC3b p.119.*

</details>

## classification

### CV1-356 · core

**What is Bag-of-Visual-Words (BoVW)?**

<details>
<summary>Show answer</summary>

Represent an image by counts or normalized counts of quantized local descriptors assigned to a learned visual vocabulary.

*Sources: HC4b pp.23–28; S4.*

</details>

### CV1-357 · core

**How is a visual vocabulary/codebook usually built?**

<details>
<summary>Show answer</summary>

Extract training-image descriptors and cluster them, commonly using k-means; the cluster centres are visual words.

*Sources: HC4b pp.25–28; S4.*

</details>

### CV1-358 · core

**What determines the dimension of a plain BoVW histogram?**

<details>
<summary>Show answer</summary>

The vocabulary size K, not the image size or number of detected descriptors.

*Sources: HC4b pp.25–28; S4.*

</details>

### CV1-359 · core

**How is one descriptor assigned to a visual word in hard quantization?**

<details>
<summary>Show answer</summary>

Choose its nearest vocabulary centre under the specified descriptor metric.

*Sources: HC4b pp.25–28; S4.*

</details>

### CV1-360 · core

**Why normalize visual-word counts?**

<details>
<summary>Show answer</summary>

Reduce dependence on the number of descriptors/image size, using a specified normalization such as L1 count proportions.

*Sources: HC4b pp.25–28; S4.*

</details>

### CV1-361 · core

**What is a major limitation of plain BoVW?**

<details>
<summary>Show answer</summary>

It discards spatial layout and quantization loses descriptor detail; different arrangements can yield the same histogram.

*Sources: HC4b pp.23–28; S4.*

</details>

### CV1-362 · core

**Should the BoVW vocabulary be fitted using held-out test images for ordinary evaluation?**

<details>
<summary>Show answer</summary>

No. Fit preprocessing on training data, select settings on validation, then evaluate the untouched test set to avoid leakage.

*Sources: HC4b pp.55–58; Lab5.*

</details>

### CV1-363 · core

**What does a k-nearest-neighbour classifier do?**

<details>
<summary>Show answer</summary>

Find the k nearest labelled training examples and combine their labels, usually by majority vote with a declared tie/weight rule.

*Sources: HC4b pp.37–53.*

</details>

### CV1-364 · core

**Give L1 and L2 feature distances.**

<details>
<summary>Show answer</summary>

L1=sum\_j abs(xj-yj). L2=sqrt(sum\_j (xj-yj)^2). Their rankings can differ in multiple dimensions.

*Sources: HC4b pp.39,51–52.*

</details>

### CV1-365 · core

**What is the usual effect of increasing k in k-NN?**

<details>
<summary>Show answer</summary>

Smoother, less noisy decision boundaries, but potentially more bias/underfitting. Choose k using validation, not a universal rule.

*Sources: HC4b pp.45–58.*

</details>

### CV1-366 · core

**Is k-NN training/prediction cost asymmetric?**

<details>
<summary>Show answer</summary>

It mainly stores training data, while naive prediction scans many examples. Per-query distance cost is roughly O(N\*D) for N examples of dimension D.

*Sources: HC4b p.40.*

</details>

### CV1-367 · core

**What is a hyperparameter?**

<details>
<summary>Show answer</summary>

A selected model/training setting such as k, vocabulary size, learning rate or architecture, rather than a parameter fitted by the training optimizer.

*Sources: HC4b pp.55–58; Lab5.*

</details>

### CV1-368 · core

**What are the roles of train, validation and test splits?**

<details>
<summary>Show answer</summary>

Train fits parameters; validation selects hyperparameters/models; test estimates performance of the final selected pipeline on held-out examples.

*Sources: HC4b pp.55–58; Lab5.*

</details>

### CV1-369 · core

**Why is tuning repeatedly on the test set invalid for a clean final estimate?**

<details>
<summary>Show answer</summary>

Model choices adapt to test outcomes, so the set is no longer an independent evaluation and its score can be optimistic.

*Sources: HC4b p.56.*

</details>

### CV1-370 · breadth

**What is cross-validation?**

<details>
<summary>Show answer</summary>

Repeatedly train on some folds and validate on another, aggregating validation results to compare choices; keep a final test set separate.

*Sources: HC4b pp.57–58.*

</details>

### CV1-371 · core

**Write a linear multiclass score function and its shapes.**

<details>
<summary>Show answer</summary>

s=W\*x+b. For input dimension D and C classes: W is (C,D), x is (D,), b and s are (C,).

*Sources: HC4b pp.62–65.*

</details>

### CV1-372 · core

**What does a linear classifier's decision boundary look like in feature space?**

<details>
<summary>Show answer</summary>

A hyperplane for a binary score threshold; pairwise equal class scores also give hyperplanes. It need not be linear in raw pixels if features are nonlinear.

*Sources: HC4b pp.61–78.*

</details>

### CV1-373 · core

**What is the central SVM goal?**

<details>
<summary>Show answer</summary>

Find a separating decision boundary with a large margin, balancing margin/regularization against allowed violations in the soft-margin setting.

*Sources: HC4b pp.69–78.*

</details>

### CV1-374 · core

**What are support vectors?**

<details>
<summary>Show answer</summary>

Training examples with nonzero dual weights in the SVM solution, typically on or inside the margin or misclassified in a soft-margin model. They determine its fitted boundary.

*Sources: HC4b p.69; Szeliski §5.1.4.*

</details>

### CV1-375 · core

**Why use a soft-margin SVM?**

<details>
<summary>Show answer</summary>

To handle nonseparable/noisy data by penalizing margin violations instead of requiring a perfect hard-margin separation.

*Sources: HC4b pp.69,74.*

</details>

### CV1-376 · core

**Write binary hinge loss for label y in {-1,+1} and score s.**

<details>
<summary>Show answer</summary>

max(0,1-y\*s). A standard soft-margin SVM also includes weight-norm regularization.

*Sources: HC4b p.74.*

</details>

### CV1-377 · core

**What does the kernel trick compute?**

<details>
<summary>Show answer</summary>

Inner products of implicit transformed features without explicitly constructing the full transformed vectors, allowing nonlinear boundaries in the original space.

*Sources: HC4b pp.77–78.*

</details>

### CV1-633 · core

**How do dense patch sampling and interest-point sampling differ?**

<details>
<summary>Show answer</summary>

Dense sampling uses a regular grid for broad image coverage; interest-point sampling chooses salient locations and can concentrate on distinctive structure.

*Sources: S4 Q2d.*

</details>

### CV1-634 · core

**Is interest-point sampling guaranteed better than dense sampling in every large database?**

<details>
<summary>Show answer</summary>

No. Distinctiveness, coverage, computation and the task determine the trade-off. The seminar's dataset-size explanation is a scenario, not a universal law.

*Sources: S4 Q2d; SOURCE\_NOTES.*

</details>

### CV1-635 · core

**What is one-vs-rest multiclass classification?**

<details>
<summary>Show answer</summary>

Train one binary classifier per class to distinguish that class from all others, then combine their scores using a stated prediction rule.

*Sources: HC4b p.66.*

</details>

### CV1-636 · core

**Write the sigmoid function and its derivative.**

<details>
<summary>Show answer</summary>

sigmoid(z)=1/(1+exp(-z)); derivative=sigmoid(z)\*(1-sigmoid(z)). Its output lies in (0,1) for finite z.

*Sources: HC4b p.73; HC5b p.58.*

</details>

### CV1-637 · core

**Write binary cross-entropy for target y in {0,1} and probability p.**

<details>
<summary>Show answer</summary>

-y\*log(p)-(1-y)\*log(1-p). It penalizes assigning low probability to the true outcome. Handle p=0 or 1 with stable computation.

*Sources: HC4b p.73; Lab5 loss discussion.*

</details>

### CV1-638 · core

**What activation and loss describe linear regression in the artificial-neuron slide?**

<details>
<summary>Show answer</summary>

Identity activation for the prediction and squared-error/MSE loss. A sigmoid is not required for an unconstrained regression target.

*Sources: HC4b p.72.*

</details>

### CV1-639 · core

**Write mean squared error for N scalar predictions.**

<details>
<summary>Show answer</summary>

MSE=(1/N)\*sum\_i (y\_i-yhat\_i)^2. Sum-squared-error omits 1/N, so scale depends on the convention.

*Sources: HC4b p.72.*

</details>

## metrics

### CV1-378 · core

**Define TP, FP, FN and TN for a chosen positive class.**

<details>
<summary>Show answer</summary>

TP: actual positive predicted positive. FP: actual negative predicted positive. FN: actual positive predicted negative. TN: actual negative predicted negative.

*Sources: HC4b pp.80–86; S4.*

</details>

### CV1-379 · core

**What is accuracy?**

<details>
<summary>Show answer</summary>

Number correct divided by number evaluated; for binary predictions, (TP+TN)/(TP+FP+FN+TN).

*Sources: HC4b pp.81–82.*

</details>

### CV1-380 · core

**What is precision?**

<details>
<summary>Show answer</summary>

TP/(TP+FP): fraction of positive predictions that are correct. Handle a zero denominator using the stated evaluation rule.

*Sources: HC4b p.83.*

</details>

### CV1-381 · core

**What is recall?**

<details>
<summary>Show answer</summary>

TP/(TP+FN): fraction of actual positives detected. Also called sensitivity or true-positive rate.

*Sources: HC4b p.84.*

</details>

### CV1-382 · core

**What is F1?**

<details>
<summary>Show answer</summary>

Harmonic mean 2\*P\*R/(P+R), equivalently 2\*TP/(2\*TP+FP+FN) when defined.

*Sources: HC4b p.80; S4.*

</details>

### CV1-383 · core

**Why is F1 not the arithmetic mean of precision and recall?**

<details>
<summary>Show answer</summary>

Its harmonic mean penalizes imbalance more; one very small component makes F1 small even if the other is high.

*Sources: HC4b p.80; S4.*

</details>

### CV1-384 · core

**Why can accuracy be misleading for imbalanced classes?**

<details>
<summary>Show answer</summary>

Correct majority predictions can dominate the score while the minority class has very low or zero recall.

*Sources: HC4b p.82.*

</details>

### CV1-385 · core

**With confusion-matrix rows actual and columns predicted, where are FP and FN for class c?**

<details>
<summary>Show answer</summary>

TP is diagonal C[c,c]; FP is column-c sum minus TP; FN is row-c sum minus TP.

*Sources: HC4b pp.80–86; S4.*

</details>

### CV1-386 · core

**What is macro averaging across classes?**

<details>
<summary>Show answer</summary>

Compute each class's metric and average them equally, irrespective of class frequency.

*Sources: HC4b evaluation; S4.*

</details>

### CV1-387 · core

**What is micro averaging across classes?**

<details>
<summary>Show answer</summary>

Pool the relevant TP/FP/FN counts first, then compute the metric. For complete single-label multiclass evaluation, micro precision/recall/F1 equal accuracy.

*Sources: HC4b evaluation; S4; prerequisite aggregation.*

</details>

### CV1-388 · core

**What usually happens when a positive-score threshold is lowered?**

<details>
<summary>Show answer</summary>

More positive predictions: recall cannot decrease for a fixed ranking, while precision may change and need not be monotone.

*Sources: HC4b pp.85–86.*

</details>

### CV1-389 · core

**What is Precision@K in retrieval?**

<details>
<summary>Show answer</summary>

Number of relevant items among the first K results divided by K, assuming K results are available. It ignores all lower ranks.

*Sources: HC5a p.19.*

</details>

### CV1-390 · core

**What is Recall@K in retrieval?**

<details>
<summary>Show answer</summary>

Number of relevant items among the first K results divided by the total number of relevant database items.

*Sources: HC5a pp.19–24; S4.*

</details>

### CV1-391 · core

**What does a precision–recall curve vary?**

<details>
<summary>Show answer</summary>

The score/rank threshold, tracing the precision and recall obtained as more predictions or results are admitted.

*Sources: HC4b p.86; HC5a evaluation.*

</details>

### CV1-392 · core

**Give the raw uninterpolated ranking-AP formula.**

<details>
<summary>Show answer</summary>

AP=sum over relevant ranks k of Precision@k, divided by the total relevant/ground-truth count. Missing relevant items contribute zero. Use this only when that AP convention is specified.

*Sources: HC5a pp.19–24,68–78; S4; SOURCE\_NOTES.*

</details>

### CV1-393 · core

**What is all-points interpolated AP?**

<details>
<summary>Show answer</summary>

Area under a precision envelope: at each recall use the maximum precision attainable at that recall or later, then sum recall increments times envelope precision.

*Sources: HC5a pp.68–78; S4; SOURCE\_NOTES.*

</details>

### CV1-394 · core

**Why should an AP computation state the interpolation convention?**

<details>
<summary>Show answer</summary>

Raw ranking AP, all-points interpolation and 11-point/sampled-recall conventions can give different values on the same predictions. AP is not a uniquely specified arithmetic procedure without that choice.

*Sources: HC5a evaluation; S4; SOURCE\_NOTES.*

</details>

### CV1-395 · core

**What is mean Average Precision (mAP) for detection classes at one IoU threshold?**

<details>
<summary>Show answer</summary>

The arithmetic mean of class AP values under the same declared matching and AP conventions. It is not precision averaged over raw boxes.

*Sources: HC5a pp.68–78.*

</details>

### CV1-396 · core

**How does mAP@0.5 differ from COCO-style averaged-IoU AP?**

<details>
<summary>Show answer</summary>

mAP@0.5 uses one matching threshold; COCO-style AP averages over thresholds 0.50,0.55,...,0.95 as well, using its defined sampled-recall evaluation.

*Sources: HC5a p.78.*

</details>

### CV1-397 · core

**How are detections matched to ground truth for AP?**

<details>
<summary>Show answer</summary>

Per class, process detections in descending score and match valid overlaps to unmatched ground-truth objects under the declared IoU rule. A ground-truth object can be claimed once.

*Sources: HC5a pp.68–76.*

</details>

### CV1-398 · core

**What happens to a duplicate high-IoU detection of an already matched object?**

<details>
<summary>Show answer</summary>

It is a false positive unless it can validly match another unmatched ground-truth object. A high overlap alone does not make every duplicate a TP.

*Sources: HC5a pp.69–76.*

</details>

### CV1-399 · core

**Must AP equal zero after one early false positive?**

<details>
<summary>Show answer</summary>

No. It lowers some precision values but later true positives can still contribute. AP summarizes the ranking and achieved recall under its convention.

*Sources: HC5a pp.68–78.*

</details>

### CV1-400 · breadth

**What is top-5 classification accuracy?**

<details>
<summary>Show answer</summary>

Fraction of examples whose true label appears among the model's five highest-scoring class labels.

*Sources: HC4b p.34.*

</details>

### CV1-640 · core

**What is mAP for image retrieval over Q queries?**

<details>
<summary>Show answer</summary>

(1/Q)\*sum\_q AP\_q, using the same AP@K/full-ranking definition for every query. Detection mAP usually averages classes instead; state the averaging axis.

*Sources: HC5a p.22; S4 Q3c.*

</details>

## cnn

### CV1-401 · core

**What are the key structural ideas in a CNN layer?**

<details>
<summary>Show answer</summary>

Local connectivity/receptive fields, tiling a filter across space and sharing its weights. Multiple filters produce multiple feature maps.

*Sources: HC5b pp.22–43.*

</details>

### CV1-402 · core

**What is a feature map?**

<details>
<summary>Show answer</summary>

The spatial array of responses for a learned filter/output channel; a layer's output stacks feature maps across channels.

*Sources: HC5b pp.35–43,61–68.*

</details>

### CV1-403 · core

**What does weight sharing mean in a convolution?**

<details>
<summary>Show answer</summary>

The same kernel parameters are used at different spatial positions, rather than learning independent weights at every location.

*Sources: HC5b pp.22–24; S5.*

</details>

### CV1-404 · core

**What is translation equivariance?**

<details>
<summary>Show answer</summary>

Shifting the input shifts the corresponding output representation under the specified operator. It is not an unchanged output.

*Sources: HC5b pp.22–24; S5.*

</details>

### CV1-405 · core

**What is translation invariance?**

<details>
<summary>Show answer</summary>

Output remains unchanged under translation. A raw convolution is generally equivariant, while aggregation/pooling can provide limited or additional invariance.

*Sources: HC5b p.64; S5.*

</details>

### CV1-406 · core

**Why do stride and boundaries limit exact convolutional equivariance?**

<details>
<summary>Show answer</summary>

Strides sample on a fixed grid, and padding/cropping can change boundary context. Only compatible translations/regions preserve the ideal relation.

*Sources: HC5b pp.35–40; S5.*

</details>

### CV1-407 · core

**How does a dense multi-channel 2D convolution make one output channel?**

<details>
<summary>Show answer</summary>

For each output location, sum spatial kernel products across all input channels and add that output channel's bias.

*Sources: HC5b pp.66–68.*

</details>

### CV1-408 · core

**What is the weight-tensor shape for a standard Cout-output, Cin-input 2D convolution in output-first notation?**

<details>
<summary>Show answer</summary>

(Cout,Cin,Kh,Kw). A library may store axes differently, but the parameter count is unchanged.

*Sources: HC5b pp.66–68; S5.*

</details>

### CV1-409 · core

**Give a standard dense 2D convolution's parameter count with bias.**

<details>
<summary>Show answer</summary>

Cout\*(Kh\*Kw\*Cin+1). Stride, batch size and image spatial size do not change the count.

*Sources: HC5b pp.66–73; S5.*

</details>

### CV1-410 · core

**Give a fully connected layer's parameter count with bias.**

<details>
<summary>Show answer</summary>

Dout\*(Din+1). Flattened input dimension includes every spatial position and channel fed to that layer.

*Sources: S5 Exercise 1.*

</details>

### CV1-411 · core

**What is the standard convolution/pooling output size per axis with no dilation?**

<details>
<summary>Show answer</summary>

floor((N+2\*P-K)/S)+1, using symmetric padding P on each side, kernel K and stride S.

*Sources: HC5b pp.25–40; S5.*

</details>

### CV1-412 · core

**What padding preserves size for an odd K at stride 1?**

<details>
<summary>Show answer</summary>

P=(K-1)/2 on each side, for no dilation and standard symmetric padding.

*Sources: HC5b pp.35–40; S5.*

</details>

### CV1-413 · core

**What does a 1x1 convolution do?**

<details>
<summary>Show answer</summary>

Mixes input channels independently at each spatial location; it can change channel count without spatial mixing in that layer.

*Sources: HC5b pp.70–73.*

</details>

### CV1-414 · core

**What is the parameter count of a dense 1x1 convolution with bias?**

<details>
<summary>Show answer</summary>

Cout\*(Cin+1). It is not parameter-free and is not necessarily an identity.

*Sources: HC5b pp.70–73.*

</details>

### CV1-415 · core

**Why use 1x1 layers in a bottleneck block?**

<details>
<summary>Show answer</summary>

Reduce channel count before an expensive spatial convolution, then expand again. This can reduce parameters and compute for suitable channel choices.

*Sources: HC5b p.73; HC6a pp.107–111.*

</details>

### CV1-416 · core

**Why add nonlinear activations between linear/affine layers?**

<details>
<summary>Show answer</summary>

A composition of affine layers without nonlinearities is still one affine mapping; nonlinearities allow more complex decision functions.

*Sources: HC5b pp.44–59.*

</details>

### CV1-417 · core

**What is ReLU?**

<details>
<summary>Show answer</summary>

ReLU(x)=max(0,x), applied elementwise. Its derivative is 1 for x>0 and 0 for x<0; define the zero-point convention when needed.

*Sources: HC5b pp.44–59; S5.*

</details>

### CV1-418 · core

**What is max pooling?**

<details>
<summary>Show answer</summary>

Replace each spatial window per channel by its maximum, often with stride to reduce resolution. It has no ordinary learned weights or biases.

*Sources: HC5b pp.64,69,74–77.*

</details>

### CV1-419 · core

**How does max-pooling backpropagation route gradients?**

<details>
<summary>Show answer</summary>

To the location(s) selected as maxima in the forward window, under the library's tie rule; other entries receive zero from that output.

*Sources: HC5b p.69; S5.*

</details>

### CV1-420 · core

**Is average pooling linear? Is max pooling linear?**

<details>
<summary>Show answer</summary>

Fixed average pooling is linear under a fixed boundary rule. Max pooling is generally nonlinear. Both can downsample.

*Sources: HC5b pooling; prerequisite linearity.*

</details>

### CV1-421 · core

**What is global average pooling?**

<details>
<summary>Show answer</summary>

Mean each feature channel across all spatial positions, producing one value per channel and no learned pooling parameters.

*Sources: HC6a architecture diagrams; Lab5.*

</details>

### CV1-422 · core

**What is a theoretical receptive field?**

<details>
<summary>Show answer</summary>

The input-region support that can influence a particular output unit through the network's connectivity. Distinguish it from observed/weighted effective influence.

*Sources: HC5b pp.80–85; HC6a pp.6–9.*

</details>

### CV1-423 · core

**What is the receptive-field side length of L stride-1 K-wide convolutions with no intervening strides?**

<details>
<summary>Show answer</summary>

1+L\*(K-1), ignoring boundaries. The simple formula changes when strides/pooling intervene.

*Sources: HC5b p.82.*

</details>

### CV1-424 · core

**Give the receptive-field recurrence that includes strides.**

<details>
<summary>Show answer</summary>

Start r=1,j=1. For kernel K and stride S: r\_new=r+(K-1)\*j; j\_new=j\*S. Apply in layer order, ignoring dilation unless specified.

*Sources: HC5b pp.80–85; HC6a pp.6–9.*

</details>

### CV1-425 · core

**How does a CNN typically change features across depth?**

<details>
<summary>Show answer</summary>

Early layers tend to represent simple local edges/textures; later layers combine them into more complex patterns, often with larger receptive fields.

*Sources: HC5b pp.88–90.*

</details>

### CV1-426 · core

**What is the multiply-accumulate count of a dense 2D convolution's forward kernel work?**

<details>
<summary>Show answer</summary>

Hout\*Wout\*Cout\*Kh\*Kw\*Cin, excluding bias/nonlinearities. Counts of scalar FLOPs can be roughly twice this if multiply and add are counted separately.

*Sources: HC5b p.68; S5.*

</details>

### CV1-427 · core

**What is a standard dense 3D convolution's parameter count with bias?**

<details>
<summary>Show answer</summary>

Cout\*(Kt\*Kh\*Kw\*Cin+1), where Kt is temporal/depth support. Frame count is not Cin unless frames were explicitly packed as channels.

*Sources: S5 Exercise 5.*

</details>

### CV1-428 · core

**How is true video 3D convolution different from independent framewise 2D convolution?**

<details>
<summary>Show answer</summary>

A 3D kernel mixes across temporal/depth neighbours as well as spatial positions. Independent 2D processing does not itself combine frames.

*Sources: S5 Exercise 5.*

</details>

### CV1-429 · breadth

**Does factorizing a 3D convolution into spatial 2D plus temporal 1D always reduce parameters?**

<details>
<summary>Show answer</summary>

No. The count depends on intermediate channels: Kh\*Kw\*Cin\*Cmid+Kt\*Cmid\*Cout, plus chosen biases. It can reduce parameters for suitable dimensions.

*Sources: S5 Exercise 5; SOURCE\_NOTES.*

</details>

### CV1-430 · core

**What is the gradient of a shared kernel weight in a CNN?**

<details>
<summary>Show answer</summary>

Sum upstream-gradient times the corresponding input sample over all output positions (and batch examples) using that weight.

*Sources: S5 Exercise 3.*

</details>

### CV1-431 · core

**Why can input-gradient contributions overlap during convolution backpropagation?**

<details>
<summary>Show answer</summary>

One input pixel can affect several output windows. Its gradient is the sum of all such contributions, not just one patch.

*Sources: S5 Exercise 3.*

</details>

### CV1-432 · core

**What is softmax for logits z?**

<details>
<summary>Show answer</summary>

p\_c=exp(z\_c)/sum\_j exp(z\_j). Subtracting max(z) before exponentiation gives the same probabilities and improves numerical stability.

*Sources: HC5a p.5; HC5b p.78; Lab5.*

</details>

### CV1-433 · core

**Does softmax normalization guarantee calibrated probabilities?**

<details>
<summary>Show answer</summary>

No. It guarantees nonnegative normalized scores, not that predicted confidence matches observed correctness frequencies.

*Sources: HC5a p.5; prerequisite probability.*

</details>

### CV1-434 · core

**What is multiclass cross-entropy for a one-hot target class y?**

<details>
<summary>Show answer</summary>

-log(p\_y), normally using natural logarithms. CrossEntropyLoss commonly consumes logits and includes the log-softmax internally.

*Sources: HC4b p.73; HC5a p.89; Lab5.*

</details>

### CV1-435 · core

**What input does a negative log-likelihood loss such as the lab's NLLLoss expect?**

<details>
<summary>Show answer</summary>

Log-probabilities and class-index targets, unlike a logits-consuming cross-entropy convenience routine. Check the routine's documented convention.

*Sources: Lab5 tutorial.*

</details>

### CV1-436 · breadth

**Why might learned weight sharing be an imperfect inductive bias for some structured tasks?**

<details>
<summary>Show answer</summary>

Different fixed locations can have different roles. Sharing helps generalization and efficiency but can limit location-specific modelling; it does not make CNNs unusable for faces.

*Sources: S5 Exercise 2; SOURCE\_NOTES.*

</details>

### CV1-641 · core

**How can a whole-image fully connected layer be represented by a convolution on a fixed-size image?**

<details>
<summary>Show answer</summary>

Use kernel size HxW, Cin input channels and Dout output channels, no padding, producing one spatial output per channel. Map the same flattened weights consistently.

*Sources: S5 Q1c.*

</details>

### CV1-642 · core

**How can one shared FC layer applied to nonoverlapping KxK patches be represented as a convolution?**

<details>
<summary>Show answer</summary>

Use KxK kernels, stride K and no padding, with output channels equal to FC units. One shared parameter set is reused over patches.

*Sources: S5 Q1b,Q1d.*

</details>

### CV1-643 · core

**What is batch normalization's role at a high level?**

<details>
<summary>Show answer</summary>

Normalize activations using batch-based statistics during training, then apply learned scale/shift; ordinary evaluation uses stored statistics. It can support stable training but does not guarantee no exploding values.

*Sources: HC5b p.60; S5 Q3; Lab5 ResNet.*

</details>

### CV1-644 · breadth

**How do batch, instance, layer and group normalization differ conceptually?**

<details>
<summary>Show answer</summary>

They normalize over different groups of activation entries: batch-based channel statistics; each instance/channel; features within a sample; or groups of channels within a sample. Exact axes depend on layer/tensor conventions.

*Sources: HC5b p.60; Szeliski neural-network chapter.*

</details>

### CV1-645 · core

**How many trainable scale/shift parameters does ordinary per-channel batch normalization have for C channels?**

<details>
<summary>Show answer</summary>

2\*C: gamma and beta per channel if affine=True. Running means/variances are stored state, not gradient-trained parameters.

*Sources: HC5b p.60; Lab5 ResNet; supporting layer definition.*

</details>

### CV1-646 · core

**Write z-score input standardization.**

<details>
<summary>Show answer</summary>

x'=(x-mean)/std, with a valid nonzero standard deviation and a stated per-channel/per-feature statistic. It is not min-max scaling.

*Sources: HC5b p.60; Lab5 preprocessing.*

</details>

### CV1-647 · core

**Write min-max normalization to [0,1].**

<details>
<summary>Show answer</summary>

x'=(x-min)/(max-min), for max>min. A constant array needs an explicit fallback to avoid zero division.

*Sources: HC5b p.60; Lab5 scale\_to\_01.*

</details>

### CV1-648 · breadth

**What is tanh and where can it saturate?**

<details>
<summary>Show answer</summary>

tanh(z)=(exp(z)-exp(-z))/(exp(z)+exp(-z)); output is in (-1,1). Its derivative 1-tanh(z)^2 is small at large absolute z.

*Sources: HC5b p.58; S5 vanishing gradients.*

</details>

### CV1-649 · core

**What is leaky ReLU?**

<details>
<summary>Show answer</summary>

max(z,alpha\*z) for a chosen 0<alpha<1, so negative inputs retain a small nonzero derivative. It reduces the completely zero negative-side gradient of ReLU.

*Sources: HC5b p.58; S5 Q3c.*

</details>

## optimization

### CV1-437 · core

**What is gradient descent's basic parameter update?**

<details>
<summary>Show answer</summary>

theta\_new=theta\_old-learning\_rate\*gradient(loss,theta). A positive learning rate moves against the local gradient.

*Sources: S5; Lab5.*

</details>

### CV1-438 · core

**What is stochastic/minibatch gradient descent?**

<details>
<summary>Show answer</summary>

Estimate the loss gradient from an example or minibatch and update parameters, rather than using the whole dataset for every step.

*Sources: Lab5 tutorial and assignment.*

</details>

### CV1-439 · core

**What does momentum add to SGD at a high level?**

<details>
<summary>Show answer</summary>

A running direction based on recent gradients, which can smooth noisy updates and accelerate consistent directions. It is not guaranteed to help every setting.

*Sources: Lab5 training; S5.*

</details>

### CV1-440 · core

**What does Adam track?**

<details>
<summary>Show answer</summary>

Exponential moving estimates of first and second gradient moments, with corrections, to adapt parameter updates. A base learning rate still matters.

*Sources: Lab5 assignment Task 3.*

</details>

### CV1-441 · core

**Does Adam remove the need to choose a learning rate?**

<details>
<summary>Show answer</summary>

No. Its base learning rate and other hyperparameters still affect stability, speed and final performance.

*Sources: Lab5 assignment Tasks 3–4.*

</details>

### CV1-442 · core

**What can an excessively large learning rate cause?**

<details>
<summary>Show answer</summary>

Overshooting, oscillating or diverging loss and unstable updates. It does not guarantee faster useful convergence.

*Sources: Lab5 assignment Task 4.*

</details>

### CV1-443 · core

**What can an excessively small learning rate cause?**

<details>
<summary>Show answer</summary>

Very slow progress or failure to reach a useful solution within the available training budget.

*Sources: Lab5 assignment Task 4.*

</details>

### CV1-444 · core

**Why initialize interchangeable hidden-unit weights randomly?**

<details>
<summary>Show answer</summary>

Break symmetry so units can learn different features, rather than producing identical activations and gradients.

*Sources: Lab5 assignment Tasks 5,8.*

</details>

### CV1-445 · core

**Are zero biases always invalid?**

<details>
<summary>Show answer</summary>

No. Randomized weights with zero biases can train normally. The symmetry problem concerns identical interchangeable weight vectors, not a blanket ban on zero values.

*Sources: Lab5 initialization; S5.*

</details>

### CV1-446 · core

**What is the purpose of Xavier/Glorot initialization at a high level?**

<details>
<summary>Show answer</summary>

Set initial variance based on layer fan-in/fan-out to control signal/gradient scale, often appropriate for roughly symmetric activations.

*Sources: S5 gradient solutions; Lab5 assignment Task 8.*

</details>

### CV1-447 · core

**What is Kaiming/He initialization designed for?**

<details>
<summary>Show answer</summary>

Rectifier activations such as ReLU, accounting for their signal statistics to preserve useful activation/gradient scale through depth.

*Sources: Lab5 assignment Task 5,8; S5.*

</details>

### CV1-448 · breadth

**Give the usual ReLU fan-in Kaiming weight variance.**

<details>
<summary>Show answer</summary>

Approximately 2/fan\_in for a zero-mean distribution under the standard assumptions. Exact library modes/distributions can differ.

*Sources: Lab5 initialization; He paper linked by lab.*

</details>

### CV1-449 · core

**What are vanishing gradients?**

<details>
<summary>Show answer</summary>

Backpropagated derivatives become very small through many transformations, so early parameters receive little useful update signal.

*Sources: HC6a pp.100–103; S5; Lab5.*

</details>

### CV1-450 · core

**What are exploding gradients?**

<details>
<summary>Show answer</summary>

Backpropagated derivatives become very large, causing unstable updates or numerical overflow.

*Sources: S5; Lab5.*

</details>

### CV1-451 · core

**What methods can help vanishing/exploding-gradient problems?**

<details>
<summary>Show answer</summary>

Suitable initialization, normalization, non-saturating activations and residual paths; gradient clipping specifically limits large gradients. These are mitigations, not universal guarantees.

*Sources: S5 Exercise 3; Lab5.*

</details>

### CV1-452 · core

**What does gradient clipping mainly address?**

<details>
<summary>Show answer</summary>

Excessive gradient magnitude, helping control exploding updates. It does not restore information from a zero/vanished gradient.

*Sources: S5 Exercise 3.*

</details>

### CV1-453 · core

**What is the dying-ReLU problem?**

<details>
<summary>Show answer</summary>

A unit stays at nonpositive preactivation for all relevant inputs, giving zero output and no gradient through its ReLU branch under the usual convention.

*Sources: S5 Exercise 3.*

</details>

### CV1-454 · core

**How can dying-ReLU risk be reduced?**

<details>
<summary>Show answer</summary>

Suitable initialization and learning rate, normalization, or activations with a nonzero negative-side derivative such as leaky ReLU. Residual paths help network signal flow but do not guarantee revival of every dead unit.

*Sources: S5 Exercise 3.*

</details>

### CV1-455 · core

**What is underfitting?**

<details>
<summary>Show answer</summary>

A model or training process fails to capture useful patterns even in training data, due to limited capacity, strong constraints or unsuccessful optimization.

*Sources: Lab5 tutorial; HC6a pp.100–101.*

</details>

### CV1-456 · core

**What is overfitting?**

<details>
<summary>Show answer</summary>

Strong fit to training data without comparable generalization to held-out data; a widening train/validation gap is one diagnostic, not proof of a single cause.

*Sources: Lab5 tutorial and assignment.*

</details>

### CV1-457 · core

**Does a deeper network necessarily generalize better?**

<details>
<summary>Show answer</summary>

No. Capacity, optimization, data volume, regularization and architecture all matter. Higher training error in a deeper model can indicate optimization difficulty rather than overfitting.

*Sources: HC6a pp.100–101; Lab5 Task 8.*

</details>

### CV1-458 · core

**What can reduce overfitting?**

<details>
<summary>Show answer</summary>

Suitable data augmentation, regularization, early stopping using validation, more representative data or reduced model complexity. Evaluate the effects, not a guaranteed ranking.

*Sources: Lab5 tutorial and assignment.*

</details>

### CV1-459 · core

**What does data augmentation do?**

<details>
<summary>Show answer</summary>

Generate task-appropriate variations of training examples to encourage robustness. Transformations must preserve or correctly update labels.

*Sources: Lab5 CIFAR tutorial; YOLOv4 §2.2.*

</details>

### CV1-460 · core

**What is dropout at a high level?**

<details>
<summary>Show answer</summary>

Randomly omit activations during training under a chosen convention to reduce co-adaptation; normal evaluation uses its defined deterministic/scaled behaviour.

*Sources: Lab5 network code; YOLOv4 §2.2.*

</details>

### CV1-461 · core

**What does optimizer.zero\_grad() do in the lab training loop?**

<details>
<summary>Show answer</summary>

Clear stored gradients, not learned weights. Backward ordinarily accumulates gradients, so clearing prevents unintended carry-over across batches.

*Sources: Lab5 tutorial code.*

</details>

### CV1-462 · core

**What do loss.backward() and optimizer.step() do?**

<details>
<summary>Show answer</summary>

Backward computes/accumulates parameter derivatives by the chain rule; step updates parameters using those gradients and the optimizer's state.

*Sources: Lab5 tutorial code.*

</details>

### CV1-463 · core

**How do training and evaluation modes affect a typical CNN?**

<details>
<summary>Show answer</summary>

They control behaviours such as dropout and batch-normalization statistics. Evaluation mode alone does not necessarily disable gradient recording or freeze parameters.

*Sources: Lab5 tutorial/assignment code.*

</details>

### CV1-464 · breadth

**What is Grad-CAM used for in Lab5?**

<details>
<summary>Show answer</summary>

Visualize class-related spatial influence in a selected convolutional layer using gradients and activations, to inspect errors and possible shortcut attention. It is not a complete causal explanation.

*Sources: Lab5 tutorial and assignment Task 6.*

</details>

### CV1-650 · core

**What is an epoch versus an optimization step?**

<details>
<summary>Show answer</summary>

An epoch is one pass through the training set under the data-loader schedule; a step is one parameter update, usually after a minibatch. Multiple steps occur per epoch.

*Sources: Lab5 training loops.*

</details>

### CV1-651 · core

**Why shuffle the training data in the CIFAR tutorial?**

<details>
<summary>Show answer</summary>

Reduce ordering effects in minibatch optimization. Evaluation normally aggregates fixed examples and does not require shuffled order for a correct total metric.

*Sources: Lab5 CIFAR tutorial cell 16.*

</details>

### CV1-652 · core

**What does torch.no\_grad() do, and does it set evaluation mode?**

<details>
<summary>Show answer</summary>

It disables gradient recording in its scope. It does not itself call model.eval() or change dropout/batch-normalization mode.

*Sources: Lab5 evaluation code; SOURCE\_NOTES.*

</details>

### CV1-653 · core

**Why can averaging per-batch accuracies differ from whole-dataset accuracy?**

<details>
<summary>Show answer</summary>

If batch sizes differ, an unweighted mean gives each batch equal weight. Whole-dataset accuracy is total\_correct/total\_examples, or a batch-size-weighted mean.

*Sources: Lab5 assignment validation\_epoch\_end.*

</details>

### CV1-654 · breadth

**Which authors are associated with Adam?**

<details>
<summary>Show answer</summary>

Diederik Kingma and Jimmy Ba. Adam stands for Adaptive Moment Estimation.

*Sources: Lab5 assignment Task 3.*

</details>

## detection

### CV1-465 · core

**What is a bounding box?**

<details>
<summary>Show answer</summary>

A rectangular localization of an object; common formats include corners [xmin,ymin,xmax,ymax] or centre [x,y,width,height]. State the format.

*Sources: HC5a pp.25–35; HC6a pp.55–72.*

</details>

### CV1-466 · core

**What is Intersection over Union (IoU)?**

<details>
<summary>Show answer</summary>

Intersection area divided by union area: intersect/(areaA+areaB-intersect), for nonempty valid regions. Also called Jaccard similarity/index.

*Sources: HC5a p.62; S4.*

</details>

### CV1-467 · core

**How is box intersection width computed for continuous corner coordinates?**

<details>
<summary>Show answer</summary>

max(0,min(xmaxA,xmaxB)-max(xminA,xminB)); analogous for height. Do not add 1 unless the question uses an inclusive integer-pixel convention.

*Sources: HC5a p.62; S4.*

</details>

### CV1-468 · core

**What are IoU's ordinary value range and endpoints?**

<details>
<summary>Show answer</summary>

0 to 1: zero for disjoint regions; one for identical regions of positive area.

*Sources: HC5a p.62.*

</details>

### CV1-469 · core

**What is greedy hard non-maximum suppression?**

<details>
<summary>Show answer</summary>

Keep the highest-scoring remaining box, suppress lower-scoring boxes with excessive IoU against it, then repeat. Use a declared threshold and class policy.

*Sources: HC5a pp.63–67.*

</details>

### CV1-470 · core

**Is confidence thresholding the same as NMS?**

<details>
<summary>Show answer</summary>

No. Thresholding removes low-scoring candidates; NMS removes redundant overlapping candidates using scores and overlap. Pipelines often use both.

*Sources: HC5a pp.63–67; HC6a p.62.*

</details>

### CV1-471 · core

**Does a box suppressed by greedy NMS suppress other boxes later?**

<details>
<summary>Show answer</summary>

No. Suppression is based on boxes actually kept in the greedy procedure; overlap is not transitively propagated through a discarded box.

*Sources: HC5a pp.63–67.*

</details>

### CV1-472 · core

**Why can hard NMS fail in crowded scenes?**

<details>
<summary>Show answer</summary>

Different genuine objects can have high box overlap, so one object's high-scoring box can suppress another object's valid detection.

*Sources: HC5a p.67.*

</details>

### CV1-473 · core

**What is sliding-window detection?**

<details>
<summary>Show answer</summary>

Apply a classifier over candidate positions, sizes and aspect ratios. Dense scanning can be computationally expensive and produce many overlapping candidates.

*Sources: HC5a pp.35–48.*

</details>

### CV1-474 · core

**What is a region proposal?**

<details>
<summary>Show answer</summary>

A candidate region likely to contain an object, intended to reduce the number of regions requiring detailed classification/localization.

*Sources: HC5b p.99; HC6a p.11.*

</details>

### CV1-475 · core

**What is Selective Search at a high level?**

<details>
<summary>Show answer</summary>

A class-agnostic heuristic proposal method that starts from oversegmentation and hierarchically merges similar regions to produce candidate boxes.

*Sources: HC5a pp.49–56; S4.*

</details>

### CV1-476 · core

**How does original R-CNN compute region features?**

<details>
<summary>Show answer</summary>

Generate external region proposals, warp/crop each region and run the CNN separately for each, then classify and refine boxes.

*Sources: HC5b pp.100–124.*

</details>

### CV1-477 · core

**What are major original R-CNN inefficiencies?**

<details>
<summary>Show answer</summary>

Repeated CNN work for overlapping crops and a multistage training/caching pipeline; the shared-image computation of later variants improves this.

*Sources: HC5b pp.118–124.*

</details>

### CV1-478 · core

**What changes in Fast R-CNN?**

<details>
<summary>Show answer</summary>

Compute one full-image convolutional feature map, extract fixed-size region features with RoI pooling, and jointly predict classes and box refinements. External proposals remain.

*Sources: HC5b pp.125–130.*

</details>

### CV1-479 · core

**What changes in Faster R-CNN?**

<details>
<summary>Show answer</summary>

Replace external proposal generation with a learned Region Proposal Network sharing backbone features, followed by the region-based detection stage.

*Sources: HC5b pp.131–133; HC6a pp.18–38.*

</details>

### CV1-480 · core

**What does an RPN predict?**

<details>
<summary>Show answer</summary>

Objectness and box-regression offsets for candidate anchors at feature-map locations; its proposals feed the detector's second stage.

*Sources: HC6a pp.19–38.*

</details>

### CV1-481 · core

**What is an anchor box?**

<details>
<summary>Show answer</summary>

A predefined reference box shape/scale at a location, refined by predicted offsets and assigned objectness/class information. Its definition depends on the detector version.

*Sources: HC6a pp.56–60.*

</details>

### CV1-482 · core

**What is the difference between one-stage and two-stage detection?**

<details>
<summary>Show answer</summary>

One-stage predicts dense boxes/classes directly from image features; two-stage first selects proposals then processes proposal features for final predictions. Both can share a backbone.

*Sources: HC6a pp.54–72; S5.*

</details>

### CV1-483 · core

**What does YOLO stand for?**

<details>
<summary>Show answer</summary>

You Only Look Once. The versions form a detector family; original v1 grid equations should not be applied unchanged to later versions.

*Sources: HC6a pp.64–72; SOURCE\_NOTES.*

</details>

### CV1-484 · core

**What is original YOLO v1's output tensor shape?**

<details>
<summary>Show answer</summary>

S x S x (5\*B+C): B boxes with four coordinates plus confidence each, and one C-class probability vector per grid cell.

*Sources: HC6a pp.66–72.*

</details>

### CV1-485 · core

**Which original YOLO v1 cell is assigned an object?**

<details>
<summary>Show answer</summary>

The cell containing the object's centre. Within it, the designated responsible box predictor is chosen using its match with the ground truth during training.

*Sources: HC6a pp.66–69.*

</details>

### CV1-486 · core

**What is original YOLO v1's box-confidence convention?**

<details>
<summary>Show answer</summary>

Pr(object)\*IoU(predicted box,ground truth). At training, no-object targets are zero; an object box's confidence relates to its IoU. This is version-specific.

*Sources: HC6a pp.69–72; SOURCE\_NOTES.*

</details>

### CV1-487 · core

**What is the original YOLO v1 class-specific detection score?**

<details>
<summary>Show answer</summary>

Pr(class|object)\*Pr(object)\*IoU, using its specified box-confidence convention. Do not assume every later detector has the same IoU factor.

*Sources: HC6a pp.69–72.*

</details>

### CV1-488 · core

**How many candidate boxes does an SxS grid with B boxes per cell produce?**

<details>
<summary>Show answer</summary>

S\*S\*B before filtering. Output scalar count is a different question and depends on the detector's channel convention.

*Sources: HC6a pp.56–62.*

</details>

### CV1-489 · core

**How does an SSD-type detector handle different object scales?**

<details>
<summary>Show answer</summary>

Predict from multiple feature-map resolutions with reference/default boxes of varying sizes and aspect ratios.

*Sources: HC6a pp.40–63; Szeliski §6.3.*

</details>

### CV1-490 · core

**What is a detector backbone, neck and head?**

<details>
<summary>Show answer</summary>

Backbone extracts features; neck combines/transforms features, often across scales; head predicts object classes, boxes and related outputs.

*Sources: S5 Exercise 4; YOLOv4 §2.1.*

</details>

### CV1-491 · core

**What is the role of a Feature Pyramid Network (FPN)?**

<details>
<summary>Show answer</summary>

Combine coarse high-level semantic features with finer spatial feature maps, using top-down and lateral paths, for multiscale detection.

*Sources: HC6a pp.40–51; S5.*

</details>

### CV1-492 · breadth

**What does the YOLOv4 paper call a bag of freebies?**

<details>
<summary>Show answer</summary>

Training methods that improve accuracy without increasing inference cost, such as suitable augmentation or training-loss changes.

*Sources: YOLOv4 §2.2; S5.*

</details>

### CV1-493 · breadth

**What does the YOLOv4 paper call a bag of specials?**

<details>
<summary>Show answer</summary>

Architectural or postprocessing additions that improve accuracy with relatively small added inference cost.

*Sources: YOLOv4 §2.3; S5.*

</details>

### CV1-494 · core

**Why use IoU-based rather than raw unnormalized coordinate error for box regression?**

<details>
<summary>Show answer</summary>

IoU measures relative overlap and is unchanged under common scaling of both boxes. Raw coordinate squared loss grows with object/error scale.

*Sources: S5 Exercise 4; YOLOv4 §2.2.*

</details>

### CV1-495 · breadth

**What limitation does plain IoU loss have for disjoint boxes?**

<details>
<summary>Show answer</summary>

IoU is zero with no overlap, so the plain overlap loss may provide poor/zero local guidance toward the target in disjoint configurations. Extensions add geometric terms.

*Sources: YOLOv4 §2.2.*

</details>

### CV1-496 · breadth

**What extra box relationships do DIoU and CIoU consider?**

<details>
<summary>Show answer</summary>

DIoU adds centre-distance information; CIoU also considers aspect-ratio consistency along with overlap and centre distance. Detailed formulas are not introduced here.

*Sources: YOLOv4 §2.2.*

</details>

### CV1-655 · core

**What is RoI pooling in Fast R-CNN?**

<details>
<summary>Show answer</summary>

Divide a proposal's shared-feature-map region into a fixed grid and pool each bin, giving fixed-size features for different-sized proposals.

*Sources: HC6a pp.13–17; HC5b Fast R-CNN.*

</details>

### CV1-656 · core

**What two kinds of prediction form the usual Fast/Faster R-CNN detection head?**

<details>
<summary>Show answer</summary>

A class/background prediction and bounding-box refinement/regression, trained with a combined task loss under the specified architecture.

*Sources: HC5b pp.125–133; HC6a p.17.*

</details>

### CV1-657 · core

**Do modern two-stage detectors run their backbone only on isolated proposal crops?**

<details>
<summary>Show answer</summary>

No. Fast/Faster R-CNN share a whole-image feature computation, then process region features. Crop-by-crop CNN computation describes original R-CNN.

*Sources: HC5b pp.118–133; S5 Q4a; SOURCE\_NOTES.*

</details>

### CV1-658 · breadth

**Who is the lead author associated with R-CNN and Fast R-CNN in the lecture?**

<details>
<summary>Show answer</summary>

Ross Girshick. Faster R-CNN is led by Shaoqing Ren with collaborators including Girshick and Kaiming He.

*Sources: HC5b R-CNN references; HC6a pp.12,18.*

</details>

### CV1-659 · breadth

**Who is associated with the original YOLO detector?**

<details>
<summary>Show answer</summary>

Joseph Redmon and collaborators; the lecture cites the CVPR 2016 work. This is separate from later YOLOv4 authors/version details.

*Sources: HC6a p.64.*

</details>

### CV1-660 · breadth

**What does Mask R-CNN add to a region-based detector?**

<details>
<summary>Show answer</summary>

A per-instance pixel-mask prediction branch in addition to class and box outputs. The pack does not introduce advanced RoIAlign mechanics.

*Sources: HC5a instance segmentation; HC6a p.75; Szeliski §6.4.*

</details>

## architectures

### CV1-497 · core

**What is transfer learning?**

<details>
<summary>Show answer</summary>

Reuse representations or weights learned on one task/dataset for another, often replacing the output head and optionally fine-tuning the backbone.

*Sources: HC6a pp.80–94; Lab5.*

</details>

### CV1-498 · core

**What does freezing a layer mean?**

<details>
<summary>Show answer</summary>

Do not update its parameters during optimization. It is distinct from selecting evaluation mode or merely disabling some output.

*Sources: HC6a pp.81–94; Lab5.*

</details>

### CV1-499 · core

**Why replace the final layer when adapting an ImageNet classifier to new classes?**

<details>
<summary>Show answer</summary>

The head must map learned features to the new class count and meanings, not the original 1000-class label set.

*Sources: HC6a pp.81–94; Lab5 Task 8.1.*

</details>

### CV1-500 · core

**When might you train only a new head versus fine-tune more layers?**

<details>
<summary>Show answer</summary>

For limited similar-domain data, frozen features can be useful; more data or domain mismatch may justify fine-tuning. Validate the choice; it is not a fixed guarantee.

*Sources: HC6a pp.80–94; Lab5.*

</details>

### CV1-501 · core

**Why match pretrained model input preprocessing?**

<details>
<summary>Show answer</summary>

Learned filters expect particular channel order, scale, normalization and often input size. Mismatched inputs can harm reused features.

*Sources: Lab5 CIFAR transfer-learning tutorial.*

</details>

### CV1-502 · breadth

**What is LeNet known for in the course history?**

<details>
<summary>Show answer</summary>

An early successful convolutional network trained by backpropagation for handwritten-character/digit recognition.

*Sources: HC5b p.91.*

</details>

### CV1-503 · breadth

**What was AlexNet's role in the course's CNN history?**

<details>
<summary>Show answer</summary>

A major 2012 ImageNet breakthrough using a deeper CNN and GPU training, helping establish modern deep vision.

*Sources: HC5b p.92; HC6a p.97.*

</details>

### CV1-504 · core

**What is VGG's regular architectural pattern?**

<details>
<summary>Show answer</summary>

Stacks of small 3x3 convolutions with nonlinearities, separated by pooling stages; deeper stages commonly increase channels.

*Sources: HC5b p.93; HC6a p.96.*

</details>

### CV1-505 · breadth

**Who are the VGG authors named correctly in the architecture lecture?**

<details>
<summary>Show answer</summary>

Karen Simonyan and Andrew Zisserman. VGG refers to Oxford's Visual Geometry Group.

*Sources: HC6a p.96; SOURCE\_NOTES.*

</details>

### CV1-506 · core

**Why can stacked small convolutions be useful instead of one large kernel?**

<details>
<summary>Show answer</summary>

They enlarge receptive field with intermediate nonlinearities and can reduce parameter count for suitable channel choices. The advantage depends on dimensions.

*Sources: HC5b receptive fields; HC6a VGG.*

</details>

### CV1-507 · core

**What is the ResNet residual-block equation before any final activation?**

<details>
<summary>Show answer</summary>

y=x+F(x), for compatible shapes. The branch learns a residual relative to the shortcut rather than the entire mapping.

*Sources: HC6a pp.99–104.*

</details>

### CV1-508 · core

**How can a residual branch express an identity mapping?**

<details>
<summary>Show answer</summary>

Set F(x)=0 so the preactivation sum is x. If a final ReLU follows, the whole block equals ReLU(x), not identity for arbitrary negative x.

*Sources: HC6a pp.102–103; SOURCE\_NOTES.*

</details>

### CV1-509 · core

**Why do residual connections help optimization of deep networks?**

<details>
<summary>Show answer</summary>

They provide direct signal/gradient paths and make identity-like mappings easy to express. They mitigate, not eliminate, optimization problems.

*Sources: HC6a pp.100–112.*

</details>

### CV1-510 · core

**What if a ResNet block changes spatial resolution or channel count?**

<details>
<summary>Show answer</summary>

Use a shape-compatible shortcut such as a projection/downsample; direct elementwise addition requires matching dimensions.

*Sources: HC6a pp.104–111.*

</details>

### CV1-511 · core

**What distinguishes a ResNet basic block from a bottleneck block?**

<details>
<summary>Show answer</summary>

A basic block commonly uses two spatial 3x3 convolutions. A bottleneck uses 1x1 reduction, 3x3 processing and 1x1 expansion. Check the particular architecture.

*Sources: HC6a pp.107–111.*

</details>

### CV1-512 · core

**What is an encoder–decoder architecture?**

<details>
<summary>Show answer</summary>

An encoder reduces/spatially compresses features; a decoder upsamples or reconstructs an output, often at image resolution.

*Sources: HC6a pp.114–140.*

</details>

### CV1-513 · core

**What is U-Net's distinctive skip connection?**

<details>
<summary>Show answer</summary>

Concatenate corresponding high-resolution encoder features with decoder features, restoring spatial information while using coarse semantic context.

*Sources: HC6a pp.122–126,137.*

</details>

### CV1-514 · core

**How do usual ResNet and U-Net skip operations differ?**

<details>
<summary>Show answer</summary>

ResNet adds compatible tensors; U-Net concatenates feature channels across the contracting and expanding paths at matching spatial scales.

*Sources: HC6a pp.136–137.*

</details>

### CV1-515 · core

**What is transposed convolution?**

<details>
<summary>Show answer</summary>

Before an optional bias, a learned linear operator corresponding to the transpose of a convolution's matrix representation, commonly used for upsampling. It is not generally the mathematical inverse of convolution.

*Sources: HC6a pp.117–119.*

</details>

### CV1-516 · breadth

**What does SegNet-style unpooling use?**

<details>
<summary>Show answer</summary>

Store max-pooling locations in the encoder and place values back at those locations during decoder unpooling, followed by refinement operations.

*Sources: HC6a pp.115–121.*

</details>

### CV1-517 · core

**What is an autoencoder's training target?**

<details>
<summary>Show answer</summary>

Reconstruct its input through an encoder and decoder, typically minimizing a reconstruction loss rather than using separate class labels.

*Sources: HC6a pp.127–130.*

</details>

### CV1-518 · core

**What is the role of an autoencoder's latent bottleneck?**

<details>
<summary>Show answer</summary>

Encourage a constrained useful representation; compression alone does not guarantee semantic features or perfect reconstruction.

*Sources: HC6a pp.129–140.*

</details>

### CV1-519 · breadth

**What is a self-supervised consistency loss in the lecture's rendering example?**

<details>
<summary>Show answer</summary>

Compare predicted/rendered observations with available images, using observations themselves as a training signal rather than manual labels for every output.

*Sources: HC6a pp.131–135.*

</details>

### CV1-520 · core

**What loss is commonly used for supervised semantic segmentation?**

<details>
<summary>Show answer</summary>

Per-pixel class cross-entropy, aggregated over labelled pixels under a specified ignore/weighting rule.

*Sources: HC5a p.89; HC6a encoder–decoder.*

</details>

### CV1-661 · breadth

**Who are the ResNet paper authors cited by the lecture?**

<details>
<summary>Show answer</summary>

Kaiming He, Xiangyu Zhang, Shaoqing Ren and Jian Sun, Deep Residual Learning for Image Recognition.

*Sources: HC6a pp.99–112; Lab5.*

</details>

### CV1-662 · core

**How does concatenating U-Net features affect channel count?**

<details>
<summary>Show answer</summary>

Matching spatial arrays with C1 and C2 channels concatenate to C1+C2 channels. Elementwise addition instead requires compatible channels and keeps that count.

*Sources: HC6a pp.122–126,136–137.*

</details>

## stereo

### CV1-521 · core

**What is epipolar geometry?**

<details>
<summary>Show answer</summary>

The geometry relating corresponding points in two views, defined by the two camera centres and a scene point. It constrains a match to an epipolar line.

*Sources: HC6b pp.50–65.*

</details>

### CV1-522 · core

**What is an epipolar plane?**

<details>
<summary>Show answer</summary>

A plane containing both camera centres and a 3D point. Its intersection with each image plane gives that point's epipolar line.

*Sources: HC6b pp.50–53.*

</details>

### CV1-523 · core

**What is an epipole?**

<details>
<summary>Show answer</summary>

The projection of one camera centre into the other camera's image. It may lie inside, outside or at infinity in the image plane.

*Sources: HC6b pp.50–63.*

</details>

### CV1-524 · core

**Why does epipolar geometry reduce a 2D correspondence search to 1D?**

<details>
<summary>Show answer</summary>

A point in one image restricts the matching point in the other to a line, rather than any image location. Appearance still selects among points along that line.

*Sources: HC6b pp.50–65.*

</details>

### CV1-525 · core

**Write the pixel-coordinate epipolar constraint.**

<details>
<summary>Show answer</summary>

x2.T\*F\*x1=0 for homogeneous image points. F maps x1 to line l2=F\*x1 in image 2.

*Sources: HC6b pp.53–55.*

</details>

### CV1-526 · core

**What are the dimensions, rank and degrees of freedom of a generic fundamental matrix?**

<details>
<summary>Show answer</summary>

3x3, rank 2, 7 degrees of freedom after scale and rank constraints, for nondegenerate two-view geometry.

*Sources: HC6b pp.54–55.*

</details>

### CV1-527 · core

**Does F map a point to its unique matching point?**

<details>
<summary>Show answer</summary>

No. It maps a point to an epipolar line; appearance and other constraints are needed to find the match on that line.

*Sources: HC6b pp.54–65.*

</details>

### CV1-528 · breadth

**What is the essential matrix?**

<details>
<summary>Show answer</summary>

The calibrated two-view epipolar matrix for normalized camera coordinates. For relative pose X2=R\*X1+t and constraint y2.T\*E\*y1=0, E=[t]\_x\*R, where [t]\_x\*v=t cross v.

*Sources: HC6b pp.53–55.*

</details>

### CV1-529 · breadth

**How are essential and fundamental matrices related?**

<details>
<summary>Show answer</summary>

F=K2^(-T)\*E\*K1^(-1), with E=K2.T\*F\*K1, under x2.T\*F\*x1=0 and corresponding calibrated coordinates.

*Sources: HC6b pp.53–55.*

</details>

### CV1-530 · breadth

**How many degrees of freedom does a generic essential matrix have?**

<details>
<summary>Show answer</summary>

Five: three relative-rotation parameters and two translation-direction parameters; translation magnitude is not observable from the epipolar relation.

*Sources: HC6b p.55.*

</details>

### CV1-531 · core

**Why is pure camera rotation degenerate for ordinary stereo depth triangulation?**

<details>
<summary>Show answer</summary>

It supplies no translation baseline or depth-dependent parallax; correspondences determine ray rotations but not distance along each ray.

*Sources: HC4a p.34; HC6b pp.114–124.*

</details>

### CV1-532 · core

**What is stereo rectification?**

<details>
<summary>Show answer</summary>

Warp both images so corresponding epipolar lines align, usually as horizontal scanlines; this simplifies matching to row-wise search.

*Sources: HC6b pp.79–90.*

</details>

### CV1-533 · core

**Does stereo rectification guarantee identical images or zero disparity?**

<details>
<summary>Show answer</summary>

No. It aligns epipolar lines; horizontal disparity still carries depth information, and occlusion/appearance differences remain.

*Sources: HC6b pp.79–90.*

</details>

### CV1-534 · core

**What is disparity in the convention used by the numerical practice questions?**

<details>
<summary>Show answer</summary>

d=uL-uR for an ideal rectified pair with equal principal-point coordinates. Other slide/camera conventions can reverse the sign; always check.

*Sources: HC6b pp.85–90; SOURCE\_NOTES.*

</details>

### CV1-535 · core

**Write ideal rectified-stereo depth from disparity.**

<details>
<summary>Show answer</summary>

Z=f\*B/d, with f in pixels, d in pixels, B in physical length units and a compatible sign/principal-point convention.

*Sources: HC6b pp.84–90; Szeliski §12.1.*

</details>

### CV1-536 · core

**How do depth and disparity relate?**

<details>
<summary>Show answer</summary>

Disparity is inversely proportional to depth for fixed focal length/baseline. Nearer points have larger disparity magnitude.

*Sources: HC6b pp.85–90.*

</details>

### CV1-537 · core

**Why are distant stereo depths sensitive to small disparity errors?**

<details>
<summary>Show answer</summary>

Z=fB/d gives sensitivity magnitude fB/d^2; small d leads to a large depth change per pixel of disparity error.

*Sources: HC6b disparity; prerequisite calculus.*

</details>

### CV1-538 · core

**What are common stereo matching difficulties?**

<details>
<summary>Show answer</summary>

Textureless/repeated patterns, occlusion, specular or lighting differences, depth boundaries and ambiguous correspondences.

*Sources: HC6b pp.87–103.*

</details>

### CV1-539 · core

**What is the stereo matching-window-size trade-off?**

<details>
<summary>Show answer</summary>

Small windows preserve detail but can be ambiguous/noisy; large windows stabilize matching but mix depths and lose boundary detail.

*Sources: HC6b p.102.*

</details>

### CV1-540 · core

**What are data and smoothness terms in stereo energy minimization?**

<details>
<summary>Show answer</summary>

Data term rewards good appearance matches for selected disparities; smoothness term encourages neighbouring disparities to be compatible, with care at real discontinuities.

*Sources: HC6b pp.91–99.*

</details>

### CV1-541 · core

**What can an excessively strong stereo smoothness penalty do?**

<details>
<summary>Show answer</summary>

Force nearly constant disparity and oversmooth real depth boundaries, sacrificing valid image-match evidence.

*Sources: HC6b pp.95–96.*

</details>

### CV1-542 · breadth

**What is triangulation?**

<details>
<summary>Show answer</summary>

Estimate a 3D point from corresponding image observations and camera geometry, ideally intersecting viewing rays; noisy rays require an approximate fit.

*Sources: HC6b pp.114–128.*

</details>

### CV1-543 · core

**What is Structure from Motion (SfM)?**

<details>
<summary>Show answer</summary>

Jointly estimate camera poses/motion and scene structure from overlapping images of a largely static scene.

*Sources: HC6b pp.113–118.*

</details>

### CV1-544 · core

**What is bundle adjustment?**

<details>
<summary>Show answer</summary>

Joint nonlinear refinement of camera parameters and 3D points to minimize reprojection error over observations, with appropriate gauge/reference constraints.

*Sources: HC6b pp.108–110,123–129.*

</details>

### CV1-545 · core

**What is reprojection error in bundle adjustment?**

<details>
<summary>Show answer</summary>

Difference between an observed image feature and the projected estimate of its 3D point using that view's camera parameters.

*Sources: HC6b pp.109–110.*

</details>

### CV1-546 · core

**What global ambiguity remains in ordinary calibrated monocular SfM without a metric reference?**

<details>
<summary>Show answer</summary>

Global scale, along with an arbitrary coordinate frame. Images alone do not make the reconstruction's units metres; unrestricted uncalibrated reconstruction can have a larger projective ambiguity.

*Sources: HC6b pp.117–118.*

</details>

### CV1-547 · core

**What is multi-view stereo (MVS) relative to SfM?**

<details>
<summary>Show answer</summary>

Densify scene geometry using multiple views and estimated/calibrated cameras; SfM usually supplies poses and sparse structure.

*Sources: HC6b pp.104,112–118.*

</details>

### CV1-548 · breadth

**What are main incremental SfM steps?**

<details>
<summary>Show answer</summary>

Initialize a suitable two-view reconstruction; triangulate; refine; register new views from 2D–3D matches; triangulate new points; repeat adjustment and outlier filtering.

*Sources: HC6b pp.120–133.*

</details>

### CV1-549 · breadth

**What is Perspective-n-Point (PnP) used for in incremental SfM?**

<details>
<summary>Show answer</summary>

Estimate a camera's pose from correspondences between known 3D points and their 2D image observations, under the specified camera calibration.

*Sources: HC6b pp.125–128.*

</details>

### CV1-550 · breadth

**How do global and hierarchical SfM differ at a high level?**

<details>
<summary>Show answer</summary>

Global methods estimate multi-camera relations jointly; hierarchical methods reconstruct subsets and merge them, often with similarity transforms.

*Sources: HC6b pp.141–149.*

</details>

### CV1-551 · breadth

**What is shape from silhouette and the visual hull?**

<details>
<summary>Show answer</summary>

Intersect silhouette viewing cones from known cameras to obtain a visual hull. Concavities invisible in all silhouettes cannot generally be recovered.

*Sources: HC6b pp.22–24.*

</details>

### CV1-552 · breadth

**What cue is used in shape from texture?**

<details>
<summary>Show answer</summary>

Changes in the appearance/density/foreshortening of an assumed repetitive texture can indicate surface orientation and depth variation.

*Sources: HC6b pp.18–19.*

</details>

### CV1-553 · breadth

**What cue is used in shape from focus?**

<details>
<summary>Show answer</summary>

The focus setting with highest local sharpness/frequency response relates to depth, under a calibrated camera/focus model.

*Sources: HC6b p.20.*

</details>

### CV1-554 · breadth

**What cue is used in shape from shadows?**

<details>
<summary>Show answer</summary>

Shadow geometry provides shape/height constraints when light and viewing geometry are sufficiently known or constrained.

*Sources: HC6b p.21.*

</details>

### CV1-663 · core

**What epipolar line corresponds to x2 in image 1?**

<details>
<summary>Show answer</summary>

l1=F.T\*x2 under x2.T\*F\*x1=0. The transpose switches which image's points and lines are involved.

*Sources: HC6b pp.53–55.*

</details>

### CV1-664 · breadth

**What nullspace relations identify epipoles for a nondegenerate F?**

<details>
<summary>Show answer</summary>

F\*e1=0 and F.T\*e2=0, with e1/e2 the epipoles in their respective images and F mapping image-1 points to image-2 lines.

*Sources: HC6b epipoles; Szeliski multi-view geometry.*

</details>

### CV1-665 · core

**Why is F rank 2, rather than rank deficient merely because it is defined up to scale?**

<details>
<summary>Show answer</summary>

Its epipolar geometry has a nonzero null direction/epipole. Scale ambiguity removes one free parameter but does not by itself force matrix rank deficiency.

*Sources: HC6b p.55; SOURCE\_NOTES.*

</details>

### CV1-666 · breadth

**What algebraic singular-value property characterizes a nondegenerate essential matrix?**

<details>
<summary>Show answer</summary>

Two equal nonzero singular values and one zero singular value, up to common scale. F generally lacks the equal-nonzero-value constraint.

*Sources: HC6b essential matrix; Szeliski multi-view geometry.*

</details>

### CV1-667 · breadth

**Which estimation algorithms does the E/F overview name?**

<details>
<summary>Show answer</summary>

The calibrated essential-matrix 5-point algorithm and the standard linear fundamental-matrix 8-point algorithm. Do not confuse 8-point's sample requirement with F's 7 degrees of freedom.

*Sources: HC6b p.55.*

</details>

### CV1-668 · core

**What is the perpendicular distance from image point (x,y) to line [a,b,c]?**

<details>
<summary>Show answer</summary>

abs(a\*x+b\*y+c)/sqrt(a^2+b^2), for a and b not both zero. The raw line-equation residual changes with homogeneous line scale.

*Sources: HC6b epipolar lines; prerequisite geometry.*

</details>

### CV1-669 · core

**Why use outlier rejection before two-view pose estimation/SfM?**

<details>
<summary>Show answer</summary>

Incorrect descriptor correspondences violate the geometric model and can corrupt camera and structure estimates. RANSAC can use an epipolar residual to select a consensus.

*Sources: HC6b pp.64–65,121–124.*

</details>

### CV1-670 · core

**Why is a static-scene assumption important in ordinary SfM?**

<details>
<summary>Show answer</summary>

Camera motion should explain correspondences to fixed 3D points. Independently moving objects can violate that common rigid-scene model.

*Sources: HC6b SfM; HC3b motion.*

</details>

## coding

### CV1-555 · core

**What is the difference between NumPy '\*' and '@' for arrays?**

<details>
<summary>Show answer</summary>

'\*' multiplies elementwise with broadcasting; '@' performs matrix multiplication. Use the one required by the model's shapes.

*Sources: Lab0; Syllabus syntax sheet.*

</details>

### CV1-556 · core

**For image shape (H,W,3), what does mean(axis=2) produce?**

<details>
<summary>Show answer</summary>

A per-pixel channel mean with shape (H,W), unless keepdims=True retains shape (H,W,1). It is not a per-channel global mean.

*Sources: Lab0; Lab1; Coding examples.*

</details>

### CV1-557 · core

**How does a vector of shape (3,) broadcast onto an image of shape (H,W,3)?**

<details>
<summary>Show answer</summary>

It aligns with the final channel dimension and applies the three values at every pixel. Incompatible trailing dimensions cause an error.

*Sources: Lab0; Coding examples Q3.*

</details>

### CV1-558 · core

**What does np.stack add compared with np.concatenate?**

<details>
<summary>Show answer</summary>

stack adds a new axis; concatenate joins arrays along an existing axis, requiring compatible shapes elsewhere.

*Sources: Lab0; Syllabus syntax sheet.*

</details>

### CV1-559 · core

**What does reshape preserve and what does it not do?**

<details>
<summary>Show answer</summary>

It reorganizes the same number of values in the specified memory/order convention. It does not resize/interpolate an image or change the underlying values by itself.

*Sources: Lab0.*

</details>

### CV1-560 · core

**What does transpose do to a multi-axis tensor?**

<details>
<summary>Show answer</summary>

Permute axes; default .T reverses all axes, not just a semantic switch between HWC and CHW. Specify the desired axis order.

*Sources: Lab0; Syllabus syntax sheet.*

</details>

### CV1-561 · core

**Does an ordinary NumPy slice always make a separate copy?**

<details>
<summary>Show answer</summary>

No. Basic slices usually share storage with the original, so editing the view can edit the original. Use copy() when independent storage is needed.

*Sources: Lab0.*

</details>

### CV1-562 · core

**What does a Python/NumPy slice stop index mean?**

<details>
<summary>Show answer</summary>

The stop is exclusive. For a centred odd-size patch, calculate bounds so the intended last row/column is included.

*Sources: Lab0; Lab2; Lab3.*

</details>

### CV1-563 · core

**What does np.argmin return when several entries have the same minimum?**

<details>
<summary>Show answer</summary>

The first minimum in the relevant flattened/axis traversal order. If a problem wants another tie rule, implement it explicitly.

*Sources: Lab0; Syllabus syntax sheet.*

</details>

### CV1-564 · core

**What numerical precision rule applies to the exam's ordinary numerical answers?**

<details>
<summary>Show answer</summary>

Keep full precision during calculation and round only the final answer to two decimals unless stated otherwise. The default tolerance is ±0.01 around the unrounded reference.

*Sources: Syllabus pp.5–6.*

</details>

### CV1-565 · core

**Are numerical count answers allowed the usual ±0.01 tolerance?**

<details>
<summary>Show answer</summary>

No. Strictly integer answers require the exact integer; the syllabus gives no numerical partial credit outside the defined tolerance.

*Sources: Syllabus pp.5–6.*

</details>

### CV1-566 · core

**Which runtime libraries are stated to be installed for exam computation?**

<details>
<summary>Show answer</summary>

NumPy, SciPy and pandas, with basic Python. OpenCV is not installed; OpenCV lab snippets may still be tested by interpretation.

*Sources: Syllabus pp.5,7–8.*

</details>

### CV1-567 · core

**How can function documentation be checked during the exam without internet?**

<details>
<summary>Show answer</summary>

Use Jupyter/IPython's built-in question-mark help, such as np.concatenate?, and the provided syntax sheet.

*Sources: Syllabus pp.4–5,14–15.*

</details>

### CV1-568 · core

**Should you leave a multiple-choice question blank if unsure?**

<details>
<summary>Show answer</summary>

No, according to the syllabus: guess correction also applies to unanswered questions, so leaving it blank is no better than a wrong answer.

*Sources: Syllabus p.6.*

</details>

### CV1-569 · core

**How many personal cheat-sheet sheets are allowed by the supplied syllabus?**

<details>
<summary>Show answer</summary>

Three A4 sheets, each permitted on both sides. This means three sheets/six sides, not three total sides.

*Sources: Syllabus pp.6–7.*

</details>

### CV1-570 · core

**What is the exam's base-grade formula after ANS guess correction?**

<details>
<summary>Show answer</summary>

mark=1+9\*obtained\_points/total\_points, with obtained\_points defined after the configured correction. The pack's raw practice score is not that official mark.

*Sources: Syllabus p.6.*

</details>

### CV1-571 · breadth

**Which supplied materials are explicitly excluded from exam coverage?**

<details>
<summary>Show answer</summary>

The guest lecture in Lecture 13 and newly introduced advanced code/applications in parts marked optional. Foundational concepts taught in mandatory material remain eligible.

*Sources: Syllabus pp.3,7–8.*

</details>

### CV1-671 · core

**What is a safe way to normalize vectors stored as rows of an (N,3) array?**

<details>
<summary>Show answer</summary>

Compute Euclidean norms along axis=1 with keepdims=True, then divide valid rows. Zero norms need an explicit mask/fallback. Flattening to one global norm gives the wrong result.

*Sources: Lab1 normals; Lab0 axes.*

</details>

### CV1-672 · core

**Why should a stable least-squares routine be preferred to explicitly forming an inverse of A.T\*A?**

<details>
<summary>Show answer</summary>

It avoids unnecessary inversion and the numerical conditioning loss from squaring the condition number. Full-rank algebraic formulas still help explain the model.

*Sources: Coding examples Q1,Q5; Szeliski least squares.*

</details>

### CV1-673 · core

**Why should rounding usually occur after a multi-step computer-vision calculation?**

<details>
<summary>Show answer</summary>

Early rounding can alter ratios, fitted parameters and threshold decisions, and can accumulate enough error to fail the final tolerance.

*Sources: Syllabus pp.5–6.*

</details>
