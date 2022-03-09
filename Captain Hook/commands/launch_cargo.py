from commands2 import WaitCommand
import commands2
from subsystems.launcher import Launcher
from commands.toggle_launcher_position import ToggleLauncherPosition

class LaunchCargo(commands2.SequentialCommandGroup):
    def __init__(self, launcher: Launcher) -> None:
        super().__init__()
        self.addCommands(
            ToggleLauncherPosition(launcher),
            WaitCommand(1.5), 
            ToggleLauncherPosition(launcher)
            )
