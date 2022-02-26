from commands2 import InstantCommand
import commands2
from wpimath.geometry import Pose2d, Translation2d, Rotation2d
from wpimath.trajectory import TrajectoryGenerator, TrajectoryConfig
from wpimath.trajectory.constraint import DifferentialDriveVoltageConstraint
from wpimath.controller import SimpleMotorFeedforwardMeters
from constants import *
from subsystems.drivetrain import Drivetrain

class MultiplePaths(commands2.SequentialCommandGroup):
    
    def __init__(self, drive: Drivetrain)-> None:
        super().__init__()

        self.drive = drive

        autoVoltageConstraint = DifferentialDriveVoltageConstraint(SimpleMotorFeedforwardMeters(kS, kA), kdriveKinematics, maxVoltage = 10)

        config = TrajectoryConfig(kmaxVelocity, kmaxAccel)
        config.setKinematics(kdriveKinematics)
        config.addConstraint(autoVoltageConstraint)
        config.setReversed(False)

        config2 = TrajectoryConfig(kmaxVelocity, kmaxAccel)
        config2.setKinematics(kdriveKinematics)
        config2.addConstraint(autoVoltageConstraint)
        config2.setReversed(True)

        trajectory1 = TrajectoryGenerator.generateTrajectory(
            Pose2d(0,0.5, Rotation2d(0)),
            [Translation2d(2,0.5), Translation2d(3, 1), Translation2d(4, 1.5), Translation2d(5, 1)],
            Pose2d(6, 0.5, Rotation2d.fromDegrees(0)),
            config,
        )
        trajectory2 = TrajectoryGenerator.generateTrajectory(
            Pose2d(6,0.5, Rotation2d(0)),
            [Translation2d(5,1), Translation2d(4, 1.5), Translation2d(3, 1), Translation2d(2, 0.5)],
            Pose2d(0, 0.5, Rotation2d.fromDegrees(0)),
            config2,
        )





        self.addCommands(
            
            InstantCommand(lambda: drive.resetOdometry(trajectory1.initialPose())),
            self.drive.createTrajectoryCommand(trajectory1, False).withTimeout(50),
            self.drive.createTrajectoryCommand(trajectory2, False).withTimeout(50),
            )
