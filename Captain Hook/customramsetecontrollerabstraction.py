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

    def CustomRamseteControllerAbstraction(self) -> None:
        super(2.0, 0.7)
        self.m_b = 2.0
        self.m_zeta = 0.7

    def sinc(self, x: float) -> float:
        if math.fabs(x) < 1e-9:
            return 1.0-1.0/6.0*x*x
        
        else:
            return math.sin(x)/x   

    def calculate(self, currentPose: Pose2d, poseRef: Pose2d, linearVelocityRefMeters: float, angularVelocityRefRadiansPerSecond: float) -> ChassisSpeeds:
            
        m_poseError = poseRef.relativeTo(currentPose)
        eX = m_poseError.translation().X()
        eY = m_poseError.translation().Y()
        eTheta = m_poseError.rotation().radians()
        vRef = linearVelocityRefMeters
        omegaRef = angularVelocityRefRadiansPerSecond

        k = 2.0*self.m_zeta*math.sqrt(math.pow(omegaRef, 2)+self.m_b*math.pow(vRef, 2))

        return ChassisSpeeds(vRef*m_poseError.rotation().cos()+k*eX, 0.0, omegaRef+k*eTheta+self.m_b*vRef*self.sinc(eTheta)*eY)

    def calculate(self,currentPose: Pose2d, desiredState: Trajectory.State) -> ChassisSpeeds:

        return self.calculate(currentPose, desiredState.pose, desiredState.velocity, desiredState.velocity*desiredState.curvature)
