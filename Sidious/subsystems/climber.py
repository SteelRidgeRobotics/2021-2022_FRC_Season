import commands2
import ctre
from constants import *


class Climber(commands2.SubsystemBase):

    def __init__(self) -> None:
        super().__init__()
        
        #initalize motors
        self.verticalClimber = ctre.TalonFX(kverticalClimber)
        self.tiltedClimber = ctre.TalonFX(ktiltedClimber)

        #set followers
        
        
        #reverse sensors-This shouldn't be necessary with TalonFX as sensors are integrated
        
        #invert motors
        self.verticalClimber.setInverted(ctre.TalonFXInvertType.Clockwise)
        self.tiltedClimber.setInverted(ctre.TalonFXInvertType.Clockwise)

        #configure encoders
        self.verticalClimber.configSelectedFeedbackSensor(ctre.FeedbackDevice.IntegratedSensor, 0, ktimeoutMs)
        self.tiltedClimber.configSelectedFeedbackSensor(ctre.FeedbackDevice.IntegratedSensor, 0, ktimeoutMs)

        self.verticalClimber.config_kF(0, kF, ktimeoutMs) 
        self.tiltedClimber.config_kF(0, kF, ktimeoutMs)

        self.verticalClimber.config_kP(0, kP, ktimeoutMs) 
        self.tiltedClimber.config_kP(0, kP, ktimeoutMs)
     
        #set motors to brake mode
        self.verticalClimber.setNeutralMode(ctre.NeutralMode.Brake)
        self.tiltedClimber.setNeutralMode(ctre.NeutralMode.Brake)
        