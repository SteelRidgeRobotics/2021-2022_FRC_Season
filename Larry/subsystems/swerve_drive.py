import commands2
import ctre
import constants
import math
import conversions
import wpimath.controller
class SwerveWheel:
    def __init__(self, directionMotor: ctre.TalonFX, speedMotor: ctre.TalonFX, P: float, I: float, D: float):
        # we assume that all the motors are the same: Falcon 500s
        self.pidController = wpimath.controller.PIDController(P, I, D, 0)
        self.directionMotor = directionMotor
        self.speedMotor = speedMotor
        
    def setPID(self, P, I, D) -> None: # incase if we need to reset it, but we probably don't, so this may be deleted later
        # Note: we could just set the pid outside of this class if we don't use the PIDController
        self.pidController.setPID(P, I, D)
    #pid controller
    def closestAngle(self, a: float, b: float) -> float:
        # this converts to angles & get the distance between the two. b is the endpoint while a is the start point
        dir = float((b % 360.0) - (a % 360.0))
        
        if math.fabs(dir) > 180.0:
            # we find the sign of dir, (+1, -1, or 0), and multiply it by 360. We then take that negative and add dir
            dir = -(conversions.Conversions.sign(dir) * 360.0) + dir
        return dir
    
    def setDirection(self, setpoint: float):
        #get current angle
        currentAngle = float(self.directionMotor.getSelectedSensorPosition())
        # find closest angle
        setpointAngle = self.closestAngle(currentAngle, setpoint)
        # find closest angle + 180
        setpointAngleFlipped = self.closestAngle(currentAngle, setpoint + 180.0)
        if math.fabs(setpointAngle) <= math.fabs(setpointAngleFlipped):
            # unflip motor & use setpoint
            self.directionMotor.set(ctre.TalonFXControlMode.MotionMagic, currentAngle + setpointAngle) # use motion magic if able
            # gain is positive
            self.directionMotor.setInverted(False)
        else:
            # flip motor direction
            self.directionMotor.set(ctre.TalonFXControlMode.MotionMagic, currentAngle + setpointAngleFlipped) # use motion magic if able
            # gain is negative
            self.directionMotor.setInverted(True)
            
        # use the fastest way to get to angle wanted
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
    def setSpeed(self, speed: float) -> None:
        self.speedMotor.set(ctre.TalonFXControlMode.PercentOutput, float(speed))

