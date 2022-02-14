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

        #create motors as list
        self.motors = [self.frontLeft, self.frontRight]

        #create list values as TalonFX objects
        self.motor = [ctre.TalonFX, ctre.TalonFX]

        #Config default and sensor positions all motors in the list
        for self.motor in self.motors:

            self.motor.configFactoryDefault()

            self.motor.setSelectedSensorPosition(0.0)
    
        self.putToSmartDashboard()

        self.flush()

    def putToSmartDashboard(self) -> None:
        """This method puts values to the smartdashboard."""

        self.motors = [self.frontLeft, self.frontRight]

        self.motor = [ctre.TalonFX, ctre.TalonFX]

        #create motor names for smartdashboard & show whether motors are inverted
        for self.motor in self.motors:
             
            self.motorName = "Motor " + str(self.motor.getDeviceID()) + " "

            SmartDashboard.putBoolean(self.motorName + "inverted", self.motor.getInverted())

        #Put boolean to "reset" values, PIDF values & a velocity setpoint            
        SmartDashboard.putBoolean("Flush", False)
        SmartDashboard.putNumber("kP", 0)
        SmartDashboard.putNumber("kI", 0)
        SmartDashboard.putNumber("kD", 0)
        SmartDashboard.putNumber("kF", 0)
        SmartDashboard.putNumber("Setpoint", 0)

    def flush(self) -> None:
        """This method resets values on the smartdashboard."""

        self.motors = [self.frontLeft, self.frontRight]

        self.motor = [ctre.TalonFX, ctre.TalonFX]

        #create names for smartdashboard, sets Talons to velocity control mode for tuning and prints when values are updated to the stream
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
        """This method puts motor values to the smartdashboard."""
        
        self.motors = [self.frontLeft, self.frontRight]

        self.motor = [ctre.TalonFX, ctre.TalonFX]

        #create names for smartdashboard & targets/errors
        for self.motor in self.motors:
            
            self.motorName = "Motor " + str(self.motor.getDeviceID()) + " "

            SmartDashboard.putNumber(self.motorName + "target", self.motor.getClosedLoopTarget())
            SmartDashboard.putNumber(self.motorName + "velocity", self.motor.getSelectedSensorVelocity())
            SmartDashboard.putNumber(self.motorName + "error", self.motor.getClosedLoopError())

    def periodic(self) -> None:
        """This method runs periodically to check whether to flush or not and continues to update the smartdashboard."""
        
        if SmartDashboard.getBoolean("Flush", False):
            self.flush()
        
        self.putMotorValuesToSmartDashboard()



