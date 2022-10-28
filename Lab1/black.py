import cv2

# read image
img_grey = cv2.imread('img.png', cv2.IMREAD_GRAYSCALE)

# define a threshold, 128 is the middle of black and white in grey scale
thresh = 60

# assign blue channel to zeros
img_binary = cv2.threshold(img_grey, thresh, 255, cv2.THRESH_BINARY)[1]

# save image
cv2.imwrite('black-and-white.png', img_binary)
cv2.imshow('black-and-white', img_binary)

cv2.waitKey(0)