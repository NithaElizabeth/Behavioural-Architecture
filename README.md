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
## State Diagram
This section explains how the states are decided.As shows in the state diagram above, there are three states : sleep, normal, paly.
The state sleep is the initial state. In the sleep , the robot returns to its home position and rests.From the "sleep" state the robot switches to the "normal"behaviour.In the normal behaviour the robot moves randomly at location withing its constrainted envirionment. In the normal behaviour, the robot will be willing to listen to the verbal commands and all the verbal commands will be registered.From the state "normal", it can switch to either "sleep" or "play".In the "play", the robot initially moves to position where the operator (person) is and then follows the operators instruction and moves to the location pointed by the operator.
## Package and File List
## Installation and Running Procedure
Clone this github repository into the ROS workspace
```
git clone https://github.com/NithaElizabeth/Behavioural-Architecture_-EXPRO-1-
```
Next the scripts had to made executable.For that navigate to the src folder of this repositiory.
```
cd assignment1/src
```
```
chmod +x state_machine.py
```
```
chmod +x verbal_interaction.py
```
```
chmod +x gesture_interaction.py
```
```
chmod +x control.py
```
After this. in another terminal run the roscore.
```
roscore
```
Once the roscore is run,then the launch file must be run.
```
cd ..
roslaunch assignment1 assignment1.launch
```
## Working Hypothesis 
Throughout this project, it was assumed that the robot moves in discrete 2D envirionment.It implies that the position of robot at any instant will be a point with x and y coordinates only. The finite state machine was built under the hypothesis that the transition between the state will be strictly like that shown in the state diagram figure given above. It was also assumed that the position of the person will be constant for an iteration of the program. The verbal interaction node assumes that the operator commands will be of type string. 
## Systems Features
## Systems Limitation
## Possible Improvements
## Author
Author  : Nitha Elizabeth John
Contact : nithaelizabethjohn@gmail.com
