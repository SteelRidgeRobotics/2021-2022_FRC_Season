import wpilib
import commands2
from subsystems.climber import Climber
import constants

class FullyRetractClimber(commands2.CommandBase):
    def __init__(self, climber: Climber, climberMotor: int):
        super().__init__()

        self.climber = climber
        self.climberMotor = climberMotor

        self.addRequirements([self.climber])

    def execute(self) -> None:
        wpilib.SmartDashboard.putNumber("   Climber Position - ", (self.climber.climberMotorShort.getSelectedSensorPosition()))
        wpilib.SmartDashboard.putNumber("   Climber Velocity - ", (self.climber.climberMotorShort.getSelectedSensorVelocity()))
        wpilib.SmartDashboard.putNumber("   Climber Position - ", (self.climber.climberMotorTilted.getSelectedSensorPosition()))
        wpilib.SmartDashboard.putNumber("   Climber Velocity - ", (self.climber.climberMotorTilted.getSelectedSensorVelocity()))
        
        if self.climberMotor == 1:
            if self.climber.climberMotorShort.getSelectedSensorVelocity() < 100:
                self.climber.useShortClimber(-constants.kClimberRate)
            else:
                self.climber.useShortClimber(0)
                
        if self.climberMotor == 2:
            if self.climber.climberMotorTilted.getSelectedSensorVelocity() < 100:
                self.climber.useTiltedClimber(-constants.kClimberRate)
            else:
                self.climber.useTiltedClimber(0)

    def end(self, interrupted: bool) -> None:
        self.climber.useShortClimber(0)
        self.climber.useTiltedClimber(0)
       
    def isFinished(self) -> bool:
        if self.climberMotor == 1:
            return self.climber.isShortClimberFullyRetracted()
        else:
            return self.climber.isTiltedClimberFullyRetracted() # this number may change but this is an estimate of the velocity of the falcon 500 when the climber is fully retracted
