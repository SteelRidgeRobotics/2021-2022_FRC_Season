from commands2 import InstantCommand
import commands2
from wpimath.geometry import Pose2d, Translation2d, Rotation2d
from wpimath.trajectory import TrajectoryGenerator, TrajectoryConfig
from wpimath.trajectory.constraint import DifferentialDriveVoltageConstraint
from wpimath.controller import SimpleMotorFeedforwardMeters
from constants import *
from subsystems.drivetrain import Drivetrain

class MultiplePaths(commands2.SequentialCommandGroup):
    """This is a sequential command group. It requires the Drivetrain subsystem.
    If a command needs another subsystem, add it to the list, then instantiate."""
    
    def __init__(self, drive: Drivetrain)-> None:
        super().__init__()
        
        #initialize drivetrain
        self.drive = drive

        #set voltage and feed forward requirements for trajectory following
        autoVoltageConstraint = DifferentialDriveVoltageConstraint(SimpleMotorFeedforwardMeters(kS, kA), kdriveKinematics, maxVoltage = 10)

        #config FORWARD trajectories
        config = TrajectoryConfig(kmaxVelocity, kmaxAccel)
        config.setKinematics(kdriveKinematics)
        config.addConstraint(autoVoltageConstraint)
        config.setReversed(False)

        #config REVERSE trajctories (see the "True")
        config2 = TrajectoryConfig(kmaxVelocity, kmaxAccel)
        config2.setKinematics(kdriveKinematics)
        config2.addConstraint(autoVoltageConstraint)
        config2.setReversed(True)

        # Our first trajectory: This is forward
        # The first Pose2d() and Rotation2d() is the start point
        # and angle.
        # The middle Translation2d() is a list [] of waypoints to pass through
        # The last Pose2d() and Rotation2d() is the end point
        # and angle. 
        trajectory1 = TrajectoryGenerator.generateTrajectory(
            Pose2d(0,0.5, Rotation2d(0)),
            [Translation2d(2,0.5), Translation2d(3, 1), Translation2d(4, 1.5), Translation2d(5, 1)],
            Pose2d(6, 0.5, Rotation2d.fromDegrees(0)),
            config,
        )

        # Our next trajectory: This is the reverse of the previous.
        # The first Pose2d() and Rotation2d() is the start point
        # and angle.
        # The middle Translation2d() is a list [] of waypoints to pass through
        # The last Pose2d() and Rotation2d() is the end point
        # and angle.
        trajectory2 = TrajectoryGenerator.generateTrajectory(
            Pose2d(6,0.5, Rotation2d(0)),
            [Translation2d(5,1), Translation2d(4, 1.5), Translation2d(3, 1), Translation2d(2, 0.5)],
            Pose2d(0, 0.5, Rotation2d.fromDegrees(0)),
            config2,
        )

        # We can add as many trajectories as needed!

        # This is our sequential commands.
        # Add as many as needed.
        # We can add parallel groups within.
        # The "self.drive.createTrajectoryCommand"
        # is a command that was build in the drivetrain.
        # Generally the commands are added from commands
        # of the robot.
        # InstantCommands are good for resetting things.
        self.addCommands(
            
            InstantCommand(lambda: drive.resetOdometry(trajectory1.initialPose())),
            self.drive.createTrajectoryCommand(trajectory1, False).withTimeout(50),
            self.drive.createTrajectoryCommand(trajectory2, False).withTimeout(50),
            )
