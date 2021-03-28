from lx16a import *
from math import *
import helper_functions as f
# This is the port that the controller board is connected to
# This will be different for different computers
# On Windows, try the ports COM1, COM2, COM3, etc... 
# On Raspbian, try each port in /dev/ 

LX16A.initialize('/dev/ttyUSB0')

servos = f.readMotor()

# 1. Query motor positions
print("Motor positions: ")
for i in range(8):
    print(servos[i].IDRead(), servos[i].getPhysicalPos())

# 2. Move to initial home positions (120 degrees)
print("Motor voltage and temperature: ")
for i in range(8):
    servos[i].moveTimeWrite(120, time=5000)
    print("motor: %d voltage: %f temperature: %f" % (servos[i].IDRead(), servos[i].vInRead(), servos[i].tempRead()))
        
# 3. Check motors have reached home configurations within acceptable tolerance
for i in range(8):
    if not (isclose(servos[i].getPhysicalPos(), 120, abs_tol = 5)):
        print("Motor %d is %f and not in target position" % (servos[i].IDRead(), servos[i].getPhysicalPos()))
#print(assert(servos[i].getPhysicalPos() == 120 for i in range(8)))
