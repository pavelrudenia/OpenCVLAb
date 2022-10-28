import cv2

# read image
img_color = cv2.imread('img.png', cv2.COLOR_RGB2GRAY)

cv2.imshow('color', img_color)

cv2.waitKey(0)