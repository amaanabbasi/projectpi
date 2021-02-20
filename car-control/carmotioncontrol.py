import RPi.GPIO as GPIO
from time import sleep
import sys, termios, time, tty

class CarMotionControl():

    def __init__(self, MotorR, MotorB, MotorF, MotorL):
        GPIO.setmode(GPIO.BOARD)
        
        self.MotorF =MotorF
        self.MotorB =MotorB
        self.MotorL =MotorL
        self.MotorR =MotorR

        GPIO.setup(self.MotorF, GPIO.OUT)
        GPIO.setup(self.MotorB, GPIO.OUT)
        GPIO.setup(self.MotorL, GPIO.OUT)
        GPIO.setup(self.MotorR, GPIO.OUT)


    #display user controls
    print ('W forward')
    print ('S Reverse')
    print ('A Left')
    print ('D Right')
    print ('Q Stop')
    print ('E Exit Programme')



    print("Turning motor on")
    def forward(self):
        
        print ('W forward')
        GPIO.output(MotorF, True)
        GPIO.output(MotorB, False)

    def reverse(self):

        print ('S Reverse')
        GPIO.output(MotorF, False)
        GPIO.output(MotorB, True)

    def right(self):
        print ('D Right')
        GPIO.output(MotorR, True)
        GPIO.output(MotorL, False)

    def left(self):
        print('A Left')
        GPIO.output(MotorR, False)
        GPIO.output(MotorL, True)
        
    def stop(self):
        GPIO.output(MotorF, False)
        GPIO.output(MotorB, False)
        GPIO.output(MotorR, False)
        GPIO.output(MotorL, False)


# setting up the user input system
def getch(self):
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

while True:
    char = getch()
    if(char == "w"):
        forward()
    if(char == "q"):
        stop()
    if(char == "s"):
        reverse()
    if(char == "a"):
        left()
    if(char == "d"):
        right()
    if(char == "e"):
        stop()
        print("Stopping motor")

    if(char == 'q'):
        print("Stopping motor")
        stop()
        GPIO.cleanup()
        quit()
