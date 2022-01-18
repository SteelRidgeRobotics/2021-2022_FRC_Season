import wpilib
import wpilib.command import Subsystem
from wpilib.drive import DifferentialDrive
import ctre

class DriveTrain(Subsystem):
    def __init__(self, robot):
        super().__init__("drivetrain")
        self.robot = robot

        self.fLeftMotor = ctre.WPI_TalonFX(0)
        self.bLeftMotor = ctre.WPI_TalonFX(1)
        self.fRightMotor = ctre.WPI_TalonFX(2)
        self.bRightMotor = ctre.WPI_TalonFX(3)

        self.spcleft = wpilib.SpeedControllerGroup(self.fLeftMotor, self.bLeftMotor)
        self.spcright = wpilib.SpeedControllerGroup(self.fRightMotor, self.bRightMotor)
        self.drive = wpilib.drive.DifferentialDrive(self.spcleft, self.spcright)

        self.drive.setSafetyEnabled(True)
        self.drive.setExpiration(0.1)

    def disable_drive():
        self.fLeftMotor.disable()
        self.bLeftMotor.disable()
        self.fRightMotor.disable()
        self.bRightMotor.disable()
        
    def drive_tank(left, right):
        self.drive.tankDrive(left, right)
    
    #def drive(left, right):
    #    self.
