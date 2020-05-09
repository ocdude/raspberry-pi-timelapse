#!/usr/bin/python3

import time
import picamera
import configparser

# set a default resolution
resolution = (4056,3040)

def take_picture(res,output):
	camera = PiCamera()
	camera.resolution = res
	time.sleep(2)
	camera.capture(output)

if __name__ = "__main__":
	take_picture(resolution, 'output.jpg')