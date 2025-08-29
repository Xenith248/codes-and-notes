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

for i in range(1,l-1):
    for j in range(1,w-1):
        img_seg=np.zeros((3,3))
        for a in range(i-1,i+2):
            for b in range(j-1,j+2):
                img_seg[a-i+1][b-j+1]=in_img[a][b]
        out_N4[i][j]=np.sum(img_seg*N4)

c=1
out_img=in_img+(c*out_N4)
fm=np.zeros((l,w),dtype='uint8')
fk=np.zeros((l,w),dtype='uint8')

for i in range(l):
    for j in range(w):
        fm[i][j]=out_img[i][j]-np.min(out_img)

for i in range(l):
    for j in range(w):
        fk[i][j]=fm[i][j]-np.max(fm)

fig = plt.figure()
ax1 = fig.add_subplot(2,3,1)
ax1.imshow(in_img,cmap='gray')
ax2 = fig.add_subplot(2,3,2)
ax2.imshow(cv2. Laplacian(in_img, cv2.CV_32F, 1),cmap='gray')
ax3 = fig.add_subplot(2,3,3)
ax3.imshow(out_N4,cmap='gray')
ax4 = fig.add_subplot(2,3,4)
ax4.imshow(out_img,cmap='gray')
ax5 = fig.add_subplot(2,3,5)
ax5.imshow(fm,cmap='gray')
ax6 = fig.add_subplot(2,3,6)
ax6.imshow(fk,cmap='gray')
plt.show()
