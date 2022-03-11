from commands2 import WaitCommand
import commands2
from subsystems.intake import Intake
from commands.timed_intake_bottom import TimedIntakeBottom
from commands.timed_intake_top import TimedIntakeTop
from commands.toggle_intake_position import ToggleIntakePosition

class AutoIntake(commands2.SequentialCommandGroup):
    def __init__(self, intake: Intake) -> None:
        super().__init__()
        self.addCommands(
            ToggleIntakePosition(intake),
            WaitCommand(1.0),
            TimedIntakeBottom(intake, 0.30, 2.0),
            #requirements for timed intake top/bottom (intake, percentage for motors to spin, time for them to spin and then stop)
            TimedIntakeTop(intake, 0.25, 0.1),
            ToggleIntakePosition(intake)
            )
