import carmotioncontrol
from config import *
import sys, termios, time, tty
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

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

if __name__ == '__main__':

    while True:

        char = getch()
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
        
        if (char == 'h'):
            car.speed()

        if (char == 'e'):
            car.exit()


        