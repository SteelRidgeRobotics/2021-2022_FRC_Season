from xmlrpc.client import Boolean
import commands2
from constants import *
from customramsetecontrollerabstraction import CustomRamseteControllerAbstraction
from wpimath.controller import RamseteController, PIDController, SimpleMotorFeedforwardMeters
from wpimath.geometry import Pose2d, Rotation2d, Translation2d
from wpimath.trajectory import Trajectory, TrajectoryConfig, TrajectoryGenerator
from wpimath.trajectory.constraint import DifferentialDriveVoltageConstraint
from commands2 import RamseteCommand
from subsystems.drivetrain import Drivetrain

class SetPathToDrive:
    def __init__(self) -> None:
        
        self.drive = Drivetrain()
        self.drive.resetEncoders()
        self.drive.stopandReset()

    def goPathA(self, isReverse: bool) -> commands2.Command:

        self.drive = Drivetrain()
        self.drive.resetEncoders()
        self.drive.stopandReset()

        print("Creating Trajectory A")

        autoVoltageConstraint = DifferentialDriveVoltageConstraint(SimpleMotorFeedforwardMeters(kS, kA), kdriveKinematics, maxVoltage = 10)

        config = TrajectoryConfig(kmaxVelocity, kmaxAccel)
        config.setKinematics(kdriveKinematics)
        config.addConstraint(autoVoltageConstraint)
        config.setReversed(isReverse)

        start = Pose2d(0,0.5, Rotation2d(0))
        waypoints = [Translation2d(2,0.5), Translation2d(3, 1), Translation2d(4, 1.5), Translation2d(5, 1)]
        end = Pose2d(6, 0.5, Rotation2d.fromDegrees(0))

        trajectory = TrajectoryGenerator.generateTrajectory(start, waypoints, end, config)

        print("Generated Trajectory A")

        ramseteCommand = RamseteCommand(
            # The trajectory to follow.
            trajectory,
            
            # A reference to a method that will return our position.
            self.drive.getPose,
            # Our RAMSETE controller.
            CustomRamseteControllerAbstraction(kramsete_B, kramsete_Zeta),
            
            # Our drive kinematics.
            kdriveKinematics,
            # A reference to a method which will set a specified
            # velocity to each motor. The command will pass the two parameters.
            self.drive.tankDriveVelocity,
            # The subsystems the command should require.
            [self.drive],
        )

        print("Finished Trajectory A")

        self.drive.resetOdometry(trajectory.initialPose())
        
        return ramseteCommand.andThen(lambda: self.drive.tankDriveVolts(0.0,0.0))


    def goPathB(self, isReverse: bool) -> commands2.Command:

        self.drive = Drivetrain()
        self.drive.resetEncoders()
        self.drive.stopandReset()

        print("Creating Trajectory B")

        autoVoltageConstraint = DifferentialDriveVoltageConstraint(SimpleMotorFeedforwardMeters(kS, kA), kdriveKinematics, maxVoltage = 10)

        config = TrajectoryConfig(kmaxVelocity, kmaxAccel)
        config.setKinematics(kdriveKinematics)
        config.addConstraint(autoVoltageConstraint)
        config.setReversed(isReverse)

        start = Pose2d(0,0.5, Rotation2d(0))
        waypoints = [Translation2d(2,0.5), Translation2d(3, 1), Translation2d(4, 1.5), Translation2d(5, 1)]
        end = Pose2d(6, 0.5, Rotation2d.fromDegrees(0))

        trajectory = TrajectoryGenerator.generateTrajectory(start, waypoints, end, config)

        print("Generated Trajectory B")

        ramseteCommand = RamseteCommand(
            # The trajectory to follow.
            trajectory,
            
            # A reference to a method that will return our position.
            self.drive.getPose,
            # Our RAMSETE controller.
            CustomRamseteControllerAbstraction(kramsete_B, kramsete_Zeta),
            
            # Our drive kinematics.
            kdriveKinematics,
            # A reference to a method which will set a specified
            # velocity to each motor. The command will pass the two parameters.
            self.drive.tankDriveVelocity,
            # The subsystems the command should require.
            [self.drive],
        )

        print("Finished Trajectory B")

        self.drive.resetOdometry(trajectory.initialPose())
        
        return ramseteCommand.andThen(lambda: self.drive.tankDriveVolts(0.0,0.0))
