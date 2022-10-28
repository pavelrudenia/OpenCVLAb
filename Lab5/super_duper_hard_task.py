import numpy as np
import cv2
import imutils


def order_points(pts):
    # Initialize the coordinates of the 4 vertices of the rectangle
    rect = np.zeros((4, 2), dtype='float32')
    # Coordinate point summation x+y
    s = pts.sum(axis=1)
    # np.argmin(s) returns the serial number of the minimum value in s
    rect[0] = pts[np.argmin(s)]
    rect[2] = pts[np.argmax(s)]
    # diff is the next element minus the previous element y-x
    diff = np.diff(pts, axis=1)
    rect[1] = pts[np.argmin(diff)]
    rect[3] = pts[np.argmax(diff)]
    # Return the 4 coordinate points of the rectangle in order
    return rect


def perTran(image, pts):
    rect = order_points(pts)
    tl, tr, br, bl = rect
    # Calculate width
    widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
    widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
    maxWidth = max(int(widthA), int(widthB))
    # Calculate the height
    heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
    heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
    maxHeight = max(int(heightA), int(heightB))
    # Define the size of the new image after transformation
    dst = np.array([[7, 0], [maxWidth - 1, 0], [maxWidth - 1, maxHeight - 1],
                    [0, maxHeight - 1]], dtype='float32')
    # Transformation matrix
    M = cv2.getPerspectiveTransform(rect, dst)
    # Perspective transformation
    warped = cv2.warpPerspective(image, M, (maxWidth, maxHeight))
    return warped


def main():
    image = cv2.imread('img_5.png')
    output = image.copy()
    # Convert to grayscale imag
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Bilateral filter can achieve smooth denoising and at the same time preserve edges well
    gray = cv2.bilateralFilter(gray, 11, 17, 17)
    # Detect edges
    edged = cv2.Canny(gray, 30, 200)
    # cv2.imshow('Canny', edged)
    # Find contour
    cnts = cv2.findContours(edged.copy(), cv2.RETR_TREE,
                            cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    # Get the top 3 largest contours
    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:3]

    screenCnt = None
    for c in cnts:
        # Contour circumference
        peri = cv2.arcLength(c, True)
        print('arcLength : {:.3f}'.format(peri))
        # The main function of # approxPolyDP is to polyline a continuous smooth curve and perform polygon fitting on the contour points of the image.
        # Approximate contour polygonal curve, approximation accuracy is 1.5% of contour circumference
        approx = cv2.approxPolyDP(c, 0.015 * peri, True)
        # The rectangular border has 4 points, and the others are eliminated
        if len(approx) == 4:
            screenCnt = approx
            break
    # Draw outline rectangle border
    cv2.drawContours(image, [screenCnt], -1, (0, 0, 255), 77)
    # Adjust to x,y coordinate point matrix
    pts = screenCnt.reshape(4, 2)
    # print('screenCnt.reshape:\n{}'.format(pts))
    # Perspective transformation
    warped = perTran(output, pts)
    image = cv2.resize(image, dsize=(1500, 700),
                       interpolation=cv2.INTER_CUBIC)
    output = cv2.resize(output, dsize=(1500, 700),
                        interpolation=cv2.INTER_CUBIC)
    warped = cv2.resize(warped, dsize=(1500, 700),
                        interpolation=cv2.INTER_CUBIC)
    cv2.imshow('warped', warped)
    cv2.imshow('image', image)
    cv2.imshow('output', output)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
