import wpilib
import typing
import commands2
from subsystems.climber import Climber


class ClimbByJoystick(commands2.CommandBase):
    def __init__(self, climber: Climber, leftJoy: typing.Callable[[], float], rightJoy: typing.Callable[[], float]):
        super().__init__()

        self.climber = climber
        self.leftJoy = leftJoy
        self.rightJoy = rightJoy
        self.percent = 0.4

        self.addRequirements([self.climber])

    def execute(self) -> None:
      
        self.climber.useShortClimberPercent(-self.leftJoy()*self.percent)
        self.climber.useTiltedClimberPercent(-self.rightJoy()*self.percent)

    def end(self, interrupted: bool) -> None:
        self.climber.useShortClimberPercent(0)
        self.climber.useTiltedClimberPercent(0)

    def isFinished(self) -> bool:
        return False
