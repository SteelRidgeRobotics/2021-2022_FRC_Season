import wpilib
import commands2
import constants

class Launcher(commands2.SubsystemBase):
    def __init__(self) -> None:
        super().__init__()
        # initialize solenoids
        self.launcherSolenoid = wpilib.DoubleSolenoid(constants.ksolenoidModule, constants.ksolenoidModuleType, *constants.klauncherSolenoidPorts)
        self.is_up = False

    def togglePosition(self) -> None:
        if self.is_up:
            self.launcherSolenoid.set(wpilib.DoubleSolenoid.Value.kReverse)
        else:
            self.launcherSolenoid.set(wpilib.DoubleSolenoid.Value.kForward)
        self.is_up = not self.is_up
    
    def isUp(self) -> bool:
        return self.is_up
        