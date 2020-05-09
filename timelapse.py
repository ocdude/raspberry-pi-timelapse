#!/usr/bin/python3

import time
import picamera
import configparser
import sys
import paramiko
import scp
from os import path

# set a default resolution to the max resolution of the HQ camera module
default_resolution = (4056,3040)

def take_picture(res,output):
	camera = picamera.PiCamera()
	camera.resolution = res
	camera.exposure_mode = 'auto'
	camera.start_preview()
	time.sleep(5)
	camera.stop_preview()
	camera.capture(output)
	camera.close()

def ssh_client(server, port, user, password):
	client = paramiko.SSHClient()
	client.load_system_host_keys()
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	client.connect(server, port, user, password)
	return client

def upload_image(image_path, remote_path, ssh_client):
	scp_client = scp.SCPClient(ssh_client.get_transport())
	scp_client.put(image_path, remote_path)


if __name__ == "__main__":
	# load configuration
	config = configparser.ConfigParser()
	config_file = sys.argv[1]
	config.read(config_file)
	resolution = (int(config.get('camera','width')), int(config.get('camera','height')))
	frequency = config.get('camera','frequency')
	ssh_server = config.get('ssh','server')
	ssh_port = config.get('ssh','port')
	ssh_user = config.get('ssh','user')
	ssh_password = config.get('ssh','password')
	ssh_remote_path = config.get('ssh','remote_path')
	output = path.join(config.get('camera','output_path'),'output.jpg')
	
	take_picture(resolution, output)
	client = ssh_client(ssh_server, ssh_port, ssh_user, ssh_password)
	upload_image(output, ssh_remote_path, client)