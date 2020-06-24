import numpy as np
import cv2 as cv
import imutils
cap = cv.VideoCapture('E:\Github\Computer_vision\Background_Substraction\People Walking.mp4')

#kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (3,3))
#fgbg = cv.bgsegm.createBackgroundSubtractorMOG()
#fgbg = cv.bgsegm.BackgroundSubtractorGMG()
fgbg = cv.createBackgroundSubtractorMOG2(history=100, varThreshold=50, detectShadows=True)
#fgbg = cv.createBackgroundSubtractorKNN(history=100, varThreshold=50, detectShadows=True)
while True:
    ret, frame = cap.read()
    frame=imutils.resize(frame,width=400)
    frame=imutils.resize(frame,height=500)
    if frame is None:
        break
    fgmask = fgbg.apply(frame)
    fgmask=imutils.resize(fgmask,width=400)
    fgmask=imutils.resize(fgmask,height=500)
    #fgmask = cv.morphologyEx(fgmask, cv.MORPH_OPEN, kernel)

    cv.imshow('Frame', frame)
    cv.imshow('FG MASK Frame', fgmask)

    keyboard = cv.waitKey(30)
    if keyboard == 'q' or keyboard == 27:
        break
cap.release()
cv.destroyAllWindows()