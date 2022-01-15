from wpilib.command import Command
from wpilib import Timer

class DriveByJoystick(Command):
    """
    This allows us to drive the robot with an xbox controller
    """
    def __init__(self, robot):
        Command.__init__(self, name='drivebyjoystick')
        self.requires(robot.drivetrain)
        self.robot = robot
    
    def initialize(self):
        # Called just before the command runs for the first time

    def execute(self):
        # Called repeatedly when this command is scheduled to run

    def isFinished(self):
        # Make this return True when this command no longer needs to run execute()

    def end(self, message="Ended"):
        # Called once after isFinished returns True
        # Stop the drivetrain from moving any further

    def interrupted(self):
        # Called when another command which requres one or more of the same subsystems is scheduled to run
        self.end(message="Interrupted")
