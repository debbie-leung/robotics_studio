from lx16a import *
from math import sin, cos
import numpy as np
import matplotlib.pyplot as plt

# This is the port that the controller board is connected to
# This will be different for different computers
# On Windows, try the ports COM1, COM2, COM3, etc... 
# On Raspbian, try each port in /dev/ 

LX16A.initialize('/dev/ttyUSB0')

# There should two servos connected, with IDs 1 and 2
servo11 = LX16A(11)
print(servo11.IDRead())
print(servo11.getPhysicalPos())
#servo1.moveTimeWrite(120, time=1000)
servo12 = LX16A(12)
print(servo12.IDRead())
print(servo12.getPhysicalPos())
servo13 = LX16A(13)
print(servo13.IDRead())
print(servo13.getPhysicalPos())
servo14 = LX16A(14)
print(servo14.IDRead())
print(servo14.getPhysicalPos())
#print(servo1.moveTimeRead())
#servo1.moveTimeWrite(120, time=10000) 

t = 0
w = 2
a = 120
b = 50
c = 0

y_servo11 = []
while t < 10:
    # Two sine waves out of phase   
    servo11.moveTimeWrite(a+b*sin(w*t+c))
    #y_servo11.append(servo11.getPhysicalPos())
    servo12.moveTimeWrite(a+b*cos(w*t+c))
    servo13.moveTimeWrite(a+b*cos(w*t+c))
    servo14.moveTimeWrite(a+b*sin(w*t+c))
    t += 0.005
    
#time = np.arange(0, t, 0.01)
#plt.plot(time, y_servo11)
#plt.show()
    