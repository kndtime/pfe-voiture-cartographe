#!/usr/bin/env python

from std_msgs.msg import String
from buggy_sensor.msg import GyroData, GPSData, Snapshot
from sensor_msgs.msg import NavSatFix
import std_msgs
import rospy
import fileinput
import csv
import datetime
import message_filters
import logging
import os
import time
import json


current_date = '{date:%Y-%B-%d-%I-%M}'.format(date=datetime.datetime.now())
filename = "Buggy__%s.csv" % (current_date)
spamwriter = csv.writer(open(filename, 'w'))

X = 0.0
Y = 0.0
lat = 0.0
lon = 0.0

def writeOnCSV(msg):
	snapshot = "lat = {}, lon = {}, X = {}, Y = {}".format(lat, lon, X, Y)
	rospy.loginfo(snapshot)
	spamwriter.writerow([lat, lon, X, Y])
	pub = rospy.Publisher('buggyServer1', String, queue_size=10)
	pub.publish(info_sensor())

def info_sensor():
	data = {
	   'gps' : {
		'lat' : lat,
		'lng' : lon
	    },
            'gyro' : {
		'X' : X,
		'Y' : Y
	    }
	}
	return json.dumps(data)

def gps_callback(gps_datas):
	global lat
	lat = gps_datas.latitude
	global lon
	lon = gps_datas.longitude

def gyro_callback(gyro_datas):
	global X
	X = gyro_datas.X
	global Y
	Y = gyro_datas.Y

def listener():
	rospy.init_node('buggyStoreDataNode', anonymous=True)
	gyro_sub = rospy.Subscriber('MPU6050', GyroData, callback=gyro_callback)
        gps_sub = rospy.Subscriber('fix', NavSatFix, callback=gps_callback)
	interrupt_sub = rospy.Subscriber('buggyInterrupt', String, callback=writeOnCSV)
	rospy.spin()

if __name__ == '__main__':
	listener()
