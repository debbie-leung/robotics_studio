from lx16a import *
from math import sin, cos
# This is the port that the controller board is connected to
# This will be different for different computers
# On Windows, try the ports COM1, COM2, COM3, etc... 
# On Raspbian, try each port in /dev/ 

LX16A.initialize('/dev/ttyUSB0')

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

for i in range(8):
    print(servos[i].IDRead())
    #1. Query motor positions
    print(servos[i].getPhysicalPos())
    #2. Enable/disable motors
    print(servos[i].loadOrUnloadRead())
    #3. Query motor power
    print(servos[i].vInRead())
    #4. Flash robot LED 1 time
    print(servos[i].LEDCtrlRead())
    servos[i].LEDCtrlWrite(1)
    print(servos[i].LEDCtrlRead())
    servos[i].LEDCtrlWrite(0)