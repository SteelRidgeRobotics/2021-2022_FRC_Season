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
        self.percent = 0.75

    def execute(self) -> None:
        # if wanting to retract short climber and fully retracted
        if self.leftJoy < 0 and not self.climber.isShortClimberFullyRetracted():
          # climb
            self.climber.useShortClimberPercent(self.leftJoy*self.percent)
        # if wanting to extend short climber not fully extended
        elif self.leftJoy > 0 and not self.climber.isShortClimberFullyExtended():
          # climb
            self.climber.useShortClimberPercent(self.leftJoy*self.percent)
        else:
          # don't climb
            self.climber.useShortClimberPercent(0)

        # if wanting to retract tilted climber and fully retracted
        if self.rightJoy < 0 and not self.climber.isTiltedClimberFullyRetracted():
          # climb
            self.climber.useTiltedClimberPercent(self.leftJoy*self.percent)
        # if wanting to extend tilted climber not fully extended
        elif self.rightJoy > 0 and not self.climber.isTiltedClimberFullyExtended():
          # climb
            self.climber.useTiltedClimberPercent(self.leftJoy*self.percent)
        else:
          # don't climb
            self.climber.useTiltedClimberPercent(0)

    def end(self, interrupted: bool) -> None:
        self.climber.useShortClimberPercent(0)
        self.climber.useTiltedClimberPercent(0)

    def isFinished(self) -> bool:
        return False
