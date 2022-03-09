import commands2
import ctre
import constants
from xmlrpc.client import Boolean
from conversions import Conversions
from wpilib import ADXRS450_Gyro
from wpimath.kinematics import DifferentialDriveOdometry, DifferentialDriveWheelSpeeds
from wpimath.geometry import Pose2d, Rotation2d
from wpimath.trajectory import Trajectory
from wpilib import SmartDashboard
import constants
from commands2 import RamseteCommand
from commands2 import InstantCommand
from customramsetecontrollerabstraction import CustomRamseteControllerAbstraction
import math

class Drivetrain(commands2.SubsystemBase):
    def __init__(self) -> None:
        super().__init__()

        #initialize motors
        self.frontLeft = ctre.TalonFX(constants.kfrontLeft)
        self.backLeft = ctre.TalonFX(constants.kbackLeft)
        self.frontRight = ctre.TalonFX(constants.kfrontRight)
        self.backRight = ctre.TalonFX(constants.kbackRight)
        
        #initialize gyro
        self.gyro = ADXRS450_Gyro()
        
        self.odometry = DifferentialDriveOdometry(Rotation2d.fromDegrees(self.getHeading()))
        self.configMotors1()
        self.resetMotors()
        self.configMotors2()
        self.gyro.reset()
    
    def periodic(self):
        self.leftDistance = Conversions.convertTalonEncoderTicksToMeters(self, self.frontLeft.getSelectedSensorPosition(), constants.kwheelDiameter, constants.kticksPerRev, False)
        self.rightDistance = Conversions.convertTalonEncoderTicksToMeters(self, self.frontRight.getSelectedSensorPosition(), constants.kwheelDiameter, constants.kticksPerRev, False)

        self.odometry.update(Rotation2d.fromDegrees(self.getHeading()), self.leftDistance, self.rightDistance)

    def resetMotors(self):
        self.frontLeft.configFactoryDefault()
        self.frontRight.configFactoryDefault()
    
    def configMotors1(self) -> None:
        #set followers
        self.backLeft.follow(self.frontLeft)
        self.backRight.follow(self.frontRight)

        #invert motors on right side
        self.frontRight.setInverted(True)
        self.backRight.setInverted(True)

        #set motors to brake mode
        self.frontLeft.setNeutralMode(ctre.NeutralMode.Brake)
        self.backLeft.setNeutralMode(ctre.NeutralMode.Brake)
        self.frontRight.setNeutralMode(ctre.NeutralMode.Brake)
        self.backRight.setNeutralMode(ctre.NeutralMode.Brake)

        #reverse sensors
        self.frontLeft.setSensorPhase(False)
        self.frontRight.setSensorPhase(False)
        
        #forward and back
        self.frontLeft.configNominalOutputForward(0, constants.ktimeoutMs)
        self.frontRight.configNominalOutputForward(0, constants.ktimeoutMs)
        self.frontLeft.configNominalOutputReverse(0, constants.ktimeoutMs)
        self.frontRight.configNominalOutputReverse(0, constants.ktimeoutMs)
        
        #peak output
        self.frontLeft.configPeakOutputForward(1, constants.ktimeoutMs)
        self.frontRight.configPeakOutputForward(1, constants.ktimeoutMs)
        self.frontLeft.configPeakOutputReverse(-1, constants.ktimeoutMs)
        self.frontRight.configPeakOutputReverse(-1, constants.ktimeoutMs)
        
        #profile slot
        self.frontLeft.selectProfileSlot(constants.kSlotIdx, constants.kPIDLoopIdx)
        self.frontRight.selectProfileSlot(constants.kSlotIdx, constants.kPIDLoopIdx)
        self.backLeft.selectProfileSlot(constants.kSlotIdx, constants.kPIDLoopIdx)
        self.backRight.selectProfileSlot(constants.kSlotIdx, constants.kPIDLoopIdx)

        #setting our acceleration and velocity (it's like cruise control but better hahaha laugh please laugh)
        self.frontLeft.configMotionCruiseVelocity(constants.kmotorCruiseVelocity, constants.ktimeoutMs)
        self.frontRight.configMotionCruiseVelocity(constants.kmotorCruiseVelocity, constants.ktimeoutMs)
        self.frontLeft.configMotionAcceleration(constants.kmotorAcceleration, constants.ktimeoutMs)
        self.frontRight.configMotionAcceleration(constants.kmotorAcceleration, constants.ktimeoutMs)
        
        #setting sensors to 0
        self.frontLeft.setSelectedSensorPosition(0, constants.kPIDLoopIdx, constants.ktimeoutMs)
        self.frontRight.setSelectedSensorPosition(0, constants.kPIDLoopIdx, constants.ktimeoutMs)

    def configMotors2(self):
        #config motors
        self.frontLeft.configSelectedFeedbackSensor(ctre.FeedbackDevice.IntegratedSensor, 0, constants.ktimeoutMs)
        self.frontRight.configSelectedFeedbackSensor(ctre.FeedbackDevice.IntegratedSensor, 0, constants.ktimeoutMs)

        #config Proportional, Integral, Derivative, and Filtered (PIDF)
        self.frontLeft.config_kP(constants.kSlotIdx, constants.kP, constants.ktimeoutMs)
        self.frontLeft.config_kI(constants.kSlotIdx, constants.kI, constants.ktimeoutMs)
        self.frontLeft.config_kD(constants.kSlotIdx, constants.kD, constants.ktimeoutMs)
        self.frontLeft.config_kF(constants.kSlotIdx, constants.kF, constants.ktimeoutMs)

        self.frontRight.config_kP(constants.kSlotIdx, constants.kP, constants.ktimeoutMs)
        self.frontRight.config_kI(constants.kSlotIdx, constants.kI, constants.ktimeoutMs)
        self.frontRight.config_kD(constants.kSlotIdx, constants.kD, constants.ktimeoutMs)
        self.frontRight.config_kF(constants.kSlotIdx, constants.kF, constants.ktimeoutMs)

        self.stopMotors()

    def stopMotors(self):
        self.frontLeft.set(ctre.TalonFXControlMode.PercentOutput, 0.0)
        self.frontRight.set(ctre.TalonFXControlMode.PercentOutput, 0.0)

    def resetEncoders(self):
        self.frontLeft.setSelectedSensorPosition(0.0, constants.kPIDLoopIdx, constants.ktimeoutMs)
        self.frontRight.setSelectedSensorPosition(0.0, constants.kPIDLoopIdx, constants.ktimeoutMs)

    def stopAndReset(self):
        self.frontLeft.set(ctre.TalonFXControlMode.PercentOutput, 0.0)
        self.frontRight.set(ctre.TalonFXControlMode.PercentOutput, 0.0)
        self.frontLeft.setSelectedSensorPosition(0.0, constants.kPIDLoopIdx, constants.ktimeoutMs)
        self.frontRight.setSelectedSensorPosition(0.0, constants.kPIDLoopIdx, constants.ktimeoutMs)
        self.gyro.reset()
    
    def clearTalonTrajectories(self):
        self.frontLeft.clearMotionProfileTrajectories()
        self.frontRight.clearMotionProfileTrajectories()
    
    def createTrajectoryCommand(self, trajectory: Trajectory, initPose: bool) -> commands2.Command:
        self.resetEncoders()

        m_trajectory = trajectory
        m_initPose = initPose

        ramseteCommand = RamseteCommand(m_trajectory, self.getPose, CustomRamseteControllerAbstraction(constants.kramsete_B, constants.kramsete_Zeta),
        constants.kdriveKinematics, self.tankDriveVelocity, [self])

        if m_initPose:
            m_reset = InstantCommand(lambda: self.resetOdometry(trajectory.initialPose()))
            return m_reset.andThen(ramseteCommand.andThen(lambda: self.tankDriveVolts(0.0,0.0)))

        else:
             return ramseteCommand.andThen(lambda: self.tankDriveVolts(0.0,0.0))

    def tankDriveVelocity(self, leftVel: float, rightVel: float) -> None:
        frontLeftNativeVelocity = Conversions.convertTrajectoryUnitsToTalonUnits(self, leftVel, constants.kwheelDiameter, False, constants.kticksPerRev)
        frontRightNativeVelocity = Conversions.convertTrajectoryUnitsToTalonUnits(self, rightVel, constants.kwheelDiameter, False, constants.kticksPerRev)

        self.frontLeft.set(ctre.ControlMode.Velocity, frontLeftNativeVelocity)
        self.frontRight.set(ctre.ControlMode.Velocity, frontRightNativeVelocity)

    def tankDriveVolts(self, leftVolts: float, rightVolts: float) -> None:
        """Method to drive robot using talons in voltage control mode. Must feed voltages from 0-12."""

        print(str(leftVolts) + ","+ str(rightVolts))
        self.frontLeft.set(ctre.ControlMode.Current, leftVolts)
        self.frontRight.set(ctre.ControlMode.Current, -rightVolts)

    def resetOdometry(self, pose) -> None:
        
        self.resetEncoders()

        self.odometry.resetPosition(pose, Rotation2d.fromDegrees(self.getHeading()))

    def getPose(self) -> Pose2d:
        return self.odometry.getPose()

    
