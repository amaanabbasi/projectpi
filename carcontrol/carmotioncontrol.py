import RPi.GPIO as GPIO
from time import sleep
import sys, termios, time, tty

class CarMotionControl():

    def __init__(self, self.MotorR, self.MotorB, self.MotorF, self.MotorL):
        GPIO.setmode(GPIO.BOARD)
        
        self.self.MotorF =self.MotorF
        self.self.MotorB =self.MotorB
        self.self.MotorL =self.MotorL
        self.self.MotorR =self.MotorR

        GPIO.setup(self.self.MotorF, GPIO.OUT)
        GPIO.setup(self.self.MotorB, GPIO.OUT)
        GPIO.setup(self.self.MotorL, GPIO.OUT)
        GPIO.setup(self.self.MotorR, GPIO.OUT)


    #display user controls
    print ('W forward')
    print ('S Reverse')
    print ('A Left')
    print ('D Right')
    print ('P Pause')
    print ('esc or ctrl+c Exit Programme')



    print("Turning Motor on")
    def forward(self):
        
        print ('W forward')
        GPIO.output(self.MotorF, True)
        GPIO.output(self.MotorB, False)

    def reverse(self):

        print ('S Reverse')
        GPIO.output(self.MotorF, False)
        GPIO.output(self.MotorB, True)

    def right(self):
        print ('D Right')
        GPIO.output(self.MotorR, True)
        GPIO.output(self.MotorL, False)

    def left(self):
        print('A Left')
        GPIO.output(self.MotorR, False)
        GPIO.output(self.MotorL, True)
        
    def stop(self):
        print("Stop")
        GPIO.output(self.MotorF, False)
        GPIO.output(self.MotorB, False)
        GPIO.output(self.MotorR, False)
        GPIO.output(self.MotorL, False)
    
    def exit(self):
        print("Exiting")
        stop()
        GPIO.cleanup()
        quit()

