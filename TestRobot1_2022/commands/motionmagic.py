import commands2
from subsystems.drivetrain import Drivetrain

class MotionMagic(commands2.CommandBase):
	def __init__(self, drive: Drivetrain, units: float) -> None:
		super().__init__()
		self.drive = drive
		self.units = units

		self.addRequirements([self.drive])
        
	def execute(self) -> None:
		self.drive.motionMagic(self.units())
	def end(self) -> None:
		self.drive.stopMotors(0.0, 0.0)
	def isFinished(self) -> bool:
		return self.drive.notInMotion()