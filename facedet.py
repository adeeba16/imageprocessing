import cv2

face_cascade = cv2.CascadeClassifier(r'C:\Users\PC PLANET\Desktop\PYTHON WORKSHOP\imageprocessing\classifiers/haarcascade_frontalface_default.xml')
img= cv2.imread(r'C:\Users\PC PLANET\Desktop\PYTHON WORKSHOP\imageprocessing/photo1.jpg',1)
grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#resize
# newimg = cv2.resize(img,(600,570))

scale_percent = 20 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
resized = cv2.resize(img, dim)
  

#image edge
# edge_img = cv2.Canny(img,100,200)

#gaussian blur
# blur_image1 = cv2.GaussianBlur(img, (7,7), 0)

# faces = face_cascade.detectMultiScale(grey_img,
# scaleFactor=1.05,
# minNeighbors=5)
# print(type(faces))
# print(faces)

# for x,y,w,h, in faces:
#     img = cv2.rectangle(img,(x,y),(x+w, y+w),(0,255,0),1)

# #cropping image
# cropped = img[y:y+h, x:x+w]
cv2.imshow("resize",resized)
# cv2.imshow("cropped window", cropped)
# cv2.imshow("grey image window",img)
# cv2.imshow("resized image window",newimg)
# cv2.imshow("Detected Edges", edge_img)
# cv2.imshow('Blur Image1', blur_image1)
# cv2.imshow('grey image',grey_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

