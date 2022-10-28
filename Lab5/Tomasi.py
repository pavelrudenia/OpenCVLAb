import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('img_3.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_blank = np.zeros(img.shape)
corners = cv2.goodFeaturesToTrack(gray, 3000, 0.01, 10)
corners = np.int0(corners)

for i in corners:
    x, y = i.ravel()
    cv2.circle(img_blank, (x, y), 5, (0, 210, 0), -1)

img = cv2.resize(img, dsize=(1200, 700), interpolation=cv2.INTER_CUBIC)
cv2.imshow("BASE", img)
img_blank = cv2.resize(img_blank, dsize=(1200, 700),
                       interpolation=cv2.INTER_CUBIC)
cv2.imshow('Image with Borders2', img_blank)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
# plt.imshow(img)
# plt.show()
