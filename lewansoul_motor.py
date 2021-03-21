from lx16a import *
from math import sin, cos
# This is the port that the controller board is connected to
# This will be different for different computers
# On Windows, try the ports COM1, COM2, COM3, etc... 
# On Raspbian, try each port in /dev/ 

LX16A.initialize('/dev/ttyUSB0')

# There should two servos connected, with IDs 1 and 2
servo1 = LX16A(11)
print(servo1.IDRead())
servo2 = LX16A(13)
print(servo2.IDRead())
#print(servo1.moveTimeRead())
#servo1.moveTimeWrite(120, time=10000) 

t=0
while True:
    # Two sine waves out of phase
    servo1.moveTimeWrite(120+sin(t)*50)
    servo2.moveTimeWrite(120+cos(t)*50)
    t += 0.01