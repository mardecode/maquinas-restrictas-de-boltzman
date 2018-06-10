import numpy as np
import cv2 as cv
import os

def read():
    i = []
    for f in os.listdir("images"):
        img = cv.imread("images/"+f,0)
        img2 = cv.resize(img, (50,50 ))
        res, tres = cv.threshold(img2,127,255,cv.THRESH_BINARY_INV)
        i.append(np.array(tres).flatten())
    return i
