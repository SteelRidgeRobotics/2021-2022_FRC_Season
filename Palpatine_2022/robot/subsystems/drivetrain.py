import commands2
import ctre
import constants

class Drivetrain(commands2.SubsystemBase):
    def __init__(self) -> None:
        super().__init__()

        #initilize motors
        self.frontLeft = ctre.TalonFX(constants.kfrontLeft)
        self.backLeft = ctre.TalonFX(constants.kbackLeft)
        self.frontRight = ctre.TalonFX(constants.kfrontRight)
        self.backRight = ctre.TalonFX(constants.kbackRight)

        #set followers
        self.backLeft.follow(self.frontLeft)
        self.backRight.follow(self.frontRight)

        #reverse sensors
        self.frontLeft.setSensorPhase(False)
        self.frontRight.setSensorPhase(False)

        #invert motors on right side
        self.frontRight.setInverted(True)
        self.backRight.setInverted(True)

        #config motors
        self.frontLeft.configSelectedFeedbackSensor(ctre.FeedbackDevice.IntegratedSensor, 0, constants.ktimeoutMs)
        self.frontRight.configSelectedFeedbackSensor(ctre.FeedbackDevice.IntegratedSensor, 0, constants.ktimeoutMs)
        
        #forward and back
        self.frontLeft.configNominalOutputForward(0, constants.ktimeoutMs)
        self.frontRight.configNominalOutputForward(0, constants.ktimeoutMs)
        self.frontLeft.configNominalOutputReverse(0, constants.ktimeoutMs)
        self.frontRight.configNominalOutputReverse(0, constants.ktimeoutMs)
        
        #peak output
        self.frontLeft.configPeakOutputForward(1, constants.ktimeoutMs)
        self.frontRight.configPeakOutputForward(1, constants.ktimeoutMs)
        self.frontLeft.configPeakOutputReverse(-1, constants.ktimeoutMs)
        self.frontRight.configPeakOutputReverse(-1, constants.ktimeoutMs)
        
        #profile slot
        self.frontLeft.selectProfileSlot(constants.kSlotIdx, constants.kPIDLoopIdx)
        self.frontRight.selectProfileSlot(constants.kSlotIdx, constants.kPIDLoopIdx)
        self.backLeft.selectProfileSlot(constants.kSlotIdx, constants.kPIDLoopIdx)
        self.backRight.selectProfileSlot(constants.kSlotIdx, constants.kPIDLoopIdx)

        #config Proportional, Integral, Derivative, and Filtered (PIDF)
        self.frontLeft.config_kP(constants.kSlotIdx, 0.2, constants.ktimeoutMs) #please change these values later (value)
        self.frontLeft.config_kI(constants.kSlotIdx, 0, constants.ktimeoutMs)
        self.frontLeft.config_kD(constants.kSlotIdx, 0, constants.ktimeoutMs)
        self.frontLeft.config_kF(constants.kSlotIdx, 0.2, constants.ktimeoutMs)

        self.frontRight.config_kP(constants.kSlotIdx, 0.2, constants.ktimeoutMs)
        self.frontRight.config_kI(constants.kSlotIdx, 0, constants.ktimeoutMs)
        self.frontRight.config_kD(constants.kSlotIdx, 0, constants.ktimeoutMs)
        self.frontRight.config_kF(constants.kSlotIdx, 0.2, constants.ktimeoutMs)        

        #setting our acceleration and velocity (it's like cruise control but better hahaha laugh please laugh)
        self.frontLeft.configMotionCruiseVelocity(constants.kmotorCruiseVelocity, constants.ktimeoutMs)
        self.frontRight.configMotionCruiseVelocity(constants.kmotorCruiseVelocity, constants.ktimeoutMs)
        self.frontLeft.configMotionAcceleration(constants.kmotorAcceleration, constants.ktimeoutMs)
        self.frontRight.configMotionAcceleration(constants.kmotorAcceleration, constants.ktimeoutMs)
        
        #setting sensors to 0
        self.frontLeft.setSelectedSensorPosition(0, constants.kPIDLoopIdx, constants.ktimeoutMs)
        self.frontRight.setSelectedSensorPosition(0, constants.kPIDLoopIdx, constants.ktimeoutMs)


        #set motors to brake mode
        self.frontLeft.setNeutralMode(ctre.NeutralMode.Brake)
        self.backLeft.setNeutralMode(ctre.NeutralMode.Brake)
        self.frontRight.setNeutralMode(ctre.NeutralMode.Brake)
        self.backRight.setNeutralMode(ctre.NeutralMode.Brake)
       
    def userDrive(self, leftJoy: float, rightJoy: float, percentage: float) -> None:
        self.frontLeft.set(ctre.TalonFXControlMode.PercentOutput, leftJoy*percentage)
        self.frontRight.set(ctre.TalonFXControlMode.PercentOutput, rightJoy*percentage)

    def magicDrive(self, targetPos: float) -> None:
        self.frontLeft.set(ctre.TalonFXControlMode.MotionMagic, targetPos)
        self.frontRight.set(ctre.TalonFXControlMode.MotionMagic, targetPos)

    def stopMotors(self) -> None:
        self.left = 0.0
        self.right = 0.0
        self.frontLeft.set(ctre.TalonFXControlMode.PercentOutput, 0.0)
        self.frontRight.set(ctre.TalonFXControlMode.PercentOutput, 0.0)

        self.frontLeft.setSelectedSensorPosition(0, 0, constants.ktimeoutMs)
        self.frontRight.setSelectedSensorPosition(0, 0, constants.ktimeoutMs)
