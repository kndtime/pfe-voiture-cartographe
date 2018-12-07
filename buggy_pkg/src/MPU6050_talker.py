#!/usr/bin/env python

from random import uniform
from buggy_sensor.msg import GyroData
import std_msgs.msg
import rospy
import smbus
import math
import sys

# dummy function, when gyro is not available
def get_rot():
	return uniform(0,90)

def read_byte(bus, address, adr):
	return bus.read_byte_data(address, adr)

def read_word(bus, address, adr):
	high = bus.read_byte_data(address, adr)
	low = bus.read_byte_data(address, adr)
	val = (high << 8) + low
	return val

def read_word_2c(bus, address, adr):
	val = read_word(bus, address, adr)
	if (val >= 0x8000):
		return -((65535 - val) + 1)
	else:
		return val

def dist(a,b):
	return math.sqrt((a*a)+(b*b))

def get_y_rotation(x,y,z):
	radians = math.atan2(x, dist(y,z))
	return - math.degrees(radians)

def get_x_rotation(x,y,z):
	radians = math.atan2(y, dist(x, z))
	return math.degrees(radians)

def MPU_talker():
	power_mgmt_1 = 0x6b
	power_mgmt_2 = 0x6c

	bus = smbus.SMBus(1)
	address = 0x68
	bus.write_byte_data(address, power_mgmt_1, 0)
	
	publisher = rospy.Publisher('MPU6050', GyroData, queue_size=10)
	rospy.init_node('MPU6050Talker', anonymous=True)
	rate = rospy.Rate(1) #1 mesure par seconde
	while not rospy.is_shutdown():
			gyro_xout = read_word_2c(bus, address, 0x43)
			gyro_yout = read_word_2c(bus, address, 0x45)
			gyro_zout = read_word_2c(bus, address, 0x47)
		
			accel_xout = read_word_2c(bus, address, 0x3b)
			accel_yout = read_word_2c(bus, address, 0x3d)
			accel_zout = read_word_2c(bus, address, 0x3f)
		
			accel_xout_scaled = accel_xout / 16384.0
			accel_yout_scaled = accel_yout / 16384.0
			accel_zout_scaled = accel_zout / 16384.0

			rotX = get_x_rotation(accel_xout_scaled, accel_yout_scaled, accel_zout_scaled)
			rotY = get_y_rotation(accel_xout_scaled, accel_yout_scaled, accel_zout_scaled)
			rotZ = get_rot() #get_z_rotation(accel_xout_scaled, accel_yout_scaled, accel_zout_scaled)
			header = std_msgs.msg.Header()
			header.stamp = rospy.Time.now()
			strmsg = "{}, {}".format(rotX, rotY)
			msg = GyroData()
			msg.X = rotX
			msg.Y = rotY
			msg.Z = rotZ
			msg.header = header
			rospy.loginfo(strmsg)
			publisher.publish(msg)
			rate.sleep()

if __name__ == '__main__':
	try:
		MPU_talker()
                rospy.spin()
	except rospy.ROSInterruptException:
		pass
