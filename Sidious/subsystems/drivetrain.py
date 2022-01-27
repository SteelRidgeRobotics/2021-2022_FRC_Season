import commands2
import ctre
import constants



class Drivetrain(commands2.SubsystemBase):

    def __init__(self) -> None:
        super().__init__()

        #initalize motors
        self.frontLeft = ctre.TalonFX(constants.kfrontLeft)
        self.backLeft = ctre.TalonFX(constants.kbackLeft)
        self.frontRight = ctre.TalonFX(constants.kfrontRight)
        self.backRight = ctre.TalonFX(constants.kbackRight)

        self.frontLeft.configFactoryDefault()
        self.backLeft.configFactoryDefault()
        self.frontRight.configFactoryDefault()
        self.backLeft.configFactoryDefault()

        #set followers
        self.backLeft.follow(self.frontLeft)
        self.backRight.follow(self.frontRight)

        #reverse sensors-This shouldn't be necessary with TalonFX as sensors are integrated
        

        #invert motors on right side
        self.frontRight.setInverted(ctre.TalonFXInvertType.Clockwise)
        self.backRight.setInverted(ctre.TalonFXInvertType.Clockwise)

        #configure encoders
        self.frontRight.configSelectedFeedbackSensor(ctre.FeedbackDevice.IntegratedSensor, 0, constants.ktimeoutMs)
        self.frontLeft.configSelectedFeedbackSensor(ctre.FeedbackDevice.IntegratedSensor, 0, constants.ktimeoutMs)
        
        #set motors to brake mode
        self.frontLeft.setNeutralMode(ctre.NeutralMode.Brake)
        self.backLeft.setNeutralMode(ctre.NeutralMode.Brake)
        self.frontRight.setNeutralMode(ctre.NeutralMode.Brake)
        self.backLeft.setNeutralMode(ctre.NeutralMode.Brake)

        

    def userDrive(self, leftJoy: float, rightJoy: float) -> None:
        
        self.frontLeft.set(ctre.TalonFXControlMode.PercentOutput, leftJoy)
        self.frontRight.set(ctre.TalonFXControlMode.PercentOutput, rightJoy)
    
    def stopMotors(self, left: float, right: float) -> None:

        self.frontLeft.set(ctre.TalonFXControlMode.PercentOutput, left)
        self.frontRight.set(ctre.TalonFXControlMode.PercentOutput, right)