import cv2
import numpy as np
import matplotlib.pyplot as plt

def gaussNoise(img):
    mean = 0
    stddev = 25
    noise = np.zeros(img.shape, np.uint8)
    cv2.randn(noise, mean, stddev)
    # Add noise to image
    noisy_img = cv2.add(img, noise)
    return noisy_img

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

img=gaussNoise(in_img)
ar_img=np.zeros((l,w),dtype='uint8')
geo_img=np.zeros((l,w),dtype='uint8')

ar_fil=np.array([[1,1,1],[1,1,1],[1,1,1]])

for i in range(1,l-1):
    for j in range(1,w-1):
        img_seg=np.zeros((n,n))
        for a in range(i-(n//2),i+((n//2)+1)):
            for b in range(j-1,j+2):
                img_seg[a-i+1][b-j+1]=img[a][b]
        ar_img[i][j]=(np.sum(img_seg*ar_fil))//(n**2)
        geo_img[i][j]=np.round(np.power(np.prod(img_seg),(1/n**2)))

fig = plt.figure()
ax1 = fig.add_subplot(2,2,1)
ax1.imshow(in_img,cmap='gray')
ax2 = fig.add_subplot(2,2,2)
ax2.imshow(img,cmap='gray')
ax3 = fig.add_subplot(2,2,3)
ax3.imshow(ar_img,cmap='gray')
ax4 = fig.add_subplot(2,2,4)
ax4.imshow(geo_img,cmap='gray')
plt.show()
