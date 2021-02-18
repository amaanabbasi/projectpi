import RPi.GPIO as GPIO
from time import sleep
import sys, termios, time, tty
GPIO.setmode(GPIO.BOARD)
 
MotorF = 16
MotorB = 18
MotorL = 11
MotorR = 13

 
GPIO.setup(MotorF,GPIO.OUT)
GPIO.setup(MotorB,GPIO.OUT)
GPIO.setup(MotorL,GPIO.OUT)
GPIO.setup(MotorR,GPIO.OUT)

#display user controls
print ('W forward')
print ('S Reverse')
print ('A Left')
print ('D Right')
print ('Q Stop')
print ('E Exit Programme')

# setting up the user input system
def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

print("Turning motor on")
def forward():
    
    print ('W forward')
    GPIO.output(MotorF, True)
    GPIO.output(MotorB, False)

def reverse():

    print ('S Reverse')
    GPIO.output(MotorF, False)
    GPIO.output(MotorB, True)

def right():
    print ('D Right')
    GPIO.output(MotorR, True)
    GPIO.output(MotorL, False)

def left():
    print('A Left')
    GPIO.output(MotorR, False)
    GPIO.output(MotorL, True)
    
def stop():
    GPIO.output(MotorF, False)
    GPIO.output(MotorB, False)
    GPIO.output(MotorR, False)
    GPIO.output(MotorL, False)
 
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
