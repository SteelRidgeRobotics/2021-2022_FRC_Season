import wpilib
import commands2
import constants
import ctre
class Intake(commands2.SubsystemBase):
    def __init__(self) -> None:
        super().__init__()
        # initialize motors & solenoids
        self.intakeSolenoid = wpilib.DoubleSolenoid(constants.ksolenoidModule, constants.ksolenoidModuleType, constants.kintakeSolenoidIn, constants.kintakeSolenoidOut)
        self.intakeBottom = ctre.TalonFX(constants.kintakeBottom)
        self.intakeTop = ctre.TalonFX(constants.kintakeTop)
        self.intakeBottom.setNeutralMode(ctre.NeutralMode.Coast)
        self.intakeTop.setNeutralMode(ctre.NeutralMode.Coast)

        self.isIntakeDown = True

    def toggleIntakePosition(self) -> None:
        if self.isIntakeDown:
            self.intakeSolenoid.set(wpilib.DoubleSolenoid.Value.kForward)
        else:
            self.intakeSolenoid.set(wpilib.DoubleSolenoid.Value.kReverse)
        
        self.isIntakeDown = not self.isIntakeDown

    def spinIntakeBottom(self, percentage: float) -> None:
        self.intakeBottom.set(ctre.TalonFXControlMode.PercentOutput, percentage)

    def spinIntakeTop(self, percentage1: float) -> None:
        self.intakeTop.set(ctre.TalonFXControlMode.PercentOutput, percentage1)

    def isIntakeOut(self) -> bool:
        return self.isIntakeDown