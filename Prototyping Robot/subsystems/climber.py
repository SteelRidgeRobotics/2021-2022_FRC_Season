import commands2
import ctre
import constants

class Climber(commands2.SubsystemBase):
    def __init__(self) -> None:
        super().__init__()

        self.climberMotor = ctre.TalonFX(constants.kclimber)
        # config feedback sensor
        self.climberMotor.configSelectedFeedbackSensor(ctre.FeedbackDevice.IntegratedSensor, 0, constants.ktimeoutMs)

        # configs
        self.climberMotor.configNominalOutputForward(0, constants.ktimeoutMs)
        self.climberMotor.configNominalOutputReverse(0, constants.ktimeoutMs)
        self.climberMotor.configPeakOutputForward(1, constants.ktimeoutMs)
        self.climberMotor.configPeakOutputReverse(-1, constants.ktimeoutMs)

        self.climberMotor.selectProfileSlot(constants.kSlotIdx, constants.kPIDLoopIdx)

        self.climberMotor.config_kP(constants.kSlotIdx, constants.kP, constants.ktimeoutMs) 
        self.climberMotor.config_kI(constants.kSlotIdx, constants.kI, constants.ktimeoutMs)
        self.climberMotor.config_kD(constants.kSlotIdx, constants.kD, constants.ktimeoutMs)
        self.climberMotor.config_kF(constants.kSlotIdx, constants.kF, constants.ktimeoutMs)

        self.climberMotor.configMotionCruiseVelocity(constants.kmotorCruiseVelocity, constants.ktimeoutMs)

        self.climberMotor.setSelectedSensorPosition(0, constants.kPIDLoopIdx, constants.ktimeoutMs)

        # zero sensor
        self.climberMotor.setNeutralMode(ctre.NeutralMode.Brake)


    def useClimber(self, positionChange) -> None:
        self.positionChange = positionChange
        self.climberMotor.set(ctre.TalonFXControlMode.MotionMagic, self.positionChange + self.climberMotor.getSelectedSensorPosition())
        
    def zeroSensor(self) -> None:
        self.climberMotor.setSelectedSensorPosition(0, 0, constants.ktimeoutMs)

    def isFullyRetracted(self) -> bool:
        self.climberPos = self.climberMotor.getSelectedSensorPosition()
        self.climberVel = self.climberMotor.getSelectedSensorVelocity()

        if self.climberVel == 0.0 and self.climberPos != 0.0:
            return True
        else:
            return False

    
    def isFullyExtended(self) -> bool:
        self.climberPos = self.climberMotor.getSelectedSensorPosition()
        self.climberVel = self.climberMotor.getSelectedSensorVelocity()

        if self.climberVel > 100.0 and self.climberPos >= 1000.0:
            return True
        else:
            return False