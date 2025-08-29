import cv2
import numpy as np
import numpy as np
in_img=cv2.imread("dark_img.jpg",0)
m,n=in_img.shape
out_img=np.zeros((m,n),dtype=np.uint8)
c=(255/(np.log2(1+np.max(in_img))))
for i in range(m):
    for j in range(n):
        out_img[i][j]=c*np.log2(1+in_img[i][j])

cv2.imshow("Input",in_img)
cv2.imshow("Output",out_img)
