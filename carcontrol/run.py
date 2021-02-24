import carmotioncontrol
from config import *

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
def exit():
    car.exit()
def speed():
    car.speed()


if __name__ == '__main__':

    while True:
        if (char == "w"):
            car.forward()

        if (char == 's'):
            car.reverse()

        if (char == 'a'):
            car.left()   

        if (char == 'd'):
            car.right()
        
        if (char == 'p'):
            car.stop()
        
        if (chat == 'h'):
            car.speed()

        if (char == 'e'):
            car.exit()


        