from posixpath import basename
import string
from xml.etree.ElementTree import fromstringlist
from xmlrpc.client import Boolean
import commands2
import ctre
from constants import *
from wpilib import SmartDashboard


class PidTest(commands2.SubsystemBase):

    def __init__(self) -> None:
        super().__init__()

        #initalize motors
        self.frontLeft = ctre.TalonFX(kfrontLeft)
        self.backLeft = ctre.TalonFX(kbackLeft)
        self.frontRight = ctre.TalonFX(kfrontRight)
        self.backRight = ctre.TalonFX(kbackRight)

        #set followers
        self.backLeft.follow(self.frontLeft)
        self.backRight.follow(self.frontRight)

        self.frontRight.setInverted(ctre.TalonFXInvertType.Clockwise)
        self.backRight.setInverted(ctre.TalonFXInvertType.Clockwise)

        #configure encoders
        self.frontRight.configSelectedFeedbackSensor(ctre.FeedbackDevice.IntegratedSensor, 0, ktimeoutMs)
        self.frontLeft.configSelectedFeedbackSensor(ctre.FeedbackDevice.IntegratedSensor, 0, ktimeoutMs)

        self.frontLeft.configFactoryDefault()
        self.frontRight.configFactoryDefault()

        self.frontLeft.setSelectedSensorPosition(0.0)
        self.frontRight.setSelectedSensorPosition(0.0)
    
        self.putToSmartDashboard()

        self.flush()

    def putToSmartDashboard(self) -> None:
        
     
        SmartDashboard.putBoolean("Flush", False)
        SmartDashboard.putNumber("kP", 0)
        SmartDashboard.putNumber("kI", 0)
        SmartDashboard.putNumber("kD", 0)
        SmartDashboard.putNumber("kF", 0)
        SmartDashboard.putNumber("Setpoint", 0)

    def flush(self) -> None:

        self.baseName = string

        baseName = "LMotor" + self.frontLeft.getDeviceID() + "" + "RMotor" + self.frontRight.getDeviceID() + ""

        self.frontLeft.config_kF(0, SmartDashboard.getNumber("kF", 0), ktimeoutMs) 
        self.frontRight.config_kF(0, SmartDashboard.getNumber("kF", 0), ktimeoutMs)

        self.frontLeft.config_kP(0, SmartDashboard.getNumber("kP", 0), ktimeoutMs) 
        self.frontRight.config_kP(0, SmartDashboard.getNumber("kP", 0), ktimeoutMs)

        self.frontLeft.config_kI(0, SmartDashboard.getNumber("kI", 0), ktimeoutMs) 
        self.frontRight.config_kI(0, SmartDashboard.getNumber("kI", 0), ktimeoutMs)

        self.frontLeft.config_kD(0, SmartDashboard.getNumber("kD", 0), ktimeoutMs) 
        self.frontRight.config_kD(0, SmartDashboard.getNumber("kD", 0), ktimeoutMs)

        self.frontLeft.set(ctre.ControlMode.Velocity, SmartDashboard.getNumber("Setpoint", 0))
        self.frontRight.set(ctre.ControlMode.Velocity, SmartDashboard.getNumber("Setpoint", 0))

        SmartDashboard.putBoolean("Flush", False)

    def putMotorValuesToSmartDashboard(self) -> None:
        
        self.baseName = string

        baseName = "LMotor" + self.frontLeft.getDeviceID() + "" + "RMotor" + self.frontRight.getDeviceID() + ""
    
        SmartDashboard.putNumber(baseName + "Ltarget", self.frontLeft.getClosedLoopTarget())
        SmartDashboard.putNumber(baseName + "Rtarget", self.frontRight.getClosedLoopTarget())

        SmartDashboard.putNumber(baseName + "LVelocity", self.frontLeft.getSelectedSensorVelocity())
        SmartDashboard.putNumber(baseName + "RVelocity", self.frontRight.getSelectedSensorVelocity())

        SmartDashboard.putNumber(baseName + "LError", self.frontLeft.getClosedLoopError())
        SmartDashboard.putNumber(baseName + "RError", self.frontRight.getClosedLoopError())

    def periodic(self) -> None:
        if SmartDashboard.getBoolean("Flush", False):
            self.flush()
        
        self.putMotorValuesToSmartDashboard()

        return super().periodic()


