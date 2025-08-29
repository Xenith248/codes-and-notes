import cv2
import numpy as np
import matplotlib.pyplot as plt

def padding(m,img):
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

in_img=cv2.imread('lena.jpg',0)
l,w=in_img.shape[0],in_img.shape[1]
n=3
pd_img=padding((n//2)+1,in_img)

#Laplacian
#N4
N4=np.array([[0,1,0],[1,-4,1],[0,1,0]])
out_N4=np.zeros((l,w),dtype='uint8')

#N8
N8=np.array([[1,1,1],[1,-8,1],[1,1,1]])
out_N8=np.zeros((l,w),dtype='uint8')

for i in range(1,l-1):
    for j in range(1,w-1):
        img_seg=np.zeros((3,3))
        for a in range(i-1,i+2):
            for b in range(j-1,j+2):
                img_seg[a-i+1][b-j+1]=in_img[a][b]
        out_N4[i][j]=np.sum(img_seg*N4)
        out_N8[i][j]=np.sum(img_seg*N8)

fig = plt.figure()
ax1 = fig.add_subplot(2,2,1)
ax1.imshow(in_img,cmap='gray')
ax2 = fig.add_subplot(2,2,2)
ax2.imshow(pd_img,cmap='gray')
ax3 = fig.add_subplot(2,2,3)
ax3.imshow(out_N4,cmap='gray')
ax4 = fig.add_subplot(2,2,4)
ax4.imshow(out_N8,cmap='gray')
plt.show()
