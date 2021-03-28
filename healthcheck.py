from lx16a import *
from math import *
import helper_functions as f
# This is the port that the controller board is connected to
# This will be different for different computers
# On Windows, try the ports COM1, COM2, COM3, etc... 
# On Raspbian, try each port in /dev/ 

LX16A.initialize('/dev/ttyUSB0')

servos = f.readMotor()

# Query motor position
def 

# Query motor temp

# Query motor current

# Query 
