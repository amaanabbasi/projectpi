# Final Year Project

The main objective of this project is to develop an autonomous ground vehicle. We will be converting a human controlled RC car into a self-driving. For that will make use of computer vision and image recognition techniques to make the car understand about its environment and drive safely, will go a step further and use state of the art deep learning techniques to train the car. Consequently, we will be developing a framework for effective data collection for the vehicle to train the deep learning model on. 

Data collection is the most important part for a machine learning or a deep learning model. Hence will put a lot of effort in making the process of data collection efficient and effective. So as to not miss any details that might be required by the deep learning model. 

## Demo Video
[![IMAGE ALT TEXT HERE](https://user-images.githubusercontent.com/30196830/136825509-3991678c-9fa2-40c0-baa0-52fd51c40687.png)](https://youtu.be/7KSSgGF1TYo)

# Components

![image](https://user-images.githubusercontent.com/30196830/212731017-a47097cc-894c-43c2-a495-086e1f4d25f6.png)

Raspberry pi 3 or Rpi3 will be the main component of the project and it can be called the brain of the car. It is powered by a portable power source through a usb 2.0 port on the Rpi3. This particular version of Rpi3 has a WIFI module preinstalled, which will allow us to control the car over WIFI and send/receive data. It has 40 GPIO pins that are used to attach sensors to the Rpi3. Which we will be using to control the DC motors through a motor driver (L298N). The camera is attached to the front usb port. Rpi3 is basically a  mini computer that needs an operating system. We have installed headless Raspbian OS on the raspberry pi, which has extremely low storage requirements (less than 2GB).   

We have two dc motors connected to a L298N motor driver. This circuit is responsible for the movement of our car. Connecting DC motors directly to the GPIO pins of Rpi3 can damage the pins hence a motor driver  is used as shown in Figure 


# Circuit

The circuit as shown in the figure below, is responsible for controlling the motors. It contains basically two circuit boards - the green colored one is the Rpi3 (left) and the red one is the L298N (right) motor driver. The Rpi3 has four usb ports, one of which is used by a usb camera

![image](https://user-images.githubusercontent.com/30196830/212731470-8c7b5550-860a-457d-9f0b-a7fe660f4ba8.png)


# Data Flow

Data flow diagram of the Vehicle
![image](https://user-images.githubusercontent.com/30196830/212735119-1f6f48c3-6db7-42f1-bf1f-bf23b209aadd.png)


# Controlling the Car

Controlling the car manually using a keyboard, this is going to be the first approach in which we will be controlling the car remotely. In this approach, will have a web browser that will be serving a frontend to control the car and also displaying the video stream from the car’s camera. Key controls as follows: 

 w -> forward
 s -> reverse
 a -> left
 d -> right
 p -> stop

The car has a usb camera attached at the front so that the user can get a live video and navigate the car safely. We are using flask a python micro web framework as the web application backend. After we boot up the car (booting up the Rpi3) we need to run the flask server on it, which is going to serve a webpage at the Rpi3’s local Ip address. The user can then access the web page from a pc connected to the same network. The user is going to be presented with a live stream from the car’s usb camera and an interface to communicate with the car. The user can now navigate the car using the key controls mentioned above. 


![image](https://user-images.githubusercontent.com/30196830/212735547-efba9d52-d734-4dac-8c4e-603c19d4170b.png)

# Circuit Diagram
![image](https://user-images.githubusercontent.com/30196830/212737688-af179d6b-8ba7-4f26-9b7f-b2a975ad3e96.png)

# Training
![image](https://user-images.githubusercontent.com/30196830/212738575-a152df59-9416-4042-be4d-e34103987122.png)
![image](https://user-images.githubusercontent.com/30196830/212738588-55f06940-c706-4bae-a600-3c015774fd91.png)
![image](https://user-images.githubusercontent.com/30196830/212738595-4cf9de2b-850f-4b76-bfe2-80c42147a756.png)

# Results
![image](https://user-images.githubusercontent.com/30196830/212739218-ff5056be-5c3e-4419-85c3-6fb9ad979608.png)
![image](https://user-images.githubusercontent.com/30196830/212739231-580bb75d-ac40-43a3-8ad3-cac7fd478e6e.png)


