#black glass image
import cv2
import numpy
cap=cv2.VideoCapture(0)
status,photo=cap.read()
cap.release()
image2=photo
blaCK_GLASS=cv2.imread("black_sunglass.jpg")
photo=blaCK_GLASS[200:450,800:1450,]
# print(numpydata.shape)
photo_resized = cv2.resize(photo, (200, 50))
photo[200:250,320:520,:]=photo_resized
cv2.imshow("merge_photo_sunglass",photo)
cv2.waitKey()
cv2.destroyAllWindows()
