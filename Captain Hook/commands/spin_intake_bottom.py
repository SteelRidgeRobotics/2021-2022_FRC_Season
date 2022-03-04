import commands2
import wpilib
from subsystems.intake import Intake

class SpinIntakeBottom(commands2.CommandBase):
    def __init__(self, intake: Intake):
        super().__init__()
        
        self.intake = intake
        self.isDone = False
        self.addRequirements([self.intake])
    
    def execute(self) -> None:
        self.intake.spinIntakeBottom(1.0)
        wpilib.SmartDashboard.putNumber('   INTAKE BOTTOM - ', 1)
        # may need to add some sort of wait here

    def end(self, interrupted: bool) -> None:
        self.intake.spinIntakeBottom(0.0)
        self.isDone = True       
    
    def isFinished(self) -> bool:
        return self.isDone