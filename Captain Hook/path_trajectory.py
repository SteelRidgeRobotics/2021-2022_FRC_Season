#import wpilib and commands2 module
import wpilib
import commands2

#wpimath is a module that helps us with poses, generating trajectories, etc.
from wpimath.geometry import Pose2d, Translation2d, Rotation2d
from wpimath.trajectory import TrajectoryGenerator, TrajectoryConfig
from wpimath.trajectory.constraint import DifferentialDriveVoltageConstraint
from wpimath.controller import SimpleMotorFeedforwardMeters

#import drivetrain system and constants
from subsystems.drivetrain import Drivetrain
import constants

#class for command
class PathTrajectory:
    #init function with self and drivetrain. here's a fun fact: you don't need to use self, you can use any name.
    def __init__(self, drive: Drivetrain, pathNum: float):
        #super init (initializes sequentialcommandgroup)
        super().__init__()

        self.drive = drive
        self.pathNum = pathNum
        #voltage and feedforward
        autoVoltageConstraint = DifferentialDriveVoltageConstraint(SimpleMotorFeedforwardMeters(constants.kS, constants.kA), constants.kdriveKinematics, maxVoltage=10)

        #configure forward and reverse trajectories
        forwardConfig = TrajectoryConfig(constants.kmaxVelocity, constants.kmaxAccel)
        forwardConfig.setKinematics(constants.kdriveKinematics)
        forwardConfig.addConstraint(autoVoltageConstraint)
        forwardConfig.setReversed(False)

        reverseConfig = TrajectoryConfig(constants.kmaxVelocity, constants.kmaxAccel)
        reverseConfig.setKinematics(constants.kdriveKinematics)
        reverseConfig.addConstraint(autoVoltageConstraint)
        reverseConfig.setReversed(True)

        self.trajectory1p1 = TrajectoryGenerator.generateTrajectory(Pose2d(7.66, 2.63, Rotation2d(-112.25)), Pose2d(7.63, 1.09, Rotation2d(-90.00)))
        self.trajectory2p1 = TrajectoryGenerator.generateTrajectory(Pose2d(7.66, 2.63, Rotation2d(-112.25)), Pose2d(5.80, 2.26, Rotation2d(-155.82)))
        self.trajectory3p1 = TrajectoryGenerator.generateTrajectory(Pose2d(6.78, 4.75, Rotation2d(-158.39)), Pose2d(5.67, 5.85, Rotation2d(-149.68)))

        self.trajectory1p2 = TrajectoryGenerator.generateTrajectory(Pose2d(7.63, 1.09, Rotation2d(-90.00)), Pose2d(7.66, 2.63, Rotation2d(-112.25)))
        self.trajectory2p2 = TrajectoryGenerator.generateTrajectory(Pose2d(5.80, 2.26, Rotation2d(-155.82)), Pose2d(7.66, 2.63, Rotation2d(-112.25)))
        self.trajectory3p2 = TrajectoryGenerator.generateTrajectory(Pose2d(5.67, 5.85, Rotation2d(-149.68)), Pose2d(6.78, 4.75, Rotation2d(-158.39)))

        self.trajectoryBlue2p1 = TrajectoryGenerator.generateTrajectory(Pose2d(7.48, 2.6, Rotation2d(-161.75)), [Translation2d(6.46, 2.47)], Pose2d(5.78, 2.38, Rotation2d(-173.06)))
        self.trajectoryBlue2p2 = TrajectoryGenerator.generateTrajectory(Pose2d(5.78, 2.38, Rotation2d(-173.06), [Translation2d(5.41, 0.73)], Pose2d(7.02, 0.61, Rotation2d(-1.16))))
        self.trajectoryBlue2p3 = TrajectoryGenerator.generateTrajectory(Pose2d(7.02, 0.61, Rotation2d(-1.16)), [Translation2d(8.09, 1.67)], Pose2d(7.49, 2.34, Rotation2d(-112.87)))
        self.trajectoryBlue2p4 = TrajectoryGenerator.generateTrajectory(Pose2d(7.49, 2.34, Rotation2d(-112.87), [Translation2d(5.41, 1.82), Translation2d(3.42, 2.06)], Pose2d(1.59, 1.70, Rotation2d(-151.65))))

        