import commands2
from subsystems.intake import Intake

class SpinIntakeTop(commands2.CommandBase):
    def __init__(self, intake: Intake):
        super().__init__()
        
        self.intake = intake
        self.isDone = False
        self.addRequirements([self.intake])
    
    def execute(self) -> None:
        print(self.intake)
        self.intake.spinIntakeTop(0.4)
        # may need to add some sort of wait here

    def end(self, interrupted: bool) -> None:
        self.intake.spinIntakeTop(0.0)
        self.isDone = True       
    
    def isFinished(self) -> bool:
        return self.isDone