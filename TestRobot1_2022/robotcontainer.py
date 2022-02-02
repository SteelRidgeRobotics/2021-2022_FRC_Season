#import stuff
import wpilib
import constants
import ctre

from wpilib import XboxController

from commands2.button import JoystickButton

from commands.drivewithjoystick import DriveWithJoystick
# from commands.bumperchange import BumperChange
from subsystems.drivetrain import Drivetrain
#robotcontainer class, it basically does all the heavy lifting for us! thanks robotcontainer, very cool!
class RobotContainer:
	#initiation function
	def __init__(self) -> None:
		#driver controller and functions controller (we are using the ports from our constants file)
		self.driverController = XboxController(constants.kdriverControllerPort)
		self.functionsController = XboxController(constants.kfunctionsControllerPort)
		#motors
		self.frontLeft = ctre.TalonFX(constants.kfrontLeft)
		self.backLeft = ctre.TalonFX(constants.kbackLeft)
		self.frontRight = ctre.TalonFX(constants.kfrontRight)
		self.backRight = ctre.TalonFX(constants.kbackRight)

		self.timer = wpilib.Timer()
		#drivetrain (from our drivetrain file, remember the imports?)
		self.drive = Drivetrain()
		#our command chooser + auto commands

		self.chooser = wpilib.SendableChooser()
		# self.chooser.setDefaultOption(f"Simple Auto ({constants.kSimpleDistance} feet)", self.simpleAuto)


		#configure button bindings
		self.configureButtonBindings()
		#set default command to drive with joystick (wowzers!) the parameters for drivewithjoystick is the leftY, rightY, and our bumpers (bumpers turn on slowmode)
		self.drive.setDefaultCommand(DriveWithJoystick(self.drive, lambda: -self.driverController.getLeftY(), lambda: -self.driverController.getRightY(), lambda: self.driverController.getLeftBumper(), lambda: self.driverController.getRightBumper()))
		# self.drive.setDefaultCommand(DriveWithJoystick(self.drive, -self.driverController.getLeftY(), -self.driverController.getRightY(), self.driverController.getLeftBumper(), self.driverController.getRightBumper()))

	#configure button bindings
	def configureButtonBindings(self) -> None:
		"""
		Configuring buttons
		"""
		#JoystickButton(self.driverController, XboxController.Button.kB).whenPressed(BumperChange(self.drive))

	#get autonomous command returns self.chooser.getSelected(). but what is getSelected()? it basically returns the selected command we have selected. currently it is literally nothing
	# def getAutonomousCommand(self) -> None:
	# 	return self.chooser.getSelected()