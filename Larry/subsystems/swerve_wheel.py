import commands2
import ctre
from constants import *
import wpilib
from conversions import *

from conversions import convertDegreesToTalonFXUnits
class SwerveWheel(commands2.SubsystemBase):
    def __init__(self, directionMotor: ctre.TalonFX, speedMotor:ctre.TalonFX) -> None:
        super().__init__()
        self.directionMotor = directionMotor
        self.speedMotor = speedMotor

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
        self.notTurning = True
    # this is are testing turn method
    def turn(self, set_point: float):
        self.notTurning = False
        current_pos = self.directionMotor.getSelectedSensorPosition()
        self.directionMotor.set(ctre.TalonFXControlMode.MotionMagic, int(set_point))

    def translate(self, direction: float, speed: float):
        # check for the closest angle (effeciency)
        currentAngle = convertTalonFXUnitsToDegrees(self.directionMotor.getSelectedSensorPosition())
        if math.fabs(direction) >= 180.0:
            opposAngle = math.fabs(direction) - 180.0
        else:
            opposAngle = math.fabs(direction) + 180.0
        wpilib.SmartDashboard.putNumber(" Original Angle -", direction)
        wpilib.SmartDashboard.putNumber(" Abs Opposit Angle -", opposAngle)
        if math.fabs(currentAngle - direction) <= math.fabs(currentAngle - opposAngle):
            #turn to the original angle
            self.directionMotor.set(ctre.TalonFXControlMode.MotionMagic, int(convertDegreesToTalonFXUnits(direction))*ksteeringGearRatio)
            self.speedMotor.set(ctre.TalonFXControlMode.PercentOutput, speed)
        else:
            #turn to the other angle
            #change direction of the speed motor
            self.directionMotor.set(ctre.TalonFXControlMode.MotionMagic, int(convertDegreesToTalonFXUnits(opposAngle))*ksteeringGearRatio)
            self.speedMotor.set(ctre.TalonFXControlMode.PercentOutput, -speed)

    def isNotinMotion(self) -> bool:

        if self.directionMotor.getActiveTrajectoryVelocity() == 0.0:
            self.notTurning = True
        else:
            self.notTurning = False
        return self.notTurning

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
        wpilib.SmartDashboard.putNumber(" Sensor Velocity -", self.directionMotor.getSelectedSensorVelocity())
        wpilib.SmartDashboard.putBoolean(" Is Not Moving? -", self.isNotinMotion())
        
        
        """
        # This allows us to change the values for the PIDF Controller
        
        self.directionMotor.config_kF(0, kF, ktimeoutMs)

        self.directionMotor.config_kP(0, kP, ktimeoutMs)
 
        self.directionMotor.config_kI(0, kI, ktimeoutMs)

        self.directionMotor.config_kD(0, kD, ktimeoutMs)
        """
        
