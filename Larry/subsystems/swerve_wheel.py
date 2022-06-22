import commands2
import ctre
import constants
import wpilib
class SwerveWheel(commands2.SubsystemBase):
    def __init__(self) -> None:
        super().__init__()
        self.directionMotor = ctre.TalonFX(constants.kleftFrontDirectionID)
        self.speedMotor = ctre.TalonFX(constants.kleftFrontSpeedID)
    def turn(self, joystick_input: float):
        current_pos = self.directionMotor.getSelectedSensorPosition()
        self.directionMotor.set(ctre.TalonFXControlMode.Position, current_pos + joystick_input)
        wpilib.SmartDashboard.putNumber("Sensor - ", current_pos)
    def move(self, joystick_input: float):
        self.speedMotor.set(ctre.TalonFXControlMode.PercentOutput, 0.1*joystick_input)
    def stopAllMotors(self):
        self.directionMotor.set(ctre.TalonFXControlMode.PercentOutput, 0.0)
        self.speedMotor.set(ctre.TalonFXControlMode.PercentOutput, 0.0)