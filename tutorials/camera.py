import cv2

camera = cv2.VideoCapture(0)

while True:
    _, img = camera.read()


    cv2.imshow('frame', img)
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break 