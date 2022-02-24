import commands2
from pybind11 import commands
from setpathtodrive import SetPathToDrive
from subsystems.drivetrain import Drivetrain

class AutoPath(commands2.SequentialCommandGroup):

    def __init__(self, setpath = SetPathToDrive):
        setpath = SetPathToDrive

        super().__init__(
            setpath.goPathA(setpath, False),
            setpath.goPathB(setpath, True),
        )


