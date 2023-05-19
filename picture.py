import os
import time
from time import sleep
import subprocess

def take_picture(duration, width, height):
    #initialization
    #delay = 600  #10 min
    #duration = 5000

    # Chemin et nom de fichier de sortie de l'image
    timestamp = time.strftime('%Y.%m.%d-%H:%M:%S')
    filename = 'photo_{}.jpg'.format(timestamp)
    output_file = os.path.join(os.path.expanduser("~"), "Pictures", filename)

    # Commande à exécuter
    cmd = ['libcamera-still', '-t', str(duration), '-n', '--width', str(width), '--height', str(height), '-o', output_file]

    # Exécuter la commande
    subprocess.run(cmd)