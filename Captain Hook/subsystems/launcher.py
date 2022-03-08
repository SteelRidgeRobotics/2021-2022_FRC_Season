import wpilib
import commands2
import constants

class Launcher(commands2.SubsystemBase):
    def __init__(self) -> None:
        super().__init__()
        # initialize solenoids
        self.launcherSolenoid = wpilib.Solenoid(constants.ksolenoidModule, constants.ksolenoidModuleType, constants.klauncherSolenoidPorts)
        self.is_up = False

    def togglePosition(self) -> None:
        if self.is_up:
            self.launcherSolenoidIn.set(True)
        else:
            self.launcherSolenoid.set(True)
        self.is_up = True
    
    def isUp(self) -> bool:
        return self.is_up
        