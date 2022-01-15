import wpilib
import commands
class OI:
    def __init__(self, robot):
        self.robot = robot
        self.init_xbox()
    def init_xbox(self):
        self.xbox = wpilib.XboxController(0)

e = OI("woajh")
