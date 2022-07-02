import typing
import commands2
from subsystems.swerve_wheel import SwerveWheel
import wpilib
import constants
import conversions
import math


class TurnToSpecificPoint(commands2.CommandBase):
    def __init__(self,  wheel: SwerveWheel, x: typing.Callable[[], float], y: typing.Callable[[], float]) -> None:
        super().__init__()
        self.wheel = wheel
        #self.units = conversions.convertDegreesToTalonFXUnits(conversions.convertJoystickInputToDegrees(x(), y()))
        self.x = x
        self.y = y
        self.addRequirements([self.wheel])

    def execute(self) -> None:
        self.angle = conversions.convertJoystickInputToDegrees(self.x(), self.y())
        self.units = conversions.convertDegreesToTalonFXUnits(self.angle)
        # we calculate what we need to rotate the wheel to, keeping in mind the gear ratios
        self.wheel.turn(self.units*constants.ksteeringGearRatio)
        self.wheel.showStats()
        wpilib.SmartDashboard.putNumber("Setpoint -", self.units)
        wpilib.SmartDashboard.putNumber("Angle -", self.angle)
        wpilib.SmartDashboard.putNumber("Input to wheel - ", self.units*constants.ksteeringGearRatio)
        

    def end(self, interrupted: bool) -> None:
        self.wheel.stopAllMotors()

    def isFinished(self) -> bool:
        return self.wheel.notTurning