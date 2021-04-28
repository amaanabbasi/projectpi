import socket
import math
import sys
import time
import RPi.GPIO as GPIO
from carcontrol.carmotioncontrol import CarMotionControl
from carcontrol.config import *

HOST_IP = "192.168.0.107"
HOST_PORT = 8001

def client_program(car):
    
    cli_soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # instantiate
    cli_soc.connect((HOST_IP, HOST_PORT))
    print("Connection Established")
    print(f"Server's addr: {HOST_IP}, port {HOST_PORT}")
    print("Waiting for commands.")
    f = open("commands.txt", "a")
    # flag = input("Turn ignition on? (Y)")
    try:
        while True:
            
            data = cli_soc.recv(52).decode()  # receive response

            # print(f"Received from server:  steering angle {data}")  # show in terminal

            steering_angle = int(data)    
            speed = 20
            lastTime = 0
            lastError = 0
            
            now = time.time()
            dt = now - lastTime

            kp = 0.4
            kd = kp * 0.65


            deviation = steering_angle - 90
            error = abs(deviation)
            
            
            
            

            if deviation < 10 and deviation > -10:
                deviation = 0
                error = 0
                car.steeringsstop()
                f.write("0\n") # x -> stop steering

            elif deviation > 10:
                car.start()
                car.right()
                f.write("1\n") # x -> right
                

            elif deviation < -10:
                car.start()
                car.left()
                f.write("-1\n") # x -> left

            derivative = kd * (error - lastError) / dt
            proportional = kp * error
            PD = int(speed + derivative + proportional)
            spd = abs(PD)
            # print(spd)
            
            if spd > 35:
                spd = 35
            
            car.forward()
            # throttle.start(spd)

            lastError = error
            lastTime = time.time()
            
        
    finally: 
        print("Closing Connection, Releasing GPIO")
        cli_soc.close()  # close the connection
        car.exit()
        f.close()
        

    
if __name__ == '__main__':
    GPIO.setwarnings(False)

    car = CarMotionControl(MotorF, MotorB, MotorR, MotorL)

    client_program(car)
    
    
    
