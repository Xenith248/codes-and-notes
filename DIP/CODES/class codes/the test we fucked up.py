import cv2
import numpy as np
img=np.zeros((500,500),dtype='uint8')
out_img=np.zeros((500,500),dtype='uint8')
shift=50
count=0
col=1
for i in range(100,200):
    if count==2:
        count=0
        shift-=1
    for j in range(col):
        img[i][j+shift+100]=255
    col+=1
    count+=1
cv2.imshow("original img",img)

tx=50
ty=100
bt=np.array([[1,0,-tx],[0,1,-ty],[0,0,1]]) #Backward warping function


#Backward warping
for i in range(500):
    for j in range(500):
        ip=np.array([[i],[j],[1]])
        op=bt@ip
        try:
            out_img[i][j]=img[op[0][0]][op[1][0]]
        except IndexError:
            pass

cv2.imshow("Output", out_img)
