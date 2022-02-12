import commands2
from subsystems.pidTest import PidTest


class GetPIDValues(commands2.CommandBase):
    def __init__(self, drive: PidTest) -> None:
        super().__init__()
        self.drive = drive
        
        self.addRequirements([self.drive])