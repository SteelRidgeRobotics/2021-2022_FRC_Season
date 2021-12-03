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

        self.left = wpilib.SpeedControllerGroup(self.frontLeftMotor, self.rearLeftMotor)
        self.right = wpilib.SpeedControllerGroup(self.frontRightMotor, self.rearRightMotor)

        self.myRobot = DifferentialDrive(self.left, self.right)
        self.myRobot.setExpiration(0.1)

        # xbox controller
        self.xbox = wpilib.XboxController(0)

        self.timer = wpilib.Timer()

        self.offset = 0.875

        # timer vairables for algorithm
        self.halfSpeedRate = 1.934029792
        self.distance = 10
        self.timeToTravel = self.distance/self.halfSpeedRate
        self.timeToTurnNinety = (((3.14159265359*(17/12))/8)/self.halfSpeedRate)*2
        self.timeToTurnHundredEighty = self.timeToTurnNinety*2
        
    def autonomousInit(self):
        self.timer.reset()
        self.timer.start()

    def autonomousPeriodic(self):
        """
        if self.timer.get() <= self.timeToTravel:
            self.myRobot.tankDrive(0.5, 0.5 * self.offset)
        """
        if self.timer.get() <= self.timeToTurnHundredEighty:
            self.myRobot.tankDrive(-0.5,0.5*1.05) # Turn 180 degrees to the left
        else:
            self.myRobot.tankDrive(0,0)
        """
        if self.timer.get() <= 3.0:
            self.myRobot.tankDrive(0.5, 0.5) # forward for 2
        elif self.timer.get() <= 4.0:
            self.myRobot.tankDrive(0, 0)
        elif self.timer.get() <= 9.0:
            self.myRobot.tankDrive(-0.5, -0.5) # backward for 2
        elif self.timer.get() <= 11.0:
            self.myRobot.tankDrive(0, 0)
        elif self.timer.get() <= 16.0:
            self.myRobot.tankDrive(-0.5, 0.5) # spin for 3
        elif self.timer.get() <= 19.0:
            self.myRobot.tankDrive(0, 0)
        elif self.timer.get() <= 24.0:
            self.myRobot.tankDrive(1, -1) # spin faster for 2
        elif self.timer.get() <= 26.0:
            self.myRobot.tankDrive(0, 0)
        elif self.timer.get() <= 31.0:
            self.myRobot.tankDrive(0.5, 0) # left for 2
        elif self.timer.get() <= 33.0:
            self.myRobot.tankDrive(0, 0)
        elif self.timer.get() <= 38.0:
            self.myRobot.tankDrive(0, 0.5) # right for 2
        elif self.timer.get() <= 40.0:
            self.myRobot.tankDrive(0, 0)
        elif self.timer.get() <= 45.0:
            self.myRobot.tankDrive(1, 1) # foeward faster 2
        else:
            self.myRobot.tankDrive(0, 0)
            """

    def teleopInit(self):
        """Executed at the start of teleop mode"""
        self.myRobot.setSafetyEnabled(True)

    def teleopPeriodic(self):
        """Runs the motors with tank steering"""
        slow = float(0)
        rbump = self.xbox.getBumper(wpilib.interfaces.GenericHID.Hand.kRightHand)
        lbump = self.xbox.getBumper(wpilib.interfaces.GenericHID.Hand.kLeftHand)
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
        
        self.myRobot.tankDrive(left, right * self.offset)


if __name__ == "__main__":
    wpilib.run(MyRobot)
