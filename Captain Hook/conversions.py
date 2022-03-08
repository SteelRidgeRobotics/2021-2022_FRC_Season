import math
import constants

class Conversions:
    def convertTalonUnitsToTrajectoryUnits(self, talonVelocity: float, wheelDiameter: float, usingMetric: bool, ticksPerRevolutiom: int) -> float:
        # Convert values like the title of the method suggests
        
        result = talonVelocity
        
        result *= 10.0
        
        circumference = 0.0
        
        if usingMetric:
            circumference = math.pi * wheelDiameter
        else:
            diameterInMeters = wheelDiameter * 0.3048
            circumference = math.pi * diameterInMeters
            
        metersPerTick = (ticksPerRevelution*constants.kgearRatio)/circumference
        
        result *= ticksPerMeter
        
        result *= 0.1
        
        return result
    def convertTrajectoryUnitsToTalonUnits(self, metersPerSecond: float, wheelDiameter: float, givenMetric: bool, ticksPerRevolution: int) -> float:
        
        result = metersPerSecond
        
        circumference = 0.0
        
        if givenMetric:
            circumference = math.pi * wheelDiameter
        else:
            diameterInMeters = wheelDiameter * 0.3048
            circumference = math.pi * diameterInMeters
            
        metersPerTick = circumference/(ticksPerRevolution*constants.kgearRatio)
        
        result *= metersPerTick
        
        return result
