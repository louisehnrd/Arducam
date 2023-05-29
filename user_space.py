from picture import take_picture, keep_picture, last_picture
from flask import Flask, redirect, url_for, request, render_template, send_from_directory, make_response
import os

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
    if request.method == 'POST':
        duration = request.form['duration']
        width = request.form['width']
        height = request.form['height']
        output_file = take_picture(int(duration), int(width), int(height))
        print(output_file)
        return redirect(url_for('keep_pic'))
    return render_template('picture.html')

@app.route('/Display', methods=['POST', 'GET'])
def keep_pic():
    #output_file = request.args.get('output_file')
    if request.method == 'POST':
        reponse = request.form['reponse']
        path_file = last_picture()
        keep_picture(path_file, reponse)
        return 'yes'
    else :
        response = make_response(render_template('display_pic.html'))
        response.headers['Cache-Control'] = 'no-cache'
        return response

@app.route('/Video')
def video():
   return 'yes'

"""
@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success',name = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))
"""

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5000)

