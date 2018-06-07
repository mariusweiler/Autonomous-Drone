# Autonomous Shooting Drone
## Introduction
Configure an autonomous shooting drone, using a DJI Phantom 2 drone, a raspberry 3 with 2 grovepis, multiple sensor from the grovepi kit, a gyroscope and a camera.

### Goals
The Autonomous Shooting Drone purpose is to controll a DJI phantom2 drone with a Raspberry Pi 3, to make it takeoff, then stabilise it at 1.5 meter, then look for a person as a target, center the target and shoot with a BB gun. The Raspi is interfaced to the drone via the remote controller, which we replace the potentiometers by the raspberry's outputs

### Why GitHub
Throughout the project we have stumbled upon documentation from various websites, which helped us going forward. Anyway, we did not found any project to fly a DJI drone with a Raspberry directly. With this GitHub documentation, we want to give back information, and maybe help other projects with our humble contribution.

## Installation
### Wiring the raspberry to the DJI remote

### Wiring the sensors

### Raspberry Configuration

## Runing the software

###

## Documentation
### Code architecture
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

### The flightCommand Class

### The sensorController Class

### Wiring the raspberry to the DJI remote

### Using OpenCV to detect a person

### Using the gyroscope to stabilise the drone

### Wheight problems

## Other features
### Connection to GitHub
