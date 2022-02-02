from xmlrpc.client import Boolean
import commands2
import ctre
import constants



class Drivetrain(commands2.SubsystemBase):

    def __init__(self) -> None:
        super().__init__()

        #initalize motors
        self.frontLeft = ctre.TalonFX(constants.kfrontLeft)
        self.backLeft = ctre.TalonFX(constants.kbackLeft)
        self.frontRight = ctre.TalonFX(constants.kfrontRight)
        self.backRight = ctre.TalonFX(constants.kbackRight)

        #self.frontLeft.configFactoryDefault()
        #self.backLeft.configFactoryDefault()
        #self.frontRight.configFactoryDefault()
        #self.backLeft.configFactoryDefault()

        #set followers
        self.backLeft.follow(self.frontLeft)
        self.backRight.follow(self.frontRight)

        #reverse sensors-This shouldn't be necessary with TalonFX as sensors are integrated
        

        #invert motors on right side
        self.frontRight.setInverted(ctre.TalonFXInvertType.Clockwise)
        self.backRight.setInverted(ctre.TalonFXInvertType.Clockwise)

        #configure encoders
        self.frontRight.configSelectedFeedbackSensor(ctre.FeedbackDevice.IntegratedSensor, 0, constants.ktimeoutMs)
        self.frontLeft.configSelectedFeedbackSensor(ctre.FeedbackDevice.IntegratedSensor, 0, constants.ktimeoutMs)

        self.frontLeft.config_kF(0, constants.kF, constants.ktimeoutMs) 
        self.frontRight.config_kF(0, constants.kF, constants.ktimeoutMs)

        self.frontLeft.config_kP(0, constants.kP, constants.ktimeoutMs) 
        self.frontRight.config_kP(0, constants.kP, constants.ktimeoutMs)

        self.frontLeft.configMotionCruiseVelocity(constants.kcruiseVel, constants.ktimeoutMs)
        self.frontRight.configMotionCruiseVelocity(constants.kcruiseVel, constants.ktimeoutMs)

        self.frontLeft.configMotionAcceleration(constants.kcruiseAccel, constants.ktimeoutMs)
        self.frontRight.configMotionAcceleration(constants.kcruiseAccel, constants.ktimeoutMs)
        
        #set motors to brake mode
        self.frontLeft.setNeutralMode(ctre.NeutralMode.Brake)
        self.backLeft.setNeutralMode(ctre.NeutralMode.Brake)
        self.frontRight.setNeutralMode(ctre.NeutralMode.Brake)
        self.backLeft.setNeutralMode(ctre.NeutralMode.Brake)

        

    def userDrive(self, leftJoy: float, rightJoy: float) -> None:
        
        self.frontLeft.set(ctre.TalonFXControlMode.PercentOutput, leftJoy)
        self.frontRight.set(ctre.TalonFXControlMode.PercentOutput, rightJoy)
    
    def stopMotors(self) -> None:

        self.frontLeft.set(ctre.TalonFXControlMode.PercentOutput, 0.0)
        self.frontRight.set(ctre.TalonFXControlMode.PercentOutput, 0.0)

        #self.frontLeft.setSelectedSensorPosition(0, 0, constants.ktimeoutMs)
        #self.frontRight.setSelectedSensorPosition(0, 0, constants.ktimeoutMs)

    def motionMagic(self, units: float) -> None:
        self.frontLeft.set(ctre.TalonFXControlMode.MotionMagic, units)
        self.frontRight.set(ctre.TalonFXControlMode.MotionMagic, units)

    def isMoving(self) -> Boolean:
        self.l_vel = self.frontLeft.getSelectedSensorVelocity()
        self.l_pos = self.frontLeft.getSelectedSensorPosition()
        #self.l_error = self.frontLeft.getClosedLoopError()
        #self.l_target = self.frontLeft.getClosedLoopTarget() 
        self.vel_traj = self.frontLeft.getActiveTrajectoryVelocity()
        """
        if  self.l_pos != 0.0 and self.l_vel == 0.0:
            return True
        
        else:
            return False
        """
        if self.vel_traj==0.0:
            return True
        else:
            return False

    def resetEncoders(self) -> None:

        self.frontLeft.setSelectedSensorPosition(0.0, 0, constants.ktimeoutMs)
        self.frontRight.setSelectedSensorPosition(0.0, 0, constants.ktimeoutMs)
