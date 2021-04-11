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
#f.homing(servos, 1000)
time.sleep(2.15)

# Read motors
FR = servos[0] #front_right
BR = servos[1] #back_right
FL = servos[2] #front_left
BL = servos[3] #back_left
SLT = servos[4] #side_left_top 
SLB = servos[5] #side_left_bottom 
SRT = servos[6] #side_right_top
SRB = servos[7] #side_right_bottom

start_time = time.time()

t = 0
w = 2
a = 120
b = 50
c = 0

flag = True
while flag:
    time_now = time.time()

    # First move from 0-7s: wavy arms
    while t < 8.5:
        FR.moveTimeWrite(a+b*sin(w*t+c))
        SRB.moveTimeWrite(a+b*cos(w*t+c))
        BR.moveTimeWrite(a+b*sin(w*t+c))
        BL.moveTimeWrite(a+b*cos(w*t+c))
        SLB.moveTimeWrite(a+b*sin(w*t+c))        
        FL.moveTimeWrite(a+b*cos(w*t+c))   
        t += 0.0075

    # if time.time() == 7:
    f.homing(servos, 200)
    time.sleep(0.5)

    # Second move 7-17s: swirl around
    t = 0
    while t < 10:
        FR.moveTimeWrite(a+30*sin(w*t+c))
        SRB.moveTimeWrite(a+30*sin(w*t+c))
        BR.moveTimeWrite(a+30*sin(w*t+10))
        BL.moveTimeWrite(a+30*sin(w*t+10))
        SLB.moveTimeWrite(a+30*sin(w*t+20))
        FL.moveTimeWrite(a+30*sin(w*t+20))     
        t += 0.0075
    
    # Third move 17-25s: lift arms and move front back legs
    f.homing(servos, 300)
    time.sleep(0.25)
    
    SRT.moveTimeWrite(150, time=200)
    SLT.moveTimeWrite(150, time=200)
    time.sleep(0.4)
    
    t = 0
    while t < 11:
        SRB.moveTimeWrite(a+b*sin(w*t+c))
        SRT.moveTimeWrite(130+30*cos(w*t+c))
        SLT.moveTimeWrite(130+30*sin(w*t+c))
        SLB.moveTimeWrite(a+b*cos(w*t+c))
        FR.moveTimeWrite(a+b*sin(w*t+c))
        BL.moveTimeWrite(a+b*sin(w*t+c))
        FL.moveTimeWrite(a+b*sin(w*t+c))
        BR.moveTimeWrite(a+b*sin(w*t+c))
        t += 0.01
    
    # Fourth move 24-32s: lift each motor up
    f.homing(servos, 300)
    time.sleep(0.5)
    
    FR.moveTimeWrite(180, time=500)
    time.sleep(0.2)
    SRB.moveTimeWrite(180, time=500)
    time.sleep(0.2)
    BR.moveTimeWrite(180, time=500)
    time.sleep(0.2)
    BL.moveTimeWrite(180, time=500)
    time.sleep(0.2)
    SLB.moveTimeWrite(180, time=500)
    time.sleep(0.2)
    FL.moveTimeWrite(180, time=500)
    time.sleep(1)
    
    FL.moveTimeWrite(120, time=500)
    time.sleep(0.2)
    SLB.moveTimeWrite(120, time=500)
    time.sleep(0.2)
    BL.moveTimeWrite(120, time=500)
    time.sleep(0.2)
    BR.moveTimeWrite(120, time=500)
    time.sleep(0.2)
    SRB.moveTimeWrite(120, time=500)
    time.sleep(0.2)
    FR.moveTimeWrite(120, time=500)
    time.sleep(0.9)
    
    SRT.moveTimeWrite(180, time=1000)
    time.sleep(0.9)
    SLT.moveTimeWrite(180, time=1000)
    time.sleep(0.9)
    SRT.moveTimeWrite(120, time=1000)
    time.sleep(0.9)
    SLT.moveTimeWrite(120, time=1000)
    time.sleep(0.9)
    
    # Fifth move: stand on toes
    f.homing(servos, 300)
    time.sleep(0.5)
    
    t = 0
    while t < 9:
        SRB.moveTimeWrite(a+b*cos(w*t+c))
        FR.moveTimeWrite(a+b*cos(w*t+c))
        BR.moveTimeWrite(a+b*cos(w*t+c))
        FL.moveTimeWrite(a+b*cos(w*t+c))
        BL.moveTimeWrite(a+b*cos(w*t+c))
        SLB.moveTimeWrite(a+b*cos(w*t+c))
        t += 0.0075
    
    SRB.moveTimeWrite(120, time=50)
    FR.moveTimeWrite(120, time=50)
    BR.moveTimeWrite(120, time=50)
    time.sleep(0.75)
        
    FL.moveTimeWrite(120, time=50)
    BL.moveTimeWrite(120, time=50)
    SLB.moveTimeWrite(120, time=50)
    time.sleep(1)
    
    t = 0
    while t < 9:
        SRB.moveTimeWrite(a+b*sin(w*t+c))
        FR.moveTimeWrite(a+b*sin(w*t+c))
        BR.moveTimeWrite(a+b*sin(w*t+c))
        FL.moveTimeWrite(a+b*sin(w*t+c))
        BL.moveTimeWrite(a+b*sin(w*t+c))
        SLB.moveTimeWrite(a+b*sin(w*t+c))
        t += 0.0075
 
    FL.moveTimeWrite(120)
    BL.moveTimeWrite(120)
    SLB.moveTimeWrite(120)
    time.sleep(0.5)
    
    SRB.moveTimeWrite(120)
    FR.moveTimeWrite(120)
    BR.moveTimeWrite(120)
    time.sleep(1.5)
         
    # Sixth move: move sideways
    
    t = 0
    while t < 8:
        SRB.moveTimeWrite(a+40*sin(w*t+c))
        FR.moveTimeWrite(a+40*sin(w*t+c))
        BR.moveTimeWrite(a+40*sin(w*t+c))
        FL.moveTimeWrite(a+40*cos(w*t+c))
        BL.moveTimeWrite(a+40*cos(w*t+c))
        SLB.moveTimeWrite(a+40*cos(w*t+c))
        t += 0.0075
        
    FL.moveTimeWrite(120, time=500)
    time.sleep(0.2)
    SLB.moveTimeWrite(120, time=500)
    time.sleep(0.2)
    BL.moveTimeWrite(120, time=500)
    time.sleep(0.2)
    BR.moveTimeWrite(120, time=500)
    time.sleep(0.2)
    SRB.moveTimeWrite(120, time=500)
    time.sleep(0.2)
    FR.moveTimeWrite(120, time=500)
    time.sleep(0.75)
    
    t = 0
    while t < 8:
        SRB.moveTimeWrite(a+40*cos(w*t+c))
        FR.moveTimeWrite(a+40*cos(w*t+c))
        BR.moveTimeWrite(a+40*cos(w*t+c))
        FL.moveTimeWrite(a+40*sin(w*t+c))
        BL.moveTimeWrite(a+40*sin(w*t+c))
        SLB.moveTimeWrite(a+40*sin(w*t+c))
        t += 0.0075
    
    FR.moveTimeWrite(120, time=500)
    time.sleep(0.75)
    SRB.moveTimeWrite(120, time=500)
    time.sleep(0.2)
    BR.moveTimeWrite(120, time=500)
    time.sleep(0.2)
    BL.moveTimeWrite(120, time=500)
    time.sleep(0.2)
    SLB.moveTimeWrite(120, time=500)
    time.sleep(0.2)
    FL.moveTimeWrite(120, time=500)
    time.sleep(0.75)
    
    
    # Weird code
#    t = 0
#    while t < 5:
#        FR.moveTimeWrite(a+b*sin(w*t+c))        
#        FR.moveTimeWrite(a+b*sin(w*t+c))
#        BR.moveTimeWrite(a+b*cos(w*t+c))
#        BL.moveTimeWrite(a+b*cos(w*t+c))
#        SRT.moveTimeWrite(a+20*cos(w*t+c))
#        SLT.moveTimeWrite(a+20*sin(w*t+c))
#        t += 0.0075
    
#    t = 0
#    while t < 12:
#        side_right_bottom.moveTimeWrite(a+b*cos(w*t+c))
#        side_left_bottom.moveTimeWrite(a+b*sin(w*t+c))
#        front_right.moveTimeWrite(a+b*cos(w*t+c))
#        back_left.moveTimeWrite(a+b*cos(w*t+c))
#        front_left.moveTimeWrite(a+b*cos(w*t+c))
#        back_right.moveTimeWrite(a+b*cos(w*t+c))
#        t += 0.0075
    
    flag = False