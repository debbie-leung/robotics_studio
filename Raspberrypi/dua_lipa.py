from lx16a import *
from math import sin, cos
import helper_functions as f
import time
# This is the port that the controller board is connected to
# This will be different for different computers
# On Windows, try the ports COM1, COM2, COM3, etc... 
# On Raspbian, try each port in /dev/ 

LX16A.initialize('/dev/ttyUSB0')

# Read motors
servos = f.readMotor()
print(servos)

# Perform homing
f.homing(10000)

# Read motors
front_right = servos[0] #LX16A(11)
back_right = servos[1]
front_left = servos[2]
back_left = servos[3]
side_left_top = servos[4]
side_left_bottom = servos[5]
side_right_top = servos[6]
side_right_bottom = servos[7]

start_time = time.time()

t = 0
w = 2.07
a = 120
b = 50
c = 0

while True:
    time_now = time.time()

    # First move from 0-7s
    while t < 7:
        front_right.moveTimeWrite(a+b*sin(w*t+c), time=1000)
        back_left.moveTimeWrite(a+b*sin(w*t+c), time=1000)
        front_left.moveTimeWrite(a+b*cos(w*t+c), time=1000)
        back_right.moveTimeWrite(a+b*cos(w*t+c),time=1000)
    	t += 0.01
    time.sleep(1)

    # if time.time() == 7:
    f.homing(1000)

    # Second move 7-17s
    side_right_top.moveTimeWrite(180, time=3)
    side_left_top.moveTimeWrite(180, time=3)

    side_right_bottom.moveTimeWrite(a+b*sin(w*t+c), time=1000)
    side_left_bottom.moveTimeWrite(a+b*cos(w*t+c), time=1000)
    front_right.moveTimeWrite(a+b*sin(w*t+c), time=1000)
    back_left.moveTimeWrite(a+b*sin(w*t+c), time=1000)
    front_left.moveTimeWrite(a+b*sin(w*t+c), time=1000)
    back_right.moveTimeWrite(a+b*sin(w*t+c),time=1000)

    # # Third move 17-24s (switch from Second move)
    # # if time.time() == 17:

    # side_right_bottom.moveTimeWrite(a+b*cos(w*t+c), time=1000)
    # side_left_bottom.moveTimeWrite(a+b*sin(w*t+c), time=1000)
    # front_right.moveTimeWrite(a+b*cos(w*t+c), time=1000)
    # back_left.moveTimeWrite(a+b*cos(w*t+c), time=1000)
    # front_left.moveTimeWrite(a+b*cos(w*t+c), time=1000)
    # back_right.moveTimeWrite(a+b*cos(w*t+c),time=1000)

	