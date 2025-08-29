import cv2
import numpy as np
import numpy as np
gma=float(input("Enter the gamma value: "))
in_img=cv2.imread("dark_img.jpg",0)
m,n=in_img.shape
c=(255/((1+np.max(in_img))**gma))
out_img=np.zeros((m,n),dtype=np.uint8)
for i in range(m):
    for j in range(n):
        out_img[i][j]=c*in_img[i][j]**gma

cv2.imshow("Input",in_img)
cv2.imshow("Output",out_img)