class SwerveDrive(commands2.SubsystemBase):
    def __init__(self) -> None:
        super().__init__()
        #init motors
        self.frontLeftDirection = ctre.TalonFX(constants.kleftFrontDirectionID)
        self.rearLeftDirection = ctre.TalonFX(constants.kleftRearDirectionID)
        self.frontRightDirection = ctre.TalonFX(constants.krightFrontDirectionID)
        self.rearRightDirection = ctre.TalonFX(constants.krightRearDirectionID)
        
        self.frontLeftSpeed = ctre.TalonFX(constants.kleftFrontSpeedID)
        self.rearLeftSpeed = ctre.TalonFX(constants.kleftRearSpeedID)
        self.frontRightSpeed = ctre.TalonFX(constants.krightFrontSpeedID)
        self.rearRightSpeed = ctre.TalonFX(constants.krightRearSpeedID)

        #init encoders
        self.frontLeftDirection.configSelectedFeedbackSensor(ctre.FeedbackDevice.IntegratedSensor, 0, constants.ktimeoutMs)
        self.rearLeftDirection.configSelectedFeedbackSensor(ctre.FeedbackDevice.IntegratedSensor, 0, constants.ktimeoutMs)
        self.frontRightDirection.configSelectedFeedbackSensor(ctre.FeedbackDevice.IntegratedSensor, 0, constants.ktimeoutMs)
        self.rearRightDirection.configSelectedFeedbackSensor(ctre.FeedbackDevice.IntegratedSensor, 0, constants.ktimeoutMs)
        
        self.frontLeftSpeed.configSelectedFeedbackSensor(ctre.FeedbackDevice.IntegratedSensor, 0, constants.ktimeoutMs)
        self.rearLeftSpeed.configSelectedFeedbackSensor(ctre.FeedbackDevice.IntegratedSensor, 0, constants.ktimeoutMs)
        self.frontRightSpeed.configSelectedFeedbackSensor(ctre.FeedbackDevice.IntegratedSensor, 0, constants.ktimeoutMs)
        self.rearRightSpeed.configSelectedFeedbackSensor(ctre.FeedbackDevice.IntegratedSensor, 0, constants.ktimeoutMs)

        self.leftFrontWheel = SwerveWheel(self.frontLeftDirection, self.frontLeftSpeed, 0.0, 0.0, 0.0)
        self.rightFrontWheel = SwerveWheel(self.frontRightDirection, self.frontRightSpeed, 0.0, 0.0, 0.0)

        self.leftBackWheel = SwerveWheel(self.rearLeftDirection, self.rearLeftSpeed, 0.0, 0.0, 0.0)
        self.rightBackWheel = SwerveWheel(self.rearRightDirection, self.rearRightSpeed, 0.0, 0.0, 0.0)

        #need to create some way to convert from Talon FX units to degrees
        # May try to make a file/method to use the position to do so
        
        #call gyro

    def stopMotors(self):
        self.frontLeftDirection.set(ctre.TalonFXControlMode.PercentOutput, 0.0)
        self.rearLeftDirection.set(ctre.TalonFXControlMode.PercentOutput, 0.0)
        self.frontRightDirection.set(ctre.TalonFXControlMode.PercentOutput, 0.0)
        self.rearRightDirection.set(ctre.TalonFXControlMode.PercentOutput, 0.0)

        self.frontLeftSpeed.set(ctre.TalonFXControlMode.PercentOutput, 0.0)
        self.rearLeftSpeed.set(ctre.TalonFXControlMode.PercentOutput, 0.0)
        self.frontRightSpeed.set(ctre.TalonFXControlMode.PercentOutput, 0.0)
        self.rearRightSpeed.set(ctre.TalonFXControlMode.PercentOutput, 0.0)

    def driveLeftFrontWheel(self, direction: float, speed: float):
        self.leftFrontWheel.setDirection(direction)
        self.leftFrontWheel.setSpeed(speed)

    def translate(self, direction: float, speed: float):
        self.leftFrontWheel.setDirection(direction)
        self.rightFrontWheel.setDirection(direction)
        self.leftBackWheel.setDirection(direction)
        self.rightBackWheel.setDirection(direction)

        self.leftFrontWheel.setSpeed(speed)
        self.rightFrontWheel.setSpeed(speed)
        self.leftBackWheel.setSpeed(speed)
        self.rightBackWheel.setSpeed(speed)
        
    def turnInPlace(self, speed: float):
        self.leftFrontWheel.setDirection(135.0)
        self.rightFrontWheel.setDirection(45.0)
        self.leftBackWheel.setDirection(-45.0)
        self.rightBackWheel.setDirection(-135.0)

        self.leftFrontWheel.setSpeed(speed)
        self.rightFrontWheel.setSpeed(speed)
        self.leftBackWheel.setSpeed(speed)
        self.rightBackWheel.setSpeed(speed)
    
    def closestAngle(self, a: float, b: float) -> float:
        # this converts to angles & get the distance between the two. b is the endpoint while a is the start point
        dir = float((b % 360.0) - (a % 360.0))
        
        if math.fabs(dir) > 180.0:
            # we find the sign of dir, (+1, -1, or 0), and multiply it by 360. We then take that negative and add dir
            dir = -(conversions.Conversions.sign(dir) * 360.0) + dir
        return dir

    def turnWhileMoving(self, direction: float, translatePwr: float, turnPwr: float):
        self.turnAngle = turnPwr * 45.0
        # left front wheel 135
        if (self.closestAngle(direction, 135.0)) >= 90.0:
            self.leftFrontWheel.setDirection(direction + self.turnAngle)
        else:
            self.leftFrontWheel.setDirection(direction - self.turnAngle)
        # left back wheel 225
        if (self.closestAngle(direction, 225.0) > 90.0):
            self.leftBackWheel.setDirection(direction + self.turnAngle)
        else:
            self.leftBackWheel.setDirection(direction - self.turnAngle)
        # right front wheel 45
        if (self.closestAngle(direction, 45.0)) > 90.0:
            self.rightFrontWheel.setDirection(direction + self.turnAngle)
        else:
            self.rightFrontWheel.setDirection(direction - self.turnAngle)
        # right back wheel 315
        if (self.closestAngle(direction, 315)) >= 90.0:
            self.rightBackWheel.setDirection(direction + self.turnAngle)
        else:
            self.rightBackWheel.setDirection(direction - self.turnAngle)
        
