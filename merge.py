#merge photo
import cv2
import numpy
cap=cv2.VideoCapture(0)
status,image1=cap.read()
cap.release()
photo1=image1[150:400,200:450]
photo1_resized = cv2.resize(photo1, (200, 200))
image1[0:200,0:200,:]=photo1_resized
cv2.imshow("merge_photo",image1)
cv2.waitKey(5000)
cv2.destroyAllWindows()
