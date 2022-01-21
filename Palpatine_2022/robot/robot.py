import wpilib
from subsystems.drivetrain import Drivetrain
from commandbased import CommandBasedRobot
from robotcontainer import RobotContainer
from commands import AutonomousCommandGroup

class MyRobot(CommandBasedRobot):

    def robotInit(self):
        '''Initialize things like subsystems'''
        super().__init__()
        #init the drive train (This is done in the robotcontainer)
        #self.drivetrain = Drivetrain(self) 
        self.container = RobotContainer

        #self.autonomous = AutonomousCommandGroup()
    #def disabledInit(self) -> None:


    #def autonomousInit(self):
    #    self.autonomous.start()
    
    
