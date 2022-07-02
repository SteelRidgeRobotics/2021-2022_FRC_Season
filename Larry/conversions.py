import math

def convertDegreesToTalonFXUnits(num: float) -> float:
    conversionFactor = 2048/360 # 1 revolution of the falcon 500 is 2048 units
    num *= conversionFactor
    return num

def sign(num) -> int:
    if num > 0:
        # positive
        return 1
    elif num < 0:
        # negative
        return -1
    else:
        # zero
        return 0
        
def convertJoystickInputToDegrees(x: float, y: float): # this allows us to use the x and y values on the joystick and convert it into degrees
    return float(math.degrees(math.atan2(y, x)))

def deadband(value: float, band: float):
     # this makes sure that joystick drifting is not an issue. 
     # It takes the small values and forces it to be zero if smaller than the band value
    if math.fabs(value) <= band:
        return 0
    else:
        return value