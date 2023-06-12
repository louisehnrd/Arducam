#!/usr/bin/python

import json
from picture import take_picture

def take_photos():
    # Charger la configuration depuis le fichier JSON
    with open('config.json','r') as config_file:
        config = json.load(config_file)
    config_file.close()

    if config['on']:
        width = config['width']
        height = config['height']
        zoom_factor = config['zoom_factor']
        lens_position = config['lens_position']

        take_picture(width, height,zoom_factor, lens_position)

        print(f"Photos prises avec les paramètres : width={width}, height={height}, zoom={zoom}, lens_position={lens_position}")
    else:
        print("La prise de photos est désactivée dans la configuration.")

if __name__ == '__main__':
    take_photos() 
