import commands2
from subsystems.drivetrain import Drivetrain



class DrivewithJoystick(commands2.CommandBase):
    def init(self,  drive: Drivetrain, left_axis: float, right_axis: float) -> None:
        super().__init__()
        self.drive = drive
        self.left_axis = left_axis
        self.right_axis = right_axis

        self.addRequirements(self.drive)

    def execute(self) -> None:
         self.drive.userDrive(self.left_axis(), self.right_axis())

    def end(self, interrupted: bool) -> None:
        self.drive.stopMotors()

    def isFinished(self) -> bool:
        return False