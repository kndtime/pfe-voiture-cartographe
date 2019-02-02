#!/usr/bin/env python

from std_msgs.msg import String
import rospy
import keyboard


def waitInterrupt():
	rospy.init_node('buggyWaitInterrupt')
	pub = rospy.Publisher('buggyInterrupt', String, queue_size=10)
	msg = "toto"
	while not rospy.is_shutdown():
		rospy.sleep(7)
		rospy.loginfo("STOP")
		rospy.sleep(3)
		pub.publish(msg)

if __name__ == '__main__':
	try:
		waitInterrupt()
		rospy.spin()
	except rospy.ROSInterruptException:
		pass
