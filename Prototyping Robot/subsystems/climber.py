import commands2
import ctre
import constants

class Climber(commands2.SubsystemBase):
    def __init__(self) -> None:
        super().__init__()

        self.climberMotorShort = ctre.TalonFX(constants.kclimber)
        # config feedback sensor
        self.climberMotorShort.configSelectedFeedbackSensor(ctre.FeedbackDevice.IntegratedSensor, 0, constants.ktimeoutMs)

        # configs
        self.climberMotorShort.configNominalOutputForward(0, constants.ktimeoutMs)
        self.climberMotorShort.configNominalOutputReverse(0, constants.ktimeoutMs)
        self.climberMotorShort.configPeakOutputForward(1, constants.ktimeoutMs)
        self.climberMotorShort.configPeakOutputReverse(-1, constants.ktimeoutMs)

        self.climberMotorShort.selectProfileSlot(constants.kSlotIdx, constants.kPIDLoopIdx)

        self.climberMotorShort.config_kP(constants.kSlotIdx, constants.kP, constants.ktimeoutMs) 
        self.climberMotorShort.config_kI(constants.kSlotIdx, constants.kI, constants.ktimeoutMs)
        self.climberMotorShort.config_kD(constants.kSlotIdx, constants.kD, constants.ktimeoutMs)
        self.climberMotorShort.config_kF(constants.kSlotIdx, constants.kF, constants.ktimeoutMs)

        self.climberMotorShort.configMotionCruiseVelocity(constants.kmotorCruiseVelocity, constants.ktimeoutMs)

        self.climberMotorShort.setSelectedSensorPosition(0, constants.kPIDLoopIdx, constants.ktimeoutMs)

        # zero sensor
        self.climberMotorShort.setNeutralMode(ctre.NeutralMode.Brake)


    def useClimber(self, positionChange) -> None:
        self.positionChange = positionChange
        self.climberMotorShort.set(ctre.TalonFXControlMode.MotionMagic, self.positionChange + self.climberMotor.getSelectedSensorPosition())
        
    def zeroSensor(self) -> None:
        self.climberMotorShort.setSelectedSensorPosition(0, 0, constants.ktimeoutMs)

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
