from picture import take_picture, suppr_picture, last_picture, param_zoom
from flask import Flask, redirect, url_for, request, render_template, send_from_directory, make_response
import os
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
            return redirect(url_for('picture'))
        else :
           return redirect(url_for('video'))
    return render_template('form.html')


@app.route('/Picture', methods=['POST', 'GET'])
def picture():
    #initialisation variable
    global width, height, zoom_factor
    width = False
    height = False
    zoom_factor = False
    lens_position = False

    if request.method == 'POST':
        if 'parameters' in request.form :
            #choice parameters & take picture
            width = int(request.form['width'])
            height = int(request.form['height'])
            zoom_factor = request.form['zoom_factor']
            lens_position = request.form['lens_position']
            take_picture(width, height,zoom_factor,lens_position)
            return redirect(url_for('picture'))
        
        elif 'choice' in request.form :
            if width == False :
                return "You didn't take a photo. Please choose the photo parameters and click on 'submit'."
            else : 
                #display & choice keep picture
                reponse = request.form['reponse']
                if reponse == 'non' :
                    path_file = last_picture()
                    suppr_picture(path_file)
                    return redirect(url_for('picture'))
                else :
                    print(width)
                    return 'yes'
    
    return render_template('picture.html')

@app.route('/Video', methods=['POST', 'GET'])
def video():
    return 'yes'


if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5000)
