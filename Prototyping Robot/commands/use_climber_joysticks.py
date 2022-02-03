import wpilib
import typing
import commands2
from subsystems.climber import Climber

class UseClimberJoysticks(commands2.CommandBase):
  def __init__(self, climber: Climber, leftJoy: typing.Callable[[], float], rightJoy: typing.Callable[[], float]):
    super().__init__()
    
    self.climber = climber
    self.leftJoy = leftJoy
    self.rightJoy = rightJoy
    self.percent = 0.75
    
  def execute(self) -> None:
    # if wanting to retract short climber
    if self.leftJoy <= 0:
      # if short climber is not fully retracted
      if not self.climber.isShortClimberFullyRetracted():
        self.climber.useShortClimberPercent(self.leftJoy*self.percent)
    else:
      self.climber.useShortClimberPercent(0)

    # if wanting to retract short climber
    if self.rightJoy <= 0:
      if not self.climber.isTiltedClimberFullyRetracted():
        self.climber.useTiltedClimberPercent(self.rightJoy*self.percent)
