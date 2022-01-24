import commands2
import ctre
import constants

class Drivetrain(commands2.SubsystemBase):
    def __init__(self):
        super().__init__()

        #initilize motors
        self.frontLeft = ctre.TalonFX(constants.kfrontLeft)
        self.backLeft = ctre.TalonFX(constants.kbackLeft)
        self.frontRight = ctre.TalonFX(constants.kfrontRight)
        self.backRight = ctre.TalonFX(constants.kbackRight)

        #set followers
        self.backLeft.follow(self.frontLeft)
        self.backRight.follow(self.frontRight)

        #reverse sensors
        self.frontLeft.setSensorPhase(False)
        self.backLeft.setSensorPhase(False)

        #invert motors on right side
        self.frontRight.setInverted(True)
        self.backRight.setInverted(True)

        self.frontRight.configSelectedFeedbackSensor(ctre.FeedbackDevice.IntegratedSensor, 0, constants.ktimeoutMs)
        self.frontLeft.configSelectedFeedbackSensor(ctre.FeedbackDevice.IntegratedSensor, 0, constants.ktimeoutMs)

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
    def stopMotors(self, left: float, right: float):
        self.left = 0.0
        self.right = 0.0
        self.frontLeft.set(ctre.TalonFXControlMode.PercentOutput, left)
        self.frontRight.set(ctre.TalonFXControlMode.PercentOutput, right)
