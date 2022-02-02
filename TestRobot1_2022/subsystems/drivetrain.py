#import stuff
import commands2
import ctre
import constants
#drive train class inherits from the subsystem base. this means it gets all stuff that the subsystem base gets, and then some (stuff that we add to personalize it)!
class Drivetrain(commands2.SubsystemBase):
        #initiation
        def __init__(self) -> None:
                #super().__init__() basically initializes subsystem base because super() refers to the class we inherit from
                super().__init__()
                
                #motors
                self.frontLeft = ctre.TalonFX(constants.kfrontLeft)
                self.backLeft = ctre.TalonFX(constants.kbackLeft)
                self.frontRight = ctre.TalonFX(constants.kfrontRight)
                self.backRight = ctre.TalonFX(constants.kbackRight)
                
                #booleans
                self.singleBumper = True


                #set backleft and backright motors to follow front motors
                self.backLeft.follow(self.frontLeft)
                self.backRight.follow(self.frontRight)
                
                #set sensor phases
                self.frontLeft.setSensorPhase(False) # THE CODE WORKS!
                self.frontRight.setSensorPhase(False)
		        
                #set right side to be inverted. this reverses the direction they rotate, so that they go in the same direction as the left side
                self.frontRight.setInverted(True)
                self.backRight.setInverted(True)
		        
                #we are now configurating the integrated sensors inside the motors. this may seem like a lot of techno-jargon, 
		        #but really all we're doing is setting the timeoutms so the motors don't go insane. they'll disable if we lose control for more than the timeout milliseconds
                self.frontLeft.configSelectedFeedbackSensor(ctre.FeedbackDevice.IntegratedSensor, 0, constants.ktimeoutMs)
                self.frontRight.configSelectedFeedbackSensor(ctre.FeedbackDevice.IntegratedSensor, 0, constants.ktimeoutMs)
                
                #more configuring
                self.frontLeft.configNominalOutputForward(0, constants.ktimeoutMs)
                self.frontRight.configNominalOutputForward(0, constants.ktimeoutMs)
                self.frontLeft.configNominalOutputReverse(0, constants.ktimeoutMs)
                self.frontRight.configNominalOutputReverse(0, constants.ktimeoutMs) #more like kjamesisintimeout

                self.frontLeft.configPeakOutputForward(1, constants.ktimeoutMs)
                self.frontRight.configPeakOutputForward(1, constants.ktimeoutMs)
                self.frontLeft.configPeakOutputReverse(-1, constants.ktimeoutMs)
                self.frontRight.configPeakOutputReverse(-1, constants.ktimeoutMs)
                
                self.frontLeft.selectProfileSlot(constants.kSlotIdx, constants.kPIDLoopIdx)
                self.frontRight.selectProfileSlot(constants.kSlotIdx, constants.kPIDLoopIdx)
                self.backLeft.selectProfileSlot(constants.kSlotIdx, constants.kPIDLoopIdx)
                self.backRight.selectProfileSlot(constants.kSlotIdx, constants.kPIDLoopIdx)

                #PID + Feed Forward
                self.frontLeft.config_kP(constants.kSlotIdx, constants.kP, constants.ktimeoutMs)
                self.frontLeft.config_kI(constants.kSlotIdx, constants.kI, constants.ktimeoutMs)
                self.frontLeft.config_kD(constants.kSlotIdx, constants.kD, constants.ktimeoutMs)
                self.frontLeft.config_kF(constants.kSlotIdx, constants.kF, constants.ktimeoutMs)

                self.frontRight.config_kP(constants.kSlotIdx, constants.kP, constants.ktimeoutMs)
                self.frontRight.config_kI(constants.kSlotIdx, constants.kI, constants.ktimeoutMs)
                self.frontRight.config_kD(constants.kSlotIdx, constants.kD, constants.ktimeoutMs)
                self.frontRight.config_kF(constants.kSlotIdx, constants.kF, constants.ktimeoutMs) # good j o b

                #acc and velocity
                self.frontLeft.configMotionCruiseVelocity(constants.kMagicVelocity, constants.ktimeoutMs)
                self.frontLeft.configMotionAcceleration(constants.kMagicAcceleration, constants.ktimeoutMs)
                self.frontRight.configMotionCruiseVelocity(constants.kMagicVelocity, constants.ktimeoutMs)
                self.frontRight.configMotionAcceleration(constants.kMagicAcceleration, constants.ktimeoutMs)

                #sensors set 0
                self.frontLeft.setSelectedSensorPosition(0, constants.kPIDLoopIdx, constants.ktimeoutMs)
                self.frontRight.setSelectedSensorPosition(0, constants.kPIDLoopIdx, constants.ktimeoutMs)

		#set motors to brake mode. this means when you don't put any input into the motors, they will stop
                self.frontLeft.setNeutralMode(ctre.NeutralMode.Brake)
                self.backLeft.setNeutralMode(ctre.NeutralMode.Brake)
                self.frontRight.setNeutralMode(ctre.NeutralMode.Brake)
                self.backRight.setNeutralMode(ctre.NeutralMode.Brake)
        #our userdrive function
        def userDrive(self, leftstick, rightstick, leftBumper, rightBumper) -> None:
                #check if either the leftbumper or rightbumper is down
                if leftBumper:
                        #if it is we multiply our motor values by our slow factor constant
                        leftstick *= constants.kslowFactor
                        if not self.singleBumper:
                                rightstick *= constants.kslowFactor
                if rightBumper:
                        rightstick *= constants.kslowFactor
                        if not self.singleBumper:
                                leftstick *= constants.kslowFactor
                
                #now we set the motors using percentoutput control mode (basically we put in a percentage for the motor to use)
                self.frontLeft.set(ctre.TalonFXControlMode.PercentOutput, leftstick)
                self.frontRight.set(ctre.TalonFXControlMode.PercentOutput, rightstick)
	#change bumpers
        def changeBumper(self) -> None:
                self.singleBumper = not self.singleBumper # this bumper is itselfn't

        #stop the motors
        def stopMotors(self) -> None:
                self.frontLeft.set(ctre.TalonFXControlMode.PercentOutput, 0.0)
                self.frontRight.set(ctre.TalonFXControlMode.PercentOutput, 0.0)

