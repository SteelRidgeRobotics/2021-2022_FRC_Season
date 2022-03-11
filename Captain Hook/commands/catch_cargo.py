#import stuff
from commands2 import WaitCommand
import commands2
from subsystems.intake import Intake
from commands.timed_intake_bottom import TimedIntakeBottom
from commands.timed_intake_top import TimedIntakeTop

#create class stuff
class CatchCargo(commands2.SequentialCommandGroup):
    #initiate stuff
    def __init__(self, intake: Intake) -> None:
        #use the  initiation function of the parent class (sequential command group). super() refers to the class we inherit from
        super().__init__()
        #this just adds all the commands to be done in sequence, you can refer to those files for more information. 
        #this will spin the bottom intake, wait, spin the top intake, wait, and then set both intakes to 0.
        self.addCommands(
            TimedIntakeBottom(intake, 0.30, 0.1),
            TimedIntakeBottom(intake, 0.25, 0.1)
            )