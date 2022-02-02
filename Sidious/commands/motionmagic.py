import typing
import commands2
from subsystems.drivetrain import Drivetrain
import wpilib



class MotionMagic(commands2.CommandBase):
    def __init__(self,  drive: Drivetrain, units: typing.Callable[[], float]) -> None:
        super().__init__()
        self.drive = drive
        self.units = units
        self.drive.initializeMotors()
        
        self.addRequirements([self.drive])

    def execute(self) -> None:
         self.drive.motionMagic(self.units)
         wpilib.SmartDashboard.putBoolean("isMoving", self.drive.isMoving())
         wpilib.SmartDashboard.putNumber("Active_Velocity", self.drive.frontLeft.getActiveTrajectoryVelocity())
         wpilib.SmartDashboard.putNumber("Active_Position", self.drive.frontLeft.getActiveTrajectoryPosition())
         wpilib.SmartDashboard.putNumber("Velocity", self.drive.frontLeft.getSelectedSensorVelocity())
         wpilib.SmartDashboard.putNumber("Position", self.drive.frontLeft.getSelectedSensorPosition())

    def end(self, interrupted: bool) -> None:
        self.drive.initializeMotors()

    def isFinished(self) -> bool:
        return self.drive.isMoving()