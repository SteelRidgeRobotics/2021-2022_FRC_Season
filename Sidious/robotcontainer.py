import commands2
from commands2.button import JoystickButton
import ctre
from constants import *
from wpilib import XboxController
from customramsetecontrollerabstraction import CustomRamseteControllerAbstraction
from wpimath.controller import RamseteController, PIDController, SimpleMotorFeedforwardMeters
from wpimath.geometry import Pose2d, Rotation2d, Translation2d
from wpimath.trajectory import Trajectory, TrajectoryConfig, TrajectoryGenerator
from wpimath.trajectory.constraint import DifferentialDriveVoltageConstraint
from commands2 import RamseteCommand
from commands.drivewithjoystick import DrivewithJoystick
from commands.motionmagic import MotionMagic
from subsystems.drivetrain import Drivetrain




class RobotContainer:
    """
    This class is where the bulk of the robot should be declared. Since Command-based is a
    "declarative" paradigm, very little robot logic should actually be handled in the :class:`.Robot`
    periodic methods (other than the scheduler calls). Instead, the structure of the robot (including
    subsystems, commands, and button mappings) should be declared here.
    """

    def __init__(self) -> None:
        
        # The driver's controller
        self.driverController = XboxController(kdriverControllerPort)
        #self.functionsController = XboxController(kfunctionsControllerPort)

        self.frontLeft = ctre.TalonFX(kfrontLeft)
        self.backLeft = ctre.TalonFX(kbackLeft)
        self.frontRight = ctre.TalonFX(kfrontRight)
        self.backRight = ctre.TalonFX(kbackRight)

        self.verticalClimber = ctre.TalonFX(kverticalClimber)
        self.tiltedClimber = ctre.TalonFX(ktiltedClimber)
        
        # The robot's subsystems
        self.drive = Drivetrain()

        #self.drive.resetMotors()
        self.drive.resetEncoders()

        # Chooser
        #self.chooser = wpilib.SendableChooser()

        # Add commands to the autonomous command chooser
        #self.chooser.setDefaultOption("Auto", self.simpleAuto)
        #self.chooser.addOption("Complex Auto", self.complexAuto)

        # Put the chooser on the dashboard
        #wpilib.SmartDashboard.putData("Autonomous", self.chooser)


        self.configureButtonBindings()

        # set up default drive command --> This has been moved to robot.py for teleop periodic.
        #self.drive.setDefaultCommand(DrivewithJoystick(self.drive, lambda: -self.driverController.getLeftY(), lambda: -self.driverController.getRightY())) 

    def setDefaultCommand(self) -> None:
        """This is here to change the initialize of our default command to Telelop-periodic."""
        self.drive.setDefaultCommand(DrivewithJoystick(self.drive, lambda: -self.driverController.getLeftY(), lambda: -self.driverController.getRightY()))
    
    def configureButtonBindings(self):
        """
        Use this method to define your button->command mappings. Buttons can be created by
        instantiating a :GenericHID or one of its subclasses (Joystick or XboxController),
        and then passing it to a JoystickButton.
        """
        (JoystickButton(self.driverController, XboxController.Button.kLeftBumper).whenPressed(DrivewithJoystick(self.drive, lambda: -0.5*self.driverController.getLeftY(), lambda: -0.5*self.driverController.getRightY())).whenReleased(DrivewithJoystick(self.drive, lambda: -self.driverController.getLeftY(), lambda: -self.driverController.getRightY())))
        (JoystickButton(self.driverController, XboxController.Button.kA).whenPressed(MotionMagic(self.drive, kUnits)))

    def getAutonomousCommand(self) -> commands2.Command:

        start = Pose2d(0,0.5, Rotation2d(0))
        waypoints = [Translation2d(2,0.5), Translation2d(3, 1), Translation2d(4, 1.5), Translation2d(5, 1)]
        end = Pose2d(6, 0.5, Rotation2d.fromDegrees(0))
        alternate = [Pose2d(0,0, Rotation2d(0)), Pose2d(2, 1, Rotation2d.fromDegrees(-45)), Pose2d(4, 2, Rotation2d.fromDegrees(-90)), Pose2d(6, 1, Rotation2d.fromDegrees(45))]
        
        print("Creating Auto Command")

        autoVoltageConstraint = DifferentialDriveVoltageConstraint(SimpleMotorFeedforwardMeters(kS, kA), kdriveKinematics, maxVoltage = 10)

        config = TrajectoryConfig(kmaxVelocity, kmaxAccel)
        config.setKinematics(kdriveKinematics)
        config.addConstraint(autoVoltageConstraint)

        config2 = TrajectoryConfig(kmaxVelocity, kmaxAccel)
        config2.setKinematics(kdriveKinematics)
        config2.addConstraint(autoVoltageConstraint)
        config2.setReversed(True)

        trajectory = TrajectoryGenerator.generateTrajectory(start, waypoints, end, config)

        backwardsTrajectory = TrajectoryGenerator.generateTrajectory(start, waypoints, end, config2)

        finalTrajectory = trajectory + backwardsTrajectory

        alternateTrajectory = TrajectoryGenerator.generateTrajectory(alternate, config)

        print("Generated Trajectory")

        ramseteCommand = RamseteCommand(
            # The trajectory to follow.
            trajectory,
            #self.alternateTrajectory,
            # A reference to a method that will return our position.
            self.drive.getPose,
            # Our RAMSETE controller.
            CustomRamseteControllerAbstraction(kramsete_B, kramsete_Zeta),
            # A feedforward object for the robot.
            #SimpleMotorFeedforwardMeters(
            #    kS,
            #    kV,
            #    kA,
            #),
            # Our drive kinematics.
            kdriveKinematics,
            # A reference to a method which will return a DifferentialDriveWheelSpeeds object.
            #self.drive.getWheelSpeeds,
            # The turn controller for the left side of the drivetrain.
            #PIDController(kP, 0, 0),
            # The turn controller for the right side of the drivetrain.
            #PIDController(kP, 0, 0),
            # A reference to a method which will set a specified
            # voltage to each motor. The command will pass the two parameters.
            self.drive.tankDriveVelocity,
            # The subsystems the command should require.
            [self.drive],
        )

        print("Finished Creating Auto Command")

        self.drive.resetOdometry(trajectory.initialPose())
        #self.drive.resetOdometry(self.alternateTrajectory.initialPose())

        return ramseteCommand.andThen(lambda: self.drive.tankDriveVolts(0.0,0.0))