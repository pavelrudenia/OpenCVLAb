from cvzone.FaceMeshModule import FaceMeshDetector
import cv2

cap = cv2.VideoCapture(0)
detector = FaceMeshDetector(maxFaces=3)
while True:
     success, img = cap.read()
     img, faces = detector.findFaceMesh(img)
     if faces:
         cv2.imshow("Image", img)
     if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()