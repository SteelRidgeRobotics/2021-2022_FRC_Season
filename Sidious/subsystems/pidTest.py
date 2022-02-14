from os import system
import string
from sys import stdout
from tkinter.tix import StdButtonBox
from xmlrpc.client import Boolean
import commands2
import ctre
from filelock import sys
from py import std
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


        self.motors = [self.frontLeft, self.frontRight]

        self.motor = [ctre.TalonFX, ctre.TalonFX]

        for self.motor in self.motors:
            self.motor.configFactoryDefault()
            self.motor.setSelectedSensorPosition(0.0)
    
        self.putToSmartDashboard()

        self.flush()

    def putToSmartDashboard(self) -> None:

        self.motors = [self.frontLeft, self.frontRight]

        self.motor = [ctre.TalonFX, ctre.TalonFX]

        for self.motor in self.motors:
             
            self.motorName = "Motor " + str(self.motor.getDeviceID()) + " "

            SmartDashboard.putBoolean(self.motorName + "inverted", False)
        
     
        SmartDashboard.putBoolean("Flush", False)
        SmartDashboard.putNumber("kP", 0)
        SmartDashboard.putNumber("kI", 0)
        SmartDashboard.putNumber("kD", 0)
        SmartDashboard.putNumber("kF", 0)
        SmartDashboard.putNumber("Setpoint", 0)

    def flush(self) -> None:

        self.motors = [self.frontLeft, self.frontRight]

        self.motor = [ctre.TalonFX, ctre.TalonFX]

        for self.motor in self.motors:

            self.motorName = "Motor " + str(self.motor.getDeviceID()) + " "

            self.motor.config_kF(0, SmartDashboard.getNumber("kF", 0), ktimeoutMs)
            self.motor.config_kP(0, SmartDashboard.getNumber("kP", 0), ktimeoutMs)
            self.motor.config_kI(0, SmartDashboard.getNumber("kI", 0), ktimeoutMs)
            self.motor.config_kD(0, SmartDashboard.getNumber("kD", 0), ktimeoutMs)
            self.motor.set(ctre.ControlMode.Velocity, SmartDashboard.getNumber("Setpoint", 0))

            print("Updated " + str(self.motor.getDeviceID()))

        SmartDashboard.putBoolean("Flush", False)

    def putMotorValuesToSmartDashboard(self) -> None:
        
        self.motors = [self.frontLeft, self.frontRight]

        self.motor = [ctre.TalonFX, ctre.TalonFX]

        for self.motor in self.motors:
            
            self.motorName = "Motor " + str(self.motor.getDeviceID()) + " "

            SmartDashboard.putNumber(self.motorName + "target", self.motor.getClosedLoopTarget())
            SmartDashboard.putNumber(self.motorName + "velocity", self.motor.getSelectedSensorVelocity())
            SmartDashboard.putNumber(self.motorName + "error", self.motor.getClosedLoopError())

    def periodic(self) -> None:
        if SmartDashboard.getBoolean("Flush", False):
            self.flush()
        
        self.putMotorValuesToSmartDashboard()

        #return super().periodic()


