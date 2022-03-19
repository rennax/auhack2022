from flask import Flask, render_template, redirect
import datetime
from gpiozero import Servo
from time import sleep

isRunning = False

app = Flask(__name__)


@app.route("/")
def hello():
   now = datetime.datetime.now()
   timeString = now.strftime("%Y-%m-%d %H:%M")
   templateData = {
      'title' : 'HELLO!',
      'time': timeString
      }
   return render_template('index.html', **templateData)

@app.route("/<servoNumber>")
def activate_servo(servoNumber):
    global isRunning
    if isRunning == True:
        return redirect("/")

    isRunning = True
    servoDev = None
    print(servoNumber)


    if servoNumber == "5":
        servoDev = Servo(5, min_pulse_width=0.5/1000, max_pulse_width = 2.4/1000)
    elif servoNumber == "6":
        servoDev = Servo(6,  min_pulse_width=0.5/1000, max_pulse_width = 2.4/1000)
    elif servoNumber == "13":
        servoDev = Servo(13, min_pulse_width=0.5/1000, max_pulse_width = 2.4/1000)
    else:
        return redirect("/", 404)

    
    servoDev.min()
    sleep(0.5)
    servoDev.max()
    sleep(0.5)
    
    isRunning = False
    return redirect("/")

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)