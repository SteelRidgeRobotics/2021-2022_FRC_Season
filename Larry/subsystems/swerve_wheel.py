import commands2
import ctre
import constants
class SwerveWheel(commands2.SubsystemBase):
    def __init__(self) -> None:
        super().__init__()
        self.frontLeftDirection = ctre.TalonFX(constants.kleftFrontDirectionID)