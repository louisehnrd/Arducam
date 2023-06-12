from picamera2 import Picamera2, Metadata
from libcamera import controls
import json
import os
import time
from time import sleep
import subprocess
from datetime import datetime

def param_zoom(zoom_factor):
    if zoom_factor == '1' :
        w = 9152
        h = 6944
    elif zoom_factor == '2' :
        w = 8236
        h = 6250
    elif zoom_factor == '3' :
        w = 7322
        h = 5556
    elif zoom_factor == '4' :
        w = 6406
        h = 4860
    elif zoom_factor == '5' :
        w = 5492
        h = 4166
    elif zoom_factor == '6' :
        w = 4576
        h = 3472
    elif zoom_factor == '7' :
        w = 3660
        h = 2778
    elif zoom_factor == '8' :
        w = 2746
        h = 2084
    elif zoom_factor == '9' :
        w = 1830
        h = 1388
    else : 
        w = 916
        h = 694

    size = [w,h]
    offset_x = int ((9152-w)/2)
    offset_y = int((6944-h)/2)
    offset = [offset_x,offset_y]

    return size, offset

def take_picture(width, height,zoom_factor, lens_position):
    
    #initialisation camera
    arducam = Picamera2()
    capture_config = arducam.create_still_configuration({"size": (width,height)})
    arducam.align_configuration(capture_config)
    arducam.configure(capture_config)
    
    #allumage camera
    arducam.start()

    #zoom
    size,offset = param_zoom(zoom_factor)
    #arducam.set_controls({"ScalerCrop": offset + size, "AfMode": 1 ,"AfTrigger": 0})
    print("size :", size)
    print("offset:",offset)
    

    #focus
    if lens_position == "None":
        print("size :", size)
        print("offset:",offset)
        #autofocus
        arducam.set_controls({"ScalerCrop": offset + size, "AfMode": 1 ,"AfTrigger": 0})
        time.sleep(5)

    else :
        print(lens_position)
        #manualfocus
        arducam.set_controls({"ScalerCrop": offset + size, "AfMode": 0, "LensPosition": int(lens_position)})
        time.sleep(5)

    # Chemin et nom de fichier de sortie de l'image
    timestamp = time.strftime('%Y_%m_%d-%H_%M_%S')
    filename = 'photo_{}.jpg'.format(timestamp)
    output_file = os.path.join(os.path.expanduser("~"),"user_space", "static", filename)

    arducam.capture_file(output_file)

    arducam.close()

    #Commander à exécuter pour copier la photo
    cmd = ['cp', output_file, '/home/camera/user_space/static/photo_recent.jpg']
    subprocess.run(cmd)

    #return output_file[1:]

def update_config(on,width,height,zoom_factor,lens_position):    
    #chargement du fichier json
    with open('config.json', 'r') as file:
        config = json.load(file)

    #maj des données
    config['on'] = on
    config['width']=width
    config['height']=height
    config['zoom_factor']=zoom_factor 
    config['lens_position']=lens_position
    print(config)
        
    #écrire dans le fichier de config json
    with open("config.json", "w") as json_file:
        json.dump(config, json_file)        
    json_file.close()

def suppr_picture(output_file):
        cmd = ['rm', output_file]
        subprocess.run(cmd)

def date(file, file1):
    date1=datetime(int(file[6:10]), int(file[11:13]), int(file[14:16]), int(file[17:19]), int(file[20:22]))
    date2=datetime(int(file1[6:10]), int(file1[11:13]), int(file1[14:16]), int(file1[17:19]), int(file1[20:22]))
    return date1, date2

def last_picture():
    # Chemin du dossier à lister
    folder = '/home/camera/user_space/static'

    # Liste tous les fichiers du dossier
    files = os.listdir(folder)
    i=0
    for file in files:
        if file == 'photo_recent.jpg':
            del files[i]
            break
        i+=1
    #photo_%YYYY_%mm_%dd-%HH_%MM_%SS

    if len(files)==1:
        print('la')
        return os.path.join(folder, files[0]) 
    
    # Affiche le nom de chaque fichier
    recent_file = files[0]
    for i in range(len(files)-1):
        date1,date2=date(files[i],recent_file)

        # Comparaison
        if date1 < date2:
            path_file = os.path.join(folder, recent_file)
            print("Date/heure 1 est antérieure à Date/heure 2")
        else :
            path_file = os.path.join(folder, files[i])
            recent_file=files[i]

    return path_file
    

    
