import wpilib
import commands2
import constants
import ctre
from wpilib import XboxController
from commands.drive_by_joystick import DriveByJoystick
from subsystems.drivetrain import Drivetrain

class RobotContainer:
    def __init__(self) -> None:
        # driver controller
        self.driverController = XboxController(constants.kdriverControllerPort)
        
        # chooser
        self.chooser = wpilib.SendableChooser()
        
        self.frontLeft = ctre.TalonFX(constants.kfrontLeft)
        self.backLeft = ctre.TalonFX(constants.kbackLeft)
        self.frontRight = ctre.TalonFX(constants.kfrontRight)
        self.backRight = ctre.TalonFX(constants.kbackRight)
        
        #subsystems
        self.drive = Drivetrain()
        # Add commands to autonomous command chooser
        #self.chooser.setDefaultOption("Simple Auto", self.chooser)
        #self.chooser.addOption("Complex Auto", self.chooser)

        #wpilib.SmartDashboard.putData("Autonomous", self.chooser)

        #self.configureButtonBindings()  
        
        
        
        
        self.drive.setDefaultCommand(
            DriveByJoystick(self.drive, lambda: -self.driverController.getLeftY(), lambda: -self.driverController.getRightY(), self.driverController.getLeftBumper(), self.driverController.getRightBumper()))
        
        # def configureButtonBindings(self):
        #     """
        #     """

        # def getAutonomousCommand(self) -> commands2.Command:
        #     return self.chooser.getSelected()
