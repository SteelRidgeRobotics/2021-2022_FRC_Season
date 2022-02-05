import wpilib
import commands2
import constants

class Launcher(commands2.SubsystemBase):
    def __init__(self) -> None:
        super().__init__()
    # initialize solenoids
        self.launcherSolenoid = wpilib.Solenoid(constants.ksolenoidModule, constants.ksolenoidModuleType, constants.klauncherSolenoidPort)

    def launch(self):
        self.launcherSolenoid.set(True)

    def goDown(self):
        self.launcherSolenoid.set(False)
