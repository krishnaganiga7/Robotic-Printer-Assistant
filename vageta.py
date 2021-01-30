import cv2
import matplotlib
import numpy
import numpy as np
from matplotlib import pyplot as plt
import pytesseract

def ResizeWithAspectRatio(image, width=None, height=None, inter=cv2.INTER_AREA):
    dim = None
    (h, w) = image.shape[:2]

    if width is None and height is None:
        return image
    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)
    else:
        r = width / float(w)
        dim = (width, int(h * r))

    return cv2.resize(image, dim, interpolation=inter)

img = cv2.imread('one.png',cv2.IMREAD_GRAYSCALE)
img=ResizeWithAspectRatio(img,width=468)
fromCenter = False
r = cv2.selectROI(img, fromCenter)
imCrop = img[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]
text=pytesseract.image_to_string(imCrop)
print(text[0])
