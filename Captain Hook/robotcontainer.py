import wpilib
import commands2
import constants
import ctre
from wpilib import XboxController


from commands.drive_by_joystick import DriveByJoystick
from subsystems.drivetrain import Drivetrain
from commands2.button import JoystickButton

from commands.climb_by_joystick import ClimbByJoystick

from subsystems.climber import Climber

#hi
class RobotContainer:
    def __init__(self) -> None:
        # driver controller
        self.driverController = XboxController(constants.kdriverControllerPort)
        self.functionsController = XboxController(constants.kfunctionsControllerPort)
        
        self.frontLeft = ctre.TalonFX(constants.kfrontLeft)
        self.backLeft = ctre.TalonFX(constants.kbackLeft)
        self.frontRight = ctre.TalonFX(constants.kfrontRight)
        self.backRight = ctre.TalonFX(constants.kbackRight)


        self.timer = wpilib.Timer
        
        
        #subsystems
        self.drive = Drivetrain()
        self.climber = Climber()
        
        # chooser
        #self.chooser = wpilib.SendableChooser()
        
        # Add commands to autonomous command chooser
        #self.driveStraight = DriveStraight(self.drive, constants.kdistanceToTravel)
        #self.chooser.setDefaultOption("Drive Straight", self.driveStraight)

        #wpilib.SmartDashboard.putData("Autonomous", self.chooser)
                
        #self.configureButtonBindings() 
        
        # SINGLE JOYSTICK
        #self.drive.userDrive(self.driveController.getY()*-1 + self.driveController.getX(), self.driveController.getY()*-1 - self.driveController.getX()
        # LEFT_JOY: FORWARD/BACKWARD; RIGHT_JOY: TURN
        self.drive.setDefaultCommand(DriveByJoystick(self.drive, lambda: (-self.driverController.getLeftY() + self.driverController.getRightX()), lambda: (-self.driverController.getLeftY() - self.driverController.getRightX()), lambda: self.driverController.getRightBumper(), lambda: self.driverController.getLeftBumper()))
        # TANK DRIVE (EACH SIDE IS CONTROLLED BY IT'S RESPECTABLE JOYSTICK)
        #self.drive.setDefaultCommand(DriveByJoystick(self.drive, lambda: -self.driverController.getLeftY(), lambda: -self.driverController.getRightY(), lambda: self.driverController.getRightBumper(), lambda: self.driverController.getLeftBumper()))
        
        # climbing
        self.climber.setDefaultCommand(ClimbByJoystick(self.climber, lambda: -self.functionsController.getLeftY(), lambda: -self.functionsController.getRightY()))
        
    #def configureButtonBindings(self):

#    def getAutonomousCommand(self) -> commands2.Command:
#        return self.chooser.getSelected()
