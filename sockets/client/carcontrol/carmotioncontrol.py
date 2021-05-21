import RPi.GPIO as GPIO
from time import sleep
import sys, termios, time, tty

class CarMotionControl():

    def __init__(self, MotorF, MotorB, MotorR, MotorL):
        GPIO.setmode(GPIO.BOARD)
        
        self.MotorF =MotorF
        self.MotorB =MotorB
        self.MotorL =MotorL
        self.MotorR =MotorR

        GPIO.setup(self.MotorF, GPIO.OUT)
        GPIO.setup(self.MotorB, GPIO.OUT)
        GPIO.setup(self.MotorL, GPIO.OUT)
        GPIO.setup(self.MotorR, GPIO.OUT)

        self.pwm = GPIO.PWM(MotorF, 36)
        
        #display user controls
        print ('W forward')
        print ('S Reverse')
        print ('A Left')
        print ('D Right')
        print ('P Pause')
        print ('esc or ctrl+c Exit Programme')



    print("Turning motor on")
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
    
    def steeringsstop(self):
        print("Stop steering")
        GPIO.output(self.MotorR, False)
        GPIO.output(self.MotorL, False)

    # For speed control, switching b/w two speed values
    # 50 & 100 

    # def pwm_start():

    def start(self):
        self.pwm.start(36)
    
    def stop(self):
        print("Stop")
        GPIO.output(self.MotorF, False)
        GPIO.output(self.MotorB, False)
        GPIO.output(self.MotorR, False)
        GPIO.output(self.MotorL, False)
    
    def exit(self):
        print("Exiting")
        self.stop()
        GPIO.cleanup()
        quit()

