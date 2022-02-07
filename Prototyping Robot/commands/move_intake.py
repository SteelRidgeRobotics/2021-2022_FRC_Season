import typing
import commands2
from subsystems.intake import Intake
import wpilib

class MoveIntake(commands2.CommandBase):
    def __init__(self, intake: Intake, out: typing.Callable[[], bool]):
        super().__init__()
        self.intake = intake
        self.out = out
        self.done = False
        self.addRequirements([self.intake])
        
    def execute(self) -> None:
        if self.out:
            self.intake.pushIntakeOut()
            self.done = True
        else:
            self.intake.pullIntakeIn()
            self.done = True
      
    def end(self) -> None:
        """Some code here, if needed"""
      
    def isFinished(self) -> bool:
        return self.done
