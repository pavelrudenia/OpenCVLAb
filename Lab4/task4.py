import cv2
import numpy as np

def getSlopeOfLine(line):
    xDis = line[0][2] - line[0][0]
    if (xDis == 0):
        return None
    return (line[0][3] - line[0][1]) / xDis

if __name__ == '__main__':
    inputFileName = 'img_3.png'
    img = cv2.imread(inputFileName)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    lines = cv2.HoughLinesP(gray, 1, np.pi / 180, 100, 30, 2)

    parallelLines = []
    for a in lines:
        for b in lines:
            if a is not b:
                slopeA = getSlopeOfLine(b)
                slopeB = getSlopeOfLine(b)
                if slopeA is not None and slopeB is not None:
                    if 0 <= abs(slopeA - slopeB) <= 0.6:
                        parallelLines.append({'lineA': a, 'lineB': b})

    for pairs in parallelLines:
        lineA = pairs['lineA']
        lineB = pairs['lineB']

        leftx, boty, rightx, topy = lineA[0]
        cv2.line(img, (leftx, boty), (rightx, topy), (0, 0, 255), 2)

    cv2.imshow('linesImg', img)
    cv2.waitKey(0)