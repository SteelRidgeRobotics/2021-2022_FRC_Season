import wpilib
import commands2
import constants
import ctre
from wpilib import XboxController


from commands.drive_by_joystick import DriveByJoystick
from subsystems.drivetrain import Drivetrain
from commands2.button import JoystickButton

from commands.climb_by_joystick import ClimbByJoystick
from commands.launch_cargo import LaunchCargo
from commands.spin_intake_bottom import SpinIntakeBottom
from commands.spin_intake_top import SpinIntakeTop
from commands.catch_cargo import CatchCargo
from commands.toggle_intake_position import ToggleIntakePosition
from commands.timed_drive import TimedDrive

from subsystems.climber import Climber
from subsystems.launcher import Launcher
from subsystems.intake import Intake
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
        self.launcher = Launcher()
        self.intake = Intake()
        # chooser
        self.chooser = wpilib.SendableChooser()
        
        # Add commands to autonomous command chooser
        self.timed_drive = TimedDrive(self.drive)
        self.chooser.setDefaultOption("Simple Auto", self.timed_drive)

        wpilib.SmartDashboard.putData("Autonomous", self.chooser)
                
        self.configureButtonBindings() 
        
        # SINGLE JOYSTICK
        #self.drive.userDrive(self.driveController.getY()*-1 + self.driveController.getX(), self.driveController.getY()*-1 - self.driveController.getX()
        # LEFT_JOY: FORWARD/BACKWARD; RIGHT_JOY: TURN
        self.drive.setDefaultCommand(DriveByJoystick(self.drive, lambda: (-self.driverController.getLeftY() + self.driverController.getRightX()), lambda: (-self.driverController.getLeftY() - self.driverController.getRightX()), lambda: self.driverController.getRightBumper(), lambda: self.driverController.getLeftBumper()))
        # TANK DRIVE (EACH SIDE IS CONTROLLED BY IT'S RESPECTABLE JOYSTICK)
        #self.drive.setDefaultCommand(DriveByJoystick(self.drive, lambda: -self.driverController.getLeftY(), lambda: -self.driverController.getRightY(), lambda: self.driverController.getRightBumper(), lambda: self.driverController.getLeftBumper()))
        
        # climbing
        self.climber.setDefaultCommand(ClimbByJoystick(self.climber, lambda: -self.functionsController.getLeftY(), lambda: -self.functionsController.getRightY()))
        
    def configureButtonBindings(self):
        
        (JoystickButton(self.functionsController, XboxController.Button.kB).whenPressed(LaunchCargo(self.launcher)))

        (JoystickButton(self.driverController, XboxController.Button.kY).whenHeld(SpinIntakeBottom(self.intake, 1.0)))
        (JoystickButton(self.driverController, XboxController.Button.kY).whenReleased(CatchCargo(self.intake)))
        (JoystickButton(self.driverController, XboxController.Button.kA).whenHeld(SpinIntakeBottom(self.intake, -1.0)))
        (JoystickButton(self.driverController, XboxController.Button.kA).whenReleased(SpinIntakeBottom(self.intake, 0.0)))

        (JoystickButton(self.functionsController, XboxController.Button.kY).whenHeld(SpinIntakeTop(self.intake, 1.0)))
        (JoystickButton(self.functionsController, XboxController.Button.kY).whenReleased(SpinIntakeTop(self.intake, 0.0)))
        (JoystickButton(self.functionsController, XboxController.Button.kA).whenHeld(SpinIntakeTop(self.intake, -1.0)))
        (JoystickButton(self.functionsController, XboxController.Button.kA).whenReleased(SpinIntakeTop(self.intake, 0.0)))

        (JoystickButton(self.functionsController, XboxController.Button.kX).whenPressed(ToggleIntakePosition(self.intake)))
        

        #(JoystickButton(self.driverController))
    def getAutonomousCommand(self) -> commands2.Command:
        return self.chooser.getSelected()
