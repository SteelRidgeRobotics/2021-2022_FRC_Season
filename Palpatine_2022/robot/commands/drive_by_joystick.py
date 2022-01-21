import wpilib
from commands2
from wpilib import Timer
from subsystems.drivetrain import Drivetrain
from robotcontainer import RobotContainer

class DriveByJoystick(commands2.CommandBase):
    """
    This allows us to drive the robot with an xbox controller
    """
    def __init__(self, drive: Drivetrain, driveController: RobotContainer.driveController) -> None:
        super().__init__()
        
        self.drive = drive
        self.driveController = driveController
        self.addRequirements([self.drive])
        self.addRequirements([self.driveController])
    
    #def initialize(self):
        # Called just before the command runs for the first time
        

    def execute(self):
        # Called repeatedly when this command is scheduled to run
        self.drive.userDrive(self.driveController.getY()*-1 + self.driveController.getX(), self.driveController.getY()*-1 - self.driveController.getX())

    def isFinished(self):
        # Make this return True when this command no longer needs to run execute()
        return False
    
    def end(self, message="Ended"):
    # 
        # Called once after isFinished returns True
        # Stop the drivetrain from moving any further
        self.drive.userDrive(0, 0)

    def interrupted(self):
        # Called when another command which requres one or more of the same subsystems is scheduled to run
        self.end(message="Interrupted")
