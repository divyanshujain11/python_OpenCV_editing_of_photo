#black glass image 
cap=cv2.VideoCapture(0)
status,photo2=cap.read()
cap.release()
image2=photo2
blCK_GLS=cv2.imread("black_sunglass.jpg")
photo2=blCK_GLS[200:450,800:1450,]
# print(numpydata.shape)
photo2_resized = cv2.resize(photo2, (200, 50))
image2[200:250,320:520,:]=photo2_resized
cv2.imshow("merge_photo_sunglass",image2)
cv2.waitKey()
cv2.destroyAllWindows()
