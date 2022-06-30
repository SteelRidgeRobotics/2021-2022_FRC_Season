import typing
import commands2
from subsystems.swerve_wheel import SwerveWheel
import wpilib
import constants



class TurnToSpecificPoint(commands2.CommandBase):
    def __init__(self,  wheel: SwerveWheel, units: typing.Callable[[], float]) -> None:
        super().__init__()
        self.wheel = wheel
        self.units = units
               
        self.addRequirements([self.wheel])

    def execute(self) -> None:
        self.wheel.turn(self.units/constants.ksteeringGearRatio)
        self.wheel.showStats()

    def end(self, interrupted: bool) -> None:
        self.wheel.stopAllMotors()

    def isFinished(self) -> bool:
        return self.wheel.isNotrotating