import commands2
import wpilib
import typing
from subsystems.swerve_drive import SwerveDrive
import conversions
class Joysticks(commands2.CommandBase):

    def __init__(self, robotcontainer: SwerveDrive, LeftX: typing.Callable[[], float], LeftY: typing.Callable[[], float], RightX: typing.Callable[[], float], RightY: typing.Callable[[], float]) -> None:
        super().__init__()
        self.robotcontainer = robotcontainer

        self.leftx = LeftX
        self.lefty = LeftY
        self.rightx = RightX
        self.righty = RightY
        self.degrees = conversions.Conversions.convertJoystickInputToDegrees(LeftX(), LeftY())

        self.addRequirements((self.robotcontainer))

    def execute(self) -> None:
        self.degrees = conversions.Conversions.convertJoystickInputToDegrees(self.leftx(), self.lefty())
        wpilib.SmartDashboard.putNumber("   LeftX - ", self.leftx())
        wpilib.SmartDashboard.putNumber("   Left Y - ", self.lefty())
        wpilib.SmartDashboard.putNumber("   RightX - ", self.rightx())
        wpilib.SmartDashboard.putNumber("   Right Y - ", self.righty())
        wpilib.SmartDashboard.putNumber("   Left Degrees - ", self.degrees)
        
    
    def end(self, interrupted: bool) -> None:
        print()
    
    def isFinished(self) -> bool:
        return False
