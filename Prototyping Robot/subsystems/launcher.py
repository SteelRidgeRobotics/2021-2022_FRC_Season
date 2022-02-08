import wpilib
import commands2
import constants

class Launcher(commands2.SubsystemBase):
    def __init__(self) -> None:
        super().__init__()
        # initialize solenoids
        self.launcherSolenoid = wpilib.Solenoid(constants.ksolenoidModule, constants.ksolenoidModuleType, constants.klauncherSolenoidPort)
        self.is_up = False

    def launch(self) -> None:
        self.launcherSolenoid.set(True)
        self.is_up = True

    def goDown(self) -> None:
        self.launcherSolenoid.set(False)
        self.is_up = False
    
    def isUp(self) -> bool:
        return self.is_up
        
