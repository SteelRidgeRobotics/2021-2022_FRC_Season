from xmlrpc.client import Boolean
import commands2
import ctre
import conversions
from wpilib import ADXRS450_Gyro
from wpilib.kinematics import DifferentialDriveOdometry, DifferentialDriveWheelSpeeds, DifferentialDriveKinematics
from wpilib.geometry import Pose2d, Rotation2d
from wpilib import SmartDashboard
from constants import *

class Drivetrain(commands2.SubsystemBase):

    def __init__(self) -> None:
        super().__init__()

        self.setupMotors()
        self.initializeMotors()

        self.gyro = ADXRS450_Gyro()

        self.odometry = DifferentialDriveOdometry(self.gyro.getRotation2d())

        self.drive_kinematics = DifferentialDriveKinematics(ktrackWidth)

    def zeroHeading(self) -> None:
        self.gyro.reset()

   
    def getHeading(self):
        """Return the current heading of the robot."""
        return self.gyro.getRotation2d()
    
    def getTurnRate(self) -> float:

        return self.gyro.getRate()

    
    def getPose(self) :
        
        return self.odometry.getPose()

    def resetOdometry(self, pose) -> None:
        
        self.resetEncoders()

        self.odometry.resetPosition(pose, self.gyro.getRotation2d())

    def getWheelSpeeds(self):
        return DifferentialDriveWheelSpeeds(conversions.Conversions.convertTalonSRXNativeUnitsToWPILibTrajectoryUnits(self, self.frontLeft.getSelectedSensorVelocity(),kwheelDiameter, False, kticksPerRev), conversions.Conversions.convertTalonSRXNativeUnitsToWPILibTrajectoryUnits(self, self.frontRight.getSelectedSensorVelocity(),kwheelDiameter, False, kticksPerRev))

    def periodic(self) -> None:
        
        self.left_Distance = conversions.Conversions.convertTalonEncoderTicksToMeters(self, self.frontLeft.getSelectedSensorPosition(), kwheelDiameter, kticksPerRev, False)
        self.right_Distance = conversions.Conversions.convertTalonEncoderTicksToMeters(self, self.frontRight.getSelectedSensorPosition(), kwheelDiameter, kticksPerRev, False)
        
        SmartDashboard.putNumber("Current Compass", self.gyro.getAngle())
        self.odometry.update(self.gyro.getRotation2d(), self.left_Distance, self.right_Distance)

    def setupMotors(self) -> None:
        """Setup all motor aspects."""
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

    def tankDriveVolts(self, leftVolts: float, rightVolts: float) -> None:
        print(str(leftVolts) + ","+ str(rightVolts))
        self.frontLeft.set(ctre.ControlMode.Current, leftVolts)
        self.frontRight.set(ctre.ControlMode.Current, rightVolts)
    
    def tankDriveVelocity(self, leftVel: float, rightVel: float) -> None:
        print(str(leftVel) + "," + str(rightVel))
        self.frontLeftNativeVelocity = conversions.Conversions.convertWPILibTrajectoryUnitsToTalonSRXNativeUnits(self, leftVel, kwheelDiameter, False, kticksPerRev)
        self.frontRightNativeVelocity = conversions.Conversions.convertWPILibTrajectoryUnitsToTalonSRXNativeUnits(self, rightVel, kwheelDiameter, False, kticksPerRev)

        self.frontLeft.set(ctre.ControlMode.Velocity, self.frontLeftNativeVelocity)
        self.frontRight.set(ctre.ControlMode.Velocity, self.frontRightNativeVelocity)

        SmartDashboard.putNumber("LeftIntendedVelocity", self.frontLeftNativeVelocity)
        SmartDashboard.putNumber("LeftIntendedvsActual", self.frontLeftNativeVelocity-self.frontLeft.getSelectedSensorVelocity())



    def isMoving(self) -> Boolean:

        self.l_vel_traj = self.frontLeft.getActiveTrajectoryVelocity()
        self.r_vel_traj = self.frontRight.getActiveTrajectoryVelocity()


        if self.l_vel_traj==0.0 and self.r_vel_traj==0.0:
            return True
        else:
            return False

    def resetEncoders(self) -> None:

        self.frontLeft.setSelectedSensorPosition(0.0, 0, ktimeoutMs)
        self.frontRight.setSelectedSensorPosition(0.0, 0, ktimeoutMs)

    def getAverageEncoderDistance(self) -> float:

        return (self.frontLeft.getSelectedSensorPosition() + self.frontRight.getSelectedSensorPosition())/2.0

    def initializeMotors(self) -> None:
        self.resetEncoders()
        self.stopMotors()