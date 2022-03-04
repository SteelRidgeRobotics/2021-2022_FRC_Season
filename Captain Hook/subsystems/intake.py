import wpilib
import commands2
import constants
import ctre
class Intake(commands2.SubsystemBase):
    def __init__(self) -> None:
        super().__init__()
        # initialize motors & solenoids
        self.leftSolenoid = wpilib.Solenoid(constants.ksolenoidModule, constants.ksolenoidModuleType, constants.kintakeSolenoidLeftPort)
        self.rightSolenoid = wpilib.Solenoid(constants.ksolenoidModule, constants.ksolenoidModuleType, constants.kintakeSolenoidRightPort)
        self.intakeBottom = ctre.TalonFX(constants.kintakeBottom)
        self.intakeTop = ctre.TalonFX(constants.kintakeTop)

        self.isIntakeDown = False

    def toggleIntakePosition(self) -> None:
        if self.isIntakeDown:
            self.leftSolenoid.set(True)
            self.rightSolenoid.set(True)
        else:
            self.leftSolenoid.set(False)
            self.rightSolenoid.set(False)
        
        self.isIntakeDown = not self.isIntakeDown

    def spinIntakeBottom(self, percentage: float) -> None:
        self.intakeBottom.set(ctre.TalonFXControlMode.PercentOutput, percentage)

    def spinIntakeTop(self, percentage1: float) -> None:
        self.intakeTop.set(ctre.TalonFXControlMode.PercentOutput, percentage1)

    def isIntakeOut(self) -> bool:
        return self.isIntakeDown