import cv2
import numpy as np


#Read image
img = cv2.imread('coins.bmp',0)

# M*N(5*5) kernel for convolution.you can also create your own kernel.
kernel = np.ones((5,5),np.uint8)

erosion = cv2.erode(img,kernel,iterations = 1)
dilation = cv2.dilate(img,kernel,iterations = 1)

cv2.imshow("Original Image",img)
cv2.imshow("Eroded image",erosion)
cv2.imshow("Dilated image",dilation)
cv2.waitkey(0)
cv2.destroyAllWindows()