import wpilib
import commands2
import constants
from subsystems.drivetrain import Drivetrain

class DriveStraight(commands2.CommandBase):
    def __init__(self, drive: Drivetrain, distance: float) -> None:
        super().__init__()

        self.drive = drive
        self.distance = distance
        #note: this targetpos is really more distance from the robot
        self.pos = constants.kunitsPerRotation * (self.distance / constants.kwheelCircumference)

        self.addRequirements([self.drive])

    def execute(self) -> None:
        self.drive.magicDrive(float(self.pos))
        wpilib.SmartDashboard.putNumber("   ClosedLoopError - ", self.drive.frontLeft.getClosedLoopError(constants.kPIDLoopIdx))

    def end(self, interrupted: bool) -> None:
        self.drive.stopMotors()

    def isFinished(self) -> bool: #note: when we get more advanced we will want to return a boolean for whether this is finished or not
        return self.drive.isNotinMotion()
