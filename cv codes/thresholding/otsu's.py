import cv2
import numpy as np
import matplotlib.pyplot as plt




# Load the image (grayscale)
image = cv2.imread('D:\Work\#1 Subjects\CV\cv codes\images\nani.jpg', cv2.IMREAD_GRAYSCALE)

# Calculate histogram
histogram = cv2.calcHist([image], [0], None, [256], [0, 256])

def Otsu(image, hist):
    mn = len(image) * len(image[0])
    pi = [h / mn for h in hist]
    mg = sum(i * pi[i] for i in range(len(pi)))
    sigb = []
    for k in range(1, len(hist) - 1):
        Pk = sum(pi[:k + 1])
        mk = sum(i * pi[i] for i in range(k + 1))
        if Pk == 0 or Pk == 1:
            sigb.append(0)
            continue
        sigbk = (((mg * Pk) - mk) ** 2) / (Pk * (1 - Pk))
        sigb.append(sigbk)
    kmax = sigb.index(max(sigb))
    return kmax


Otsu(image,histogram)