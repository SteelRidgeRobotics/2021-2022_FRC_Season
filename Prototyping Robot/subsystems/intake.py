import wpilib
import commands2
import constants
import ctre
class Intake(commands2.SubsystemBase):
    def __init__(self) -> None:
        super().__init__()
        # initialize motors & solenoids
        self.leftSolenoid = wpilib.Solenoid(constants.ksolenoidModuleType, constants.ksolenoidModuleType, constants.kintakeSolenoidLeftPort)
        self.rightSolenoid = wpilib.Solenoid(constants.ksolenoidModuleType, constants.ksolenoidModuleType, constants.kintakeSolenoidRightPort)
        self.intakeMotor = ctre.TalonFX(constants.kintake)
        self.intakeOut = False # robot starts with the intake in
    
    
    # method to move motor in/out of the chassis
    def pushIntakeOut(self) -> None:
        self.leftSolenoid.set(True)
        self.rightSolenoid.set(True)
        self.intakeOut = True

    def pullIntakeIn(self) -> None:
        self.leftSolenoid.set(False)
        self.rightSolenoid.set(False)
        self.intakeOut = False
        
        
    # use percent output control mode for operating the intake
    # method to spin the rollers on intake
    def spinIntake(self, percentage: float) -> None:
        self.intakeMotor.set(ctre.TalonFXControlMode.PercentOutput, percentage)
        
    def isIntakeOut(self) -> bool:
        return self.intakeOut
