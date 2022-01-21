import wpilib
import commands2
import constants
import ctre
from commands.drive_by_joystick import DriveByJoystick

class Drivetrain(commands2.SubsystemBase):
    def __init__(self):
        super().__init__()

        #initilize motors
        self.frontLeft = ctre.TalonFX(constants.kfrontLeft)
        self.backLeft = ctre.TalonFX(constants.kbackLeft)
        self.frontRight = ctre.TalonFX(constants.kfrontLeft)
        self.backRight = ctre.TalonFX(constants.kbackLeft)

        #set followers
        self.backLeft.follow(self.frontLeft)
        self.backRight.follow(self.frontRight)

        #reverse sensors
        self.frontLeft.setSensorPhase(False)
        self.backLeft.setSensorPhase(False)

        #invert motors on right side
        self.frontRight.setSensorPhase(True)
        self.backRight.setSensorPhase(True)

        self.frontRight.configSelectedFeedbackSensor(ctre.FeedbackDevice.QuadEncoder, 0, constants.ktimeoutMs)
        self.frontLeft.configSelectedFeedbackSensor(ctre.FeedbackDevice.QuadEncoder, 0, constants.ktimeoutMs)

        #set motors to brake mode
        self.frontLeft.setNeutralMode(ctre.NeutralMode.Brake)
        self.backLeft.setNeutralMode(ctre.NeutralMode.Brake)
        self.frontRight.setNeutralMode(ctre.NeutralMode.Brake)
        self.backRight.setNeutralMode(ctre.NeutralMode.Brake)
        """
        def userDrive(self, RobotContainer.driveController) -> None:
            left = float((RobotContainer.driveController.getY()*-1) + RobotContainer.driveController.getX())
            right = float((RobotContainer.driveController.getY()*-1) - RobotContainer.driveController.getX())

            self.frontLeft.set(ctre.TalonFXControlMode.PercentOutput, left)
            self.frontRight.set(ctre.TalonFXControlMode.PercentOutput, right)
        
        def userDrive(self, controller) -> None:
            left = float((controller.getY()*-1) + RobotContainer.driveController.getX())
            right = float((controller.getY()*-1) - RobotContainer.driveController.getX())

            self.frontLeft.set(ctre.TalonFXControlMode.PercentOutput, left)
            self.frontRight.set(ctre.TalonFXControlMode.PercentOutput, right)
        """
        def userDrive(self, left: float, right: float):
            self.frontLeft.set(ctre.TalonFXControlMode.PercentOutput, left)
            self.frontRight.set(ctre.TalonFXControlMode.PercentOutput, right)
            
        """

        self.fLeftMotor = ctre.WPI_TalonFX(constants.kfrontLeft)
        self.bLeftMotor = ctre.WPI_TalonFX(constants.kbackLeft)
        self.fRightMotor = ctre.WPI_TalonFX(constants.kfrontRight)
        self.bRightMotor = ctre.WPI_TalonFX(constants.kbackRight)

        self.spcleft = wpilib.SpeedControllerGroup(self.fLeftMotor, self.bLeftMotor)
        self.spcright = wpilib.SpeedControllerGroup(self.fRightMotor, self.bRightMotor)
        self.drive = wpilib.drive.DifferentialDrive(self.spcleft, self.spcright)

        self.drive.setSafetyEnabled(True)
        self.drive.setExpiration(0.1)
        """
    """
    def disable_drive():
        self.fLeftMotor.disable()
        self.bLeftMotor.disable()
        self.fRightMotor.disable()
        self.bRightMotor.disable()
        """
    def initDefaultCommand(self):
        self.drive.setDefaultCommand(DriveByJoystick(self.robot))