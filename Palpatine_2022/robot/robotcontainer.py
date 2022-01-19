import wpilib
import commands2
import constants
import subsystem.drivetrain import Drivetrain()

class RobotContainer:
    def __init__(self, robot):
        self.robot = robot
        self.init_controllers()
    def init_controllers(self):
        self.xbox = wpilib.XboxController(constants.kdriverControllerPort)
