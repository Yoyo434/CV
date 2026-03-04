import cv2
print("OpenCV Version:",cv2.__version__)
img=cv2.imread('Capture.PNG')

print(img.shape)

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


cv2.imshow('Gray Image',gray)

canny_image=cv2.Canny(gray,100,200)
cv2.imshow('Canny image',canny_image)

#cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()