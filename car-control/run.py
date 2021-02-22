
import carmotioncontrol
from config import *

car = carmotioncontrol.CarMotionControl(MotorF, MotorB, MotorR, MotorL)

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

    