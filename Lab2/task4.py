# importing opencv
import cv2

# reading the images
start = cv2.imread('task2.png')
dilation = cv2.imread('dimadilation.jpg')

# subtract the images
subtracted = cv2.subtract(dilation, start)

# TO show the output
cv2.imshow('image', subtracted)

# To close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
