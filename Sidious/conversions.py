import math


class Conversions:
    """Convert units for autonomous routines."""
     
    def convertTalonSRXNativeUnitsToWPILibTrajectoryUnits(self, talonVelocity: float, wheelDiameter: float, usingMetric: bool, ticksPerRevolution: int) -> float:
        """Convert the values from native Talon units (ticks/100ms) to WPITrajectory Units (m/s)"""
        
        self.result = talonVelocity

        #Convert from ticks/100ms to ticks/s
        self.result = self.result*10.0

        self.circumference = 0.0

        if usingMetric:
            self.circumference = math.pi * wheelDiameter
        
        else :
            self.diameterInMeters = wheelDiameter * 0.3048
            self.circumference = math.pi*self.diameterInMeters
        
        self.metersPerTick = self.circumference/ticksPerRevolution

        self.result = self.result*self.metersPerTick

        return self.result
    
    def convertWPILibTrajectoryUnitsToTalonSRXNativeUnits(self, metersPerSecond: float, wheelDiameter: float, givenMetric: bool, ticksPerRevolution: int) -> float:
        """Convert the values from WPITrajectory Units (m/s) to native Talon units (ticks/100ms)"""
        
        self.result = metersPerSecond

        self.circumference = 0.0

        if givenMetric:
            self.circumference = math.pi*wheelDiameter

        else :
            self.diameterInMeters = wheelDiameter * 0.3048
            self.circumference = math.pi*self.diameterInMeters
        
        self.ticksPerMeter = ticksPerRevolution/self.circumference

        self.result = self.result*self.ticksPerMeter

        self.result = self.result*0.1

        return self.result

    def convertTalonEncoderTicksToMeters(self, ticks: int, diameter: float, ticksPerRevolution: float, givenMetric: bool) -> float:

        self.result = ticks

        self.circumference = 0.0

        if givenMetric:
            self.circumference = math.pi*diameter

        else: 
            self.diameterInMeters = diameter*0.3048
            self.circumference = math.pi*self.diameterInMeters
        
        self.metersPerTick = self.circumference/ticksPerRevolution

        self.result = self.result*self.metersPerTick

        return self.result

    def convertFeetToMeters(self, value: float) -> float:
        """Converts feet to meters."""
        return value*0.3048

    def convertMetersToFeet(self, value: float) -> float:
        """Converts meters to feet."""
        return value/0.3048
    

