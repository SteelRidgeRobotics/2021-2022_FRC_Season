import wpilib
import commands2
import constants
import ctre
class Intake(commands2.SubsystemBase):
    def __init__(self) -> None:
        super().__init__()
        # initialize motors & solenoids
        self.intakeSolenoid = wpilib.DoubleSolenoid(constants.ksolenoidModule, constants.ksolenoidModuleType, constants.kintakeSolenoidIn, constants.kintakeSolenoidOut)
        self.intakeBottom = ctre.TalonSRX(constants.kintakeBottom)
        self.intakeTop = ctre.TalonSRX(constants.kintakeTop)

        self.isIntakeUp = False

    def toggleIntakePosition(self) -> None:
        if self.isIntakeUp:
            self.intakeSolenoid.set(wpilib.DoubleSolenoid.Value.kForward)
        else:
            self.intakeSolenoid.set(wpilib.DoubleSolenoid.Value.kReverse)
        
        self.isIntakeUp = not self.isIntakeUp

    def spinIntakeBottom(self, percentage: float) -> None:
        self.intakeBottom.set(ctre.TalonSRXControlMode.PercentOutput, percentage)

    def spinIntakeTop(self, percentage1: float) -> None:
        self.intakeTop.set(ctre.TalonSRXControlMode.PercentOutput, percentage1)

    def isIntakeOut(self) -> bool:
        return self.isIntakeUp