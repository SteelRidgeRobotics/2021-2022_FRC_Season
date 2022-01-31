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
                
                #set backleft and backright motors to follow front motors
                self.backLeft.follow(self.frontLeft)
                self.backRight.follow(self.frontRight)
                
                #set sensor phases
                self.frontLeft.setSensorPhase(False)
                self.frontRight.setSensorPhase(False)
		        
                #set right side to be inverted. this reverses the direction they rotate, so that they go in the same direction as the left side
                self.frontRight.setInverted(True)
                self.backRight.setInverted(True)
		        
                #we are now configurating the integrated sensors inside the motors. this may seem like a lot of techno-jargon, 
		        #but really all we're doing is setting the timeoutms so the motors don't go insane. they'll disable if we lose control for more than the timeout milliseconds
                self.frontLeft.configSelectedFeedbackSensor(ctre.FeedbackDevice.IntegratedSensor, 0, constants.ktimeoutMs)
                self.frontRight.configSelectedFeedbackSensor(ctre.FeedbackDevice.IntegratedSensor, 0, constants.ktimeoutMs)
                
                #more configuring
                self.frontLeft.config_kF(0, constants.kF, constants.ktimeoutMs)
                self.frontRight.config_kF(0, constants.kF, constants.ktimeoutMs)

                self.frontLeft.config_kP(0, constants.kP, constants.ktimeoutMs)
                self.frontRight.config_kP(0, constants.kP, constants.ktimeoutMs)

                self.frontLeft.configMotionCruiseVelocity(constants.kVelocity, constants.ktimeoutMs)
                self.frontRight.configMotionCruiseVelocity(constants.kVelocity, constants.ktimeoutMs)

                self.frontLeft.configMotionAcceleration(constants.kAcceleration, constants.ktimeoutMs)
                self.frontRight.configMotionAcceleration(constants.kAcceleration, constants.ktimeoutMs)

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
                if rightBumper:
                        rightstick *= constants.kslowFactor
                
                #now we set the motors using percentoutput control mode (basically we put in a percentage for the motor to use)
                self.frontLeft.set(ctre.TalonFXControlMode.PercentOutput, leftstick)
                self.frontRight.set(ctre.TalonFXControlMode.PercentOutput, rightstick)
	    
        #motionmagic function
        def motionMagic(self, units) -> None:
            self.frontLeft.set(ctre.TalonFXControlMode.MotionMagic, units)
            self.frontRight.set(ctre.TalonFXControlMode.MotionMagic, units)
        
        #check if robot is moving
        def notInMotion(self) -> bool:
            self.frontLeftPos = self.frontLeft.getSelectedSensorPosition()
            self.frontLeftVel = self.frontLeft.getSelectedSensorVelocity()
            if self.frontLeftPos != 0.0 and self.frontLeftVel == 0.0:
                return True
            else:
                return False

        #stop the motors
        def stopMotors(self, left, right) -> None:
                self.frontLeft.set(ctre.TalonFXControlMode.PercentOutput, left)
                self.frontRight.set(ctre.TalonFXControlMode.PercentOutput, right)

                self.frontLeft.setSelectedSensorPosition(0.0, 0, constants.ktimeoutMs)
                self.frontRight.setSelectedSensorPosition(0.0, 0, constants.ktimeoutMs)
