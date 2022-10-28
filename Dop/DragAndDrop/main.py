import cv2
from Dop.DragAndDrop import DragAndDrop as htm
import cvzone
import numpy as np

cap = cv2.VideoCapture(0)

cap.set(3, 1580)
cap.set(4, 1080)

detector = htm.handDetector(detectionCon=0.8)
colorR = (255, 0, 255)

cx, cy, w, h = 100, 100, 200, 200


class DragAndDrogRectangle():
    def __init__(self, posCenter, size=[60, 60]):
        self.posCenter = posCenter
        self.size = size

    def update(self, cursor):
        cx, cy = self.posCenter
        w, h = self.size

        # If the index finger tip is in rectangle region
        if cx - w // 2 < cursor[0] < cx + w // 2 and cy - h // 2 < cursor[
            1] < cy + h // 2:
            self.posCenter = cursor


rectList = []
for x in range(10):
    rectList.append(DragAndDrogRectangle([x * 96 + 30, 50]))

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    img = detector.findHands(img)
    lmList, _ = detector.findPosition(img)

    if len(lmList) != 0:
        length, _, _ = detector.findDistance(8, 12, img, draw=False)
        if length < 40:
            cursor = lmList[8][1:]  # index finger tip landmark
            # call the update
            for rect in rectList:
                rect.update(cursor)

    # Draw
    imgNew = np.zeros_like(img, np.uint8)
    for rect in rectList:
        cx, cy = rect.posCenter
        w, h = rect.size
        cv2.rectangle(imgNew, (cx - w // 2, cy - h // 2),
                      (cx + w // 2, cy + h // 2), colorR, cv2.FILLED)
        cvzone.cornerRect(imgNew, (cx - w // 2, cy - h // 2, w, h),10, rt=0,colorC=(0,255,0))

    out = img.copy()
    alpha = 0.1
    mask = imgNew.astype(bool)
    out[mask] = cv2.addWeighted(img, alpha, imgNew, 1 - alpha, 0)[mask]

    res = cv2.resize(out, dsize=(1500, 700), interpolation=cv2.INTER_CUBIC)
    cv2.imshow("Image", res)
    cv2.waitKey(1)