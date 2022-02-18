import math
from wpimath.kinematics import DifferentialDriveKinematics


#Controller ports
kdriverControllerPort = 0
kfunctionsControllerPort = 1

#Motors
kfrontLeft = 0
kbackLeft = 1
kfrontRight = 2
kbackRight = 3

kverticalClimber = 4
ktiltedClimber = 5

kleftIntake = 6
krightIntake = 7

#Encoders
ktimeoutMs = 10
kF = 0.05 #Feed forward
kP = 0.075 #Proportional
kI = 0.0 #Integral
kD = 0.0 #Derivative
kcruiseVel = 10567.0 #Cruise Velocity at 50% of max
kcruiseAccel = 10567.0 #Cruise Acceleration same as velocity
kUnits = 204800.0 #10 rotations of encoders for motion magic testing
kticksPerRev = 8192*2

#Physical constants
ktrackWidth = 0.99761 #trackwidth from robot characteristics NEED TO GET THIS
kwheelbaseWidth = 0.4572 #meters
kwheelDiameter = 0.5 #ft

kS=0.55843
kV=2.395
kA=0.18422
kdriveKinematics = DifferentialDriveKinematics(ktrackWidth)
kmaxVelocity = 6.0
kmaxAccel = 2.5
kmaxJerk = 1.0
kramsete_B = 2.0
kramsete_Zeta = 0.7