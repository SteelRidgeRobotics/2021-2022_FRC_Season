# import commands2
# from subsystems.drivetrain import Drivetrain
# class BumperChange(commands2.CommandBase):
#     def __init__(self, drive: Drivetrain) -> None:
#         super().__init__()
#         self.drive = drive
#         self.addRequirements([self.drive])
    
#     def execute(self) -> None:
#         self.end(True)
    
#     def end(self, interrupted: bool) -> None:
#         self.drive.changeBumper()


#     def isFinished(self) -> bool:
#         return True