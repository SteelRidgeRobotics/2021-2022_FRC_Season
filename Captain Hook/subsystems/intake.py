import wpilib
import commands2
import constants
import ctre
class Intake(commands2.SubsystemBase):
    def __init__(self) -> None:
        super().__init__()
        # initialize motors & solenoids
        self.intakeSolenoid = wpilib.DoubleSolenoid(constants.ksolenoidModule, constants.ksolenoidModuleType, *constants.kintakeSolenoidPorts)
        self.intakeBottom = ctre.TalonFX(constants.kintakeBottom)
        self.intakeTop = ctre.TalonFX(constants.kintakeTop)

        self.isIntakeUp = False

    def toggleIntakePosition(self) -> None:
        if self.isIntakeUp:
            self.intakeSolenoid.set(wpilib.DoubleSolenoid.Value.kForward)
        else:
            self.intakeSolenoid.set(wpilib.DoubleSolenoid.Value.kReverse)
        
        self.isIntakeUp = not self.isIntakeUp

    def spinIntakeBottom(self, percentage: float) -> None:
        self.intakeBottom.set(ctre.TalonFXControlMode.PercentOutput, percentage)

    def spinIntakeTop(self, percentage1: float) -> None:
        self.intakeTop.set(ctre.TalonFXControlMode.PercentOutput, percentage1)

    def isIntakeOut(self) -> bool:
        return self.isIntakeUp