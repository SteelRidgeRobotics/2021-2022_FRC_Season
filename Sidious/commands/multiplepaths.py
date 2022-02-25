import commands2
from subsystems.drivetrain import Drivetrain
from commands.runramsetepath import RunRamsetePath
from wpimath.geometry import Pose2d, Translation2d, Rotation2d

class MultiplePaths(commands2.SequentialCommandGroup):
    def __init__(self):
        
        super().__init__(
            # Drive forward the specified distance
            RunRamsetePath(self, Pose2d(0,0.5, Rotation2d(0)), [Translation2d(2,0.5), Translation2d(3, 1), Translation2d(4, 1.5), Translation2d(5, 1)], Pose2d(6, 0.5, Rotation2d.fromDegrees(0)), False),
            RunRamsetePath(self, Pose2d(0,0.5, Rotation2d(0)), [Translation2d(2,0.5), Translation2d(3, 1), Translation2d(4, 1.5), Translation2d(5, 1)], Pose2d(6, 0.5, Rotation2d.fromDegrees(0)), True)
            
        )
