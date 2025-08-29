import cv2
import numpy as np
import matplotlib.pyplot as plt
import random as rn

def sNoise(img):
    noisy_img = np.copy(img)
    L,W=img.shape
    for i in range(L):
        for j in range(W):
            rand=rn.randint(1,10)
            if rand==10:
                noisy_img[i][j]=255
    return(noisy_img)

in_img=cv2.imread('lena.jpg',0)
l,w=in_img.shape[0],in_img.shape[1]
n=3

img=sNoise(in_img)
out_img=np.zeros((l,w),dtype='uint8')

for i in range(1,l-1):
    for j in range(1,w-1):
        img_seg=np.zeros((n,n),dtype=float)
        for a in range(i-(n//2),i+((n//2)+1)):
            for b in range(j-1,j+2):
                img_seg[a-i+1][b-j+1]=img[a][b]
        out_img[i][j]=(n**2)//(np.sum(img_seg**-1))

fig = plt.figure()
ax1 = fig.add_subplot(2,2,1)
ax1.imshow(in_img,cmap='gray')
ax2 = fig.add_subplot(2,2,2)
ax2.imshow(img,cmap='gray')
ax3 = fig.add_subplot(2,2,3)
ax3.imshow(out_img,cmap='gray')
plt.show()
