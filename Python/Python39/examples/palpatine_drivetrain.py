import wpilib
import wpilib.interfaces
from wpilib.drive import DifferentialDrive


class MyRobot(wpilib.TimedRobot):
    def robotInit(self):
        """Robot initialization function"""

        # object that handles basic drive operations
        self.frontLeftMotor = wpilib.VictorSP(0)
        self.rearLeftMotor = wpilib.VictorSP(1)
        self.frontRightMotor = wpilib.VictorSP(2)
        self.rearRightMotor = wpilib.VictorSP(3)
        #setting up controller groups
        self.left = wpilib.SpeedControllerGroup(self.frontLeftMotor, self.rearLeftMotor)
        self.right = wpilib.SpeedControllerGroup(self.frontRightMotor, self.rearRightMotor)

        self.myRobot = DifferentialDrive(self.left, self.right)
        self.myRobot.setExpiration(0.1)

        # joystick on the driver station
        self.xbox = wpilib.XboxController(0)

    def teleopInit(self):
        """Executed at the start of teleop mode"""
        self.myRobot.setSafetyEnabled(True)

    def teleopPeriodic(self):
        """Runs the motors with tank steering"""
        slow = float(0)
        #initiate bumper variables
        rbump = self.xbox.getBumper(wpilib.interfaces.GenericHID.Hand.kRightHand)
        lbump = self.xbox.getBumper(wpilib.interfaces.GenericHID.Hand.kLeftHand)
        #initiate drive side values
        left = (self.xbox.getY(wpilib.interfaces.GenericHID.Hand.kLeftHand) * -1) + self.xbox.getX(wpilib.interfaces.GenericHID.Hand.kLeftHand)
        right = (self.xbox.getY(wpilib.interfaces.GenericHID.Hand.kLeftHand) * -1) - self.xbox.getX(wpilib.interfaces.GenericHID.Hand.kRightHand)
        
        if lbump > 0 or rbump > 0:
            slow = 0.5
        else:
            slow = 1

        if left > 0.1 or left < -0.1:
            left *= slow
        else:
            left = 0

        if right > 0.1 or right < -0.1:
            right *= slow
        else:
            right = 0
        
        self.myRobot.tankDrive(left, right)


if __name__ == "__main__":
    wpilib.run(MyRobot)
