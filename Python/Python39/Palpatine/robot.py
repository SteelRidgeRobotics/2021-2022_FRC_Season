import wpilib
import ctre
from wpilib.drive import DifferentialDrive

class MyRobot(wpilib.IterativeRobot):
    # NOTE: There are 2048 units per revolution for the talon fx (which is integrated in the falcon 500)
    #kSlotIdx = 0
    #kPIDLoopIdx = 0
    #kTimeoutMs = 10
    def robotInit(self):
        self.Stick = wpilib.Joystick(0)
        
        self.fLeftMotor = ctre.TalonFX(0) 
        self.bLeftMotor = ctre.TalonFX(1) 
        self.fRightMotor = ctre.TalonFX(2) 
        self.bRightMotor = ctre.TalonFX(3) 
        
        # We can get positions by using the integrated sensor for autonomous code in the future
        #self.fLeftMotor.configSelectedFeedbackSensor(ctre.TalonFXFeedbackDevice.IntegratedSensor, self.kPIDLoopIdx, self.kTimeoutMs)
        #self.fRightMotor.configSelectedFeedbackSensor(ctre.TalonFXFeedbackDevice.IntegratedSensor, self.kPIDLoopIdx, self.kTimeoutMs)
        
        
        self.timer = wpilib.Timer()
        self.bLeftMotor.follow(self.fLeftMotor)
        self.bRightMotor.follow(self.fRightMotor)
        #self.left = wpilib.SpeedControllerGroup(self.fLeftMotor, self.bLeftMotor)
        #self.right = wpilib.SpeedControllerGroup(self.fRightMotor, self.bRightMotor)
  
#    def autonomousInit(self):
#        self.timer.reset()
#        wpilib.SmartDashboard.putNumber("Left Encoder Raw", self.fLeftMotor.getSensorPosition())
#        wpilib.SmartDashboard.putNumber("Right Encoder Raw", self.fRightMotor.getSensorPosition())
#        wpilib.SmartDashboard.putNumber("Left Rotations", self.fLeftMotor.getSensorPosition()/360)
#        wpilib.SmartDashboard.putNumber("Right Rotations", self.fRightMotor.getSensorPosition()/360)
#        self.timer.start()
#        
#    def autonomousPeriodic(self):
#        if self.timer.get() <= 5.0:
#            self.drive.tankDrive(0.5, 0.5)
#        

    def teleopPeriodic(self):
        left = (self.Stick.getY()*-1) + self.Stick.getX()  #0.000 to become negative -0.001
        right = (self.Stick.getY()*-1) - self.Stick.getX() #0.000
        self.fLeftMotor.set(left)
        self.fRightMotor.set(right)
        #self.bLeftMotor.set(ctre.TalonFXControlMode.Follower, 0)
        #self.bRightMotor.set(ctre.TalonFXControlMode.Follower, 2)

if __name__ == "__main__":
    wpilib.run(MyRobot)
