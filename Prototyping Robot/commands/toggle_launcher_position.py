import wpilib
import typing
import commands2
from subsystems.launcher import Launcher
import wpilib

class ToggleLauncherPosition(commands2.CommandBase):
    def __init__(self, launcher: Launcher, up: typing.Callable[[], bool]):
        super().__init__()
        
        self.launcher = launcher
        self.up = up
        
        self.addRequirements([self.launcher])
    
    def execute(self):
        if self.up and not self.launcher.isUp():
            self.launcher.launch()
        else:
            if self.launcher.isUp():
                self.launcher.goDown()
     
    
