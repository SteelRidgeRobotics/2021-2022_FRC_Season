import commands2
import ctre
import constants

class Climber(commands2.SubsystemBase):
    def __init__(self) -> None:
        super().__init__()

        self.climberMotorShort = ctre.TalonFX(constants.kclimber1)
        self.climberMotorTilted = ctre.TalonFX(constants.kclimber2)
        
        # config feedback sensor
        self.climberMotorShort.configSelectedFeedbackSensor(ctre.FeedbackDevice.IntegratedSensor, 0, constants.ktimeoutMs)
        
        self.climberMotorTilted.configSelectedFeedbackSensor(ctre.FeedbackDevice.IntegratedSensor, 0, constants.ktimeoutMs)
        

        # configs
        self.climberMotorShort.configNominalOutputForward(0, constants.ktimeoutMs)
        self.climberMotorShort.configNominalOutputReverse(0, constants.ktimeoutMs)
        self.climberMotorShort.configPeakOutputForward(1, constants.ktimeoutMs)
        self.climberMotorShort.configPeakOutputReverse(-1, constants.ktimeoutMs)
        
        self.climberMotorTilted.configNominalOutputForward(0, constants.ktimeoutMs)
        self.climberMotorTilted.configNominalOutputReverse(0, constants.ktimeoutMs)
        self.climberMotorTilted.configPeakOutputForward(1, constants.ktimeoutMs)
        self.climberMotorTilted.configPeakOutputReverse(-1, constants.ktimeoutMs)
        

        self.climberMotorShort.selectProfileSlot(constants.kSlotIdx, constants.kPIDLoopIdx)
        
        self.climberMotorTilted.selectProfileSlot(constants.kSlotIdx, constants.kPIDLoopIdx)
        

        self.climberMotorShort.config_kP(constants.kSlotIdx, constants.kP, constants.ktimeoutMs) 
        self.climberMotorShort.config_kI(constants.kSlotIdx, constants.kI, constants.ktimeoutMs)
        self.climberMotorShort.config_kD(constants.kSlotIdx, constants.kD, constants.ktimeoutMs)
        self.climberMotorShort.config_kF(constants.kSlotIdx, constants.kF, constants.ktimeoutMs)
        
        self.climberMotorTilted.config_kP(constants.kSlotIdx, constants.kP, constants.ktimeoutMs) 
        self.climberMotorTilted.config_kI(constants.kSlotIdx, constants.kI, constants.ktimeoutMs)
        self.climberMotorTilted.config_kD(constants.kSlotIdx, constants.kD, constants.ktimeoutMs)
        self.climberMotorTilted.config_kF(constants.kSlotIdx, constants.kF, constants.ktimeoutMs)
        

        self.climberMotorShort.configMotionCruiseVelocity(constants.kmotorCruiseVelocity, constants.ktimeoutMs)
        
        self.climberMotorTilted.configMotionCruiseVelocity(constants.kmotorCruiseVelocity, constants.ktimeoutMs)
        

        self.climberMotorShort.setSelectedSensorPosition(0, constants.kPIDLoopIdx, constants.ktimeoutMs)
        
        self.climberMotorTilted.setSelectedSensorPosition(0, constants.kPIDLoopIdx, constants.ktimeoutMs)
        

        # zero sensor
        self.climberMotorShort.setNeutralMode(ctre.NeutralMode.Brake)
        
        self.climberMotorTilted.setNeutralMode(ctre.NeutralMode.Brake)
        


    def useShortClimber(self, positionChange) -> None:
        self.positionChange = positionChange
        self.climberMotorShort.set(ctre.TalonFXControlMode.MotionMagic, self.positionChange + self.climberMotor.getSelectedSensorPosition())
        
    def zeroSensor(self, climber: int) -> None:
        self.climber = climber
        if self.climber == 1:
           self.climberMotorShort.setSelectedSensorPosition(0, 0, constants.ktimeoutMs)
        elif self.climber == 2:
            self.climberMotorTilted.setSelectedSensorPosition(0, 0, constants.ktimeoutMs)
        else:
            self.climberMotorShort.setSelectedSensorPosition(0, 0, constants.ktimeoutMs)
            self.climberMotorTilted.setSelectedSensorPosition(0, 0, constants.ktimeoutMs)
            

    def isShortClimberFullyRetracted(self) -> bool:
        self.climberPos = self.climberMotorShort.getSelectedSensorPosition()
        self.climberVel = self.climberMotorShort.getSelectedSensorVelocity()

        if self.climberVel == 0.0 and self.climberPos != 0.0:
            return True
        else:
            return False
        
    def isTiltedClimberFullyRetracted(self) -> bool:
        self.climberPos = self.climberMotorTilted.getSelectedSensorPosition()
        self.climberVel = self.climberMotorTilted.getSelectedSensorVelocity()

        if self.climberVel == 0.0 and self.climberPos != 0.0:
            return True
        else:
            return False

    
    def isShortClimberFullyExtended(self) -> bool:
        self.climberPos = self.climberMotorShort.getSelectedSensorPosition()
        self.climberVel = self.climberMotorShort.getSelectedSensorVelocity()

        if self.climberVel > 100.0 and self.climberPos >= 1000.0:
            return True
        else:
            return False
        
    def isTiltedClimberFullyExtended(self) -> bool:
        self.climberPos = self.climberMotorTilted.getSelectedSensorPosition()
        self.climberVel = self.climberMotorTilted.getSelectedSensorVelocity()

        if self.climberVel > 100.0 and self.climberPos >= 1000.0:
            return True
        else:
            return False
        
    def useShortClimberPercent(self, sPercentage: float) -> None:
        self.percentage = sPercentage
        self.climberMotorShort.set(ctre.TalonFXControlMode.PercentOutput, self.percent)
        
    def useTiltedClimberPercent(self, tPercentage: float) -> None:
        self.percentage = tPercentage
        self.climberMotorTilted.set(ctre.TalonFXControlMode.PercentOutput, self.percent)
