from flask import Flask, render_template, redirect, url_for
import datetime
from gpiozero import Servo
from time import sleep
import os
isRunning = False
isSettingProject = False
app = Flask(__name__)


@app.route("/")
def index():
    now = datetime.datetime.now()
    timeString = now.strftime("%Y-%m-%d %H:%M")
    templateData = {
      'title' : 'HELLO!',
      'time': timeString
      }
    
    os.system('./webcam.sh')
    return render_template('index.html', **templateData)


@app.route("/project/<project>")
def set_project(project):
    global isSettingProject
    if isSettingProject == True:
        return redirect("/")
    
    isSettingProject = True
    bigServo = Servo(5, min_pulse_width=0.6/1000, max_pulse_width = 1.8/1000)


    if project == "1":
        bigServo.min()
    elif project == "2":
        bigServo.mid()
    elif project == "3":
        bigServo.max()
    else:
        return redirect("/", 404)
    sleep(1)

    isSettingProject = False
    return redirect(url_for('index'))

@app.route("/user/<servoNumber>")
def activate_servo(servoNumber):
    global isRunning
    if isRunning == True:
        return redirect("/")

    isRunning = True
    servoDev = None
    print(servoNumber)


    if servoNumber == "1":
        print("Servo 1")
        servoDev = Servo(6, min_pulse_width=0.5/1000, max_pulse_width = 2.4/1000)
    elif servoNumber == "2":
        print("Servo 2")
        servoDev = Servo(13,  min_pulse_width=0.5/1000, max_pulse_width = 2.4/1000)
    elif servoNumber == "3":
        print("Servo 3")
        servoDev = Servo(19, min_pulse_width=0.5/1000, max_pulse_width = 2.4/1000)
    else:
        return redirect("/", 404)

    
    servoDev.min()
    sleep(0.5)
    servoDev.max()
    sleep(0.5)
    
    isRunning = False
    return redirect(url_for('index'))

@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)