#######################################################################################################
    def userDrive(self, leftJoy: float, rightJoy: float, percentage: float) -> None:
        self.frontLeft.set(ctre.TalonFXControlMode.PercentOutput, leftJoy*percentage)
        self.frontRight.set(ctre.TalonFXControlMode.PercentOutput, rightJoy*percentage)

    def magicDrive(self, targetPos: float) -> None:
        self.targetPos = targetPos
        self.frontLeft.set(ctre.TalonFXControlMode.MotionMagic, self.targetPos)
        self.frontRight.set(ctre.TalonFXControlMode.MotionMagic, self.targetPos)

    def stopMotors(self) -> None:
        self.left = 0.0
        self.right = 0.0
        self.frontLeft.set(ctre.TalonFXControlMode.PercentOutput, 0.0)
        self.frontRight.set(ctre.TalonFXControlMode.PercentOutput, 0.0)

        self.frontLeft.setSelectedSensorPosition(0, 0, constants.ktimeoutMs)
        self.frontRight.setSelectedSensorPosition(0, 0, constants.ktimeoutMs)

    def isNotinMotion(self) -> bool:
        self.vel_traj = self.frontLeft.getActiveTrajectoryVelocity()
        return self.vel_traj == 0.0

    def getHeading(self):
        return -1*math.remainder(self.gyro.getAngle(), 360)

    def getTurnRate(self) -> float:

        return self.gyro.getRate()

    
    def getPose(self) -> Pose2d:
        
        return self.odometry.getPose()

    def resetOdometry(self, pose) -> None:
        
        self.resetEncoders()

        self.odometry.resetPosition(pose, Rotation2d.fromDegrees(self.getHeading()))

    def getWheelSpeeds(self):

        return DifferentialDriveWheelSpeeds(Conversions.convertTrajectoryUnitsToTalonUnits(self, self.frontLeft.getSelectedSensorVelocity(),constants.kwheelDiameter, False, constants.kticksPerRev), Conversions.convertTrajectoryUnitsToTalonUnits(self, self.frontRight.getSelectedSensorVelocity(),constants.kwheelDiameter, False, constants.kticksPerRev))
