#!/usr/bin/python2
# coding: utf-8

import fileinput
import csv
import sys

x_gps = 0
y_gps = 0

with open('test.cvs', 'w') as csvfile:
    print 'lol'
    spamwriter = csv.writer(csvfile)
    while True:
        line_x = sys.stdin.readline()
        line_y = sys.stdin.readline()
        x_gyro = line_x.split(' ')[2][:-3]
        y_gyro = line_y.split(' ')[2][:-3]
        spamwriter.writerow([x_gyro, y_gyro, x_gps, y_gps]);
