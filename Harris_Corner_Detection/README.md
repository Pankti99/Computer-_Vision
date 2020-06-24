Harris Corner Detection

=>Harris Corner Detector is a corner detection operator that is commonly used in computer vision algorithms to extract corners and infer features of an image.

=>The idea behind the Harris method is to detect points based on the intensity variation in a localneighborhood: a small region around the feature should showa large intensity change when comparedwith windows shifted in any direction.


cv2.cornerHarris(src, blockSize, ksize, k) 

Parameters Explained:	

    src – Input single-channel 8-bit or floating-point image.
    dst – Image to store the Harris detector responses. It has the type CV_32FC1 and the same size as src .
    blockSize – Neighborhood size (see the details on cornerEigenValsAndVecs() ).
    ksize – Aperture parameter for the Sobel() operator.
    k – Harris detector free parameter.



For better understanding refer to this pdf:

http://www.cse.psu.edu/~rtc12/CSE486/lecture06.pdf
