#!/usr/bin/env python

from std_msgs.msg import String
from buggy_sensor.msg import GyroData, GPSData
from sensor_msgs.msg import NavSatFix
import std_msgs
import rospy
import fileinput
import csv
import datetime
import message_filters

current_date = '{date:%Y-%B-%d-%I-%M}'.format(date=datetime.datetime.now())
filename = "Buggy__%s.csv" % (current_date)
spamwriter = csv.writer(open(filename, 'w'))

def callback(gps_datas, gyro_datas):
	msg = "{}, {}, {}, {}".format(gps_datas.latitude, gps_datas.longitude, gyro_datas.X, gyro_datas.Y)
	rospy.loginfo(rospy.get_caller_id() + "received : %s", msg)
	spamwriter.writerow([gps_datas.latitude, gps_datas.longitude, gyro_datas.X, gyro_datas.Y])
	rospy.loginfo(gps_datas)

def gyro(gyro_data):
	rospy.init_mode('buggyStoreDataNode', anonymous=True)
	rospy.loginfo(gyro_data.x)

def gps(gps_data):
	ropsy.loginfo(gps_data.latitude)

def listener():
	rospy.init_node('buggyStoreDataNode', anonymous=True)
	gyro_sub = message_filters.Subscriber('MPU6050', GyroData, callback=gyro)
	gps_sub = message_filters.Subscriber('sensor_msgs/NavSatFix', NavSatFix, callback=gps)
	#ats = message_filters.ApproximateTimeSynchronizer([gps_sub, gyro_sub], 10, 0.1)
	#ats.registerCallback(callback)
	rospy.loginfo("Listener setup")
	rospy.spin()

if __name__ == '__main__':
	listener()
