import wpilib
import commands2
from commands2.button import JoystickButton
import ctre
from constants import *
from wpilib import XboxController
from commands.drivewithjoystick import DrivewithJoystick
from commands.motionmagic import MotionMagic
from commands.multiplepaths import MultiplePaths
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

        
        self.drive.resetEncoders()
        self.drive.stopandReset()

        # Autonomous commands. 
        # We can add as many as we need.
        self.autoPath = MultiplePaths(self.drive) #This runs the multiple paths and requires the drivetrain subsystem.

        # Chooser
        self.chooser = wpilib.SendableChooser()

        # Add commands to the autonomous command chooser
        self.chooser.setDefaultOption("Multiple Paths", self.autoPath)
        #self.chooser.addOption("Original Auto", self.autoPath)
        #self.chooser.addOption("Complex Auto", self.complexAuto)

        # Put the chooser on the dashboard
        wpilib.SmartDashboard.putData("Autonomous", self.chooser)


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
        return self.chooser.getSelected()