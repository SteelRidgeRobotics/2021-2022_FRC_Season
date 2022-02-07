import typing
import commands2
from subsystems.intake import Intake
import wpilib

class SpinIntakeWithPOV(commands2.CommandBase):
    def __init__(self, intake: Intake, povNum: typing.Callable[[], float]):
        super().__init__()
        self.intake = intake
        self.povNum = povNum
        self.done = False
        self.addRequirements([self.intake])
        
    def execute(self) -> None:
        if self.povNum == 0:
            self.intake.spinIntake(1.0)
        elif self.povNum == 180:
            self.intake.spinIntake(-1.0)
        else:
            self.intake.spinIntake(0.0)
      
    def end(self) -> None:
        self.intake.spinIntake(0.0)
      
    def isFinished(self) -> bool:
        return False
