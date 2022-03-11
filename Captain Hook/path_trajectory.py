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
    def __init__(self, drive: Drivetrain):
        #super init (initializes sequentialcommandgroup)
        super().__init__()

        self.drive = drive
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

        self.trajectoryBlue1p1 = TrajectoryGenerator.generateTrajectory(Pose2d(6.95, 4.64, Rotation2d(157.09)), [Translation2d(6.2, 5.16)], Pose2d(5.53, 5.64, Rotation2d(144.25)), reverseConfig)
        self.trajectoryBlue1p2 = TrajectoryGenerator.generateTrajectory(Pose2d(5.53, 5.64, Rotation2d(144.25)), [Translation2d(6.2, 5.16)], Pose2d(6.95, 4.64, Rotation2d(157.09)), forwardConfig)
        