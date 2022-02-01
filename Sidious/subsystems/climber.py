import commands2
import ctre
import constants



class Climber(commands2.SubsystemBase):

    def __init__(self) -> None:
        super().__init__()
        
        #initalize motors
        self.verticalClimber = ctre.TalonFX(constants.kverticalClimber)
        self.tiltedClimber = ctre.TalonFX(constants.ktiltedClimber)

        #set followers
        
        
        #reverse sensors-This shouldn't be necessary with TalonFX as sensors are integrated
        
        #invert motors
        #self.frontClimber.setInverted(ctre.TalonFXInvertType.Clockwise)
        #self.backClimber.setInverted(ctre.TalonFXInvertType.Clockwise)

        #configure encoders
        #self.frontClimber.configSelectedFeedbackSensor(ctre.FeedbackDevice.IntegratedSensor, 0, constants.ktimeoutMs)
        #self.backClimber.configSelectedFeedbackSensor(ctre.FeedbackDevice.IntegratedSensor, 0, constants.ktimeoutMs)

        #self.frontClimber.config_kF(0, constants.kF, constants.ktimeoutMs) 
        #self.backClimber.config_kF(0, constants.kF, constants.ktimeoutMs)

        #self.frontClimber.config_kP(0, constants.kP, constants.ktimeoutMs) 
        #self.backClimber.config_kP(0, constants.kP, constants.ktimeoutMs)
     
        #set motors to brake mode
        self.verticalClimber.setNeutralMode(ctre.NeutralMode.Brake)
        self.tiltedClimber.setNeutralMode(ctre.NeutralMode.Brake)
        