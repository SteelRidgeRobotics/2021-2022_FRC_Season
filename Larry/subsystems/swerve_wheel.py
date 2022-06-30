import commands2
import ctre
from constants import *
import wpilib
class SwerveWheel(commands2.SubsystemBase):
    def __init__(self) -> None:
        super().__init__()
        self.directionMotor = ctre.TalonFX(kleftFrontDirectionID)
        self.speedMotor = ctre.TalonFX(kleftFrontSpeedID)

        self.directionMotor.configSelectedFeedbackSensor(ctre.FeedbackDevice.IntegratedSensor, 0, ktimeoutMs)

        #self.directionMotor.setSelectedSensorPosition(0.0, 0, ktimeoutMs)

        self.directionMotor.config_kF(0, kF, ktimeoutMs)

        self.directionMotor.config_kP(0, kP, ktimeoutMs)
 
        self.directionMotor.config_kI(0, kI, ktimeoutMs)

        self.directionMotor.config_kD(0, kD, ktimeoutMs)

        # MOTOR CONFIG
        self.directionMotor.configNominalOutputForward(0, ktimeoutMs)
        self.directionMotor.configNominalOutputReverse(0, ktimeoutMs)

        self.directionMotor.configPeakOutputForward(1, ktimeoutMs)
        self.directionMotor.configPeakOutputReverse(-1, ktimeoutMs)

        self.directionMotor.selectProfileSlot(kSlotIdx, kPIDLoopIdx)

        self.directionMotor.configMotionCruiseVelocity(kcruiseVel, ktimeoutMs)
        self.directionMotor.configMotionAcceleration(kcruiseAccel, ktimeoutMs)
        
        self.directionMotor.setNeutralMode(ctre.NeutralMode.Coast)

        #self.directionMotor.setSelectedSensorPosition(0.0, kPIDLoopIdx, ktimeoutMs)

        wpilib.SmartDashboard.putNumber(" P -", kP)
        wpilib.SmartDashboard.putNumber(" I -", kI)
        wpilib.SmartDashboard.putNumber(" D -", kD)
        wpilib.SmartDashboard.putNumber(" F -", kF)
        wpilib.SmartDashboard.putNumber(" Sensor Position -", self.directionMotor.getSelectedSensorPosition())
        self.isNotrotating = True

    def turn(self, set_point: float):
        self.isNotrotating = False
        current_pos = self.directionMotor.getSelectedSensorPosition()
        self.directionMotor.set(ctre.TalonFXControlMode.MotionMagic, int(set_point))
        wpilib.SmartDashboard.putNumber("Sensor - ", current_pos)

    def move(self, joystick_input: float):
        self.speedMotor.set(ctre.TalonFXControlMode.PercentOutput, 0.1*joystick_input)

    def stopAllMotors(self):
        self.directionMotor.set(ctre.TalonFXControlMode.PercentOutput, 0.0)
        self.speedMotor.set(ctre.TalonFXControlMode.PercentOutput, 0.0)

    def showStats(self):
        wpilib.SmartDashboard.putNumber(" P -", kP)
        wpilib.SmartDashboard.putNumber(" I -", kI)
        wpilib.SmartDashboard.putNumber(" D -", kD)
        wpilib.SmartDashboard.putNumber(" F -", kF)
        wpilib.SmartDashboard.putNumber(" Sensor Position -", self.directionMotor.getSelectedSensorPosition())
        wpilib.SmartDashboard.putBoolean(" Is Not Moving? -", self.isNotrotating)
        
        
        """
        # This allows us to change the values for the PIDF Controller
        
        self.directionMotor.config_kF(0, kF, ktimeoutMs)

        self.directionMotor.config_kP(0, kP, ktimeoutMs)
 
        self.directionMotor.config_kI(0, kI, ktimeoutMs)

        self.directionMotor.config_kD(0, kD, ktimeoutMs)
        """