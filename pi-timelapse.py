#!/usr/bin/python3.5.2
# _*_coding: Utf-8- *


#pitimelapse use raspberry pi to take picture each hour and make a movie

import time
import os
import configparser
from picamera import PiCamera
import RPi.GPIO as GPIO

def config_cam(file_config,camera):

    config=configparser.ConfigParser()
    config.read(file_config)
    camera.rotation=int(config['config_pi_camera']['rotation'])
    camera.brightness=int(config['config_pi_camera']['brightness'])    
    camera.image_effect=config['config_pi_camera']['image_effect']
    camera.awb_mode=config['config_pi_camera']['awb_mode']
#   camera.exposure_mode=['config_pi_camera']['exposure_mode']

#config directory

def config_directory(value_GPIO):
    
    current_directory=os.getcwd()

    if value_GPIO:
        name=time.strftime('%d_%B_%Y_%H_%M_%S')
        directory = os.path.join(current_directory,"scene",name)
        os.mkdir(directory)            
    else : 
        directory_scene = os.path.join(os.getcwd(),"scene")
        os.chdir(directory_scene)
        list_dir=os.listdir()       
        if list_dir !=[]:

            timestamp = 0
            for last_directory in list_dir :
                                                
                if timestamp < os.path.getctime(last_directory) :
                    timestamp = os.path.getctime(last_directory)
                    directory = os.path.join(current_directory,"scene",last_directory)
                    

        else :
            name=time.strftime('%d_%B_%Y_%H_%M_%S')
            directory = os.path.join(current_directory,"scene",name)
            os.mkdir(directory)

    print(directory)
    return directory    

    

camera=PiCamera()

file_config="config.cfg"
config_cam(file_config,camera)

# inspect the value of gpio14

GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.IN)

config_directory(False)

