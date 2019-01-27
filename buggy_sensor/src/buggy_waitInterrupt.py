#!/usr/bin/env python

from std_msgs.msg import String
import rospy
import keyboard


def waitInterrupt():
	rospy.init_node('buggyWaitInterrupt')
	pub = rospy.Publisher('buggyInterrupt', String, queue_size=10)
	msg = "toto"
	while not rospy.is_shutdown():
		#rospy.loginfo("msg")
		pub.publish(msg)
		rospy.sleep(1)

if __name__ == '__main__':
	try:
		waitInterrupt()
		rospy.spin()
	except rospy.ROSInterruptException:
		pass
