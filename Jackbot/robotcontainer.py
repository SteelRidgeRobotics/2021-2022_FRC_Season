import wpilib
import commands2
import constants
import ctre
from wpilib import XboxController

#import subsystems

#import commands

class RobotContainer:
    def __init__(self) -> None:
        #init controllers
        self.driverController = XboxController(constants.kdriverControllerPort)
        
        #init drive motors (may not be necessary)
        
        self.timer = wpilib.Timer
        
        #init subsystems
        
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
        
    def configureButtonBindings(self):
        """This is where our trigger bindings for commands go"""
    """    
    def getAutonomousCommand(self) -> commands2.Command:
        return self.chooser.getSelected()
    """
            
        
