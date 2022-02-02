import commands2
import wpilib
from robotcontainer import RobotContainer

class MyRobot(commands2.TimedCommandRobot):
	def robotInit(self) -> None:
		"""
		Our robot is initiated
		"""
		#our robot container
		self.container = RobotContainer()
	#these disabled functions work when the robot is disabled
	def disabledInit(self) -> None:
		"""
		Our robot is disabled
		"""
	def disabledPeriodic(self) -> None: # yo, angelo
		"""
		Disabled periodic
		"""
	#this is our autonomous initiation function
	def autonomousInit(self) -> None:
		"""
		Auto initiation
		"""
	#this is our autonomous periodic function (called periodically during auto)
	def autonomousPeriodic(self) -> None:
		"""
		Auto periodic
		"""
	#teleop initiation
	def teleopInit(self) -> None:
		"""
		Teleop initiation
		"""
	#teleop periodical (nothing happens, so our default command, drivewithjoystick, is called)
	#fun fact: in this sentence, drivewithjoystick is an appositive. it basically clarifies stuff, woah! grammar!
	def teleopPeriodic(self) -> None:
		if self.container.driverController.getAButtonPressed():
			self.container.drive.changeBumper()
	def testInit(self) -> None:
		#Cancel all running commands
		commands2.CommandScheduler.getInstance().cancelAll()
if __name__ == '__main__':
	wpilib.run(MyRobot)

	#this is a robot, you know what that is?

	#yes sir?

	#well obviously you don't. They will tak over the world someday, and I'm happy to leave such a great footprint on the world

	#that's scary Mr. Haddix!

	#don't worry, if they don't betray me, though they probably will, i'll tell the robots to keep you safe

	#how?

	#WITH THE POWER OF COMPUTERS! HAHAHAHAHAHHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHA

	#well that turned stereotype cringe cartoon villlain real fast``