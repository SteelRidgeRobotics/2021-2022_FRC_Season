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
        # Called Just before the command runs fro the first time

    def execute(self):
        # Called repeatedly when this command is scheduled to run

    def isFinished(self):
        # Make this return true when this command no longer needs to run execute()
        return False
    def end(self, message="Ended"):
        # called once after isFinished returns true
        # Stop the drivetrain from moving any further

    def interrupted(self):
        # Called when another command which requres one or more of the same subsystems is scheduled to run
        self.end(message="Interrupted")