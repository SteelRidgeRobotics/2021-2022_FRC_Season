from commands2 import InstantCommand
import commands2
from wpimath.geometry import Pose2d, Translation2d, Rotation2d
from wpimath.trajectory import TrajectoryGenerator

from subsystems.drivetrain import Drivetrain

class MultiplePaths(commands2.SequentialCommandGroup):
    
    def __init__(self, drive: Drivetrain)-> None:
        super().__init__()

        self.drive = drive

        trajectory1 = TrajectoryGenerator.generateTrajectory(
            Pose2d(0,0.5, Rotation2d(0)),
            [Translation2d(2,0.5), Translation2d(3, 1), Translation2d(4, 1.5), Translation2d(5, 1)],
            Pose2d(6, 0.5, Rotation2d.fromDegrees(0)),
            self.drive.generateConfig(False),
        )
        trajectory2 = TrajectoryGenerator.generateTrajectory(
            Pose2d(6,0.5, Rotation2d(180)),
            [Translation2d(5,1), Translation2d(4, 1.5), Translation2d(3, 1), Translation2d(2, 0.5)],
            Pose2d(0, 0.5, Rotation2d.fromDegrees(0)),
            self.drive.generateConfig(True),
        )


        self.addCommands(
            InstantCommand(lambda: drive.resetOdometry(trajectory1.initialPose())),
            self.drive.createTrajectoryCommand(trajectory1, False).withTimeout(50),
            self.drive.createTrajectoryCommand(trajectory2, False).withTimeout(50),
            )
