import socket
import math
import sys
import time
import RPi.GPIO as GPIO
from carcontrol.carmotioncontrol import CarMotionControl
from carcontrol.config import *

HOST_IP = "192.168.0.110"
HOST_PORT = 8001

def client_program(car):
    
    cli_soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # instantiate
    cli_soc.connect((HOST_IP, HOST_PORT))
    print("Connection Established")
    print(f"Server's addr: {HOST_IP}, port {HOST_PORT}")
    print("Waiting for commands.")
    # flag = input("Turn ignition on? (Y)")
    try:
        while True:
            
            data = cli_soc.recv(52).decode()  # receive response

            # print(f"Received from server:  steering angle {data}")  # show in terminal

            direction = int(data) 
            
            if direction == 1:
                deviation = 0
                error = 0
                car.start()
                car.steeringsstop() # x -> stop steering

            elif direction == 2:
                car.start()
                car.right() # x -> right
                

            elif direction == 0:
                car.start()
                car.left() # x -> left

  
            car.forward()
            # throttle.start(spd)

            
        
    finally: 
        print("Closing Connection, Releasing GPIO")
        cli_soc.close()  # close the connection
        car.exit()
        f.close()
        

    
if __name__ == '__main__':
    GPIO.setwarnings(False)

    car = CarMotionControl(MotorF, MotorB, MotorR, MotorL)

    client_program(car)
    
    
    
