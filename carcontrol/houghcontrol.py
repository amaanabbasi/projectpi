# Controlling the car using hough transform
# https://www.hackster.io/Abhinav_Abhi/road-lane-detection-with-raspberry-pi-a4711f#team
from run import forward, reverse, left, right, stop, hh

import time
import cv2
import numpy as np
import math
theta=0
minLineLength = 5
maxLineGap = 10
time.sleep(0.1)
camera = cv2.VideoCapture(0)
while True:
    _, image = camera.read()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edged = cv2.Canny(blurred, 85, 85)
    lines = cv2.HoughLinesP(edged,1,np.pi/180,10,minLineLength,maxLineGap)
    try:
        if(lines.any() !=None):
            for x in range(0, len(lines)):
                for x1,y1,x2,y2 in lines[x]:
                    cv2.line(image,(x1,y1),(x2,y2),(0,255,0),2)
                    theta=theta+math.atan2((y2-y1),(x2-x1))
    except AttributeError as error:
        pass


    #print(theta)GPIO pins were connected to arduino for servo steering control
    threshold=6
    print(theta)
    if(theta>threshold):
        left()
        print("left")
    if(theta<-threshold):
        right()
        print("right")
    if(abs(theta)<threshold):
        forward()
        print ("straight")
    theta=0
    cv2.imshow("Frame",image)
    key = cv2.waitKey(1) & 0xFF
    #    image.truncate(0)
    if key == ord("q"):
        exit()
        break