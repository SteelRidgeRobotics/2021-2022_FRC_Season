import commands2
from subsystems.intake import Intake

class ToggleIntakePosition(commands2.CommandBase):
    def __init__(self, intake: Intake):
        super().__init__()
        
        self.intake = intake
        
        self.isDone = False
        self.addRequirements([self.intake])
    
    def execute(self) -> None:
        self.intake.toggleIntakePosition()
        # may need to add some sort of wait here
        self.isDone = True
    
    #def end(self) -> None:
        
    
    def isFinished(self) -> bool:
        return self.isDone