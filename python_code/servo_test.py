from gpiozero import Servo
from time import sleep

servo1 = Servo(13)
servo2 = Servo(5)
servo3 = Servo(6)

servo1.min()
servo2.min()
servo3.min()
sleep(0.5)
servo1.mid()
servo2.mid()
servo3.mid()
sleep(0.5)
servo1.max()
servo2.max()
servo3.max()
sleep(0.5)

