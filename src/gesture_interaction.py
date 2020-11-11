#!/usr/bin/env python
"""This is the Gesture Interaction node

This is node receives the pointed location from the sensors and publishes 
the pointed location to the state machine and the robot controller node

"""

import rospy
import time
import random
from std_msgs.msg import String
from geometry_msgs.msg import Point

"""The parameters x_lim and y_lim  corresponds to the boundary limit of the descrete 2D envirionment of the robot."""
x_lim = rospy.get_param("x_limit")
y_lim = rospy.get_param("y_limit")


def gesture_interaction():
    """This is the function which defines the node and its parameters.

    This method initialises the the parameters.It publishes the pointed 
    location and also logs in the details.

    """
    rospy.init_node('gesture_interaction', anonymous=True)
    pub_gesture_loc = rospy.Publisher('pointed_location', Point, queue_size=1)
    gesture_target = Point()
    
    while not rospy.is_shutdown():
		if rospy.get_param('current') == 'play':
			gesture_target.x = random.randint(0, x_lim)
			gesture_target.y = random.randint(0, y_lim)
			rospy.set_param('pointed_x',gesture_target.x)
	        	rospy.set_param('pointed_y',gesture_target.y)	
            		rospy.loginfo('The operator points to a location %i %i', gesture_target.x, gesture_target.y)
			pub_gesture_loc.publish(gesture_target)
            		rand_time = random.uniform(5, 30)
			rospy.sleep(rand_time)


if __name__ == '__main__':
    try:
        gesture_interaction()
    except rospy.ROSInterruptException:
    	pass
