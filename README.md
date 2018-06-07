# Autonomous Shooting Drone
## Introduction
Configure an autonomous shooting drone, using a DJI Phantom 2 drone, 2 raspberries 3 with 3 grovepis, multiple sensor from the grovepi kit, a gyroscope and a camera.

### Goals
The Autonomous Shooting Drone purpose is to controll a DJI phantom2 drone with 2 Raspberries Pi 3, to make it takeoff, then stabilise it at 1.5 meter, then look for a person as a target, center the target and shoot with a BB gun. The Raspi is interfaced to the drone via the remote controller, which we replace the potentiometers by the raspberry's outputs.

There is 2 devices managing the flight :
- A Raspberry with a grovepi, a camera, a ultrasonic range sensor, a relay, a gyroscope and a battery to power the Raspi. All of this is on the Drone and communicates with the other device to send the height and the position of the person.
- A Raspberry with 2 grovepies, the remote board with batteries, a LCD display, a LED, a button. All of this is placed on a box, and operates as mission controll to send commands to the drone to make it fly.

### Why GitHub
Throughout the project we have stumbled upon documentation from various websites, which helped us going forward. Anyway, we did not found any project to fly a DJI drone with a Raspberry directly. With this GitHub documentation, we want to give back information, and maybe help other projects with our humble contribution.

## Installation
### Wiring the raspberry to the DJI remote

### Wiring the sensors

### Raspberry Configuration
#### Connect Raspberry to a WIFI connection
In this project, we used a Smartphone sharing WIFI connection to connect to the raspberries.

## Runing the software

###

## Documentation
### Code architecture
The main script manages the flight, and uses other Scripts and Classes to communicate with the devices it needs.

Here is the files that you'll find in the project folder :

- Flight Controller
  Main Script, manage the whole flight and actions, uses others classes to perform specific actions

- Flight Commands
  Class containing all the flights commands, to move the drone. It's a class so we can use class variables in the Script

- Captor Management
  Class managing all the sensors used during the flight. It's a class so we can use class variables in the Script

- Pedestrian Detection
  Script performing the person detection and returning the x and y (horizontal sides) coordinates of the rectangle containing the person

- LCD Controll
  Script Controlling the LCD to display live informations

- Buzzer
  Script Controlling the buzzer to emit music during the flight

### The flightController script


### Wiring the raspberry to the DJI remote
To move the Drone, the remote of the DJI was opened and we took out the main board with the components needed.

### Using OpenCV to detect a person

### Using the gyroscope to stabilise the drone

### Wheight problems

### Communication between both Raspberries


## Other features
### Connection to GitHub
