import cv2
import numpy as np
in_img=cv2.imread("images\image0.jpg",0)
m,n=in_img.shape
out_img=np.zeros((m,n),dtype=np.uint8)
for i in range(m):
    for j in range(n):
        out_img[i][j]=255-in_img[i][j]

cv2.imshow("Input",in_img)
cv2.imshow("Output",out_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

