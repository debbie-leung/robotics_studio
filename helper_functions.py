from lx16a import *
from math import *

# Read motor function
def readMotor():
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
    return servos
