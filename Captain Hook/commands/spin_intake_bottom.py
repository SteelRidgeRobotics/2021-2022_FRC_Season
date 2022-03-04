import commands2
from subsystems.intake import Intake

class SpinIntakeBottom(commands2.CommandBase):
    def __init__(self, intake: Intake, percent: float):
        super().__init__()
        
        self.intake = intake
        self.percent = percent
        self.isDone = False
        self.addRequirements([self.intake])
    
    def execute(self) -> None:
        self.intake.spinIntakeBottom(self.percent)
        # may need to add some sort of wait here
        

    def end(self, interrupted: bool) -> None:
       self.intake.spinIntakeBottom(0.0)   
       self.isDone = True    
    
    def isFinished(self) -> bool:
        return self.isDone