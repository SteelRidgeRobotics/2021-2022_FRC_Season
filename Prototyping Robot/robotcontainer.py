from hal import JoystickPOVs
import wpilib
import constants
import ctre
from wpilib import XboxController

import commands2
from commands2.button import JoystickButton
from commands2.button import POVButton


from commands.drive_by_joystick import DriveByJoystick
from commands.motion_magic import MotionMagic

from commands.fully_retract_climber import FullyRetractClimber
from commands.fully_extend_climber import FullyExtendClimber
from commands.climb_by_joystick import ClimbByJoystick

from commands.launch_cargo import LaunchCargo

from commands.move_intake import MoveIntake
from commands.spin_intake_with_pov import SpinIntakeWithPOV
from commands.launch_cargo import LaunchCargo


from subsystems.drivetrain import Drivetrain
from subsystems.climber import Climber
from subsystems.intake import Intake
from subsystems.launcher import Launcher


class RobotContainer:
    def __init__(self) -> None:
        # driver controller & functions
        self.driverController = XboxController(constants.kdriverControllerPort)
        self.functionsController = XboxController(constants.kfunctionsControllerPort)
        
        self.frontLeft = ctre.TalonFX(constants.kfrontLeft)
        self.backLeft = ctre.TalonFX(constants.kbackLeft)
        self.frontRight = ctre.TalonFX(constants.kfrontRight)
        self.backRight = ctre.TalonFX(constants.kbackRight)
        
        self.intakeOut = True


        self.timer = wpilib.Timer
        
        
        #subsystems
        self.drive = Drivetrain()
        self.climber = Climber()
        self.launcher = Launcher()
        self.intake = Intake()
        
        # chooser
        self.chooser = wpilib.SendableChooser()
        
        # Add commands to autonomous command chooser
        self.driveStraight = MotionMagic(self.drive, constants.kdistanceToTravel*12)
        self.chooser.setDefaultOption("Drive Straight", self.driveStraight)

        wpilib.SmartDashboard.putData("Autonomous", self.chooser)

       

        

        
                
        self.configureButtonBindings()  
        
        self.drive.setDefaultCommand(DriveByJoystick(self.drive, lambda: -self.driverController.getLeftY(), lambda: -self.driverController.getRightY(), lambda: self.driverController.getRightBumper(), lambda: self.driverController.getLeftBumper()))
        self.climber.setDefaultCommand(ClimbByJoystick(self.climber, lambda: -self.functionsController.getLeftY(), lambda: -self.functionsController.getRightY()))
        #self.intake.setDefaultCommand(SpinIntakeWithPOV(self.intake, lambda: self.driverController.getPOV()))
        
        
    def configureButtonBindings(self):
        (JoystickButton(self.functionsController, XboxController.Button.kA).whenPressed(FullyRetractClimber(self.climber, 2)))
        (JoystickButton(self.functionsController, XboxController.Button.kY).whenPressed(FullyExtendClimber(self.climber, 2)))
        #(JoystickButton(self.functionsController, XboxController.getPOV(0))).whenPressed(FullyExtendClimber(self.climber, 1)))
        #(JoystickButton(self.functionsController, XboxController.getPOV(180)).whenPressed(FullyRetractClimber(self.climber, 1)))
        (POVButton(self.functionsController, 0, 0).whenPressed(FullyExtendClimber(self.climber, 1))) # if this doesn't work, we may want to make a command to use the POV
        (POVButton(self.functionsController, 180, 0).whenPressed(FullyRetractClimber(self.climber, 1)))
        
        #(JoystickButton(self.functionsController, XboxController.Button.kB).whenPressed(LaunchCargo(self.launcher)))

        # Functions Controller buttons 
        # Left joystick: Extends/Retracts first climber ####DONE
        # Right joystick: Extends/Retracts second climber ####DONE
        # POV: Fully Extend/Fully Retract first climber ####DONE but may not be needed
        # Y: Fully Extend second climber ####DONE
        # A: Fully Retract second climber ####DONE
        # B: Launch Cargo ####DONE
        
        #(JoystickButton(self.driverController, XboxController.Button.kStart).whenPressed(self.intake, not self.intakeOut))
        
        # Remainding Driver Controller buttons
        # Start: Move intake in/out ####DONE
        # POV: Use to rotate motors in one direction or the other ####DONE


    def getAutonomousCommand(self) -> commands2.Command:
        return self.chooser.getSelected()
