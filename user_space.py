import picture
from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)
app.config["DEBUG"]=True

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
    """if request.method == 'POST':
        duration = request.form['duration']
        width = request.form['width']
        height = request.form['height']
        picture.take_picture(duration, width, height)
        return 'photo prise' """
    return render_template('picture.html')
    

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
