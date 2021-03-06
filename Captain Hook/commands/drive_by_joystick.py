#import stuff
import typing
import commands2
from subsystems.drivetrain import Drivetrain
import wpilib 

#create class inheriting from commandbase. inheritance means we can get attributes and functions of a class, and use them in a new class.
#ex: a great dane could inherit from the dog class, which inherits from the mammal class, etc.
class DriveByJoystick(commands2.CommandBase):
    """
    This allows us to drive the robot with an xbox controller
    """
    #init function
    def __init__(self, drive: Drivetrain, left_axis: typing.Callable[[], float], right_axis: typing.Callable[[], float], bumperRight: typing.Callable[[], bool], bumperLeft: typing.Callable[[], bool]) -> None:
    #def __init__(self, drive: Drivetrain, left_axis, right_axis) -> None:
        #initiate from the parent class, super() refers to commands2.CommandBase
        super().__init__()
        
        #our drivetrain, left joystick value, right joystick value, bumper values, and the percentage (how much we multiply value by)
        self.drive = drive
        self.left_axis = left_axis
        self.right_axis = right_axis
        self.bumperRight = bumperRight
        self.bumperLeft = bumperLeft
        self.percent = 1.0
        self.isZero = False
        #this command requires the drivetrain class
        self.addRequirements([self.drive])
        
        #slow factor (why do we have this i have no idea)
        self.slowFactor = 0.5
  
    def execute(self) -> None:
        # Called repeatedly when this command is scheduled to run
        
        # when the one of the bumpers is pressed, halve the speed
        if self.bumperRight() or self.bumperLeft():
            self.percent = 0.5
            #drive using the userdrive function with the joystick values times the percentage chosen
            self.drive.userDrive(self.left_axis(), self.right_axis(), self.percent)
        #otherwise drive normally
        else:
            self.percent = 1.0
            #drive function
            self.drive.userDrive(self.left_axis(), self.right_axis(), self.percent)
        
        #self.drive.userDrive(self.left_axis(), self.right_axis())
        """
        wpilib.SmartDashboard.putNumber('   leftJoy - ', self.left_axis())
        wpilib.SmartDashboard.putNumber('   rightJoy - ', self.right_axis())
        wpilib.SmartDashboard.putNumber("  Left Velocity - ", self.drive.frontLeft.getSelectedSensorVelocity())
        wpilib.SmartDashboard.putNumber("  Right Velocity - ", self.drive.frontRight.getSelectedSensorVelocity())
        wpilib.SmartDashboard.putBoolean('  Right Bumper Pressed - ', self.bumperRight())
        wpilib.SmartDashboard.putBoolean('  Left Bumper Pressed - ', self.bumperLeft())
        wpilib.SmartDashboard.putNumber('   Speed Percentage - ', self.percent)
        """

    def end(self, interrupted: bool) -> None:
    # 
        # Called once after isFinished returns True
        # Stop the drivetrain from moving any further
        self.drive.stopMotors()
        
    def isFinished(self) -> bool:
        # Make this return True when this command no longer needs to run execute()
        return False
"""
    def interrupted(self):
        # Called when another command which requres one or more of the same subsystems is scheduled to run
        self.end(message="Interrupted")
        """

