import commands2
from subsystems.pidTest import PidTest


class GetPIDValues(commands2.CommandBase):
    def __init__(self, pid: PidTest) -> None:
        super().__init__()
        self.pid = pid
        
        self.addRequirements([self.pid])

    def execute(self) -> None:
        self.pid.periodic()
        #self.pid.putMotorValuesToSmartDashboard()
        #self.pid.putToSmartDashboard()
        #self.pid.flush()
        