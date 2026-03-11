import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread("shapes.png")
plt.imshow(img)
plt.show()

hsv_img=cv2.cvtColor(img,cv2.COLOR_HSV2RGB)
plt.imshow(hsv_img)
plt.show()

lower_blue=np.array([65,0,0])
upper_blue=np.array([110,225,225])

mask=cv2.inRange(hsv_img,lower_blue,upper_blue)
plt.imshow(mask,cmap='gray')
plt.show()

result=cv2.bitwise_and(img,img,mask=mask)
plt.imshow(cv2.cvtColor(result,cv2.COLOR_BGR2RGB))
plt.show()