import commands2
from setpathtodrive import SetPathToDrive

class AutoPath(commands2.SequentialCommandGroup):

    def __init__(self):
        setpath = SetPathToDrive
        super().__init__(
             setpath.goPathA(setpath, False),
             setpath.goPathB(setpath, True),
         )
