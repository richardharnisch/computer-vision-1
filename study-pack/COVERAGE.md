# Coverage and sources

## Scope

The pack follows the supplied **2026 course**, not the entire contents of either textbook. The syllabus says that a reading-only concept is not examinable if it is absent from lectures, seminars and labs. The 9 October preparation checklist sets priorities but explicitly says it is not exhaustive.

The source review included all 12 supplied lecture decks, all five seminar exercise/solution pairs, Lab 0 and Labs 1–5, and the current exam-preparation documents. Both textbooks were consulted for relevant explanations, conventions and formulas; they were **not read cover to cover**. PDF text and notebook source were extracted for searching; selected formula pages were also checked visually. This is not a claim that every figure, external link or lecture recording was reviewed.

The questions use new values, examples and failure cases. They are not copied from the exercise sets or old mocks. They require transfer of the same course ideas, not additional advanced algorithms.

## Lecturer checklist → practice

`E2Q38` means Exam 2, Question 38. These are representative links by question ID; [the topic index](TOPIC_INDEX.md) lists every question's primary topic and all card counts.

| Lecturer priority | Skills covered | Representative questions | Card topics |
|---|---|---|---|
| Intrinsics, extrinsics, projection, homogeneous coordinates | Construct/use K and pose; distinguish t from camera centre; divide by homogeneous scale; crop/resize; transform directions | E1Q01–03, E1Q31, E2Q01–02, E2Q31, E3Q01, E3Q31 | camera |
| Reflectance and photometric stereo | Lambertian/Phong/BRDF; light–normal geometry; albedo/normal least squares; weighting; rank; height integration and signs | E1Q04–06, E1Q32–33, E2Q05–07, E2Q33–34, E3Q03–06, E3Q33–34 | reflectance, photometric |
| Neighbourhood processing | 4/8 connectivity; label equivalences; erosion/dilation/opening/closing; support and boundary rules | E1Q08–09, E1Q35, E2Q09–10, E2Q36, E3Q08–09, E3Q35 | morphology |
| Filtering and local features | Correlation vs convolution; Gaussian derivatives; separability; median; Canny; structure tensor; Harris/Shi–Tomasi; HoG | E1Q10–15, E1Q36–38, E2Q11, E2Q14–17, E2Q37–38, E3Q07, E3Q12, E3Q36, E3Q38–39 | filtering, features |
| Fourier transform | Complex magnitude/phase; Euler's formula; angular frequency; shift symmetry; DFT and circular convolution | E1Q12, E1Q37, E2Q12–13, E2Q39, E3Q02, E3Q10–11, E3Q37 | fourier, filtering |
| RANSAC and keypoint matching | Minimal nondegenerate samples; consensus/refit; iteration probabilities; descriptor ambiguity; ratio thresholds | E1Q16–17, E1Q23, E1Q40, E2Q22–23, E2Q43, E3Q13–16, E3Q41, E3Q43 | fitting, matching |
| Optical flow | Brightness constancy; Taylor expansion; local least squares; conditioning/aperture problem; pyramid vector units; lighting/occlusion failures | E1Q18–19, E1Q39, E2Q18–19, E2Q40, E3Q17–18, E3Q40 | flow |
| Global transforms and stitching | Transform families/invariants; affine and homography fitting; composition; backward sampling/interpolation; blending and parallax | E1Q20–22, E1Q41–42, E2Q23–24, E2Q42, E3Q20–21, E3Q42 | geometry, matching |
| Classification metrics | Confusion matrices; precision/recall/F1; imbalance; thresholds; macro aggregation | E1Q26, E1Q43, E2Q45, E3Q25, E3Q45 | metrics |
| Retrieval, detection and segmentation | Visual representation/ranking; AP conventions; one-to-one box matching; IoU; semantic/instance distinctions; partial-occlusion keypoint retrieval | E1Q44–45, E2Q10/Q22/Q26, E3Q46 | foundations, metrics, detection, classification, matching |
| CNN computation and trainable parameters | Output shape; shared weights; FC/convolution equivalence; bias; receptive fields; kernel gradients; bottlenecks; 3D kernels | E1Q27, E1Q46–49, E2Q47–48, E3Q47–48 | cnn, architectures |
| Clustering — conceptual priority | K-means assignments/means and limitations; feature scaling; mean-shift modes/bandwidth | E2Q21, E2Q44, E3Q23 | clustering |
| k-NN and BoVW — conceptual priority | Quantization/count representation; loss of layout; training/validation/test; codebook leakage; distance and k choices | E1Q24–25, E2Q25, E3Q22–24, E3Q44 | classification, clustering |
| NMS, Selective Search, AP/mAP — conceptual priority | Greedy suppression, non-transitivity and crowd failures; proposals; score-ranked evaluation | E2Q26–27, E2Q46, E3Q46; proposal comparison E1Q28 | detection, metrics |
| Optimization and R-CNN family — conceptual priority | Initialization/symmetry; learning rate/Adam; gradients; model capacity; shared feature/proposal differences | E1Q28, E2Q28–29, E3Q26 | optimization, detection, cnn |
| RPN, YOLO and ResNet — conceptual priority | Objectness/anchors; version-specific output/confidence; residual shape and parameter counts | E1Q28–29, E2Q49, E3Q27–28, E3Q47, E3Q49 | detection, architectures |
| Shape from X, stereo, SfM — conceptual priority | Epipolar lines; E/F distinctions; rectification; disparity; baseline degeneracy; bundle adjustment and scale | E1Q30, E1Q50, E2Q30, E2Q50, E3Q29–30, E3Q50 | stereo, camera |

