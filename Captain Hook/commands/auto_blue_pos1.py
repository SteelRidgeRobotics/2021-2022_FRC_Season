import commands2
from commands2 import InstantCommand, ParallelCommandGroup, WaitCommand
from commands.toggle_intake_position import ToggleIntakePosition
from commands.timed_intake_bottom import TimedIntakeBottom
from commands.timed_intake_top import TimedIntakeTop
from subsystems.drivetrain import Drivetrain
from subsystems.intake import Intake

from path_trajectory import PathTrajectory

from commands.launch_cargo import LaunchCargo
from commands.auto_intake import AutoIntake
from subsystems.launcher import Launcher

class AutoBluePos1(commands2.SequentialCommandGroup):
    #initiate stuff
    def __init__(self, intake: Intake, launcher: Launcher, drivetrain: Drivetrain, pathTrajectory: PathTrajectory) -> None:
        #use the  initiation function of the parent class (sequential command group). super() refers to the class we inherit from
        super().__init__()
        #this just adds all the commands to be done in sequence, you can refer to those files for more information. 
        #this will spin the bottom intake, wait, spin the top intake, wait, and then set both intakes to 0.
        self.addCommands(
            InstantCommand(lambda: drivetrain.resetOdometry(pathTrajectory.trajectoryBlue2p1.initialPose())),
            WaitCommand(3.0),
            ParallelCommandGroup(LaunchCargo(launcher),ToggleIntakePosition(intake)),
            ParallelCommandGroup(drivetrain.createTrajectoryCommand(pathTrajectory.trajectoryBlue2p1, False).withTimeout(50),TimedIntakeBottom(intake, 0.30, 4.0)),
            ToggleIntakePosition(intake),
            WaitCommand(3.0),
            TimedIntakeTop(intake, -0.25, 2.0),
            drivetrain.createTrajectoryCommand(pathTrajectory.trajectoryBlue2p2, False).withTimeout(50),
            LaunchCargo(launcher),
            )