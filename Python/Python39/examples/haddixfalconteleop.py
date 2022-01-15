#importing necessary stuff
import wpilib
from wpilib.drive import DifferentialDrive
import ctre
#the robot (woah)
class myRobot(wpilib.TimedRobot):
    #init func
    def robotInit(self):
        #motors
        self.flm = ctre.WPI_TalonFX(0)
        self.blm = ctre.WPI_TalonFX(1)
        self.frm = ctre.WPI_TalonFX(2)
        self.brm = ctre.WPI_TalonFX(3)
        #setting masters + followers
        self.flm.set(ctre.ControlMode.PercentOutput, 0)
        self.blm.set(ctre.ControlMode.Follower, 0)
        self.frm.set(ctre.ControlMode.PercentOutput, 0)
        self.brm.set(ctre.ControlMode.Follower, 2)
        #drive
        self.drive = DifferentialDrive(self.flm, self.frm)
        #controller
        self.xbox = wpilib.XboxController(0)
    def disabledPeriodic(self):
        self.flm.disable()
        self.blm.disable()
        self.frm.disable()
        self.brm.disable()
    def teleopPeriodic(self):
        self.drive.tankDrive(self.xbox.getY(self.xbox.Hand.kLeftHand)*-1,
                             self.xbox.getY(self.xbox.Hand.kRightHand)*-1)
if __name__ == "__main__":
    wpilib.run(myRobot)
        
        
