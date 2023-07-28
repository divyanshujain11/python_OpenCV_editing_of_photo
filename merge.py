#merge photo
import cv2
import numpy
cap=cv2.VideoCapture(0)
status,photo=cap.read()
cap.release()
photo=image1[150:400,200:450]
photo_resized = cv2.resize(photo, (200, 200))
photo[0:200,0:200,:]=photo_resized
cv2.imshow("merge_photo",photo)
cv2.waitKey(5000)
cv2.destroyAllWindows()
