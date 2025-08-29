import cv2
import numpy as np

# Load the image
img = cv2.imread('images\i (1).jpeg',0)
# Generate random Gaussian noise
mean = 0
stddev = 180
noise = np.zeros(img.shape, np.uint8)
cv2.randn(noise, mean, stddev)
# Add noise to image
noisy_img = cv2.add(img, noise)
cv2.imshow('original image',img)
cv2.imshow('noisy img', noisy_img)
img=noisy_img
L,W=img.shape

def create_mask(n):
    mask=np.zeros((n,n))
    m=(n//2)+1
    for i in range(m):
        val=2**i
        for j in range(m):
            mask[i][j]=val
            mask[n-i-1][j]=val
            val*=2
        val//=2
        for j in range(m,n):
            val//=2
            mask[i][j]=val
            mask[n-i-1][j]=val
    return mask,np.ones((n,n))

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

#correlation
def blur(n,img):
    img=padding(n,img)
    mask,mask_1=create_mask(n)
    out_img=np.zeros((L,W),dtype='uint8')
    out_img_1=np.zeros((L,W),dtype='uint8')
    for i in range(L):
        for j in range(W):
            img_seg=np.zeros((n,n))
            for a in range(i,i+n):
                for b in range(j,j+n):
                    img_seg[a-i][b-j]=img[a][b]
            out_img[i][j]=(np.sum(img_seg*mask))//(np.sum(mask))
            out_img_1[i][j]=(np.sum(img_seg*mask_1))//(np.sum(mask_1))
    
    cv2.imshow('Output {} N4'.format(n),out_img)
    cv2.imshow('Output {} ones'.format(n),out_img_1)

blur(3,img)
blur(5,img)
blur(9,img)
