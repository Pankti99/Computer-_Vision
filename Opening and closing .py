import cv2
import numpy as np

#Read image
img = cv2.imread('star.jpg',0)
cv2.imshow("Original Image",img)

#5*5 kernel for convolution 
# Increase and decrease the lernel size to see changes.
kernel = np.ones((3,3),np.uint8)

opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
cv2.imshow("Opening",opening)

closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
cv2.imshow("Closing",closing)

cv2.waitkey(0)
cv2.destroyAllWindows()