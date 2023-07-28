#color image
image3=cv2.imread("blank.jpg")
photo1_resized = cv2.resize(image3, (700, 500))
print(photo1_resized.shape)
#start
photo1_resized[0:1,:,] = [0]
#bird
for x in range(40,50,1):
    for y in range(300,330,x+1):
        photo1_resized[x:x+1,y:y+1,] = [0]
#road
photo1_resized[400:500,:,] = [0]
#road white strip
for x in range(0,700,100):photo1_resized[440:460,x:x+50,]=[255]
#poll
photo1_resized[250:400,20:22]=[0]
photo1_resized[250:252,3:40]=[0]
photo1_resized[247:253,0:6]=[0,0,255]
photo1_resized[247:253,37:43]=[0,0,255]
#building structure
photo1_resized[100:400,50:250]=[0,255,255]#BRG
#building window
for x in range(120,400,60):photo1_resized[x:x+30,65:130]=[36,x+28,237]
for x in range(120,400,60):photo1_resized[x:x+30,155:230]=[36,x+28,237]

#person
photo1_resized[390:400,270:271]=[0]
photo1_resized[390:400,274:275]=[0]

photo1_resized[389:390,266:278]=[0]

photo1_resized[380:390,265:266]=[0]
photo1_resized[380:390,277:278]=[0]

photo1_resized[385:386,260:265]=[0]
photo1_resized[385:386,277:282]=[0]

photo1_resized[379:380,266:278]=[0]

photo1_resized[373:379,270:271]=[0]
photo1_resized[373:379,274:275]=[0]

photo1_resized[372:373,270:274]=[0]

photo1_resized[375:378,273:274]=[36,28,237]

#poll
photo1_resized[250:400,300:302]=[0]
photo1_resized[250:252,280:320]=[0]
photo1_resized[247:253,277:283]=[0,0,255]
photo1_resized[247:253,317:323]=[0,0,255]

#glass building
photo1_resized[150:400,350:600]=[234,217,153]#BRG
for x in range(370,590,30):
    photo1_resized[150:400,x:x+1]=[0]
for x in range(180,400,30):
    photo1_resized[x:x+1,350:600]=[0]
#poll
photo1_resized[250:400,650:652]=[0]
photo1_resized[250:252,630:670]=[0]
photo1_resized[247:253,627:633]=[0,0,255]
photo1_resized[247:253,667:673]=[0,0,255]


cv2.imshow("divu",photo1_resized)
cv2.waitKey()
cv2.destroyAllWindows()
