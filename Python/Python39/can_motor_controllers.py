import wpilib
import ctre
import wpilib.drive

class MyRobot(wpilib.TimedRobot):
    # Will need to install CTRE library through robotpy package with python
    def robotInit(self):
        self.fLeftMotor = ctre.TalonFX(0) 
        self.bLeftMotor = ctre.TalonFX(1) 
        self.fRightMotor = ctre.TalonFX(2) 
        self.bRightMotor = ctre.TalonFX(3) 
        
        # Set Controll Modes & makes sure there is no movement
        self.fLeftMotor.set(ControlMode.PercentOutput, 0)
        self.bLeftMotor.set(ControlMode.Follower, 0)
        self.fRightMotor.set(ControlMode.PercentOutput, 0) 
        self.bRightMotor.set(ControlMode.Follower, 2)
        
        
        
        """
        Need to use a different object. CANTalon object is not accepted anymore
        self.fLeftMotor = wpilib.CANTalon(0) 
        self.bLeftMotor = wpilib.CANTalon(1) 
        self.fRightMotor = wpilib.CANTalon(2) 
        self.bRightMotor = wpilib.CANTalon(3) 
        
        self.bLeftMotor.changeControlMode(wpilib.CANTalon.ControlMode.Follower)
        self.bLeftMotor.set(0)
        self.bRightMotor.changeControlMode(wpilib.CANTalon.ControlMode.Follower)
        self.bRightMotor.set(2)
        
        self.fLeftMotor.reverseSensor(True)
        self.fRightMotor.reverseSensor(True)
        
        self.fLeftMotor.reverseOutput(True)
        self.fRightMotor.reverseOutput(True)
        
        self.fLeftMotor.setFeedbackDevice(QuadEncoder)
        self.fRightMotor.setFeedbackDevice(QuadEncoder)
        
        self.fLeftMotor.getBrakeEnableDuringNeutral(True)
        self.bLeftMotor.getBrakeEnableDuringNeutral(True)
        self.fRightMotor.getBrakeEnableDuringNeutral(True)
        self.bRightMotor.getBrakeEnableDuringNeutral(True)
        
        self.drive = wpilib.drive.DifferentialDrive(self.fLeftMotor, fRightMotor)
        
        self.timer = wpilib.Timer()
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
    def teleopInit(self):
    def teleopPeriodic(self):

if __name__ == "__main__":
    wpilib.run(MyRobot)
