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

def pNoise(img):
    noisy_img = np.copy(img)
    L,W=img.shape
    for i in range(L):
        for j in range(W):
            rand=rn.randint(1,10)
            if rand==10:
                noisy_img[i][j]=0
    return(noisy_img)

def spNoise(img):
    noisy_img = np.copy(img)
    L,W=img.shape
    for i in range(L):
        for j in range(W):
            rand=rn.randint(1,10)
            if rand==10:
                noisy_img[i][j]=0
            elif rand==9:
                noisy_img[i][j]=255
    return(noisy_img)

in_img=cv2.imread('lena.jpg',0)
l,w=in_img.shape[0],in_img.shape[1]
n=3

simg=sNoise(in_img)
pimg=pNoise(in_img)
spimg=spNoise(in_img)
s_out_img=np.zeros((l,w),dtype='uint8')
p_out_img=np.zeros((l,w),dtype='uint8')
sp_out_img=np.zeros((l,w),dtype='uint8')

for i in range(1,l-1):
    for j in range(1,w-1):
        s_img_seg=np.zeros((n,n),dtype=float)
        p_img_seg=np.zeros((n,n),dtype=float)
        sp_img_seg=np.zeros((n,n),dtype=float)
        for a in range(i-(n//2),i+((n//2)+1)):
            for b in range(j-1,j+2):
                s_img_seg[a-i+1][b-j+1]=simg[a][b]
                p_img_seg[a-i+1][b-j+1]=pimg[a][b]
                sp_img_seg[a-i+1][b-j+1]=spimg[a][b]
        s_out_img[i][j]=np.min(s_img_seg)
        p_out_img[i][j]=np.max(p_img_seg)
        sp_out_img[i][j]=np.median(sp_img_seg)

fig = plt.figure()
ax1 = fig.add_subplot(2,4,1)
ax1.imshow(in_img,cmap='gray')
ax2 = fig.add_subplot(2,4,2)
ax2.imshow(simg,cmap='gray')
ax3 = fig.add_subplot(2,4,3)
ax3.imshow(pimg,cmap='gray')
ax4 = fig.add_subplot(2,4,4)
ax4.imshow(spimg,cmap='gray')
ax5 = fig.add_subplot(2,4,6)
ax5.imshow(s_out_img,cmap='gray')
ax6 = fig.add_subplot(2,4,7)
ax6.imshow(p_out_img,cmap='gray')
ax7 = fig.add_subplot(2,4,8)
ax7.imshow(sp_out_img,cmap='gray')
plt.show()
        
