import wpilib
import commands2
from subsystems.intake import Intake

class SpinIntakeTop(commands2.CommandBase):
    def __init__(self, intake: Intake, percent: float):
        super().__init__()
        
        self.intake = intake
        self.isDone = False
        self.percent = percent
        self.addRequirements([self.intake])
    
    def execute(self) -> None:
        wpilib.SmartDashboard.putNumber('   top intake wheel - ', self.percent)
        self.intake.spinIntakeTop(self.percent)
        # may need to add some sort of wait here

    def end(self, interrupted: bool) -> None:
        self.isDone = True
        wpilib.SmartDashboard.putNumber('   top intake wheel - ', self.percent)
      
    def isFinished(self) -> bool:
        return self.isDone