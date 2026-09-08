import cv2 as cv
import numpy as np
import os 

def openImage(path):
    return cv.imread(path)

def main():
    if main.__name__ == "__main__":
        fileName = input("Enter the image file name: ")
        openImage(fileName)
