import commands2
import ctre
import constants
import math
import wpimath.controller.PIDController as PIDController
class SwerveWheel():
    def __init__(self, directionMotor: ctre.TalonFX, speedMotor: ctre.TalonFX, P: float, I: float, D: float):
        # we assume that all the motors are the same: Falcon 500s
        self.pidController = PIDController
        self.pidController.setPID(P, I, D)
        self.directionMotor = directionMotor
        self.speedMotor = speedMotor
        
    def setPID(self, P, I, D) -> None: # incase if we need to reset it, but we probably don't, so this may be deleted later
        self.pidController.setPID(P, I, D)
    #pid controller
    def setDirection(self, setpoint: float):
        self.pidController.reset()
        self.pidController.setSetpoint(setpoint)
        error = self.pidController.calculate(directionMotor.getSelectedSensorPosition(), setpoint)
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
        
        
