#!/usr/bin/env python
"""This is the Robot Controller Node

This is node receives the the order to where to move the robot from the 
state machine and accordingly moves the robot to the position mentioned 
by the state machine node.

"""

import rospy
import time
import random
from geometry_msgs.msg import Point

"""The parameters x_lim and y_lim  corresponds to the boundary limit of the descrete 2D envirionment of the robot."""
x_limit = rospy.get_param("x_limit")
y_limit = rospy.get_param("y_limit")


def constraints(x, y):
    """This method checks if the provided position is reachable
    
    It checks whether the given coordinates lies in the world described for 
    the experiment.If the given position is not reachable , it provides an 
    error message and will not move to that location.
    
    """
    if x >= 0 and x <= x_limit and y >= 0 and y <= y_limit:
        return True
    else:
        print('The given location is out of bound.Cannot move to that location')
        return False


def sub_callback(loc):
    """This method is a callback function
    
    It checks with the costraints if the points are valid and if its 
    valid then moves the robot to that location as given
    
    """
    pub = rospy.Publisher('position', Point, queue_size=1)
    isValid = constraints(loc.x, loc.y)
    if isValid:
        time.sleep(random.randint(5, 30))
	rospy.loginfo('The robot reached destination %i %i', loc.x, loc.y)
        pub.publish(loc)


def sub_callback_gesture(loc_gest):
    """This method is callback function to the subscribed gesture topic
    
    It checks with the costraints if the points are valid and if its 
    valid then moves the robot to that location as pointed by the operator
    
    """
    pub = rospy.Publisher('position', Point, queue_size=1)
    isValid = constraints(loc_gest.x, loc_gest.y)
    if isValid:
        time.sleep(random.randint(5, 30))
	rospy.loginfo('The robot reached destination %i %i', loc_gest.x, loc_gest.y)
        pub.publish(loc_gest)


def robot_controller():
    """This method is initialises the node
    
    Here this function initialises the node.It also subscribes to the topic 
    /robot_control and /pointed_location.
    
    """
    rospy.init_node('robot_controller',anonymous=True)
    rospy.Subscriber('robot_control', Point, sub_callback)
    rospy.Subscriber('pointed_location', Point, sub_callback_gesture)
    rospy.spin()

if __name__ == "__main__":
    try:
        robot_controller()
    except rospy.ROSInterruptException:
        pass
