import commands2
import wpilib
from subsystems.intake import Intake

class TimedIntakeTop(commands2.CommandBase):
    def __init__(self, intake: Intake, percent: float, duration: float) -> None:
        super().__init__()
        self.intake = intake
        self.percent = percent
        self.duration = duration 
        
        self.startTime = 0.0
        
        self.addRequirements([self.intake])
        
    def initialize(self) -> None:
        self.startTime = wpilib.Timer.getFPGATimestamp()
        self.intake.spinIntakeTop(0.0)
            
    def execute(self) -> None:
        self.intake.spinIntakeTop(self.percent)
            
    def end(self, interrupted: bool) -> None:
        self.intake.spinIntakeTop(0.0)
            
    def isFinished(self) -> bool:
        return wpilib.Timer.getFPGATimestamp() - self.startTime >= self.duration
