from lx16a import *
from math import *
import helper_functions as f
# This is the port that the controller board is connected to
# This will be different for different computers
# On Windows, try the ports COM1, COM2, COM3, etc... 
# On Raspbian, try each port in /dev/ 

LX16A.initialize('/dev/ttyUSB0')

servos = f.readMotor()

for i in range(8):
    # Query motor position
    if not (120 <= servos[i].getPhysicalPos() <= 240):
        print("Motor %d is %f and not in range" % (servos[i].IDRead(), servos[i].getPhysicalPos()))
        servos[i].moveTimeWrite(120, time=5000)

    # Query motor temp
    # Query motor current
    print("motor: %d voltage: %f temperature: %f" % (servos[i].IDRead(), servos[i].vInRead(), servos[i].tempRead()))
           
# Check communication error by printing to terminal
print("Established communication")
