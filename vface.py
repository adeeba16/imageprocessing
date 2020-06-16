import cv2

video = cv2.VideoCapture(r'C:\Users\PC PLANET\Desktop\PYTHON WORKSHOP\imageprocessing\faceDetection.mp4')
face_cascade = cv2.CascadeClassifier(r'C:\Users\PC PLANET\Desktop\PYTHON WORKSHOP\imageprocessing\classifiers\haarcascade_frontalface_default.xml')
# print(type(video))
# print(video)
check, img = video.read()
while(check == True):
    check, img = video.read()
    grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(grey_img,
    scaleFactor=1.25,
    minNeighbors=10)
    for x,y,w,h, in faces:
        img = cv2.rectangle(img,(x,y),(x+w, y+w),(0,255,0),3)

    cv2.imshow('video-first frame',img)
    # cv2.waitKey(1)
    key = cv2.waitKey(10)
    if (key == ord('q')):
        break
cv2.destroyAllWindows()
video.release()