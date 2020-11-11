#!/usr/bin/env python
"""This is the Verbal Interaction node

This is node receives the voice commands from the sensors and publishes 
the received commands to the state machine node

"""


import rospy
import time
import random
from std_msgs.msg import String
from geometry_msgs.msg import Point


"""The parameter per_x and per_y extracts the operator's position"""
per_x = rospy.get_param('person_x')
per_y = rospy.get_param('person_y')


def verbal_interaction():
    """This is the function which defines the node and its parameters.

    This method initialises the the parameters.It publishes the voice  
    commands.

    """
    rospy.init_node('verbal_interaction', anonymous=True)
    pub_command = rospy.Publisher('voice_command', String, queue_size=1)
    rate = rospy.Rate(200)
    while not rospy.is_shutdown():
        time.sleep(random.randint(1, 10))
        if rospy.get_param('current') == 'normal':
			voice=random.choice(['play','sleep'])
			if (voice =='play'):
				pub_command.publish(voice)
				rospy.set_param('position_x',per_x)
				rospy.set_param('position_y',per_y)
				time.sleep(random.randint(1,10))
				rate.sleep()


if __name__ == '__main__':
    try:
        verbal_interaction()
    except rospy.ROSInterruptException:
        pass
