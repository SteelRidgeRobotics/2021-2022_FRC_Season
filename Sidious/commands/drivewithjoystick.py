import typing
import commands2
from subsystems.drivetrain import Drivetrain



class DrivewithJoystick(commands2.CommandBase):
    def __init__(self,  drive: Drivetrain, left_axis: typing.Callable[[], float], right_axis: typing.Callable[[], float]) -> None:
        super().__init__()
        self.drive = drive
        self.left_axis = left_axis
        self.right_axis = right_axis

        self.addRequirements([self.drive])

    def execute(self) -> None:
         self.drive.userDrive(self.left_axis(), self.right_axis())

    def end(self, interrupted: bool) -> None:
        self.drive.stopMotors()
        self.drive.resetEncoders()

    def isFinished(self) -> bool:
        return False