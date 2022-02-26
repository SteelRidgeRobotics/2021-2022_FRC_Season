from xmlrpc.client import Boolean
import commands2
import ctre
from conversions import Conversions
from wpilib import ADXRS450_Gyro
from wpimath.kinematics import DifferentialDriveOdometry, DifferentialDriveWheelSpeeds
from wpimath.geometry import Pose2d, Rotation2d
from wpimath.trajectory import Trajectory
from wpilib import SmartDashboard
from constants import *
from commands2 import RamseteCommand
from commands2 import InstantCommand
from customramsetecontrollerabstraction import CustomRamseteControllerAbstraction


class Drivetrain(commands2.SubsystemBase):

    def __init__(self) -> None:
        super().__init__()

        #initalize motors
        self.frontLeft = ctre.TalonFX(kfrontLeft)
        self.backLeft = ctre.TalonFX(kbackLeft)
        self.frontRight = ctre.TalonFX(kfrontRight)
        self.backRight = ctre.TalonFX(kbackRight)

        #initialize the gyro
        self.gyro = ADXRS450_Gyro()

        #Set up the gyro's heading.
        self.odometry = DifferentialDriveOdometry(Rotation2d.fromDegrees(self.getHeading()))

        #See methods below that setup motors, etc.
        self.setUpMotors()
        self.resetMotors()
        self.configMotors()
        self.gyro.reset()

    
    
    def periodic(self) -> None:
        """A periodic method to update the gyro."""
        
        self.left_Distance = Conversions.convertTalonEncoderTicksToMeters(self, self.frontLeft.getSelectedSensorPosition(), kwheelDiameter, kticksPerRev, False)
        self.right_Distance = Conversions.convertTalonEncoderTicksToMeters(self, self.frontRight.getSelectedSensorPosition(), kwheelDiameter, kticksPerRev, False)
        
        SmartDashboard.putNumber("Current Compass", Rotation2d.fromDegrees(self.getHeading()).radians())
        self.odometry.update(Rotation2d.fromDegrees(self.getHeading()), self.left_Distance, self.right_Distance)
        SmartDashboard.putNumber("Left Sensor Velocity", self.frontLeft.getSelectedSensorVelocity())
        SmartDashboard.putNumber("Right Sensor Velocity", self.frontRight.getSelectedSensorVelocity())
        SmartDashboard.putNumber("Left Distance", self.left_Distance)
        SmartDashboard.putNumber("Right Disance", self.right_Distance)
       
    
    """Methods for motors & encoders"""

    def resetMotors(self)-> None:
        """Reset the motor configurations to factory default."""
        self.frontLeft.configFactoryDefault()
        self.frontRight.configFactoryDefault()    
    
    def setUpMotors(self) -> None:
        """Setup all motor aspects."""

        #set followers
        self.backLeft.follow(self.frontLeft)
        self.backRight.follow(self.frontRight)
     
        #invert motors on right side
        self.frontRight.setInverted(ctre.TalonFXInvertType.Clockwise)
        self.backRight.setInverted(ctre.TalonFXInvertType.Clockwise)
       
        #set motors to brake mode
        self.frontLeft.setNeutralMode(ctre.NeutralMode.Brake)
        self.backLeft.setNeutralMode(ctre.NeutralMode.Brake)
        self.frontRight.setNeutralMode(ctre.NeutralMode.Brake)
        self.backLeft.setNeutralMode(ctre.NeutralMode.Brake)

    
    def configMotors(self) -> None:
        """Here we set up all configs for motors"""
        #configure encoders
        self.frontRight.configSelectedFeedbackSensor(ctre.FeedbackDevice.IntegratedSensor, 0, ktimeoutMs)
        self.frontLeft.configSelectedFeedbackSensor(ctre.FeedbackDevice.IntegratedSensor, 0, ktimeoutMs)

        self.frontLeft.config_kF(0, kF, ktimeoutMs) 
        self.frontRight.config_kF(0, kF, ktimeoutMs)

        self.frontLeft.config_kP(0, kP, ktimeoutMs) 
        self.frontRight.config_kP(0, kP, ktimeoutMs)

        self.frontLeft.config_kI(0, kI, ktimeoutMs) 
        self.frontRight.config_kI(0, kI, ktimeoutMs)

        self.frontLeft.config_kD(0, kD, ktimeoutMs) 
        self.frontRight.config_kD(0, kD, ktimeoutMs)
        self.stopMotors()
    
    def stopMotors(self) -> None:
        """Stops motors and sets mode to percent output"""
        self.frontLeft.set(ctre.TalonFXControlMode.PercentOutput, 0.0)
        self.frontRight.set(ctre.TalonFXControlMode.PercentOutput, 0.0)    
    
    def resetEncoders(self) -> None:
        """Resets the encoder position to 0."""

        self.frontLeft.setSelectedSensorPosition(0.0, 0, ktimeoutMs)
        self.frontRight.setSelectedSensorPosition(0.0, 0, ktimeoutMs)

    def stopandReset(self) -> None:
        """Resets entire drivetrain."""
        self.frontLeft.set(ctre.TalonFXControlMode.PercentOutput, 0.0)
        self.frontRight.set(ctre.TalonFXControlMode.PercentOutput, 0.0)
        self.frontLeft.setSelectedSensorPosition(0.0, 0, ktimeoutMs)
        self.frontRight.setSelectedSensorPosition(0.0, 0, ktimeoutMs)
        self.gyro.reset()

    def clearTalonTrajectories(self) -> None:
        """Clears any trajectories that are on the talons."""
        self.frontLeft.clearMotionProfileTrajectories()
        self.frontRight.clearMotionProfileTrajectories()

    def getAverageEncoderDistance(self) -> float:
        """Returns the average position of left & right encoders."""

        return (self.frontLeft.getSelectedSensorPosition() + self.frontRight.getSelectedSensorPosition())/2.0
    
    def createTrajectoryCommand(self, trajectory: Trajectory, initPose: bool) -> commands2.Command:
        """Creates a command for path planning. You feed the command a trajectory and whether the
        reset the initial pose."""

        # Reset the encoders before running.
        self.resetEncoders()

        # Member variables for the trajectory and initial pose
        m_trajectory = trajectory
        m_initPose = initPose
        
        # The ramsete command.
        ramseteCommand = RamseteCommand(
            # The trajectory to follow.
            m_trajectory,
            # A reference to a method that will return our position.
            self.getPose,
            # Our RAMSETE controller.
            CustomRamseteControllerAbstraction(kramsete_B, kramsete_Zeta),
            # Our drive kinematics.
            kdriveKinematics,
            # A reference to a method which will set a specified
            # velocity to each motor. The command will pass the two parameters.
            self.tankDriveVelocity,
            # The subsystems the command should require (this drivetrain)
            [self],
        )

        # If needed, reset the pose and then run the command.
        if m_initPose:
            m_reset = InstantCommand(lambda: self.resetOdometry(trajectory.initialPose()))
            return m_reset.andThen(ramseteCommand.andThen(lambda: self.tankDriveVolts(0.0,0.0)))
        
        # Run the command if the pose doesn't need to be reset.
        else:
            return ramseteCommand.andThen(lambda: self.tankDriveVolts(0.0,0.0))
    
    def userDrive(self, leftJoy: float, rightJoy: float) -> None:
        """Method to drive robot using left and right joysticks."""
        
        self.frontLeft.set(ctre.TalonFXControlMode.PercentOutput, leftJoy)
        self.frontRight.set(ctre.TalonFXControlMode.PercentOutput, rightJoy)

    def motionMagic(self, units: float) -> None:
        """Method to set talons to motion magic mode. Must feed native talon units."""

        self.frontLeft.configMotionCruiseVelocity(kcruiseVel, ktimeoutMs)
        self.frontRight.configMotionCruiseVelocity(kcruiseVel, ktimeoutMs)

        self.frontLeft.configMotionAcceleration(kcruiseAccel, ktimeoutMs)
        self.frontRight.configMotionAcceleration(kcruiseAccel, ktimeoutMs)

        self.frontLeft.set(ctre.TalonFXControlMode.MotionMagic, units)
        self.frontRight.set(ctre.TalonFXControlMode.MotionMagic, units)

    def tankDriveVolts(self, leftVolts: float, rightVolts: float) -> None:
        """Method to drive robot using talons in voltage control mode. Must feed voltages from 0-12."""

        print(str(leftVolts) + ","+ str(rightVolts))
        self.frontLeft.set(ctre.ControlMode.Current, leftVolts)
        self.frontRight.set(ctre.ControlMode.Current, -rightVolts)
    
    def tankDriveVelocity(self, leftVel: float, rightVel: float) -> None:
        """Method to drive robot using talons in velocity control mode. Must feed wpilib trajectory units."""

        print(str(leftVel) + "," + str(rightVel))
        frontLeftNativeVelocity = Conversions.convertWPILibTrajectoryUnitsToTalonSRXNativeUnits(self, leftVel, kwheelDiameter, False, kticksPerRev)
        frontRightNativeVelocity = Conversions.convertWPILibTrajectoryUnitsToTalonSRXNativeUnits(self, rightVel, kwheelDiameter, False, kticksPerRev)

        self.frontLeft.set(ctre.ControlMode.Velocity, frontLeftNativeVelocity)
        self.frontRight.set(ctre.ControlMode.Velocity, frontRightNativeVelocity)

        SmartDashboard.putNumber("LeftIntendedVelocity", frontLeftNativeVelocity)
        SmartDashboard.putNumber("LeftIntendedvsActual", frontLeftNativeVelocity-self.frontLeft.getSelectedSensorVelocity())

    def isMoving(self) -> Boolean:
        """A method to determine whether the robot has finished an active trajectory. Returns a boolean."""

        self.l_vel_traj = self.frontLeft.getActiveTrajectoryVelocity()
        self.r_vel_traj = self.frontRight.getActiveTrajectoryVelocity()


        if self.l_vel_traj==0.0 and self.r_vel_traj==0.0:
            return True
        else:
            return False


    """Methods for Gyro"""
    def zeroHeading(self) -> None:
        """Reset the gyro"""

        self.gyro.reset()

   
    def getHeading(self):
        """Return the current heading of the robot."""

        return -1*math.remainder(self.gyro.getAngle(),360)
    
    def getTurnRate(self) -> float:

        return self.gyro.getRate()

    
    def getPose(self) -> Pose2d:
        
        return self.odometry.getPose()

    def resetOdometry(self, pose) -> None:
        
        self.resetEncoders()

        self.odometry.resetPosition(pose, Rotation2d.fromDegrees(self.getHeading()))

    def getWheelSpeeds(self):

        return DifferentialDriveWheelSpeeds(Conversions.convertTalonSRXNativeUnitsToWPILibTrajectoryUnits(self, self.frontLeft.getSelectedSensorVelocity(),kwheelDiameter, False, kticksPerRev), Conversions.convertTalonSRXNativeUnitsToWPILibTrajectoryUnits(self, self.frontRight.getSelectedSensorVelocity(),kwheelDiameter, False, kticksPerRev))
  

