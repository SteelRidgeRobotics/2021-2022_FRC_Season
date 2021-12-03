"""
Palpatine Basic Driving
"""
#!/usr/bin/env python3
"""
    This is a demo program showing the use of the RobotDrive class,
    specifically it contains the code necessary to operate a robot with
    tank drive.
"""

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

        # joysticks 1 & 2 on the driver station
        self.xbox = wpilib.XboxController(0)

    def teleopInit(self):
        """Executed at the start of teleop mode"""
        self.myRobot.setSafetyEnabled(True)

    def teleopPeriodic(self):
        """Runs the motors with tank steering"""
        left = self.xbox.getY(wpilib.interfaces.GenericHID.Hand.kLeftHand) * -1
        right = self.xbox.getY(wpilib.interfaces.GenericHID.Hand.kRightHand) * -1
        self.myRobot.tankDrive(left, right)


if __name__ == "__main__":
    wpilib.run(MyRobot)
