#!/usr/bin/env python

from std_msgs.msg import String
import rospy
import keyboard

userin = ""

def waitInterrupt():
	rospy.init_node('buggyWaitInterrupt')
	pub = rospy.Publisher('buggyInterrupt', String, queue_size=10)
	while not rospy.is_shutdown():
		pub.publish('toto')
		rospy.sleep(10)

if __name__ == '__main__':
	try:
		waitInterrupt()
		rospy.spin()
	except rospy.ROSInterruptException:
		pass
