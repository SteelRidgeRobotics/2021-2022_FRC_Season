import math


class Conversions:
    """Convert units for autonomous routines."""
     
    def convertTalonSRXNativeUnitsToWPILibTrajectoryUnits(self, talonVelocity: float, wheelDiameter: float, usingMetric: bool, ticksPerRevolution: float) -> float:
        """Convert the values from native Talon units (ticks/100ms) to WPITrajectory Units (m/s)"""
        
        result = talonVelocity

        #Convert from ticks/100ms to ticks/s
        result = result*10.0

        circumference = 0.0

        if usingMetric:
            circumference = math.pi * wheelDiameter
        
        else :
            diameterInMeters = wheelDiameter * 0.3048
            circumference = math.pi*diameterInMeters
        
        metersPerTick = circumference/ticksPerRevolution

        result = result*metersPerTick

        return result
    
    def convertWPILibTrajectoryUnitsToTalonSRXNativeUnits(self, metersPerSecond: float, wheelDiameter: float, givenMetric: bool, ticksPerRevolution: float) -> float:
        """Convert the values from WPITrajectory Units (m/s) to native Talon units (ticks/100ms)"""
        
        result = metersPerSecond

        circumference = 0.0

        if givenMetric:
            circumference = math.pi*wheelDiameter

        else :
            diameterInMeters = wheelDiameter * 0.3048
            circumference = math.pi*diameterInMeters
        
        ticksPerMeter = ticksPerRevolution/circumference

        result = result*ticksPerMeter

        result = result*0.1

        return result

    def convertTalonEncoderTicksToMeters(self, ticks: int, diameter: float, ticksPerRevolution: float, givenMetric: bool) -> float:

        result = ticks

        circumference = 0.0

        if givenMetric:
            circumference = math.pi*diameter

        else: 
            diameterInMeters = diameter*0.3048
            circumference = math.pi*diameterInMeters
        
        metersPerTick = circumference/ticksPerRevolution

        result = result*metersPerTick

        return result

    def convertFeetToMeters(self, value: float) -> float:
        """Converts feet to meters."""
        return value*0.3048

    def convertMetersToFeet(self, value: float) -> float:
        """Converts meters to feet."""
        return value/0.3048
    

