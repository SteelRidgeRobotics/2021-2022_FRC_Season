from conversions import Conversions
from wpimath.controller import RamseteController
from wpimath.geometry import Pose2d
from wpimath.kinematics import ChassisSpeeds
from wpimath.trajectory import Trajectory
import wpilib
from constants import *
import math

class CustomRamseteControllerAbstraction(RamseteController):
    m_poseError = Pose2d

    m_poseTolerance = Pose2d

    m_b = 0.0

    m_zeta = 0.0

    def CustomRamseteControllerAbstraction(self, b: float, zeta: float) -> None:
        super(b, zeta)
        self.m_b = b
        self.m_zeta = zeta

    #def CustomRamseteControllerAbstraction(self) -> None:
        #super(2.0, 0.7)
        #self.m_b = 2.0
        #self.m_zeta = 0.7

    def sinc(self, x: float) -> float:
        if math.fabs(x) < 0.0:
            return 1.0-1.0/6.0*x*x
        
        else:
            return math.sin(x)/x

      

    def calculate(self, currentPose: Pose2d, poseRef: Pose2d, linearVelocityRefMeters: float, angularVelocityRefRadiansPerSecond: float) -> ChassisSpeeds:
            
        m_poseError = poseRef.relativeTo(currentPose)
        eX = self.m_poseError.translation().X()
        eY = self.m_poseError.translation().Y()
        eTheta = self.m_poseError.rotation().radians()
        vRef = linearVelocityRefMeters
        omegaRef = angularVelocityRefRadiansPerSecond

        wpilib.SmartDashboard.putNumber("Current X", currentPose.translation().X())
        wpilib.SmartDashboard.putNumber("Reference X", poseRef.translation().X())

        wpilib.SmartDashboard.putNumber("eX", eX)
        wpilib.SmartDashboard.putNumber("eY", eY)
        wpilib.SmartDashboard.putNumber("eTheta", eTheta)
        wpilib.SmartDashboard.putNumber("vRef", vRef)
        wpilib.SmartDashboard.putNumber("omegaRef", omegaRef)

        k = 2.0*self.m_zeta*math.sqrt(math.pow(omegaRef, 2)+self.m_b*math.pow(vRef, 2))

        wpilib.SmartDashboard.putNumber("k", k)

        wpilib.SmartDashboard.putNumber("vX [m/s]", vRef * m_poseError.rotation().cos() + k * eX)
        wpilib.SmartDashboard.putNumber("vY [m/s]", 0.0)
        wpilib.SmartDashboard.putNumber("vOmega [rad/s]", omegaRef + k * eTheta + self.m_b * vRef * self.sinc(eTheta) * eY)

        wpilib.SmartDashboard.putNumber("vX [t/100ms]", Conversions.convertWPILibTrajectoryUnitsToTalonSRXNativeUnits(vRef * m_poseError.rotation().cos() + k * eX, kwheelDiameter, False, kticksPerRev))

        return ChassisSpeeds(vRef*m_poseError.rotation().cos()+k*eX, 0.0, omegaRef+k*eTheta+self.m_b*vRef*self.sinc(eTheta)*eY)

    def calculate(self,currentPose: Pose2d, desiredState: Trajectory.State) -> ChassisSpeeds:

        return self.calculate(currentPose, desiredState.pose, desiredState.velocity, desiredState.velocity*desiredState.curvature)
