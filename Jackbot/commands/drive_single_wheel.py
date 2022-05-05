#import stuff
import typing
import commands2
from subsystems.swerve_drive import SwerveDrive
import wpilib 

#create class inheriting from commandbase. inheritance means we can get attributes and functions of a class, and use them in a new class.
#ex: a great dane could inherit from the dog class, which inherits from the mammal class, etc.
class DriveSingleWheel(commands2.CommandBase):
    """
    This allows us to drive the robot with an xbox controller
    """
    #init function
    def __init__(self, swerveDrive: SwerveDrive, direction: float, speed: float) -> None:
    #def __init__(self, drive: Drivetrain, left_axis, right_axis) -> None:
        #initiate from the parent class, super() refers to commands2.CommandBase
        super().__init__()
        #init stuff
        self.direction = direction
        self.speed = speed
        self.swerveDrive = swerveDrive

        #add requirement
        self.addRequirements([self.swerveDrive])
    def execute(self) -> None:
        self.swerveDrive.driveLeftFrontWheel(self.swerveDrive, self.direction, self.speed)
        wpilib.SmartDashboard.putNumber("   direction - ", self.direction)
        wpilib.SmartDashboard.putNumber("   speed - ", self.speed)
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
        self.swerveDrive.stopMotors()
        
    def isFinished(self) -> bool:
        # Make this return True when this command no longer needs to run execute()
        return False
"""
    def interrupted(self):
        # Called when another command which requres one or more of the same subsystems is scheduled to run
        self.end(message="Interrupted")
        """

