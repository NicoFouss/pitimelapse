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
    
    return directory
    


    # get the last file

def get_last_photo(directory):
    
    list_dir=os.listdir(directory)
    
    
    if list_dir==[]:
        
        nb_photo='0001'
        return nb_photo

    else :

        last_file =''
        timestamp = 0
        

        for f in list_dir :
            
            
            f=os.path.join(directory,f)
            timestamp_f=os.stat(f)
            timestamp_f=timestamp_f.st_mtime

            if timestamp <timestamp_f :

                timestamp = timestamp_f
                last_file = os.path.split(f)
                nb_photo=last_file[1]
                nb_photo = nb_photo[5:9]
                nb_photo =str(int(nb_photo)+1)
                nb_photo="000{}".format(nb_photo)
                nb_photo=nb_photo[len(nb_photo)-4:len(nb_photo)]
    return nb_photo



    


memory=input("est ce une nouvelle session oui=1 et non =0")

if memory == 1:
    memory =True
else :
    memory = False


camera=PiCamera()

file_config="config.cfg"
config_cam(file_config,camera)

# inspect the value of gpio14

GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.IN)


directory=config_directory(memory)
last_image = get_last_photo(directory)


camera.start_preview()
time.sleep(2)
camera.capture(os.path.join(directory,'image{}.jpg'.format(last_image)))
