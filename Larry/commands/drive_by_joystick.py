import typing
import commands2
from subsystems.swerve_drive import SwerveDrive
import wpilib
import conversions

class DriveByJoystick(commands2.CommandBase):

    def __init__(self, drive: SwerveDrive, leftJoyX: typing.Callable[[], float], leftJoyY: typing.Callable[[], float], rightJoyY: typing.Callable[[], float]) -> None:
        super().__init__()
        self.drive = drive
        
        self.leftx = leftJoyX
        self.lefty = leftJoyY
        self.direction = conversions.Conversions.convertJoystickInputToDegrees(self.leftx(), self.lefty())
        self.speed = rightJoyY

        self.addRequirements((self.drive))

    def execute(self) -> None:
        self.direction = conversions.Conversions.convertJoystickInputToDegrees(self.leftx(), self.lefty())
        wpilib.SmartDashboard.putNumber("   direction - ", self.direction)
        wpilib.SmartDashboard.putNumber("   speed - ", self.speed())
        self.drive.translate(self.direction, self.speed())
    
    def end(self, interrupted: bool) -> None:
        self.drive.stopMotors()
    
    def isFinished(self) -> bool:
        return False
