from hal import JoystickButtons
import wpilib
import commands2
from commands2.button import JoystickButton
import constants
import ctre
from wpilib import XboxController
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
        self.driverController = XboxController(constants.kdriverControllerPort)
        #self.functionsController = XboxController(constants.kfunctionsControllerPort)

        self.frontLeft = ctre.TalonFX(constants.kfrontLeft)
        self.backLeft = ctre.TalonFX(constants.kbackLeft)
        self.frontRight = ctre.TalonFX(constants.kfrontRight)
        self.backRight = ctre.TalonFX(constants.kbackRight)

        self.verticalClimber = ctre.TalonFX(constants.kverticalClimber)
        self.tiltedClimber = ctre.TalonFX(constants.ktiltedClimber)
        
        # The robot's subsystems
        self.drive = Drivetrain()

        
        
        # Autonomous routines
        #self.AUTOCOMMANDHERE = COMMAND()


        # Chooser
        self.chooser = wpilib.SendableChooser()

        # Add commands to the autonomous command chooser
        #self.chooser.setDefaultOption("Simple Auto", self.simpleAuto)
        #self.chooser.addOption("Complex Auto", self.complexAuto)

        # Put the chooser on the dashboard
        #wpilib.SmartDashboard.putData("Autonomous", self.chooser)


        self.configureButtonBindings()

        # set up default drive command
        self.drive.setDefaultCommand(DrivewithJoystick(self.drive, lambda: -self.driverController.getLeftY(), lambda: -self.driverController.getRightY())) 

    def configureButtonBindings(self):
        """
        Use this method to define your button->command mappings. Buttons can be created by
        instantiating a :GenericHID or one of its subclasses (Joystick or XboxController),
        and then passing it to a JoystickButton.
        """
        (JoystickButton(self.driverController, XboxController.Button.kLeftBumper).whenPressed(DrivewithJoystick(self.drive, lambda: -0.5*self.driverController.getLeftY(), lambda: -0.5*self.driverController.getRightY())).whenReleased(DrivewithJoystick(self.drive, lambda: -self.driverController.getLeftY(), lambda: -self.driverController.getRightY())))
        (JoystickButton(self.driverController, XboxController.Button.kA).whenPressed(MotionMagic(self.drive, constants.kUnits)))

    def getAutonomousCommand(self) -> commands2.Command:
        return self.chooser.getSelected()