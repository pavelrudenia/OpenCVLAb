import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('img_3.png')

img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)

# equalize the histogram of the Y channel
img_yuv[:, :, 0] = cv2.equalizeHist(img_yuv[:, :, 0])

# convert the YUV image back to RGB format
img_output = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)

cv2.imshow('Color input image', img)
plt.hist(img_yuv.ravel(), 256, [0, 256])
plt.show()
cv2.imshow('Histogram equalized', img_output)
plt.hist(img_output.ravel(), 256, [0, 256])
plt.show()
cv2.waitKey(0)
