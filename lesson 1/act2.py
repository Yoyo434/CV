import cv2
import matplotlib.pyplot as plt
print(cv2.__version__)

image=cv2.imread('Capture.png')
print(image.shape)

image_rgb=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

startpt=(50,50)
endpt=(1000,600)
color=(0,0,0)
thickness=5
img_rect=cv2.rectangle(image_rgb.copy(),startpt,endpt,color,thickness)

text='Annotated Image'
font=cv2.FONT_HERSHEY_SIMPLEX
font_scale=1
text_color=(0,0,0)
text_thickness=2
img_text=cv2.putText(img_rect.copy(),text,(50,40),font,font_scale,text_color,text_thickness,cv2.LINE_AA)

plt.imshow(img_text)
plt.show()