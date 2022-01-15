import wpilib
from commandbased import CommandBasedRobot

from commands import AutonomousCommandGroup

class MyRobot(CommandBasedRobot):

    def robotInit(self):
        '''Initialize things like subsystems'''
        super().__init__()
        #init the drive train
        self.drivetrain = Drivetrain(self)

        self.autonomous = AutonomousCommandGroup()


    def autonomousInit(self):
        self.autonomous.start()
