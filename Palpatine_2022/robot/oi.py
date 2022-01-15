import wpilib
import commands
class OI:
    def init_xbox(self):
        self.xbox = wpilib.XboxController(0)
