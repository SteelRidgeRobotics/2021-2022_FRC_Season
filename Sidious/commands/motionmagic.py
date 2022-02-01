import typing
import commands2
from subsystems.drivetrain import Drivetrain



class MotionMagic(commands2.CommandBase):
    def __init__(self,  drive: Drivetrain, units: typing.Callable[[], float]) -> None:
        super().__init__()
        self.drive = drive
        self.units = units
        self.drive.resetEncoders()
        
        self.addRequirements([self.drive])

    def execute(self) -> None:
         self.drive.motionMagic(self.units)

    def end(self, interrupted: bool) -> None:
        self.drive.stopMotors()
        self.drive.resetEncoders()

    def isFinished(self) -> bool:
        return self.drive.isMoving()