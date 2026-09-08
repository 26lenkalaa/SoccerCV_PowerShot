import cv2 as cv
import numpy as np
import os 

def openImage(path):
    return cv.imread(path)