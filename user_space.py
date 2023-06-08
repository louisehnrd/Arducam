from picture import take_picture, suppr_picture, last_picture, param_zoom
from flask import Flask, redirect, url_for, request, render_template, send_from_directory, make_response
import os
from time import sleep
from picamera2 import Picamera2, Metadata
from libcamera import controls

os.environ['LD_LIBRARY_PATH'] = '/usr/lib/arm-linux-gnueabihf/'

app = Flask(__name__)
app.static_folder = 'static'
app.config["DEBUG"] = True

@app.route('/', methods=['POST', 'GET'])
def choice():
    if request.method == 'POST':
        valeur_select = request.form['action']
        if valeur_select == 'Picture':
            return redirect(url_for('param'))
        else :
           return redirect(url_for('video'))
    return render_template('form.html')


@app.route('/Param', methods=['POST', 'GET'])
def param():
    #initialisation variable
    global width, height, zoom_factor,lens_position
    """
    width = False
    height = False
    zoom_factor = False
    lens_position = False
"""
    if request.method == 'POST':
        if 'parameters' in request.form :
            #choice parameters & take picture
            width = int(request.form['width'])
            height = int(request.form['height'])
            zoom_factor = request.form['zoom_factor']
            lens_position = request.form['lens_position']
            take_picture(width, height,zoom_factor,lens_position)
            print(width)
            return redirect(url_for('param'))
        
        elif 'choice' in request.form :
            if width is None :
                #à modifier pour s'assurer que ça ne fasse pas d'erreur
                return "You didn't take a photo. Please choose the photo parameters and click on 'submit'."
            else : 
                #display & choice keep picture
                reponse = request.form['reponse']
                #Deletes the photo and re-selects the settings
                if reponse == 'non' :
                    path_file = last_picture()
                    suppr_picture(path_file)
                    return redirect(url_for('param'))
                #send to picture page
                else :
                    return redirect(url_for('picture', width=width, height=height, zoom_factor=zoom_factor, lens_position=lens_position))
    
    return render_template('param.html')

@app.route('/Picture/<width>/<height>/<zoom_factor>/<lens_position>', methods=['POST', 'GET'])
def picture(width,height,zoom_factor,lens_position):
    if request.method == 'POST':
        take_picture(width,height,zoom_factor,lens_position)
        sleep(10)
    return render_template('picture.html')


@app.route('/Video', methods=['POST', 'GET'])
def video():
    return 'yes'


if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5000)
