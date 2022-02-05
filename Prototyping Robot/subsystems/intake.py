import wpilib
import commands2
import constants

class Intake(commands2.SubsystemBase):
    def __init__(self) -> None:
        super().__init__()
    # initialize motors & solenoids
        self.leftSolenoid = wpilib.Solenoid(constants.ksolenoidModuleType, constants.ksolenoidModuleType, constants.kintakeSolenoidLeftPort)
        self.rightSolenoid = wpilib.Solenoid(constants.ksolenoidModuleType, constants.ksolenoidModuleType, constants.kintakeSolenoidRightPort)
    # use percent output control mode for operating the intake
    
    # method to move motor in/out of the chassis
    
    # method to spin the rollers on intake
