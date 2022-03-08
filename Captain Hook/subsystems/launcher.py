import wpilib
import commands2
import constants

class Launcher(commands2.SubsystemBase):
    def __init__(self) -> None:
        super().__init__()
        # initialize solenoids
        self.launcherSolenoid = wpilib.Solenoid(constants.ksolenoidModule, constants.ksolenoidModuleType, *constants.klauncherSolenoidPorts)
        self.is_up = False

    def togglePosition(self) -> None:
        if self.is_up:
            self.launcherSolenoid.set(wpilib.DoubleSolenoid.Value.kReverse)
        else:
<<<<<<< Updated upstream
            self.launcherSolenoid.set(True)
        self.is_up = True

=======
            self.launcherSolenoid.set(wpilib.DoubleSolenoid.Value.kForward)
        self.is_up = not self.is_up
    
>>>>>>> Stashed changes
    def isUp(self) -> bool:
        return self.is_up
        