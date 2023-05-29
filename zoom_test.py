from picamera2 import Picamera2, Preview
from picamera2.encoders import H264Encoder
import os
import time
import sys

def zoom_picture(zoom_factor):
    arducam.start()

    size = arducam.capture_metadata()['ScalerCrop'][zoom_factor:]
    full_res = arducam.camera_properties['PixelArraySize']
    #print(full_res)

    #zoom progressif
    for _ in range(20):
        # This syncs us to the arrival of a new camera frame:
        arducam.capture_metadata()

        size = [int(s * 0.95) for s in size]
        offset = [(r - s) // 2 for r, s in zip(full_res, size)]
        arducam.set_controls({"ScalerCrop": offset + size})

    #chemin du fichier sortant
    timestamp = time.strftime('%Y.%m.%d-%H:%M:%S')
    filename = 'picture_{}.jpg'.format(timestamp)
    output_file = os.path.join(os.path.expanduser("~"), "Pictures", filename)

    #prend un photo
    arducam.capture_file(output_file)
    
    arducam.close()


def video():

    #temps de la capture de la video
    encoder = H264Encoder(10000000)

    #prise de la video
    arducam.start_recording(encoder, 'video.h264')
    time.sleep(10)
    arducam.stop_recording()



if len(sys.argv) < 4:
    print("missing input file")
    sys.exit()
if len(sys.argv) > 4:
    print("too many argument")
    sys.exit()

#Initialisation des variables
zoom_factor = int(sys.argv[1])
width = int(sys.argv[2])
height = int(sys.argv[3])

# Initialiser la caméra PiCamera
arducam = Picamera2()
#arducam.start_preview(Preview.QTGL)

#configuration en plein résolution
capture_config = arducam.create_still_configuration(main={"size": (width,height)})
arducam.configure(capture_config)

video_config = arducam.create_video_configuration()
#arducam.configure(video_config)
#video()

while(1):
    zoom_picture(zoom_factor)
    sleep(600)

