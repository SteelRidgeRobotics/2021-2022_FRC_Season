import typing
import commands2
from subsystems.drivetrain import Drivetrain
import wpilib



class MotionMagic(commands2.CommandBase):
    def __init__(self,  drive: Drivetrain, units: typing.Callable[[], float]) -> None:
        super().__init__()
        self.drive = drive
        self.units = units
               
        self.addRequirements([self.drive])

    def execute(self) -> None:
         self.drive.motionMagic(self.units)

         
         wpilib.SmartDashboard.putBoolean("isMoving", self.drive.isMoving())

         #Left Values
         wpilib.SmartDashboard.putNumber("l_Active_Velocity", self.drive.frontLeft.getActiveTrajectoryVelocity())
         wpilib.SmartDashboard.putNumber("l_Active_Position", self.drive.frontLeft.getActiveTrajectoryPosition())
         wpilib.SmartDashboard.putNumber("l_Velocity", self.drive.frontLeft.getSelectedSensorVelocity())
         wpilib.SmartDashboard.putNumber("l_Position", self.drive.frontLeft.getSelectedSensorPosition())
         wpilib.SmartDashboard.putNumber("l_Error", self.drive.frontLeft.getClosedLoopError())
         
         #Right Values
         wpilib.SmartDashboard.putNumber("r_Active_Velocity", self.drive.frontRight.getActiveTrajectoryVelocity())
         wpilib.SmartDashboard.putNumber("r_Active_Position", self.drive.frontRight.getActiveTrajectoryPosition())
         wpilib.SmartDashboard.putNumber("r_Velocity", self.drive.frontRight.getSelectedSensorVelocity())
         wpilib.SmartDashboard.putNumber("r_Position", self.drive.frontRight.getSelectedSensorPosition())
         wpilib.SmartDashboard.putNumber("r_Error", self.drive.frontRight.getClosedLoopError())

    def end(self, interrupted: bool) -> None:
        self.drive.stopMotors()
        self.drive.resetEncoders()
        self.drive.clearTalonTrajectories()

    def isFinished(self) -> bool:
        return self.drive.isMoving()