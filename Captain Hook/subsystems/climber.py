import commands2
import ctre
import constants

class Climber(commands2.SubsystemBase):
    def __init__(self) -> None:
        super().__init__()

        self.climberMotorShort = ctre.TalonFX(constants.kclimber1)
        self.climberMotorTilted = ctre.TalonFX(constants.kclimber2)

        # zero sensor
        self.climberMotorShort.setNeutralMode(ctre.NeutralMode.Brake)
        
        self.climberMotorTilted.setNeutralMode(ctre.NeutralMode.Brake)

    def zeroSensor(self, climber: int) -> None:
        self.climber = climber
        if self.climber == 1:
           self.climberMotorShort.setSelectedSensorPosition(0, 0, constants.ktimeoutMs)
        elif self.climber == 2:
            self.climberMotorTilted.setSelectedSensorPosition(0, 0, constants.ktimeoutMs)
        else:
            self.climberMotorShort.setSelectedSensorPosition(0, 0, constants.ktimeoutMs)
            self.climberMotorTilted.setSelectedSensorPosition(0, 0, constants.ktimeoutMs)
        
    def useShortClimberPercent(self, sPercentage: float) -> None:
        self.percentage = sPercentage
        self.climberMotorShort.set(ctre.TalonFXControlMode.PercentOutput, self.percentage)
        
    def useTiltedClimberPercent(self, tPercentage: float) -> None:
        self.percentage = tPercentage
        self.climberMotorTilted.set(ctre.TalonFXControlMode.PercentOutput, self.percentage)
