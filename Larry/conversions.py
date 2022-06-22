import math
def deadband(value: float, band: float):
    if math.fabs(value) <= band:
        return 0
    else:
        return value