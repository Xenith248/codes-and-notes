import numpy as np
import cv2
import matplotlib.pyplot as plt
in_img=cv2.imread("images\image0.jpg",0)
m,n=in_img.shape
dct_cnt=dict()
dct_sk=dict()
for i in range(256):
    dct_cnt[i]=0
    dct_sk[i]=0
for i in range(m):
    for j in range(n):
        dct_cnt[in_img[i][j]]+=1
plt.bar(list(dct_cnt.keys()),list(dct_cnt.values()))
plt.show()

sum=0
for i in range(256):
    sum+=(dct_cnt[i]/(m*n))
    dct_sk[i]=np.round(sum*255)

out_img=np.zeros((m,n),dtype=np.uint8)
for i in range(m):
    for j in range(n):
        out_img[i][j]=dct_sk[in_img[i][j]]

for i in range(m):
    for j in range(n):
        dct_cnt[out_img[i][j]]+=1
plt.bar(list(dct_cnt.keys()),list(dct_cnt.values()))
plt.show()

cv2.imshow("input:",in_img)
cv2.imshow("Output:",out_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
