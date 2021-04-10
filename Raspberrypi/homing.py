from lx16a import *
from math import sin, cos
# This is the port that the controller board is connected to
# This will be different for different computers
# On Windows, try the ports COM1, COM2, COM3, etc... 
# On Raspbian, try each port in /dev/ 

LX16A.initialize('/dev/ttyUSB0')

# 1. Query motor positions
servos = []
servo11 = LX16A(11)
servos.append(servo11)
servo12 = LX16A(12)
servos.append(servo12)
servo13 = LX16A(13)
servos.append(servo13)
servo14 = LX16A(14)
servos.append(servo14)
servo21 = LX16A(21)
servos.append(servo21)
servo22 = LX16A(22)
servos.append(servo22)
servo23 = LX16A(23)
servos.append(servo23)
servo24 = LX16A(24)
servos.append(servo24)

print(servo11.IDRead())
print(servo11.getPhysicalPos())
print(servos)

# 2. Move to initial home positions (120 degrees)
for i in range(8):
    if (servos[i].getPhysicalPos() != 120):
        servos[i].moveTimeWrite(120, time=1000)
    print(servos[i].getPhysicalPos())
        
# Check motors have reached home configurations
#print(assert(servos[i].getPhysicalPos() == 120 for i in range(8)))
