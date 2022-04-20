import commands2
import ctre
import constants
import math
import conversions
import wpimath.controller.PIDController as PIDController
class SwerveWheel:
    def __init__(self, directionMotor: ctre.TalonFX, speedMotor: ctre.TalonFX, P: float, I: float, D: float):
        # we assume that all the motors are the same: Falcon 500s
        self.pidController = PIDController
        self.pidController.setPID(P, I, D)
        self.directionMotor = directionMotor
        self.speedMotor = speedMotor
        
    def setPID(self, P, I, D) -> None: # incase if we need to reset it, but we probably don't, so this may be deleted later
        # Note: we could just set the pid outside of this class if we don't use the PIDController
        self.pidController.setPID(P, I, D)
    #pid controller
    def closestAngle(self, a: float, b: float) -> float:
        # this converts to angles & get the distance between the two. b is the endpoint while a is the start point
        dir = float((b % 360.0) - (a % 360.0))
        
        if math.abs(dir) > 180.0:
            # we find the sign of dir, (+1, -1, or 0), and multiply it by 360. We then take that negative and add dir
            dir = -(conversions.sign(dir) * 360.0) + dir
        return dir
    
    def setDirection(self, setpoint: float):
        #get current angle
        currentAngle = float(directionMotor.getSelectedSensorPosition())
        # find closest angle
        setpointAngle = closestAngle(currentAngle, setpoint)
        # find closest angle + 180
        setpointAngleFlipped = closestAngle(currentAngle, setpoint + 180.0)
        if math.abs(setpointAngle) <= math.abs(setpointAngleFlipped):
            # unflip motor & use setpoint
            # gain is positive
        else:
            # flip motor direction
            # gain is negative
            
        # use the fastest way to get to angle wanted
        self.directionMotor.set(ctre.TalonFXControlMode.MotionMagic, currentAngle + closestAngle(currentAngle, setpoint)) # use motion magic if able
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
    def setSpeed(speed: float) -> None:
        speedMotor.set(ctre.TalonFXControlMode.PercentOutput, speed)
class SwerveDrive(commands2.SubsystemBase):
    def __init__(self) -> None:
        super().__init__()
        #init motors
        #init encoders
        
        #need to create some way to convert from Talon FX units to degrees
        # May try to make a file/method to use the position to do so
        
        #call gyro
        
        
