# **Hough Transform**

## - The Hough transform is an incredible tool that lets you identify lines. Not just lines, but other shapes as well.it is a popular feature extraction technique that converts an image from Cartesian to polar coordinates.

## - It somehow manage to detect the shape even if it is broken or distorted a little bit. We will see how it works for a line.

### The function used for detecting edge is cv2.Canny() edge detector.

- Now apply the hough transform using cv2.HoughLinesP() function:

## HoughLinesP(dst, lines, 1, CV_PI/180, 50, 50, 10 );

## Parameters Explained:


    dst: Output of the edge detector. It should be a grayscale image (although in fact it is a binary one)
    lines: A vector that will store the parameters (x_{start}, y_{start}, x_{end}, y_{end}) of the detected lines
    rho : The resolution of the parameter r in pixels. We use 1 pixel.
    theta: The resolution of the parameter \theta in radians. We use 1 degree (CV_PI/180)
    threshold: The minimum number of intersections to “detect” a line
    minLinLength: The minimum number of points that can form a line. Lines with less than this number of points are disregarded.
    maxLineGap: The maximum gap between two points to be considered in the same line.



## For detail understanding watch the following videos:

https://youtu.be/4zHbI-fFIlI

https://youtu.be/5gik4qtNoNo

https://youtu.be/Lbu9SnoucW4

https://youtu.be/ebfi7qOFLuo
