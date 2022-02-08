import wpilib
import typing
import commands2
from subsystems.launcher import Launcher
import wpilib

class LaunchCargo(commands2.CommandBase):
    def __init__(self, launcher: Launcher):
        super().__init__()
        
        self.launcher = launcher
        
        self.isDone = False
        self.addRequirements([self.launcher])
        
        if self.launcher.isUp():
                self.launcher.goDown()
    
    def execute(self) -> None:
        self.launcher.launch()
        # may need to add some sort of wait here
        self.isDone = True
    
    def end(self) -> None:
        self.launcher.goDown()
        
    
    def isFinished(self) -> bool:
        return self.isDone
