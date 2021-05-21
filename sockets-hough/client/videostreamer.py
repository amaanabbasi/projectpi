import io
import socket
import struct
import time 
import cv2
import pickle
import sys
# from camera.camera import Camera

HOST_IP = "192.168.0.107"
HOST_PORT = 8000
# create socket and bind host
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

clientsocket.connect((HOST_IP, HOST_PORT))
connection = clientsocket.makefile('wb')
print("Connection Established")
print(f"Server's addr: {HOST_IP}, port {HOST_PORT}")
print("Streaming Video from usb cam")

cap=cv2.VideoCapture(0)

# used to record the time when we processed last frame 
prev_frame_time = 0
# used to record the time at which we processed current frame 
new_frame_time = 0
try:
    while True:
        ret,frame=cap.read()
        frame = cv2.resize(frame, (200, 200))

        ############ CALCULATING FPS ##################
        new_frame_time = time.time()
        # Calculating the fps 
        # fps will be number of frame processed in given time frame 
        # since their will be most of time error of 0.001 second 
        # we will be subtracting it to get more accurate result
        fps = 1/(new_frame_time-prev_frame_time)
        prev_frame_time = new_frame_time
        fps = int(fps)

        
        # frame = camera.get_frame()
        # Serialize frame
        data = pickle.dumps(frame)

        # Send message length first
        message_size = struct.pack("=L", len(data)) ### CHANGED
        
        print(f"FPS {fps} size of data {sys.getsizeof(data)} frame shape {frame.shape}")
        # Then data
        
        clientsocket.sendall(message_size + data)


finally:
    print("closing")
    connection.close()
    clientsocket.close()