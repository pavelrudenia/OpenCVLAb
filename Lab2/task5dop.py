import cv2
import numpy as np
kernel = np.ones((5, 5), np.uint8)
#read image
img_grey = cv2.imread('task2.png')

# define a threshold, 128 is the middle of black and white in grey scale
thresh = 128

# assign blue channel to zeros
img_binary = cv2.threshold(img_grey, thresh, 255, cv2.THRESH_BINARY)[1]
img_dilation = cv2.dilate(img_binary, kernel, iterations=1)
#save image
cv2.imwrite('task5.png', img_dilation)
cv2.imshow('image', img_dilation)

# reading the images
start = cv2.imread('task2.png')
# subtract the images
subtracted = cv2.subtract(img_dilation, start)

# TO show the output
cv2.imshow('image', subtracted)

# To close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
