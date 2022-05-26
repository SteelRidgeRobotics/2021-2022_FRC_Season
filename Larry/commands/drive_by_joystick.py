import typing
import commands2
from subsystems.swerve_drive import SwerveDrive
import wpilib
from conversions import *

class DriveByJoystick(commands2.CommandBase):

    def __init__(self, drive: SwerveDrive, direction: typing.Callable[[], float], rightJoyY: typing.Callable[[], float]) -> None:
        super().__init__()
        self.drive = drive
        self.direction = direction
        self.speed = rightJoyY

        self.addRequirements((self.drive))

    def execute(self) -> None:
        self.drive.translate(self.direction, self.speed)
    
    def end(self, interrupted: bool) -> None:
        self.drive.stopMotors()
    
    def isFinished(self) -> bool:
        return False
