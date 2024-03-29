import pickle
import socket
import struct
import numpy as np
import cv2
import math
import datetime, os



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

def detect_edges(frame):
    # filter for blue lane lines
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # cv2.imshow("HSV",hsv)
    lower_blue = np.array([90, 120, 0], dtype="uint8")
    upper_blue = np.array([150, 255, 255], dtype="uint8")
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    # cv2.imshow("mask",mask)

    # detect edges
    edges = cv2.Canny(mask, 50, 100)
    # cv2.imshow("edges",edges)

    return edges

def region_of_interest(edges):
    height, width = edges.shape
    mask = np.zeros_like(edges)

    # only focus lower half of the screen
    polygon = np.array([[
        (0, height),
        (0, height / 2),
        (width, height / 2),
        (width, height),
    ]], np.int32)

    cv2.fillPoly(mask, polygon, 255)

    cropped_edges = cv2.bitwise_and(edges, mask)
    cv2.imshow("roi", cropped_edges)

    return cropped_edges


def detect_line_segments(cropped_edges):
    rho = 1
    theta = np.pi / 180
    min_threshold = 10

    line_segments = cv2.HoughLinesP(cropped_edges, rho, theta, min_threshold,
                                    np.array([]), minLineLength=5, maxLineGap=150)

    return line_segments


def average_slope_intercept(frame, line_segments):
    lane_lines = []

    if line_segments is None:
        print("no line segments detected")
        return lane_lines

    height, width, _ = frame.shape
    left_fit = []
    right_fit = []

    boundary = 1 / 3
    left_region_boundary = width * (1 - boundary)
    right_region_boundary = width * boundary


    for line_segment in line_segments:
        for x1, y1, x2, y2 in line_segment:
            if x1 == x2:
                print("skipping vertical lines (slope = infinity")
                continue

            fit = np.polyfit((x1, x2), (y1, y2), 1)
            slope = (y2 - y1) / (x2 - x1)
            intercept = y1 - (slope * x1)

            if slope < 0:
                if x1 < left_region_boundary and x2 < left_region_boundary:
                    left_fit.append((slope, intercept))
            else:
                if x1 > right_region_boundary and x2 > right_region_boundary:
                    right_fit.append((slope, intercept))

    left_fit_average = np.average(left_fit, axis=0)
    if len(left_fit) > 0:
        lane_lines.append(make_points(frame, left_fit_average))

    right_fit_average = np.average(right_fit, axis=0)
    if len(right_fit) > 0:
        lane_lines.append(make_points(frame, right_fit_average))

    return lane_lines


def make_points(frame, line):
    height, width, _ = frame.shape

    slope, intercept = line

    y1 = height  # bottom of the frame
    y2 = int(y1 / 2)  # make points from middle of the frame down

    if slope == 0:
        slope = 0.1

    x1 = int((y1 - intercept) / slope)
    x2 = int((y2 - intercept) / slope)

    return [[x1, y1, x2, y2]]


def display_lines(frame, lines, line_color=(0, 255, 0), line_width=6):
    line_image = np.zeros_like(frame)

    if lines is not None:
        for line in lines:
            for x1, y1, x2, y2 in line:
                cv2.line(line_image, (x1, y1), (x2, y2), line_color, line_width)

    line_image = cv2.addWeighted(frame, 0.8, line_image, 1, 1)

    return line_image


def display_heading_line(frame, steering_angle, line_color=(0, 0, 255), line_width=5):
    heading_image = np.zeros_like(frame)
    height, width, _ = frame.shape

    steering_angle_radian = steering_angle / 180.0 * math.pi

    x1 = int(width / 2)
    y1 = height
    x2 = int(x1 - height / 2 / math.tan(steering_angle_radian))
    y2 = int(height / 2)

    cv2.line(heading_image, (x1, y1), (x2, y2), line_color, line_width)
    heading_image = cv2.addWeighted(frame, 0.8, heading_image, 1, 1)

    return heading_image


def get_steering_angle(frame, lane_lines):
    height, width, _ = frame.shape

    if len(lane_lines) == 2:
        _, _, left_x2, _ = lane_lines[0][0]
        _, _, right_x2, _ = lane_lines[1][0]
        mid = int(width / 2)
        x_offset = (left_x2 + right_x2) / 2 - mid
        y_offset = int(height / 2)

    elif len(lane_lines) == 1:
        x1, _, x2, _ = lane_lines[0][0]
        x_offset = x2 - x1
        y_offset = int(height / 2)

    elif len(lane_lines) == 0:
        x_offset = 0
        y_offset = int(height / 2)

    angle_to_mid_radian = math.atan(x_offset / y_offset)
    angle_to_mid_deg = int(angle_to_mid_radian * 180.0 / math.pi)
    steering_angle = angle_to_mid_deg + 90
    #print(steering_angle)
    
    return steering_angle

import sys

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

                edges = detect_edges(frame)
                roi = region_of_interest(edges)
                line_segments = detect_line_segments(roi)
                lane_lines = average_slope_intercept(frame, line_segments)
                lane_lines_image = display_lines(frame, lane_lines)
                steering_angle = get_steering_angle(frame, lane_lines) #pass value through socket
                # print(steering_angle)
                try:
                    server_program(steering_angle)
                except Exception as e:
                    print(e)
                heading_image = display_heading_line(lane_lines_image, steering_angle)
                # self.dataset(steering_angle, heading_image)
                # Display
                cv2.imshow('frame', heading_image)
<<<<<<< HEAD:sockets/server/server.py
                cv2.imwrite(os.path.join("dataset/", datetime.datetime.now().time() + '.jpg'), img)
=======
                # cv2.imwrite(os.path.join("dataset/", str(datetime.datetime.now().time()) + '.jpg'), heading_image)
>>>>>>> d76cec353c609dc0e1f4b2761ef15e1b245821cd:sockets-hough/server/server.py
                cv2.waitKey(1)

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break   
        finally:
            self.connection.close()
            self.server_socket.close()


# host, port for video streaming
h, p = HOST_IP, 8000
VideoStreamingTest(h, p)




