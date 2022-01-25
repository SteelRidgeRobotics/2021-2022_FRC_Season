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
        self.frontRight.setSensorPhase(False)

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
       
    def userDrive(self, left: float, right: float) -> None:
        self.frontLeft.set(ctre.TalonFXControlMode.PercentOutput, left)
        self.frontRight.set(ctre.TalonFXControlMode.PercentOutput, right)

    def stopMotors(self, left: float, right: float) -> None:
        self.left = 0.0
        self.right = 0.0
        self.frontLeft.set(ctre.TalonFXControlMode.PercentOutput, left)
        self.frontRight.set(ctre.TalonFXControlMode.PercentOutput, right)
