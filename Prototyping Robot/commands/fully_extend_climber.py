import wpilib
import commands2
from subsystems.climber import Climber
import constants

class FullyExtendClimber(commands2.CommandBase):
    def __init__(self, climber: Climber):
        super().__init__()

        self.climber = climber

        self.addRequirements([self.climber])

    def execute(self) -> None:
        wpilib.SmartDashboard.putNumber("   Climber Position - ", (self.climber.climberMotor.getSelectedSensorPosition()))
        wpilib.SmartDashboard.putNumber("   Climber Velocity - ", (self.climber.climberMotor.getSelectedSensorVelocity()))
        

        if self.climber.climberMotor.getSelectedSensorVelocity() < 100:
            self.climber.useClimber(-constants.kClimberRate)
        else:
            self.climber.useClimber(0)

    def end(self, interrupted: bool) -> None:
        self.climber.useClimber(0)
       
        
    
    def isFinished(self) -> bool:
        return self.climber.isFullyExtended() # this number may change but this is an estimate of the velocity of the falcon 500 when the climber is fully retracted