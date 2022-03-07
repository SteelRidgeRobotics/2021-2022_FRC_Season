import commands2
from subsystems.drivetrain import Drivetrain
import wpilib

class TimedDrive(commands2.CommandBase):
    def __init__(self, drivetrain: Drivetrain):
        super().__init__()
        self.drivetrain = drivetrain
        self.addRequirements([self.drivetrain])

        self.startTime = 0.0

    def initialize(self) -> None:
        self.startTime = wpilib.Timer.getFPGATimestamp()
        self.drivetrain.userDrive(0.0, 0.0, 0.0)

    def execute(self) -> None:
        self.drivetrain.userDrive(-1.0, -1.0, 0.25)
        wpilib.SmartDashboard.putNumber('   right_auto', -1)
        wpilib.SmartDashboard.putNumber('   left_auto - ', -1)
    
    def end(self, interrupted: bool) -> None:
        self.drivetrain.stopMotors()
        wpilib.SmartDashboard.putNumber('   right_auto', 0)
        wpilib.SmartDashboard.putNumber('   left_auto - ', 0)

    def isFinished(self) -> bool:
        return wpilib.Timer.getFPGATimestamp() - self.startTime >= 2.0




