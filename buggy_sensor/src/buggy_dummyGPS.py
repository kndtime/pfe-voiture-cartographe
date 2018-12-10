#!/usr/bin/env python

from random import uniform
from buggy_sensor.msg import GPSData
import std_msgs.msg
import rospy
import math

def get_latitude():
	return uniform(-180, 180)

def get_longitude():
	return uniform(-90, 90)

def gps_talker():
	publisher = rospy.Publisher('buggyGPSublox', GPSData, queue_size=10)
	rospy.init_node('BuggyGPSTalker', anonymous=True)
	rate = rospy.Rate(1) #1 mesure par seconde
	while not rospy.is_shutdown():
		lat = get_latitude()
		lon = get_longitude()
		header = std_msgs.msg.Header()
		header.stamp = rospy.Time.now()
		msg = GPSData()
		msg.latitude = lat
		msg.longitude = lon
		msg.header = header

		strmsg = "{}, {}".format(lat, lon)
		rospy.loginfo(strmsg)
		publisher.publish(msg)
		rate.sleep()

if __name__ == '__main__':
	try:
		gps_talker()
	except rospy.ROSInterruptException:
		pass
