from hal import JoystickPOVs
import wpilib
import commands2
from commands.fully_extend_climber import FullyExtendClimber
import constants
import ctre
from wpilib import XboxController
from commands2.button import JoystickButton
from commands2.button import POVButton

from commands.drive_by_joystick import DriveByJoystick
from commands.motion_magic import MotionMagic
from commands.fully_retract_climber import FullyRetractClimber
from commands.climb_by_joystick import ClimbByJoystick

from subsystems.drivetrain import Drivetrain
from subsystems.climber import Climber




#hi
class RobotContainer:
    def __init__(self) -> None:
        # driver controller & functions
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
        self.chooser = wpilib.SendableChooser()
        
        # Add commands to autonomous command chooser
        self.driveStraight = MotionMagic(self.drive, constants.kdistanceToTravel*12)
        self.chooser.setDefaultOption("Drive Straight", self.driveStraight)

        wpilib.SmartDashboard.putData("Autonomous", self.chooser)

       

        

        
                
        self.configureButtonBindings()  
        
        self.drive.setDefaultCommand(DriveByJoystick(self.drive, lambda: -self.driverController.getLeftY(), lambda: -self.driverController.getRightY(), lambda: self.driverController.getRightBumper(), lambda: self.driverController.getLeftBumper()))
        self.climber.setDefaultCommand(ClimbByJoystick(self.climber, lambda: -self.functionsController.getLeftY(), lambda: -self.functionsController.getRightY()))
        
        
    def configureButtonBindings(self):
        (JoystickButton(self.functionsController, XboxController.Button.kA).whenPressed(FullyRetractClimber(self.climber, 2)))
        (JoystickButton(self.functionsController, XboxController.Button.kY).whenPressed(FullyExtendClimber(self.climber, 2)))
        #(JoystickButton(self.functionsController, XboxController.getPOV(0))).whenPressed(FullyExtendClimber(self.climber, 1)))
        #(JoystickButton(self.functionsController, XboxController.getPOV(180)).whenPressed(FullyRetractClimber(self.climber, 1)))
        (POVButton(self.functionsController, 0, constants.kfunctionsControllerPort).whenPressed(FullyExtendClimber(self.climber, 2)))
        (POVButton(self.functionsController, 180, constants.kfunctionsControllerPort).whenPressed(FullyExtendClimber(self.climber, 2)))
        # Functions Controller buttons
        # Left joystick: Extends/Retracts first climber ####DONE
        # Right joystick: Extends/Retracts second climber ####DONE
        # POV: Fully Extend/Fully Retract first climber
        # Y: Fully Extend second climber ####DONE
        # A: Fully Retract second climber ####DONE
        # B: Launch Cargo


    def getAutonomousCommand(self) -> commands2.Command:
        return self.chooser.getSelected()
