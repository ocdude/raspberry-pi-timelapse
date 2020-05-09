#!/usr/bin/python3

import time
import picamera
import configparser
import paramiko
import scp

# set a default resolution to the max resolution of the HQ camera module
default_resolution = (4056,3040)

def take_picture(res,output):
	camera = picamera.PiCamera()
	camera.resolution = res
	camera.capture(output)

def ssh_client(server, port, user, password):
	client = paramiko.SSHClient()
	client.load_system_host_keys()
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	client.connect(server, port, user, password)
	return client

def upload_image(image_path, ssh_client):
	scp_client = scp.SCPClient(ssh_client.get_transport())
	scp.put(image_path)


if __name__ == "__main__":
	# load configuration
	config = configparser.ConfigParser()
	config.read('config.ini')
	resolution = config.get('resolution')
	ssh_server = config.get('server')
	ssh_port = config.get('port')
	ssh_user = config.get('user')
	ssh_password = config.get('password')

	take_picture(resolution, 'output.jpg')