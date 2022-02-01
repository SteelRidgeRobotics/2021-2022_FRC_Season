import wpilib
import commands2
import constants
import ctre
from wpilib import XboxController
from commands2.button import JoystickButton

from commands.drive_by_joystick import DriveByJoystick
from commands.motion_magic import MotionMagic
from commands.restore_climber_to_default import RestoreClimberToDefault

from subsystems.drivetrain import Drivetrain
from subsystems.climber import Climber




#hi
class RobotContainer:
    def __init__(self) -> None:
        # driver controller
        self.driverController = XboxController(constants.kdriverControllerPort)
        
        self.frontLeft = ctre.TalonFX(constants.kfrontLeft)
        self.backLeft = ctre.TalonFX(constants.kbackLeft)
        self.frontRight = ctre.TalonFX(constants.kfrontRight)
        self.backRight = ctre.TalonFX(constants.kbackRight)


        self.timer = wpilib.Timer
        
        
        #subsystems
        self.drive = Drivetrain()
        self.climber = Climber()
        
        # chooser
        self.chooser = wpilib.SendableChooser()
        
        # Add commands to autonomous command chooser
        self.driveStraight = MotionMagic(self.drive, constants.kdistanceToTravel)
        self.chooser.setDefaultOption("Drive Straight", self.driveStraight)

        wpilib.SmartDashboard.putData("Autonomous", self.chooser)

       

        

        
                
        self.configureButtonBindings()  
        
        self.drive.setDefaultCommand(DriveByJoystick(self.drive, lambda: -self.driverController.getLeftY(), lambda: -self.driverController.getRightY(), lambda: self.driverController.getRightBumper(), lambda: self.driverController.getLeftBumper()))
        
        
        
    def configureButtonBindings(self):
        (JoystickButton(self.driverController, XboxController.Button.kA).whenPressed(RestoreClimberToDefault(self.climber))


    def getAutonomousCommand(self) -> commands2.Command:
        return self.chooser.getSelected()
