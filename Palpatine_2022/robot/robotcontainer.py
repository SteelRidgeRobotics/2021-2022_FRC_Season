import wpilib
import commands2
import constants
from wpilib import XboxController
from subsystems.drivetrain import Drivetrain()
from commands.drive_by_joystick import DriveByJoystick

class RobotContainer:
    def __init__(self, robot) -> None:
        self.robot = robot
        self.init_controllers()
    def init_controllers(self):
        self.driverController = wpilib.XboxController(constants.kdriverControllerPort)

        # chooser
        self.chooser = wpilib.SendableChooser()

        # Add commands to autonomous command chooser
        #self.chooser.setDefaultOption("Simple Auto", self.chooser)
        #self.chooser.addOption("Complex Auto", self.chooser)

        #wpilib.SmartDashboard.putData("Autonomous", self.chooser)

        self.configureButtonBindings
        
        wpilib.drive.setDefaultCommand(
            DriveByJoystick(self.drive, lambda: -self.driverController.getLeftY, lambda: -self.driverController.getRightY)
        )
        def configureButtonBindings(self):

        #def getAutonomousCommand(self) -> commands.,Command:
        #    return self.chooser.getSelected()