Supporting calculations are deliberately included even for topics listed under the lecturer's conceptual priority. They are overtraining exercises, not a claim that those calculations will be set on the exam.

## Coverage beyond the checklist

- **Colour:** grayscale definitions, RGB/BGR, normalized RGB, opponent colour, HSV/YCbCr and Grey-World assumptions. White-Patch is one example for Lab1's open-choice request for another colour-constancy algorithm, not a specifically required name. E2Q03–04, E2Q32 and E3Q05/Q32; broader formulas and distinctions in cards.
- **Point processing:** histograms, CDF, gamma and equalization. E1Q07/Q34 and E2Q08/Q35.
- **Tracking:** SSD/correlation, search constraints, drift and colour-histogram tracking. E2Q20/Q41 and E3Q19; remaining details in cards.
- **Architecture breadth:** LeNet/AlexNet/VGG, transfer learning, encoder–decoder, U-Net, SegNet and autoencoders. E1Q29 and E3Q27/Q47; broader names/relations in cards.
- **Code fluency:** array axes, broadcasting, integer types, reshape/transpose, slicing, gradients and training/evaluation distinctions. Exam code is integrated into subject questions, not a separate syntax test.
- **Names and terms:** names explicitly used in the materials, plus acronym expansions; marked `breadth` when not part of the checklist's central calculations. Introductory application examples remain brief and do not become advanced implementation topics.

## Lab map

| Source | Mandatory/foundational content carried into this pack | Deliberately not added as advanced exam requirements |
|---|---|---|
| Lab0 | NumPy arrays, axes, broadcasting, types, slicing; image representation and BGR/RGB | Setup/download commands and incidental plotting syntax |
| Lab1 | Colour spaces/constancy; diffuse intrinsic reconstruction/recolouring; calibrated and weighted photometric stereo; integration/integrability | Implementing an unspecified literature method merely because an open-ended prompt suggests reading one |
| Lab2 | Correlation/convolution; Gaussian construction/derivatives/separability/cost; image gradients and edges | Optional PSNR tasks and advanced Gabor implementation/filter-bank experiments. Gabor definition remains because HC2b teaches it |
| Lab3 | Shi–Tomasi features; Lucas–Kanade and feature tracking; Harris basics also supported by Seminar 3 | Optional new Horn–Schunck code and advanced tracking extensions. Only the taught high-level distinction appears in breadth cards |
| Lab4 | SIFT matching; affine RANSAC/warping; alignment, interpolation, stitching and blending | Optional new extensions beyond the taught pipeline |
| Lab5 | MNIST/CIFAR tutorials; garbage-classification assignment; optimizers, initialization, loss, capacity, transfer and Grad-CAM | GPU training/download requirements and optional experiment design as a new implementation requirement |

The supplied Lab5 notebooks actually teach CNN classification. The syllabus's schedule label also mentions BoW; BoVW is covered using HC4b and Seminar 4, not invented as a missing notebook.

The local lab notebooks contain unfinished answer/code cells; no separate official Lab1–4 solution files were found locally. Conceptual work is cross-checked with lectures, seminar solutions and the textbooks. Do not treat a `YOUR CODE HERE` cell as a verified lecturer implementation. No course notebook's training or data-download cells were run.

## Source aliases and exact paths

Lecture page numbers are **1-based PDF pages**, not necessarily the printed slide numbers. `S1`–`S5` identify the matching seminar exercise/solution pair. Textbook sections use the editions supplied here.

