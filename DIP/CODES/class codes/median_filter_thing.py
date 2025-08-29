import cv2
import numpy as np
import random as rn

#padding
def padding(n,img):
    m=(n//2)+1
    for k in range(m-1):
        l,w=img.shape
        new_img=np.zeros((l+2,w+2),dtype='uint8')
        for i in range(1,l+1):
            for j in range(1,w+1):
                new_img[i][j]=img[i-1][j-1]
        new_img[0][0],new_img[0][w+1],new_img[l+1][0],new_img[l+1][w+1]=img[0][0],img[0][w-1],img[l-1][0],img[l-1][w-1]
        for i in range(l):
            new_img[i+1][0],new_img[i+1][w+1]=img[i][0],img[i][w-1]
        for j in range(w):
            new_img[0][j+1],new_img[l+1][j+1]=img[0][j],img[l-1][j]
        img=new_img
    return img

#Salt and Pepper noise
img = cv2.imread('lena.jpg',0)
noisy_img = np.copy(img)
L,W=img.shape
for i in range(L):
    for j in range(W):
        rand=rn.randint(1,5)
        if rand==4:
            noisy_img[i][j]=0
        elif rand==5:
            noisy_img[i][j]=255
cv2.imshow("Original image",img)
cv2.imshow("S & P noise",noisy_img)

n=7  #size of the filter
out_img=np.zeros((L,W),dtype='uint8')
in_img=padding(n,noisy_img)
for i in range(L):
    for j in range(W):
        img_seg=np.zeros((n,n))
        for a in range(i,i+n):
            for b in range(j,j+n):
                img_seg[a-i][b-j]=in_img[a][b]
        out_img[i][j]=np.median(img_seg)

cv2.imshow("median filter",out_img)
