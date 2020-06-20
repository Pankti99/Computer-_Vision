# Computer_Vision
This repository contains basic image processing operations

Morphology:

=>Morphology is a broad set of image processing operations that process images based on shapes. In a morphological operation, the value of each pixel in the output image is based on a comparison of the corresponding pixel in the input image with its neighbors.

=>Morphological operations apply structuring element (kernel) to an input image , creating an output image of same size.


(1) Erosion:

=> It shrinks the foreground and enlarges the background. It removes pixel on object boundaries. erodes the white pixels. areas of the foreground pixels shrink in size while holes within these regions becomes larger.

(2) Dilation:

=> It enlarges the foreground and shrinks  the background.Add pixels to the object boundaries. areas of the foreground pixels grow in size      while holes within these regions becomes smaller.

(3) Opening:

=> Smoothing contours and eliminates protrusions. used for spot and noise removal. performed by erosion and next dialtion. reduces salt noise.


(4) Closing:

=> Smoothin sections of contours , fuses narrow breaks,fill gaps in contours. used for removal of holes. performed by dialtion and next erosion. reduces pepper noise.
