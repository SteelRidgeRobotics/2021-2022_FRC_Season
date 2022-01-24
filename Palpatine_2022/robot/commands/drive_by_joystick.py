import typing
import commands2
from subsystems.drivetrain import Drivetrain

class DriveByJoystick(commands2.CommandBase):
    """
    This allows us to drive the robot with an xbox controller
    """
    def __init__(self, drive: Drivetrain, left_axis: typing.Callable[[], float], right_axis: typing.Callable[[], float]) -> None:
        super().__init__()
        
        self.drive = drive
        self.left_axis = left_axis
        self.right_axis = right_axis
        self.addRequirements([self.drive])

    
    #def initialize(self):
        # Called just before the command runs for the first time
        

    def execute(self) -> None:
        # Called repeatedly when this command is scheduled to run
        #self.drive.userDrive(self.driveController.getY()*-1 + self.driveController.getX(), self.driveController.getY()*-1 - self.driveController.getX())
        self.drive.userDrive(self.left_axis(), self.right_axis())
    
    def end(self, inturrupted: bool) -> None:
    # 
        # Called once after isFinished returns True
        # Stop the drivetrain from moving any further
        self.drive.stopMotors()
        
    def isFinished(self) -> None:
        # Make this return True when this command no longer needs to run execute()
        return False
"""
    def interrupted(self):
        # Called when another command which requres one or more of the same subsystems is scheduled to run
        self.end(message="Interrupted")
        """
