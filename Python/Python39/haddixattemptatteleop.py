import wpilib
from wpilib.drive import DifferentialDrive
class myRobot(TimedRobot):
    def robotInit(self):
        self.flm = VictorSP(0)
        self.blm = VictorSP(1)
        self.frm = VictorSP(2)
        self.brm = VictorSP(3)
        self.left = SpeedControllerGroup(self.flm, self.blm)
        self.right = SpeedControllerGroup(self.frm, self.brm)
        self.myRobot = DifferentialDrive(self.left, self.right)
        self.myRobot.setExpiration(0.1)
        self.xbox = XboxController(0)
    def teleopInit(self):
        self.myRobot.setSafetyEnabled(True)
    def teleopPeriodic(self):
        self.myRobot.tankDrive(self.xbox.getY(self.xbox.Hand.kLeftHand)*-1,
                               self.xbox.getY(self.xbox.Hand.kRightHand)*-1)
if __name__ == "__main__":
    wpilib.run(MyRobot)
        
