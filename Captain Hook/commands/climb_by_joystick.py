#import stuff
import typing
import commands2
from subsystems.climber import Climber

#create a class for the command
class ClimbByJoystick(commands2.CommandBase):
    def __init__(self, climber: Climber, leftJoy: typing.Callable[[], float], rightJoy: typing.Callable[[], float]):
        #init from parent class (command base)
        super().__init__()

        #this is our climber, our left joystick on the xbox controller, and our, you guessed it, right joystick
        self.climber = climber
        self.leftJoy = leftJoy
        self.rightJoy = rightJoy
        
        #this percent is how fast the climber motors will go
        self.percent = 0.4
        
        #the climber is a requirement for this command.
        self.addRequirements([self.climber])

    #executed when command is called
    def execute(self) -> None:
        
        #use the short climber, and tall climber based on the joysticks, then multiply by the percentage we defined earlier
        self.climber.useShortClimberPercent(-self.leftJoy()*self.percent)
        self.climber.useTiltedClimberPercent(-self.rightJoy()*self.percent)

    #end the command by setting the climbers to 0
    def end(self, interrupted: bool) -> None:
        self.climber.useShortClimberPercent(0)
        self.climber.useTiltedClimberPercent(0)

    #return false when isfinished is called. this means the command will go continuously
    def isFinished(self) -> bool:
        return False