| Alias | Local source, relative to the course folder |
|---|---|
| Syllabus | `syllabus.pdf` — last update 5 October 2026 |
| Checklist | `exam-prep/Suggested topics for CV1 exam preparation.pdf` — 9 October 2026 |
| Coding examples | `exam-prep/Coding Question Examples for CV1.pdf` — 29 September 2026 |
| ANS interface test | `exam-prep/ans_test.md` — interface familiarization instructions, not a source of question content |
| HC1a | `slides/CV1_2026_HC1a - Intro.pdf` |
| HC1b | `slides/CV1_2026_HC1b - Camera - Image Formation - Color.pdf` |
| HC2a | `slides/CV1_2026_HC2a - Reflection - Photometric Stereo - Image Processing.pdf` |
| HC2b | `slides/CV1_2026_HC2b - Neighborhood Processing - Image filtering.pdf` |
| HC3a | `slides/CV1_2026_HC3a - Local Features - Edges - Lines - Corners.pdf` |
| HC3b | `slides/CV1_2026_HC3b - Motion - Optical Flow - Tracking.pdf` |
| HC4a | `slides/CV1_2026_HC4a - Global Transforms - Image Stitching.pdf` |
| HC4b | `slides/CV1_2026_HC4b - Image Classification.pdf` |
| HC5a | `slides/CV1_2026_HC5a - Object Detection, Instance Segmentation.pdf` |
| HC5b | `slides/CV1_2026_HC5b - ConvNets Detection Basics.pdf` |
| HC6a | `slides/CV1_2026_HC6a - Single-Shot-Detection, Network Architectures.pdf` |
| HC6b | `slides/CV1_2026_HC6b - Shape-from-X Multi-view Stereo.pdf` |
| S1 | `seminars/CV1_Seminar_1_Exercises.pdf`, `seminars/CV1_Seminar_1_Solutions.pdf` |
| S2 | `seminars/CV1_Seminar_2_Exercises.pdf`, `seminars/CV1_Seminar_2_Solutions.pdf` |
| S3 | `seminars/CV1_Seminar_3_Exercises.pdf`, `seminars/CV1_Seminar_3_Solutions.pdf` |
| S4 | `seminars/CV1_Seminar_4_Exercises.pdf`, `seminars/CV1_Seminar_4_Solutions.pdf` |
| S5 | `seminars/CV1_Seminar_5_Exercises.pdf`, `seminars/CV1_Seminar_5_Solutions.pdf` |
| YOLOv4 | `seminars/CV1_Seminar_5_YOLOv4_paper.pdf` — especially §§2.1–2.3 named in the seminar |
| Lab0 | `labs/cv1-lab-0/cv1-lab-0.ipynb` |
| Lab1 | `labs/cv1-lab-1/cv1-lab-1.ipynb` |
| Lab2 | `labs/cv1-lab-2/cv1-lab-2.ipynb` |
| Lab3 | `labs/cv1-lab-3/cv1-lab-3.ipynb` |
| Lab4 | `labs/cv1-lab-4/cv1-lab-4.ipynb` |
| Lab5 | `labs/cv1-lab-5/docs/assignment-image-data-notebook.ipynb`, `tutorial-image-data-notebook.ipynb`, `tutorial-cifar-image-data-notebook.ipynb` in the same folder; supporting `overview-image-data.md`, `preparation-image-data.md`, `assignment-image-data.md`, `answer.md` |
| Szeliski | `Computer Vision: Algorithms and Applications.pdf` — second edition, supplied September 2021 final draft |
| Forsyth–Ponce | `Computer Vision: A Modern Approach.pdf` — second edition |
| SOURCE_NOTES | [Source/convention notes](SOURCE_NOTES.md) in this pack |

### Textbook support used

- **Szeliski:** geometric/photometric image formation (§§2.1–2.3); point processing, filtering, morphology and Fourier (§§3.1–3.4); SVM support (§5.1.4) and neural-network/CNN definitions (§§5.3–5.4); recognition (§§6.1–6.4); local features (§7.1); pairwise alignment/RANSAC/stitching (§§8.1–8.2); matching and Lucas–Kanade (§9.1, especially §9.1.3); disparity support (§12.1); normal integration/photometric stereo (§13.1.1). These are relevant passages, not an assertion that every subsection was exhaustively reviewed.
- **Forsyth–Ponce:** camera model and ambiguity (Chapter 1); reflection/photometric stereo/integration (§§2.1–2.2); colour representations (§3.3); Fourier interpretation (§4.3); SIFT/HoG (§5.4). This is supporting clarification for taught concepts, not a second full syllabus.

## Limits

- Old mock exams are **not** a template for format, length, weighting or content. Their `exam-prep/past-mock-exams/readme.md` warning was followed.
- Guest Lecture 13 and optional-only advanced content are excluded. An outline-only Hough mention receives a brief breadth definition, not an advanced Hough examination.
- No supplied document fixes this year's exact duration, question count or topic weighting. This pack's 150-minute, 30-MC/20-numerical design is an author-selected training format.
- No study pack can guarantee every possible question. The coverage map makes the reviewed scope and priorities explicit; it is not a prediction.
