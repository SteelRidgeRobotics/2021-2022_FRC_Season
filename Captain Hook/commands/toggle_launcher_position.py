import commands2
from subsystems.launcher import Launcher

class ToggleLauncherPosition(commands2.CommandBase):
    def __init__(self, launcher: Launcher):
        super().__init__()
        
        self.launcher = launcher
        
        self.isDone = False
        self.addRequirements([self.launcher])
    
    def execute(self) -> None:
        self.launcher.togglePosition()
        # may need to add some sort of wait here
        self.isDone = True
    
    #def end(self) -> None:
        
    
    def isFinished(self) -> bool:
        return self.isDone
