import typing
import commands2
from subsystems.swerve_drive import SwerveDrive
import wpilib
import conversions
import math

class DriveByJoystick(commands2.CommandBase):

    def __init__(self, drive: SwerveDrive, leftJoyX: typing.Callable[[], float], leftJoyY: typing.Callable[[], float]) -> None:
        super().__init__()
        self.drive = drive
        
        self.leftx = leftJoyX
        self.lefty = leftJoyY
        self.direction = conversions.Conversions.convertJoystickInputToDegrees(self.leftx(), self.lefty())

        self.addRequirements((self.drive))

    def execute(self) -> None:
        if conversions.Conversions.sign(self.lefty()) == -1:
            self.magnitude = -(math.hypot(self.leftx(), self.lefty()))
        else:
            self.magnitude = math.hypot(self.leftx(), self.lefty())
        self.direction = conversions.Conversions.convertJoystickInputToDegrees(self.leftx(), self.lefty())
        wpilib.SmartDashboard.putNumber("   direction - ", self.direction)
        wpilib.SmartDashboard.putNumber("   speed - ", self.magnitude)
        self.drive.translate(self.direction, self.magnitude)
    
    def end(self, interrupted: bool) -> None:
        self.drive.stopMotors()
    
    def isFinished(self) -> bool:
        return False
