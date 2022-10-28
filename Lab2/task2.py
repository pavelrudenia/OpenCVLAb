import cv2

# read image
img_src = cv2.imread('task2.png')
# blur the image
img_rst = cv2.blur(img_src, (20, 20))
# save result image
cv2.imwrite('task2-1.png', img_rst)

img_rst = cv2.GaussianBlur(img_src, (5, 5), 0)
# save result image
cv2.imwrite('task2-2.png', img_rst)

img_rst = cv2.medianBlur(img_src, 5)
# save result image
cv2.imwrite('task2-3.png', img_rst)
