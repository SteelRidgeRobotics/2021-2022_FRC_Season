import commands2
import ctre
import constants
import math
import wpimath.controller.PIDController as PIDController
import numpy
class SwerveWheel:
    def __init__(self, directionMotor: ctre.TalonFX, speedMotor: ctre.TalonFX, P: float, I: float, D: float):
        # we assume that all the motors are the same: Falcon 500s
        self.pidController = PIDController
        self.pidController.setPID(P, I, D)
        self.directionMotor = directionMotor
        self.speedMotor = speedMotor
        
    def setPID(self, P, I, D) -> None: # incase if we need to reset it, but we probably don't, so this may be deleted later
        self.pidController.setPID(P, I, D)
    #pid controller
    def closestAngle(self, a: float, b: float):
        # this converts to angles
        dir = float((b % 360.0) - (a % 360))
        
        if math.abs(dir) > 180.0:
            dir = -(numpy.sign(dir) * 360.0) + dir
        return dir
    
    def setDirection(self, setpoint: float):
        # use motion magic if able
        #direction motor
        self.directionMotor.set(ctre.TalonFXControleMode.MotionMagic, self.setpoint)
        """
        self.pidController.reset()
        self.pidController.setSetpoint(setpoint)
        error = self.pidController.calculate(directionMotor.getSelectedSensorPosition(), setpoint)
        output = 0
        if not self.pidController.atSetpoint():
            output = max(min(error, 1), -1)
        # may have to be voltage instead of position
        self.directionMotor.set(ctre.TalonFXControlMode.Position, output)
        """
    
class SwerveDrive(commands2.SubsystemBase):
    def __init__(self) -> None:
        super().__init__()
        #init motors
        #init encoders
        
        #need to create some way to convert from Talon FX units to degrees
        # May try to make a file/method to use the position to do so
        
        #call gyro
        
        
