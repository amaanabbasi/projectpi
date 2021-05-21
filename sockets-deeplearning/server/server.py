import pickle
import socket
import struct
import numpy as np
import cv2
import datetime, os, sys
from keras.models import load_model
from keras.preprocessing.image import img_to_array
# example of loading an image with the Keras API
import numpy as np

model = load_model("../../../projectpi-train/car-10-0.0001-adam.h5")

HOST_IP, HOST_PORT = '192.168.0.110', 8001
ser_soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ser_soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ser_soc.bind((HOST_IP, HOST_PORT))
ser_soc.listen(20)
conn, address = ser_soc.accept()

print("Connection Established")
print(f"Server's addr: {HOST_IP}, port {HOST_PORT}")
print("Waiting for video stream.")

def server_program(data):
    # receive data stream. it won't accept data packet greater than 1024 bytes
    data = str(data)
    print(f"{data} {type(data)}command data size: {sys.getsizeof(data)}")
    conn.send(data.encode())  # send data to the client
    # conn.send(data)

def preprocessing(frame):
    img_array = img_to_array(frame)
    img_array = np.expand_dims(img_array, axis=0)
    return img_array
    
def predict(frame):
    processed_frame = preprocessing(frame)
    prediction_arr = model.predict(processed_frame)
    prediction = np.argmax(prediction_arr)
    return prediction


class VideoStreamingTest(object):
    def __init__(self, host, port):

        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((host, port))
        self.server_socket.listen(10)
        self.connection, self.client_address = self.server_socket.accept()
        
        # self.connection = self.connection.makefile('rb')
        self.host_name = socket.gethostname()
        self.host_ip = socket.gethostbyname(self.host_name)

        self.data = b''
        self.payload_size = struct.calcsize("=L")
        self.streaming()

        print("Host: ", self.host_name + ' ' + self.host_ip)
        print("Connection from: ", self.client_address)
        print("Streaming...")
        print("Press 'q' to exit")

    def dataset(self, steering_angle, heading_image):
        deviation = steering_angle - 90
        error = abs(deviation)
        
        if deviation < 10 and deviation > -10:
            deviation = 0
            error = 0
            cv2.imwrite(os.path.join("dataset/0/", str(datetime.datetime.now().time()) + '.jpg'), heading_image)
        
        elif deviation > 10:
            cv2.imwrite(os.path.join("dataset/1/", str(datetime.datetime.now().time()) + '.jpg'), heading_image)

        elif deviation < -10:
            cv2.imwrite(os.path.join("dataset/-1/", str(datetime.datetime.now().time()) + '.jpg'), heading_image)


    def streaming(self):
        try:

            while True:
                # Retrieve message size
                while len(self.data) < self.payload_size:
                    self.data += self.connection.recv(2048)

                

                packed_msg_size = self.data[:self.payload_size]
                self.data = self.data[self.payload_size:]
                
                msg_size = struct.unpack("=L", packed_msg_size)[0] ### CHANGED

                # Retrieve all data based on message size
                while len(self.data) < msg_size:
                    self.data += self.connection.recv(4096)

                # print(f"size of image in bytes: {sys.getsizeof(self.data)}")
                
                frame_data = self.data[:msg_size]
                self.data = self.data[msg_size:]
                
               
                
                # Extract frame
                frame = pickle.loads(frame_data)
                prediction = predict(frame)
                try:
                    server_program(prediction)
                except Exception as e:
                    print(e)
                # heading_image = display_heading_line(lane_lines_image, steering_angle)
                # self.dataset(steering_angle, heading_image)
                # Display
                cv2.imshow('frame', frame)
                # cv2.imwrite(os.path.join("dataset/", str(datetime.datetime.now().time()) + '.jpg'), heading_image)
                cv2.waitKey(1)

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break   
        finally:
            self.connection.close()
            self.server_socket.close()


# host, port for video streaming
h, p = HOST_IP, 8000
VideoStreamingTest(h, p)




