import math
import constants

class Conversions:
    def convertTalonUnitsToTrajectoryUnits(self, talonVelocity: float, wheelDiameter: float, usingMetric: bool, ticksPerRevolution: int) -> float:
        # Convert values like the title of the method suggests
        
        result = talonVelocity
        
        result *= 10.0
        
        circumference = 0.0
        
        if usingMetric:
            circumference = math.pi * wheelDiameter
        else:
            diameterInMeters = wheelDiameter * 0.3048
            circumference = math.pi * diameterInMeters
            
        metersPerTick = circumference/(ticksPerRevolution*constants.kgearRatio)
        
        result *= metersPerTick
        
        return result
    def convertTrajectoryUnitsToTalonUnits(self, metersPerSecond: float, wheelDiameter: float, givenMetric: bool, ticksPerRevolution: int) -> float:
        
        result = metersPerSecond
        
        circumference = 0.0
        
        if givenMetric:
            circumference = math.pi * wheelDiameter
        else:
            diameterInMeters = wheelDiameter * 0.3048
            circumference = math.pi * diameterInMeters
            
        ticksPerMeter = (ticksPerRevolution*constants.kgearRatio)/circumference
        
        result *= ticksPerMeter
        
        result *= 0.1
        
        return result
    
    def convertTalonEncoderTicksToMeters(self, ticks: int, wheelDiameter: float, ticksPerRevolution: int, givenMetric: bool) -> bool:
        result = ticks
        
        circumference = 0
        
        if givenMetric:
            circumference = math.pi * wheelDiameter
        else:
            diameterInMeters = wheelDiameter * 0.3048
            circumference = math.pi * diameterInMeters
            
        metersPerTick = circumference/(ticksPerRevolution*constants.kgearRatio)
        result *= metersPerTick
        
        return result
    
    def convertFeetToMeters(self, value: float) -> float:
        return value*0.3048
    
    def convertMetersToFeet(self, value: float) -> float:
        return value*1/0.3048
        
           
