from xmlrpc.client import Boolean
import commands2
import ctre
from constants import *


class Drivetrain(commands2.SubsystemBase):

    def __init__(self) -> None:
        super().__init__()

        #initalize motors
        self.frontLeft = ctre.TalonFX(kfrontLeft)
        self.backLeft = ctre.TalonFX(kbackLeft)
        self.frontRight = ctre.TalonFX(kfrontRight)
        self.backRight = ctre.TalonFX(kbackRight)

        #set followers
        self.backLeft.follow(self.frontLeft)
        self.backRight.follow(self.frontRight)

        #reverse sensors-This shouldn't be necessary with TalonFX as sensors are integrated
        

        #invert motors on right side
        self.frontRight.setInverted(ctre.TalonFXInvertType.Clockwise)
        self.backRight.setInverted(ctre.TalonFXInvertType.Clockwise)

        #configure encoders
        self.frontRight.configSelectedFeedbackSensor(ctre.FeedbackDevice.IntegratedSensor, 0, ktimeoutMs)
        self.frontLeft.configSelectedFeedbackSensor(ctre.FeedbackDevice.IntegratedSensor, 0, ktimeoutMs)

        self.frontLeft.config_kF(0, kF, ktimeoutMs) 
        self.frontRight.config_kF(0, kF, ktimeoutMs)

        self.frontLeft.config_kP(0, kP, ktimeoutMs) 
        self.frontRight.config_kP(0, kP, ktimeoutMs)

        self.frontLeft.configMotionCruiseVelocity(kcruiseVel, ktimeoutMs)
        self.frontRight.configMotionCruiseVelocity(kcruiseVel, ktimeoutMs)

        self.frontLeft.configMotionAcceleration(kcruiseAccel, ktimeoutMs)
        self.frontRight.configMotionAcceleration(kcruiseAccel, ktimeoutMs)
        
        #set motors to brake mode
        self.frontLeft.setNeutralMode(ctre.NeutralMode.Brake)
        self.backLeft.setNeutralMode(ctre.NeutralMode.Brake)
        self.frontRight.setNeutralMode(ctre.NeutralMode.Brake)
        self.backLeft.setNeutralMode(ctre.NeutralMode.Brake)        


    def userDrive(self, leftJoy: float, rightJoy: float) -> None:
        
        self.frontLeft.set(ctre.TalonFXControlMode.PercentOutput, leftJoy)
        self.frontRight.set(ctre.TalonFXControlMode.PercentOutput, rightJoy)
    
    def stopMotors(self) -> None:

        self.frontLeft.set(ctre.TalonFXControlMode.PercentOutput, 0.0)
        self.frontRight.set(ctre.TalonFXControlMode.PercentOutput, 0.0)


    def motionMagic(self, units: float) -> None:
        self.frontLeft.set(ctre.TalonFXControlMode.MotionMagic, units)
        self.frontRight.set(ctre.TalonFXControlMode.MotionMagic, units)

    def isMoving(self) -> Boolean:

        self.vel_traj = self.frontLeft.getActiveTrajectoryVelocity()

        if self.vel_traj==0.0:
            return True
        else:
            return False

    def resetEncoders(self) -> None:

        self.frontLeft.setSelectedSensorPosition(0.0, 0, ktimeoutMs)
        self.frontRight.setSelectedSensorPosition(0.0, 0, ktimeoutMs)

    def initializeMotors(self) -> None:
        self.resetEncoders()
        self.stopMotors()