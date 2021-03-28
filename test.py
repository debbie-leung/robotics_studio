from lx16a import *
from math import sin, cos
# This is the port that the controller board is connected to
# This will be different for different computers
# On Windows, try the ports COM1, COM2, COM3, etc... 
# On Raspbian, try each port in /dev/ 

LX16A.initialize('/dev/ttyUSB0')

# There should two servos connected, with IDs 1 and 2
servo21 = LX16A(21)
print(servo21.IDRead())
print(servo21.getPhysicalPos())
#servo1.moveTimeWrite(120, time=1000)
servo22 = LX16A(22)
print(servo22.IDRead())
print(servo22.getPhysicalPos())
servo23 = LX16A(23)
print(servo23.IDRead())
print(servo23.getPhysicalPos())
servo24 = LX16A(24)
print(servo24.IDRead())
print(servo24.getPhysicalPos())
#print(servo1.moveTimeRead())
#servo1.moveTimeWrite(120, time=10000) 

servo21.moveTimeWrite(100, time = 10000)
servo23.moveTimeWrite(100, time = 10000)

t=0
w = 2
a = 120
b = 50
c = 0

while True:
    # Two sine waves out of phase   
    
    servo22.moveTimeWrite(a+b*sin(w*t+c), time = 10)
    
    servo24.moveTimeWrite(a+b*cos(w*t+c), time = 10)
    t += 0.01
    
