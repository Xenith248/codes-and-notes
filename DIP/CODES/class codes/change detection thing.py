import cv2
import numpy as np

in_img=cv2.imread('lena.jpg',0)
l,w=in_img.shape[0],in_img.shape[1]

#Gradient filters
#Roberts
rob_x=np.array([[-1,0],[0,1]])
rob_y=np.array([[0,-1],[1,0]])
out_rob_x=np.zeros((l,w),dtype='uint8')
out_rob_y=np.zeros((l,w),dtype='uint8')

#Prewitt
prwt_x=np.array([[-1,-1,-1],[0,0,0],[1,1,1]])
prwt_y=np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
out_prwt_x=np.zeros((l,w),dtype='uint8')
out_prwt_y=np.zeros((l,w),dtype='uint8')

#Sobel
sbl_x=np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
sbl_y=np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
out_sbl_x=np.zeros((l,w),dtype='uint8')
out_sbl_y=np.zeros((l,w),dtype='uint8')

#Laplacian
#N4
N4=np.array([[0,1,0],[1,-4,1],[0,1,0]])
out_N4=np.zeros((l,w),dtype='uint8')

#N8
N8=np.array([[1,1,1],[1,-8,1],[1,1,1]])
out_N8=np.zeros((l,w),dtype='uint8')

cv2.imshow("Original image",in_img)
#change detection part
for i in range(1,l-1):
    for j in range(1,w-1):
        '''img_seg2=np.zeros((2,2))
        for a in range(i,i+2):
            for b in range(j,j+2):
                img_seg2[a-i][b-j]=in_img[a][b]'''
        img_seg3=np.zeros((3,3))
        for a in range(i-1,i+2):
            for b in range(j-1,j+2):
                img_seg3[a-i+1][b-j+1]=in_img[a][b]
        out_rob_x[i][j]=np.sum(img_seg2*rob_x)
        out_rob_y[i][j]=np.sum(img_seg2*rob_y)
        out_prwt_x[i][j]=np.sum(img_seg3*prwt_x)
        out_prwt_y[i][j]=np.sum(img_seg3*prwt_y)
        out_sbl_x[i][j]=np.sum(img_seg3*sbl_x)
        out_sbl_y[i][j]=np.sum(img_seg3*sbl_y)
        out_N4[i][j]=np.sum(img_seg3*N4)
        out_N8[i][j]=np.sum(img_seg3*N8)

#cv2.imshow("Robert x",out_rob_x)
#cv2.imshow("Robert y",out_rob_y)
#cv2.imshow("Robert",(np.abs(out_rob_y)+np.abs(out_rob_x)))
#cv2.imshow("Prewitt x",out_prwt_x)
#cv2.imshow("Prewitt y",out_prwt_y)
#cv2.imshow("Prewitt",(np.abs(out_prwt_y)+np.abs(out_prwt_x)))
#cv2.imshow("Sobel x",out_sbl_x)
#cv2.imshow("Sobel y",out_sbl_y)
cv2.imshow("Sobel",(np.abs(out_sbl_y)+np.abs(out_sbl_x)))
#cv2.imshow("N4",out_N4)
#cv2.imshow("N8",out_N8)
