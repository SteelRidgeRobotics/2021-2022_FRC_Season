import wpilib
import commands2
import constants





class FullyExtendClimber(commands2.CommandBase):
    def __init__(self, climber: Climber):
        super().__init__()