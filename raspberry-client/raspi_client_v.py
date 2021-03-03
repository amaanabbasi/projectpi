import io
import socket
import struct
import time 
import cv2
import pickle
# from camera.camera import Camera

HOST_IP = "192.168.0.105"
HOST_PORT = 8000
# create socket and bind host
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect((HOST_IP, HOST_PORT))
connection = clientsocket.makefile('wb')
cap=cv2.VideoCapture(0)

# used to record the time when we processed last frame 
prev_frame_time = 0
# used to record the time at which we processed current frame 
new_frame_time = 0
try:
    while True:
        ret,frame=cap.read()
        frame = cv2.resize(frame, (480, 200))

        ############ CALCULATING FPS ##################
        new_frame_time = time.time()
        # Calculating the fps 
        # fps will be number of frame processed in given time frame 
        # since their will be most of time error of 0.001 second 
        # we will be subtracting it to get more accurate result
        fps = 1/(new_frame_time-prev_frame_time)
        prev_frame_time = new_frame_time
        fps = int(fps)
        
        print(fps)
        # frame = camera.get_frame()
        # Serialize frame
        data = pickle.dumps(frame)

        # Send message length first
        message_size = struct.pack("=L", len(data)) ### CHANGED
        
        # Then data
        clientsocket.sendall(message_size + data)
        
finally:
    connection.close()
    clientsocket.close()