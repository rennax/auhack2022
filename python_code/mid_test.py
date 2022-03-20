from gpiozero import Servo
from time import sleep

# Dispensers

# YAW
servo_big = Servo(5, min_pulse_width=0.6/1000, max_pulse_width = 1.8/1000)

def push_out():
    servo1 = Servo(6,  min_pulse_width=0.5/1000, max_pulse_width = 2.4/1000)
    servo2 = Servo(13, min_pulse_width=0.5/1000, max_pulse_width = 2.4/1000)
    servo3 = Servo(19, min_pulse_width=0.5/1000, max_pulse_width = 2.4/1000)
    servo1.min()
    servo2.min()
    servo3.min()
    sleep(0.5)
    servo1.max()
    servo2.max()
    servo3.max()
    sleep(0.5)


# Run test!

servo_big.mid()
push_out()
sleep(0.5)
push_out()
sleep(0.5)


#servo1.min()
#servo2.min()
#servo3.min()



