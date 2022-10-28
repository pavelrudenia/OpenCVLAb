import cv2

import HandTrackingModule as htm
import numpy as np
import os


brushThickness = 25
eraserThickness = 100
xp,yp= 0,0
imgCanvas = np.zeros((720,1200,3),np.uint8)
folderPath = "Header"

myList = os.listdir(folderPath)
#print(myList)
overlayList = []
for imPath in myList:
    image = cv2.imread(f'{folderPath}/{imPath}')
    overlayList.append(image)
#print(len(overlayList))
header = overlayList[0]
drawColor = (255,0,255)


cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)

detector = htm.handDetector(detectionCon=0.85)

while True:
    success, img = cap.read()
    img = cv2.flip(img,1)
    img = detector.findHands(img)
    lmList = detector.findPosition(img,draw=False)

    if lmList:

        x1, y1 = lmList[8][1:]  # tip of index finger
        x2, y2 = lmList[12][1:]  # tip of middle finger

        # 3. Check which fingers are up

        fingers = detector.fingersUp()
        #print(fingers)


        if fingers[1] and fingers[2]:
            cv2.rectangle(img,(x1,y1-25),(x2,y2+25),drawColor,cv2.FILLED)
            xp,yp = 0,0
            print("Selection Mode")
            if y1 < 125:
                print(x1,y1)
                if 125<x1<225:
                    header = overlayList[0]
                    drawColor = (255,0,255)
                elif 275<x1<375:
                    header = overlayList[1]
                    drawColor = (255, 0, 0)
                elif 425<x1<500:
                    header = overlayList[2]
                    drawColor = (0, 255, 0)
                if 525<x1<650:
                    header = overlayList[3]
                    drawColor = (0, 0, 0)

        if fingers[1] and fingers[2]==False:
            cv2.circle(img,(x1,y1),15,drawColor,cv2.FILLED)
            print("Drawing Mode")
            if xp==0  and yp==0:
                xp,yp = x1,y1

            if drawColor == (0,0,0):
                cv2.line(img, (xp, yp), (x1, y1), drawColor, eraserThickness)
                cv2.line(imgCanvas, (xp, yp), (x1, y1), drawColor,
                         eraserThickness)
            else:
                cv2.line(img,(xp,yp),(x1,y1),drawColor,brushThickness)
                cv2.line(imgCanvas, (xp, yp), (x1, y1), drawColor, brushThickness)

            xp,yp = x1,y1

    imgGray = cv2.cvtColor(imgCanvas,cv2.COLOR_BGR2GRAY)
    _,imgInv = cv2.threshold(imgGray,58,255,cv2.THRESH_BINARY_INV)
    imgInv = cv2.cvtColor(imgInv,cv2.COLOR_GRAY2BGR)
    # img = cv2.bitwise_and(img,imgInv.shape)
    # img = cv2.bitwise_or(img, imgCanvas.shape)

    img[0:125,0:1280] = header

    #img = cv2.addWeighted(img,0.5,imgCanvas,0.5,0.0)

    cv2.imshow("Image",img)
    cv2.imshow("ImageCanvas",imgCanvas)
    cv2.waitKey(1)