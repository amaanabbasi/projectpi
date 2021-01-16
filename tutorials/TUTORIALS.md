# motor.py

Controlling a single 5V dc motor using Rasperry pi 3 with a l293D circuit

__l293D__

1) This is an IC which contains dual H bridge 
2) It allows the motor to run in clockwise and anti clockwise direction
3) 2 motors can be connected since its a dual H bridge

![](https://cms-assets.tutsplus.com/uploads/users/228/posts/20051/image/Data%20pins.png)

# sonar.py

For measuring distance. 

__HC-SR04__

1) 4 pins - VCC, Trig, Echo, Ground.
2) Echo takes 5V it can damage the GPIO pin to which it is connected to, so use resistors.
3) I think damage will happen if you use it over extended period of time, I teste for a couple of seconds that worked.


