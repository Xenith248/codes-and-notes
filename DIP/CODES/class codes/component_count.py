import cv2
import numpy as np
in_img=cv2.imread("objects.jpg",0)
m,n=in_img.shape
cv2.imshow("The image", in_img)

dct_ct=dict()
dct_rep=dict()
pix=[]
count=0
flag=0
for i in range(m):
    for j in range(n):
        if in_img[i][j]>127:
            pix.append((i,j))
            if ((i-1,j) not in pix) and ((i,j-1) not in pix):
                count+=1
                dct_ct[(i,j)]=count
            elif ((i-1,j) in pix) and ((i,j-1) not in pix):
                dct_ct[(i,j)]=dct_ct[(i-1,j)]
            elif ((i-1,j) not in pix) and ((i,j-1) in pix):
                dct_ct[(i,j)]=dct_ct[(i,j-1)]
            else:
                dct_ct[(i,j)]=dct_ct[(i-1,j)]
                if dct_ct[(i-1,j)]!=dct_ct[(i,j-1)]:
                    flag=1
                    dct_rep[dct_ct[(i-1,j)]]=dct_ct[(i,j-1)]

if flag==1:
    for i in list(dct_rep.keys()):
        count-=1
        for j in pix:
            if dct_ct[j]==dct_rep[i]:
                dct_ct[j]=dct_rep[i]

print("The number of objects in the image:",count)
