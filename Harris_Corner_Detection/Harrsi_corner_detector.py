import numpy as np
import cv2

file = 'E:\Github\Computer_vision\Harris_Corner_Detection\wood.png'

img = cv2.imread(file)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#cv2.cornerHarris accepts float32 gray image so first convert the gray image
gray = np.float32(gray)

dst = cv2.cornerHarris(gray,2,3,0)

#result is dilated for marking the corners, not important
dst = cv2.dilate(dst,None)

# Threshold for an optimal value, it may vary depending on the image.
img[dst>0.01*dst.max()]=[0,0,255]
cv2.imwrite("E:\Github\Computer_vision\Harris_Corner_Detection\wood_output.png",img)
cv2.imshow('dst',img)

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()