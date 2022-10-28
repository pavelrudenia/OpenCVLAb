from cvzone.HandTrackingModule import HandDetector
import cv2

cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)
success,img=cap.read()
h,w,_=img.shape
detector = HandDetector(detectionCon=0.8,maxHands=2)


while True:
    success,img = cap.read()

    hands,img = detector.findHands(img)

    data=[]

    if hands:
        hand=hands[0]
        lmList=hand["lmList"]

        for lm in lmList:
            data.extend([lm[0],h - lm[1],lm[2]])

    res = cv2.resize(img, dsize=(1200, 700), interpolation=cv2.INTER_CUBIC)
    cv2.imshow("Image",res)
    cv2.waitKey(1)