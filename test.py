import numpy as np
import cv2

cap = cv2.VideoCapture(0)

def drawPolygon(frame, *points):
    for i in xrange(points[0], points[2]):
        for j in xrange(points[1], points[3]):
            frame[i,j] = [255,255,255]

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    #drawPolygon(frame, 10, 20, 150, 250)
    pts1 = np.float32([[156,65],[268,52],[28,387],[389,390]])
    pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])

    M = cv2.getPerspectiveTransform(pts1,pts2)

    frame = cv2.warpPerspective(frame,M,(1300,1300))

    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
