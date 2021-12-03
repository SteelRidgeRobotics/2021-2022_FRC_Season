#note: this code does not work as of 12/3/21
#Haddix Attempt at Teleop (for certification)
import wpilib
from wpilib.drive import DifferentialDrive
class myRobot(wpilib.TimedRobot):
    def robotInit(self):
        self.flm = wpilib.VictorSP(0)
        self.blm = wpilib.VictorSP(1)
        self.frm = wpilib.VictorSP(2)
        self.brm = wpilib.VictorSP(3)
        self.left = wpilib.SpeedControllerGroup(self.flm, self.blm)
        self.right = wpilib.SpeedControllerGroup(self.frm, self.brm)
        self.myRobot = DifferentialDrive(self.left, self.right)
        self.myRobot.setExpiration(0.1)
        self.xbox = wpilib.XboxController(0)
    def teleopInit(self):
        self.myRobot.setSafetyEnabled(True)
    def teleopPeriodic(self):
        self.myRobot.tankDrive(self.xbox.getY(self.xbox.Hand.kLeftHand)*-1,
                               self.xbox.getY(self.xbox.Hand.kRightHand)*-1)
if __name__ == "__main__":
    wpilib.run(MyRobot)
        
