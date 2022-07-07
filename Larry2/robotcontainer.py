from hal import JoystickButtons
import wpilib
import commands2
from commands2.button import JoystickButton

import constants
import ctre
from wpilib import XboxController

#import subsystems
from subsystems.swerve_drive import SwerveDrive
#import commands
from commands.joysticks import Joysticks
from commands.turn_to_specific_point import TurnToSpecificPoint
from commands.drive_left_front import DriveLeftFront
from commands.move_in_place import MoveInPlace

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

        self.swerveDrive.setDefaultCommand(MoveInPlace(self.swerveDrive, lambda: self.driverController.getRightX()))
        #self.swerveDrive.setDefaultCommand(DriveLeftFront(self.swerveDrive,  lambda: self.driverController.getLeftX(), lambda: self.driverController.getLeftY()))
        #self.swerveDrive.setDefaultCommand(TurnToSpecificPoint(self.swerveDrive,  lambda: self.driverController.getLeftX(), lambda: self.driverController.getLeftY()))
        #self.swerveDrive.setDefaultCommand(Joysticks(self.swerveDrive, lambda: self.driverController.getLeftX(), lambda: self.driverController.getLeftY(), lambda: self.driverController.getRightX(), lambda: self.driverController.getRightY()))

    def configureButtonBindings(self):
        """This is where our trigger bindings for commands go"""
    """    
    def getAutonomousCommand(self) -> commands2.Command:
        return self.chooser.getSelected()
    """
            
        
