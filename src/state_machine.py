#!/usr/bin/env python
"""This is the state machine that switches between the three states

This node is a satate machine that is implemented in position of command
manager in the whole architecture.This state machine is implemented in 
smach.It switches between three nodes sleep, normal and play.

"""

import roslib
import rospy
import smach
import smach_ros
import time
import random
from geometry_msgs.msg import Point
from std_msgs.msg import String

"""The parameters x_lim and y_lim  corresponds to the boundary limit of the descrete 2D envirionment of the robot."""
x_lim = rospy.get_param('x_limit')
y_lim = rospy.get_param('y_limit')

"""The parameters person_pos_x and person_pos_y extracts the location of the operator"""
person_pos_x = rospy.get_param('person_x')
person_pos_y = rospy.get_param('person_y')

"""The parameters home_position_x and home_position_y extracts the location of the home as described in the launch file"""
home_position_x = rospy.get_param('home_x')
home_position_y= rospy.get_param('home_y')


def user_action():
    """This function choses randomly a state from the 3 states:"sleep","normal","play" """
    return random.choice(['sleep','normal', 'play'])

# define state Sleep
class Sleep(smach.State):
    """This class defines the state Sleep
	
    This is the state in which robots return to home position and does 
    not indulge in any activities.
    
    Methods
    ----------
    _init_(self)
		This methods initialises all the attributes of the class
    execute(self,userdata)
		This methods executes the sleep state
    Sleep_callback(self,arg)
		This method is the subscriber callback function for the topic 'position'.
		The loaction of the home is assigned to the topic /position
	
    """
    def __init__(self):
		smach.State.__init__(self, 
                             outcomes=['goto_NORMAL_state'])
		rospy.Subscriber('position',Point,self.Sleep_callback)
		self.home_position = Point()
	
    def Sleep_callback(self,arg):
		rospy.set_param('position_x',home_position_x)
		rospy.set_param('position_y',home_position_y)
                             
        
    def execute(self, userdata):
        	rospy.set_param('current','sleep')
        	rospy.loginfo('_______________________Executing state SLEEP ________________________')
        	
        	"""Sets the home position"""
        	
		self.home_position.x=home_position_x
		self.home_position.y=home_position_x
			
		"""Publishes the home position to the robot's control node"""
			
		pub = rospy.Publisher("robot_control",Point,queue_size=10)
		pub.publish(self.home_position)
		rospy.loginfo('Robot reached HOME position')
		time.sleep(5)
		return 'goto_NORMAL_state'

    

class Normal(smach.State):
    """This class defines the state Normal
    
    This is the state in which robots moves randomly and is willing to 
    listen to its operators commands.
    	
    Methods
    ----------
    _init_(self)
	This methods initialises all the attributes of the class
    execute(self,userdata)
	This methods executes the normal state
    Normal_callback(self,arg)
	Thsi is the callback function for the subscribed topic 
	position.
    Normal_callback1(self,arg)
	Thsi is the callback function for the subscribed topic 
	voice_command.
    Normal_callback2(self,arg)
	Thsi is the callback function for the subscribed topic 
	voice_commands_sleep.	
    """	
    def __init__(self):
        	smach.State.__init__(self, 
                             outcomes=['goto_SLEEP_state','goto_PLAY_state'])
		rospy.Subscriber('position',Point,self.Normal_callback)
		rospy.Subscriber('voice_command', String, self.Normal_callback1)
		self.target = Point()

   
    def Normal_callback(self,arg):
		if(rospy.get_param('current'=='normal')):
			if(rospy.wait_for_message('position',Point)):
				
				"""Sets the position to the target position as described by the operator"""
				
				rospy.set_param('position_x',target.x)
				rospy.set_param('position_y',target.y)
	
    
    def Normal_callback1(self,arg):
		if rospy.get_param('current') == 'normal':
			
			"""Logs the voice command"""
			rospy.loginfo('Voice command registered')
			
	
	
    def execute(self, userdata):
		rospy.set_param('current','normal')
		rospy.loginfo('______________________Executing state NORMAL _______________________')
		while (rospy.get_param('current')=='normal' and not rospy.is_shutdown()): 
			pub = rospy.Publisher("robot_control",Point,queue_size=1)
			self.target.x = random.randrange(1,x_lim,1)
			self.target.y = random.randrange(1,y_lim,1)
			self.target.z = 0
			"""Some random position is published to the control"""
			pub.publish(self.target)
            		time.sleep(30)
			state= user_action()
			if(state == 'sleep'):
				return 'goto_SLEEP_state'
            		elif (state== 'play'):
				return 'goto_PLAY_state'


class Play(smach.State):
    """This class defines the state Play
    
    This is the state in which robots moves according to the operators 
    will. When in this state , it first moves to the location of the operator 
    and then moves to the position to which the operator points.
    
    Methods
    ----------
    _init_(self)
	This methods initialises all the attributes of the class
    execute(self,userdata)
	This methods executes the normal state
    Play_callback_gesture(self,arg)
	Thsi is the callback function for the subscribed topic 
    	pointed_position.
    
    """	
    def __init__(self):
        	smach.State.__init__(self, 
                             outcomes=['goto_NORMAL_state'])
	
		rospy.Subscriber('pointed_location',Point,self.Play_callback_gesture)
        	self.target = Point()
		self.gesture = Point()



    def execute(self, userdata):
		rospy.set_param('current','play')
		pub = rospy.Publisher("robot_control",Point,queue_size=1)
		rospy.loginfo('______________________Executing state PLAY _______________________')
        	while (rospy.get_param('current')=='play' and not rospy.is_shutdown()):  
			self.target.x = person_pos_x
			self.target.y = person_pos_y 
			self.target.z = 0
			rospy.loginfo('The operator is at position %i %i', self.target.x, self.target.y)
			pub.publish(self.target)
			time.sleep(60)
			return 'goto_NORMAL_state'  


    def Play_callback_gesture(self,arg):
		if(rospy.get_param('current'=='play')):
			if(rospy.wait_for_message('position',Point)):
				self.gesture.x = arg.x
				self.gesture.y = arg.y
				pub.publish(self.gesture)
				time.sleep(10)

        
def main():
    """This class is the main class
	
    This class defines the relation of each state parameters to corresponding 
    states.From the sleep state , the robot moves to Normal state.From the 
    normal state the robot can move to either Sleep state or PLay state.And 
    from the Play state the robot moves back to normal state.
		
    """	
    rospy.init_node('state_machine')

    # Create a SMACH state machine
    sm = smach.StateMachine(outcomes=['container_interface'])
    sm.userdata.sm_counter = 0

    # Open the container
    with sm:
        # Add states to the container
        smach.StateMachine.add('SLEEP', Sleep(), 
                               transitions={'goto_NORMAL_state':'NORMAL'})
        smach.StateMachine.add('NORMAL', Normal(), 
                               transitions={'goto_SLEEP_state':'SLEEP', 
                                            'goto_PLAY_state':'PLAY'})
        smach.StateMachine.add('PLAY', Play(), 
                               transitions={'goto_NORMAL_state':'NORMAL'})


    # Create and start the introspection server for visualization
    sis = smach_ros.IntrospectionServer('server_name', sm, '/SM_ROOT')
    sis.start()

    # Execute the state machine
    outcome = sm.execute()

    # Wait for ctrl-c to stop the application
    rospy.spin()
    sis.stop()


if __name__ == '__main__':
    main()
