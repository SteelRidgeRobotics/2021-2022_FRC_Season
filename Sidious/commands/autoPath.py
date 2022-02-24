import commands2
from setpathtodrive import SetPathToDrive

class AutoPath(commands2.SequentialCommandGroup):
        
        SetPathToDrive.goPathA(SetPathToDrive, False)

        SetPathToDrive.goPathB(SetPathToDrive, True)
