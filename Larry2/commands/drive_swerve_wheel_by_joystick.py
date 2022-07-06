import commands2
import typing
import conversions
import constants
from subsystems.swerve_wheel import SwerveWheel
import wpilib

class DriveSwerveWheelByJoysticks(commands2.CommandBase):
    def __init__(self, swerve_wheel: SwerveWheel, leftx: typing.Callable[[], float], righty: typing.Callable[[], float]) -> None:
        super().__init__()
        self.leftx = leftx
        self.righty = righty
        self.swerveWheel = swerve_wheel

        self.addRequirements((self.swerveWheel))
    def execute(self) -> None:
        wpilib.SmartDashboard.putNumber("   LeftX - ", conversions.deadband(self.leftx(), constants.kdeadband))
        wpilib.SmartDashboard.putNumber("   Right Y - ", conversions.deadband(self.righty(), constants.kdeadband))
        self.swerveWheel.turn(conversions.deadband(self.leftx(), constants.kdeadband))
        self.swerveWheel.move(conversions.deadband(self.righty(), constants.kdeadband))

    def end(self, interrupted: bool) -> None:
        self.swerveWheel.stopAllMotors()
        
    def isFinished(self) -> bool:
        return False