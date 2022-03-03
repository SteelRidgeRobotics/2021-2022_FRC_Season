from commands1 import WaitCommand
import commands2
from subsystems.launcher import Launcher
from commands.toggle_launcher_position import ToggleLauncherPosition

class LaunchCargo(commands2.SequentialCommandGroup):
    def __init__(self, launcher: Launcher):
        super().__init__()
        self.addCommands(
            ToggleLauncherPosition(launcher),
            WaitCommand(3),
            ToggleLauncherPosition(launcher)
            )
