import commands2
from subsystems.drivetrain import Drivetrain
from constants import *
from customramsetecontrollerabstraction import CustomRamseteControllerAbstraction
from wpimath.controller import SimpleMotorFeedforwardMeters
from wpimath.geometry import Pose2d, Translation2d, Rotation2d
from wpimath.kinematics import DifferentialDriveOdometry
from wpimath.trajectory import TrajectoryConfig, TrajectoryGenerator
from wpimath.trajectory.constraint import DifferentialDriveVoltageConstraint
from commands2 import RamseteCommand


class RunRamsetePath(commands2.CommandBase):
    def __init__(self,  drive: Drivetrain, start: Pose2d, waypoints: list[Translation2d], end: Pose2d, isReversed: bool) -> None:
        super().__init__()
        drive = Drivetrain()
        self.drive = drive
        self.drive.resetEncoders()
        self.drive.stopandReset()
        self.m_start = start
        self.m_waypoints = waypoints
        self.m_end = end
        self.m_isReversed = isReversed

        print("Creating Trajectory A")

        autoVoltageConstraint = DifferentialDriveVoltageConstraint(SimpleMotorFeedforwardMeters(kS, kA), kdriveKinematics, maxVoltage = 10)

        config = TrajectoryConfig(kmaxVelocity, kmaxAccel)
        config.setKinematics(kdriveKinematics)
        config.addConstraint(autoVoltageConstraint)
        config.setReversed(self.m_isReversed)

        #m_start = Pose2d(0,0.5, Rotation2d(0))
        #waypoints = [Translation2d(2,0.5), Translation2d(3, 1), Translation2d(4, 1.5), Translation2d(5, 1)]
        #end = Pose2d(6, 0.5, Rotation2d.fromDegrees(0))

        self.trajectory = TrajectoryGenerator.generateTrajectory(self.m_start, self.m_waypoints, self.m_end, config)

        print("Generated Trajectory A")

        self.ramseteCommand = RamseteCommand(
            # The trajectory to follow.
            self.trajectory,
            
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

        self.drive.resetOdometry(self.trajectory.initialPose())


        self.addRequirements([self.drive])

    def execute(self) -> None:
        self.ramseteCommand.execute()

    def end(self, interrupted: bool) -> None:
        self.ramseteCommand.end(interrupted)


    def isFinished(self) -> bool:
        return self.ramseteCommand.isFinished()