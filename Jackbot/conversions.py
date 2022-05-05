#2048 units
def convertDegreesToTalonFXUnits(float: num) -> float:
    #Just need to multiply this factor to the number of degrees
    conversionFactor = 2048/360
    num *= conversionFactor
    return num

def sign(num) -> int:
    if num > 0:
        return 1
    elif num < 0:
        return -1
    else:
        return 0
