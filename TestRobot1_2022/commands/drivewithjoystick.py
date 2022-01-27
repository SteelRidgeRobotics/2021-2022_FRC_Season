#importing (we are importing drivetrain from drivetrain file)
import commands2
from subsystems.drivetrain import Drivetrain
#this is our command class (inheriting from commandbase)
class DriveWithJoystick(commands2.CommandBase):
	#initiation function using our drivetrain, our left_axis_, our right_axis, our leftbumper, and our rightbumper
	def __init__(self, drive: Drivetrain, left_axis: float, right_axis: float, leftBumper: bool, rightBumper: bool) -> None:
		super().__init__()
		#setting drive, left and right axes, and bumpers
		self.drive = drive
		self.left_axis = left_axis
		self.right_axis = right_axis
		self.leftBumper = leftBumper
		self.rightBumper = rightBumper
		#this basically says we need the drivetrain subsystem for this command
		self.addRequirements([self.drive])
	#executing the command by using userdrive
	def execute(self) -> None:
		#userDrive using our left and right values, plus our bumpers
		self.drive.userDrive(self.left_axis(), self.right_axis(), self.leftBumper(), self.rightBumper())
	#stopping the motors
	def end(self, interrupted: bool) -> None:
		self.drive.stopMotors(0.0, 0.0)
	#isfinished function
	def isFinished(self) -> bool:
		return False