import wpilib
import ctre
from wpilib.drive import DifferentialDirve

class MyRobot(wpilib.TimedRobot):
    # Will need to install CTRE library through robotpy package with python
    def robotInit(self):
        self.Stick = wpilib.Joystick(0)
        
        self.fLeftMotor = ctre.WPI_TalonFX(0) 
        self.bLeftMotor = ctre.WPI_TalonFX(1) 
        self.fRightMotor = ctre.WPI_TalonFX(2) 
        self.bRightMotor = ctre.WPI_TalonFX(3) 
        
        
        """
        # Set Controll Modes & makes sure there is no movement
        self.fLeftMotor.set(ctre.ControlMode.PercentOutput, 0)
        self.bLeftMotor.set(ctre.ControlMode.Follower, 0)
        self.fRightMotor.set(ctre.ControlMode.PercentOutput, 0) 
        self.bRightMotor.set(ctre.ControlMode.Follower, 2)
        
        # Configure Sensors
        #.configSelectedFeedbackSensor(feedback device, pidIdx, timeoutMs)
        # pidIdx: 0 for primary loop, 1 for auxillary
        # timeoutMs: timeout value in ms. Will not check if 0, will send error message if exceeds timeout
        self.fLeftMotor.configSelectedFeedbackSensor(ctre.FeedbackDevice.IntegratedSensor, 0, 0)
        self.bLeftMotor.configSelectedFeedbackSensor(ctre.FeedbackDevice.IntegratedSensor, 0, 0)
        self.fRightMotor.configSelectedFeedbackSensor(ctre.FeedbackDevice.IntegratedSensor, 0, 0)
        self.bRightMotor.configSelectedFeedbackSensor(ctre.FeedbackDevice.IntegratedSensor, 0, 0)
        
        # Getting Sensor feedback
        #ctre.TalonFXSensorCollection(motorController)
        """
        
        self.timer = wpilib.Timer()
        self.drive = wpilib.drive.DifferentialDrive(self.fLeftMotor, self.fRightMotor)
        """
    def autonomousInit(self):
        self.timer.reset()
        wpilib.SmartDashboard.putNumber("Left Encoder Raw", self.fLeftMotor.getSensorPosition())
        wpilib.SmartDashboard.putNumber("Right Encoder Raw", self.fRightMotor.getSensorPosition())
        wpilib.SmartDashboard.putNumber("Left Rotations", self.fLeftMotor.getSensorPosition()/360)
        wpilib.SmartDashboard.putNumber("Right Rotations", self.fRightMotor.getSensorPosition()/360)
        self.timer.start()
        
    def autonomousPeriodic(self):
        if self.timer.get() <= 5.0:
            self.drive.tankDrive(0.5, 0.5)
        """
    def disabledPeriodic(self):
        self.fLeftMotor.disable()
        self.bLeftMotor.di
        self.fRightMotor
        self.bRightMotor
    
    def teleopInit(self):
        self.myRobot.setSafetyEnabled(True)
    def teleopPeriodic(self):
        left = (self.Stick.getY()*-1) + self.Stick.getX()  #0.000 to become negative -0.001
        right = (self.Stick.getY()*-1) - self.Stick.getX() #0.000
        self.drive.tankDrive(left, right)

if __name__ == "__main__":
    wpilib.run(MyRobot)