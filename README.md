# Experimental Robotics Laboratory - Assignment 1
#### Behavioural Architecture
## Intoduction
This contains the Assignment 1 of Experimental Robotics Lab.The aim of this assignment is to implement a behavioural architecure for a robot that moves in a discrete 2D envirionment.The architecture involves perception components, a finite state machine as the command manager and a controller component.
## Software Architecture
![expro_arch](https://user-images.githubusercontent.com/47361086/98854383-eb276a80-2473-11eb-9eb9-54fccfeeff82.PNG)
The picture above is the component diagram of the implemented system.The major components of the system are :
* Verbal Interaction
* Gesture Interaction
* State Machine
* Control
#### Verbal Interaction Component
This component is responsible for obtaining the verbal orders from the operator(person).This is used to receive the voice commands of the person and then to process it . Once processed it will be passed on to the state machine to initiate the corresponding behavior.In this project, it is assumed that the operator says a command of type string (eg. "play" ) and it is processed and send to to the state machine.
#### Gesture Interaction
This component is responsible for obtaining the gestures from the operator(person). This components will recieve the cordinates of the location pointed by the operator and it is published to the state machine so that if the robot is in state "play" it should move the location pointed by the operator.
#### State Machine
This acts as the command manager.It switches between three states i.e. sleep,normal,play. Sleep being the initial state, the robot rset in its home location. At normal state, the robot wanders randomly throughout the envirionment.In the play state , the robot moves to the location og the operator and then follows the operators gestures and move toward the position pointed by the operator.
#### Control
This component is responsible for the robot motion and control. After obtaining the location or commands from the previous components, the robot moves to the position respectively.This component also publishes its current location via topic /position.
## Package and File List
## Installation and Running Procedure
## Working Hypothesis 
## Systems Features
## Systems Limitation
## Possible Improvements
## Author
Author  : Nitha Elizabeth John
Contact : nithaelizabethjohn@gmail.com
