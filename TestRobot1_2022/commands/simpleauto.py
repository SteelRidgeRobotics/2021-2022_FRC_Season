import commands2
import constants
from subsystems.drivetrain import Drivetrain

class SimpleAuto(commands2.CommandBase):
        def __init__(self, drive: Drivetrain) -> None:
                super().__init__()
                self.drive = drive
                self.distance = constants.kSimpleDistance
		#self.rotations = 0
                self.addRequirements([self.drive])
        
        def execute(self) -> None:
                self.drive.userDrive(constants.kSimplePercent, constants.kSimplePercent)
                
        def end(self) -> None:
                self.drive.stopMotors()
        def isFinished(self) -> bool:
                return self.drive.frontLeft.getSelectedSensorPosition(constants.kPIDLoopIdx) >= constants.kSimpleDistance
