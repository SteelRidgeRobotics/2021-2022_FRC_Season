import commands2
import ctre
import constants
import math
import wpimath.controller.PIDController as PIDController
class SwerveWheel():
    def __init__(self, directionMotor, speedMotor):
        self.pidController = PIDController
        
    def setPID(P, I, D):
        self.pidController.setPID()
    #pid controller
    #direction motor
    #direction sensor
    
class SwerveDrive(commands2.SubsystemBase):
    def __init__(self) -> None:
        super().__init__()
        #init motors
        #init encoders
        
        #need to create some way to convert from Talon FX units to degrees
        # May try to make a file/method to use the position to do so
        
        #call gyro
        
        
