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
	def disabledPeriodic(self) -> None:
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
		"""
		teleop periodic
		"""
	def testInit(self) -> None:
		#Cancel all running commands
		commands2.CommandScheduler.getInstance().cancelAll()
if __name__ == '__main__':
	wpilib.run(MyRobot)