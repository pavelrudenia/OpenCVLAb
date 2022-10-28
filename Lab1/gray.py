import cv2

# read image
img_grey = cv2.imread('img.png', cv2.IMREAD_GRAYSCALE)

cv2.imshow('gray', img_grey)

cv2.waitKey(0)
