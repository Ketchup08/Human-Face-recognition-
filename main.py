import cv2

faces_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img=cv2.imread("img4.jpg")
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces=faces_cascade.detectMultiScale(gray_img,scaleFactor=1.05,minNeighbors=5)

for x,y,w,h in faces:
    img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),4)

resized=cv2.resize(img,(int(img.shape[1]/3),int(img.shape[0]/3)))

cv2.imshow("new",resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
