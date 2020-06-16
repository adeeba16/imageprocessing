import cv2

eye_cascade = cv2.CascadeClassifier(r'C:\Users\PC PLANET\Desktop\PYTHON WORKSHOP\imageprocessing\classifiers/haarcascade_eye.xml')
img= cv2.imread(r'C:\Users\PC PLANET\Desktop\PYTHON WORKSHOP\imageprocessing/photo1.jpg',1)
grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

eyes = eye_cascade.detectMultiScale(grey_img,
scaleFactor=2.05,
minNeighbors=2)
print(type(eyes))
print(eyes)
for x,y,w,h, in eyes:
    img = cv2.rectangle(img,(x,y),(x+w, y+w),(0,255,0),3)
    
cv2.imshow("grey image window",img)
cv2.waitKey(0)
cv2.destroyAllWindows()