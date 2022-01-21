import wpilib
import commands2
import constants
from wpilib import XboxController
from commands.drive_by_joystick import DriveByJoystick
from subsystems.drivetrain import Drivetrain

class RobotContainer:
    def __init__(self) -> None:
        self.init_controllers()
    def init_controllers(self):
        self.driverController = XboxController(constants.kdriverControllerPort)

        self.drive = Drivetrain(self)
        # chooser
        self.chooser = wpilib.SendableChooser()

        # Add commands to autonomous command chooser
        #self.chooser.setDefaultOption("Simple Auto", self.chooser)
        #self.chooser.addOption("Complex Auto", self.chooser)

        #wpilib.SmartDashboard.putData("Autonomous", self.chooser)

        self.configureButtonBindings
        
        self.drive.setDefaultCommand(
            DriveByJoystick(self.drive, lambda: -self.driverController.getLeftY, lambda: -self.driverController.getRightY)
        )
        def configureButtonBindings(self):
            print()

        #def getAutonomousCommand(self) -> commands.,Command:
        #    return self.chooser.getSelected()