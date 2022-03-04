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
        self.intake.spinIntakeTop(self.percent)
        # may need to add some sort of wait here
        self.isDone = True 

    def end(self, interrupted: bool) -> None:
        self.intake.spinIntakeTop(0.0)
      
    def isFinished(self) -> bool:
        return self.isDone