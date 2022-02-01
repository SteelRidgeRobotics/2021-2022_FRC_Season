# import commands2
# import constants
# from subsystems.drivetrain import Drivetrain

# class MotionMagic(commands2.CommandBase):
# 	def __init__(self, drive: Drivetrain) -> None:
# 		super().__init__()
# 		self.drive = drive
# 		self.distance = constants.kDistance
# 		self.pos = constants.kunitsPerRotation * (self.distance / constants.kwheelCircumference)
		
# 		#self.rotations = 0
# 		self.addRequirements([self.drive])
        
# 	def execute(self) -> None:
# 		self.drive.motionMagic(self.pos)
# 	def end(self) -> None:
# 		self.drive.stopMotors()
# 	def isFinished(self) -> bool:
# 		return self.drive.notInMotion()