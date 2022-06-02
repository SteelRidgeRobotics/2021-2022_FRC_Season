import wpilib
import commands2
import constants
import ctre
from wpilib import XboxController
from conversions import Conversions

#import subsystems
from subsystems.swerve_drive import SwerveDrive
#import commands
from commands.drive_by_joystick import DriveByJoystick
from commands.joysticks import Joysticks

class RobotContainer:
    def __init__(self) -> None:
        #init controllers
        self.driverController = XboxController(constants.kdriverControllerPort)
        
        #init drive motors (may not be necessary)
        
        self.timer = wpilib.Timer
        
        #init subsystems
        self.swerveDrive = SwerveDrive()
        
        #auto chooser
        #self.chooser = wpilib.SendableChooser()
        
        #Add commands to auto command chooser
        """
        self.simple_auto = SimpleAuto(self.drive)
        self.complex_auto = ComplexAuto(self.drive)
        #set a default option
        #add options
        #show autonomous on the driver station
        """
        
        self.configureButtonBindings()

        self.swerveDrive.setDefaultCommand(DriveByJoystick(self.swerveDrive, lambda: self.driverController.getLeftX(), lambda: -self.driverController.getLeftY()))
        #self.swerveDrive.setDefaultCommand(Joysticks(self.swerveDrive, lambda: self.driverController.getLeftX(), lambda: self.driverController.getLeftY(), lambda: self.driverController.getRightX(), lambda: self.driverController.getRightY()))
    def configureButtonBindings(self):
        """This is where our trigger bindings for commands go"""
    """    
    def getAutonomousCommand(self) -> commands2.Command:
        return self.chooser.getSelected()
    """
            
        
