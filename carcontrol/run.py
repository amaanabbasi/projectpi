import keyboard
import carcontrol.carmotioncontrol
from carcontrol.config import *

car = carmotioncontrol.CarMotionControl(MotorF, MotorB, MotorR, MotorL)


def forward():
    car.forward()
def reverse():
    car.reverse()
def left():
    car.left()
def right():
    car.right()
def stop():
    car.stop()



if __name__ == '__main__':

    while True:
        if keyboard.read_key() == 'w':
            car.forward()

        if keyboard.read_key() == 's':
            car.reverse()

        if keyboard.read_key() == 'a':
            car.left()   

        if keyboard.read_key() == 'd':
            car.right()
        
        if keyboard.read_key() == 'p':
            car.stop()
        
        if keyboard.read_key() == 'esc' or 'ctrl+c':
            car.exit()

        