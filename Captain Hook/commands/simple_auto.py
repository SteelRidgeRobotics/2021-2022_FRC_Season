import commands2
from commands2 import WaitCommand
from subsystems.drivetrain import Drivetrain

from commands.launch_cargo import LaunchCargo
from subsystems.launcher import Launcher
from commands.timed_drive import TimedDrive

class SimpleAuto(commands2.SequentialCommandGroup):
    #initiate stuff
    def __init__(self, launcher: Launcher, drivetrain: Drivetrain) -> None:
        #use the  initiation function of the parent class (sequential command group). super() refers to the class we inherit from
        super().__init__()
        #this just adds all the commands to be done in sequence, you can refer to those files for more information. 
        #this will spin the bottom intake, wait, spin the top intake, wait, and then set both intakes to 0.
        self.addCommands(
            WaitCommand(5.0),
            LaunchCargo(launcher),
            WaitCommand(3.0),
            TimedDrive(drivetrain)
            )