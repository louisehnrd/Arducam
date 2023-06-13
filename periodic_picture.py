#!/usr/bin/python

import json
from picture import take_picture

def take_photos():
    #Load configuration from JSON file
    with open('/home/camera/user_space/config.json','r') as config_file:
        config = json.load(config_file)
    config_file.close()

    if config['on']:
        width = config['width']
        height = config['height']
        zoom_factor = config['zoom_factor']
        lens_position = config['lens_position']

        take_picture(width, height,zoom_factor, lens_position)

        print(f"Pictures taken with settings : width={width}, height={height}, zoom={zoom_factor}, lens_position={lens_position}")
    else:
        print("Photo-taking is deactivated in the configuration.")

if __name__ == '__main__':
    take_photos() 
