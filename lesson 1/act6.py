import cv2

try:
    face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
except FileExistsError:
    print("File does not load.")

else:
    cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT,480)


if not cap.isOpened():
    print("Error: Couldn't open camera")
    exit()

while True:
    ret , frame=cap.read()

    if not ret:
        print("Error:failed to capture image.")
        break
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    faces= face_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(30,30))

    for rect in faces:
        cv2.rectangle(frame,rect,(255,0,0),2)

    cv2.imshow("Face detection - press q to Quit",frame)

    if cv2.waitKey(1)& 0xFF==ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
