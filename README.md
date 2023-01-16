# Final Year Project

The main objective of this project is to develop an autonomous ground vehicle. We will be converting a human controlled RC car into a self-driving. For that will make use of computer vision and image recognition techniques to make the car understand about its environment and drive safely, will go a step further and use state of the art deep learning techniques to train the car. Consequently, we will be developing a framework for effective data collection for the vehicle to train the deep learning model on. 

Data collection is the most important part for a machine learning or a deep learning model. Hence will put a lot of effort in making the process of data collection efficient and effective. So as to not miss any details that might be required by the deep learning model. 

## Demo Video
[![IMAGE ALT TEXT HERE](https://user-images.githubusercontent.com/30196830/136825509-3991678c-9fa2-40c0-baa0-52fd51c40687.png)](https://youtu.be/7KSSgGF1TYo)

# Components

![image](https://user-images.githubusercontent.com/30196830/212731017-a47097cc-894c-43c2-a495-086e1f4d25f6.png)

Raspberry pi 3 or Rpi3 will be the main component of the project and it can be called the brain of the car. It is powered by a portable power source through a usb 2.0 port on the Rpi3. This particular version of Rpi3 has a WIFI module preinstalled, which will allow us to control the car over WIFI and send/receive data. It has 40 GPIO pins that are used to attach sensors to the Rpi3. Which we will be using to control the DC motors through a motor driver (L298N). The camera is attached to the front usb port. Rpi3 is basically a  mini computer that needs an operating system. We have installed headless Raspbian OS on the raspberry pi, which has extremely low storage requirements (less than 2GB).   

We have two dc motors connected to a L298N motor driver. This circuit is responsible for the movement of our car. Connecting DC motors directly to the GPIO pins of Rpi3 can damage the pins hence a motor driver  is used as shown in Figure 

*Components Prices*

Raspberry PI GPIO (1) The Raspberry Pi is a low cost (₹ 3,010), credit-card sized computer that plugs into a computer monitor or TV, and uses a standard keyboard and mouse. It is a capable little device that enables people of all ages to explore computing, and to learn how to program in languages like Scratch and Python. This is going to be the CPU of our self-driving car. Other options are Arduino UNO for the CPU but I choose it because raspberry pi has good support for python.

L298N (2) (₹ 322) is an IC which contains a dual H bridge. Hence two motors can be connected to it. It allows the motor to run in clockwise and anti-clockwise direction. It prevents any damage to the Rpi3.

USB Camera (3) (₹ 1,195) USB camera specifications - Video Capture Resolution 1080p, Connector Type USB, Lens Type  Wide-Angle. 

Portable Power Supply (4) We will be using an Ambrane power bank (₹ 699) that is used to power the raspberry pi 3 using type 2.0 usb cable that can transfer current up to 2.4A,  as well as the dc motors (front & rear both) using a usb cable that is cut open from the other end. Power bank specifications Ambrane Model PP-111, Capacity 10000 mAh, Input: 5V/2.1A, Output: 5V/2.4A.

DC motor(s) (5,6) We have two types of dc motors (₹30)- The rear motor is a 12-volt dc motor which is responsible for the forward and backward movement of the car and the front motor is a 5-volt dc motor which turns the car left or right depending on the command it receives.

SD card Sd card is required to store the Raspberry pi os and project files for which we will be using a 32 GB 96Mbps SD card (₹ 369). Any card size would work but it is recommended to have at least 8 GB storage.

# Circuit

The circuit as shown in the figure below, is responsible for controlling the motors. It contains basically two circuit boards - the green colored one is the Rpi3 (left) and the red one is the L298N (right) motor driver. The Rpi3 has four usb ports, one of which is used by a usb camera

![image](https://user-images.githubusercontent.com/30196830/212731470-8c7b5550-860a-457d-9f0b-a7fe660f4ba8.png)


# Positioning the Camera

Positioning the camera - If the view of the camera is too far sighted then the car will receive the commands too early from the appropriate time, and likewise if it's positioned too close then it will receive the commands after the car has passed. The camera should be positioned not too close and not too far just at a right spot which can be done using hit and try method. Shown below is a snapshot of the car and the final camera position, this was the position that gave the best results.


![image](https://user-images.githubusercontent.com/30196830/212731728-e127fd83-c59e-4a3f-8374-cf5a01df9145.png)


# Controlling the Car

Controlling the car manually using a keyboard, this is going to be the first approach in which we will be controlling the car remotely. In this approach, will have a web browser that will be serving a frontend to control the car and also displaying the video stream from the car’s camera. Key controls as follows: 

 w -> forward
 s -> reverse
 a -> left
 d -> right
 p -> stop

The car has a usb camera attached at the front so that the user can get a live video and navigate the car safely. We are using flask a python micro web framework as the web application backend. After we boot up the car (booting up the Rpi3) we need to run the flask server on it, which is going to serve a webpage at the Rpi3’s local Ip address. The user can then access the web page from a pc connected to the same network. The user is going to be presented with a live stream from the car’s usb camera and an interface to communicate with the car. The user can now navigate the car using the key controls mentioned above. 




