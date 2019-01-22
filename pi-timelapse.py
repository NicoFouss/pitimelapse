#!/usr/bin/python3.5.2
# _*_coding: Utf-8- *


#pitimelapse use raspberry pi to take picture each hour and make a movie

import time
import configparser
from picamera import PiCamera

def config_cam(file_config,camera):

    config=configparser.ConfigParser()
    config.read(file_config)
    camera.rotation=int(config['config_pi_camera']['rotation'])
    camera.brightness=int(config['config_pi_camera']['brightness'])    
    camera.image_effect=config['config_pi_camera']['image_effect']
    camera.awb_mode=config['config_pi_camera']['awb_mode']
#   camera.exposure_mode=['config_pi_camera']['exposure_mode']
    

camera=PiCamera()

file_config="config.cfg"
config_cam(file_config,camera)
