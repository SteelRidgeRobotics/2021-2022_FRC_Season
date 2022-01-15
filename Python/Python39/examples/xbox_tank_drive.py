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

        # joystick on the driver station
        self.Stick = wpilib.Joystick(0)

    def teleopInit(self):
        """Executed at the start of teleop mode"""
        self.myRobot.setSafetyEnabled(True)

    def teleopPeriodic(self):
        """Runs the motors with tank steering"""
        left = (self.Stick.getY()*-1) + self.Stick.getX()  #0.000 to become negative -0.001
        right = (self.Stick.getY()*-1) - self.Stick.getX() #0.000
        self.myRobot.tankDrive(left, right)


if __name__ == "__main__":
    wpilib.run(MyRobot)
