from commands2 import WaitCommand
import commands2
from subsystems.intake import Intake
from commands.spin_intake_bottom import SpinIntakeBottom
from commands.spin_intake_top import SpinIntakeTop
from commands.toggle_intake_position import ToggleIntakePosition

class autoIntake(commands2.SequentialCommandGroup):
    def __init__(self, intake: Intake) -> None:
        super().__init__()
        self.addCommands(
            ToggleIntakePosition(intake),
            WaitCommand(0.6),
            SpinIntakeBottom(intake, 1.0),
            WaitCommand(0.1),
            SpinIntakeBottom(intake, 0.0),
            ToggleIntakePosition(intake),
            WaitCommand(0.6),
            SpinIntakeTop(intake, 1.0),
            WaitCommand(0.1),
            SpinIntakeTop(intake, 0.0)
            )
