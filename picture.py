import os
import time
from time import sleep
import subprocess
from datetime import datetime

def take_picture(duration, width, height):
    #initialization
    #delay = 600  #10 min
    #duration = 5000

    # Chemin et nom de fichier de sortie de l'image
    timestamp = time.strftime('%Y_%m_%d-%H_%M_%S')
    filename = 'photo_{}.jpg'.format(timestamp)
    #output_file = os.path.join(os.path.expanduser("~"), "Pictures", filename)
    #filename = 'photo.jpg'
    output_file = os.path.join(os.path.expanduser("~"),"user_space", "static", filename)



    # Commande à exécuter pour prendre la photo
    cmd = ['libcamera-still', '-t', str(duration), '-n', '--width', str(width), '--height', str(height), '-o', output_file]

    # Exécuter la commande
    subprocess.run(cmd)

    #Commander à exécuter pour copier la photo
    cmd = ['cp', output_file, '/home/camera/user_space/static/photo_recent.jpg']
    subprocess.run(cmd)


    return output_file[1:]

def keep_picture(output_file, reponse):
    if reponse == 'non':
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
