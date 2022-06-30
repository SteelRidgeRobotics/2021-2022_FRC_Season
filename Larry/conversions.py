import math
def convertDegreesToTalonFXUnits(num: float) -> float:
    conversionFactor = 2048/360
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
        
def convertJoystickInputToDegrees(x: float, y: float):
    return float(math.degrees(math.atan2(y, x)))

def deadband(value: float, band: float):
    if math.fabs(value) <= band:
        return 0
    else:
        return value