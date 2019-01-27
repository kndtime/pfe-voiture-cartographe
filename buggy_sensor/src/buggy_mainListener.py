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
import logging
import os
import time
from flask import Flask, render_template
from flask_socketio import SocketIO


current_date = '{date:%Y-%B-%d-%I-%M}'.format(date=datetime.datetime.now())
filename = "Buggy__%s.csv" % (current_date)
spamwriter = csv.writer(open(filename, 'w'))
snapshot = ""

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@sio.on('connect')
def connect(sid, environ):
    print('connect ', sid)

@sio.on('my message')
def message(sid, data):
    print('message ', data)

@sio.on('disconnect')
def disconnect(sid):
    print('disconnect ', sid)

@socketio.on('sensor')
def handle_sensor(json):
    send(json, json=True)

@socketio.on('info')
def handle_info(json):
    send(json, json=True)

X = 0.0
Y = 0.0
lat = 0.0
lon = 0.0

def writeOnCSV(msg):
	spamwriter.writerow([snapshot])
	snapshot = "{}, {}, {}, {}".format(lat, lon, X, Y)
	handle_sensor(info_sensor(lat, lon, X, Y))
	handle_info(info_data())
	rospy.loginfo("PUBLISH INTERRUPT received : %s", snapshot)

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
        gps_sub = rospy.Subscriber('buggyGPSublox', GPSData, callback=gps_callback) # 'ublox_gps_rover', NavSatFix)
	interrupt_sub = rospy.Subscriber('buggyInterrupt', String, writeOnCSV)
	rospy.spin()

def info_data():

    disk_write_data_start = psutil.disk_io_counters(perdisk=False)
    io_data_start = psutil.net_io_counters()

    # Some metrics are only reported in values since uptime,
    # so sample over a period (in seconds) to get rate.

    time.sleep(period)

    cpu_data = psutil.cpu_percent(interval=None)
    ram_data = psutil.virtual_memory()

    ram_total = ram_data.total / 2**20       # MiB.
    ram_used = ram_data.used / 2**20
    ram_free = ram_data.free / 2**20

    disk_data = psutil.disk_usage('/')
    disk_total = disk_data.total / 2**30     # GiB.
    disk_used = disk_data.used / 2**30
    disk_free = disk_data.free / 2**30
    disk_percent_used = disk_data.percent
    disk_write_data = psutil.disk_io_counters(perdisk=False)
    io_data = psutil.net_io_counters()

    data = {
        'cpu': {
            'percent': cpu_data
        },
        'ram': {
            'percent': ram_data[2],
            'total': round(ram_total, 2),
            'used': round(ram_used, 2),
            'free': round(ram_free, 2),
            'unit': "Mo"
        },
        'disk': {
            'total': round(disk_total, 2),
            'used': round(disk_used, 2),
            'free': round(disk_free, 2),
            'percent': round(disk_percent_used, 2),
            'read_bytes_sec': round((disk_write_data[2] - disk_write_data_start[2])
            / period, 2),
            'write_bytes_sec': round((disk_write_data[3] - disk_write_data_start[3])
            / period, 2),
            'unit' : "Go"
        },
        'io': {
            'sent_bytes_sec': (io_data[0] - io_data_start[0]) / period,
            'received_bytes_sec': (io_data[1] - io_data_start[1]) / period
        }
    }

    return json.dumps(data)

def info_sensor(lat, lon, X, Y):
    data = {
        'gps': {
            'lat': lat,
			'lng': lon
        },
        'gyro': {
            'X': X,
            'Y': Y
        },
        'time': '{date:%Y-%B-%d-%I-%M}'.format(date=datetime.datetime.now())
    }
    return json.dumps(data)

if __name__ == '__main__':
	socketio.run(app)
	listener()
