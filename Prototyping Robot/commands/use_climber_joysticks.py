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
    
  def
