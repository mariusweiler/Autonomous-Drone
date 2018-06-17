# Autonomous Shooting Drone
## More information, setup and configuration :
All usefull information are here : [Autonomous Shooting Drone WIKI](https://github.com/mariusweiler/Autonomous-Shooting-Drone/wiki)

## Introduction
Configure an autonomous BB gun drone, using a DJI Phantom 2 drone, 2 raspberries 3 with 3 grovepis, multiple sensor from the grovepi kit, a gyroscope and a camera. **All of the programmation is done in Python**

## Goals
The Autonomous Shooting Drone purpose is to controll a DJI phantom2 drone with 2 Raspberries Pi 3, to make it takeoff, then stabilise it at 1.5 meter, then look for a person as a target, center the target and shoot with a BB gun. The Raspi is interfaced to the drone via the remote controller, which we replace the potentiometers by the raspberry's outputs.

There is 2 devices managing the flight :
- A Raspberry with a grovepi, a camera, a ultrasonic range sensor, a relay, a gyroscope and a battery to power the Raspi. All of this is on the Drone and communicates with the other device to send the height and the position of the person.
- A Raspberry with 2 grovepies, the remote board with batteries, a LCD display, a LED, a button. All of this is placed on a box, and operates as mission controll to send commands to the drone to make it fly.

## Current state
We achieved the following :
* Start / Stop the drone via the raspberry
* Fly the drone with the raspberry
* Recognise and localise target with the camera
* Communicate between the 2 raspberries to share information
* LCD, LED, Buzzer, Relay working.

To see the drone in action (video) [click here](https://www.youtube.com/watch?v=76PfgulFEIY&feature=youtu.be)

TO DO : 
* Improve take off in order to be soft and slow
* Improve stabilisation with the accelerometer to make the drone steady
* Final testing with a really light BB gun

## Why GitHub
Throughout the project we have stumbled upon documentation from various websites, which helped us going forward. Anyway, we did not found any project to fly a DJI drone with a Raspberry directly. With this GitHub documentation, we want to give back information, and maybe help other projects with our humble contribution.
