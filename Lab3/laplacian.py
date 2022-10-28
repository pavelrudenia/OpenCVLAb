import numpy as np
import cv2

kernelSize = 11  # Kernel Bluring size




cap = cv2.VideoCapture(0)
while (True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here

    frame = cv2.Laplacian(frame,cv2.CV_64F) # Laplacian edge detection


    # Display the resulting frame
    cv2.imshow('Laplacian', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # press q to quit
        break
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()