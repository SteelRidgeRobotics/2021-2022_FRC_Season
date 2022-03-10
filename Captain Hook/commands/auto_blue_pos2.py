import commands2
from commands2 import InstantCommand
from subsystems.drivetrain import Drivetrain
from subsystems.intake import Intake

from path_trajectory import PathTrajectory

from commands.launch_cargo import LaunchCargo
from commands.auto_intake import AutoIntake
from subsystems.launcher import Launcher

class AutoBluePos2(commands2.SequentialCommandGroup):
    #initiate stuff
    def __init__(self, intake: Intake, launcher: Launcher, drivetrain: Drivetrain, pathTrajectory: PathTrajectory) -> None:
        #use the  initiation function of the parent class (sequential command group). super() refers to the class we inherit from
        super().__init__()
        #this just adds all the commands to be done in sequence, you can refer to those files for more information. 
        #this will spin the bottom intake, wait, spin the top intake, wait, and then set both intakes to 0.
        self.addCommands(
            InstantCommand(lambda: drivetrain.resetOdometry(pathTrajectory.trajectoryBlue2p1.initialPose())),
            LaunchCargo(launcher),
            drivetrain.createTrajectoryCommand(pathTrajectory.trajectoryBlue2p1, False).withTimeout(50),
            AutoIntake(intake),
            drivetrain.createTrajectoryCommand(pathTrajectory.trajectoryBlue2p2, False).withTimeout(50),
            AutoIntake(intake),
            drivetrain.createTrajectoryCommand(pathTrajectory.trajectoryBlue2p3, False).withTimeout(50),
            LaunchCargo(launcher),
            drivetrain.createTrajectoryCommand(pathTrajectory.trajectoryBlue2p4, False).withTimeout(50)
            #drivetrain.createTrajectoryCommand(pathTrajectory.trajectory1p1, False).withTimeout(50),
            #pick up cargo
            #drivetrain.createTrajectoryCommand(pathTrajectory.trajectory1p2, False).withTimeout(50),
            )
