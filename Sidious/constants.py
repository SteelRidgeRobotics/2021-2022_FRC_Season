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
kF = 0.0455 #Feed forward
kP = 0.2 #Proportional
kcruiseVel = 10567.0 #Cruise Velocity at 50% of max
kcruiseAccel = 10567.0 #Cruise Acceleration same as velocity
kUnits = 204800.0 #10 rotations of encoders
kticksPerRev = 1.0

#Physical constants
ktrackWidth = 1.5082966671798224 #trackwidth from robot characteristics NEED TO GET THIS
kwheelbaseWidth = 0.4572 #meters
kwheelDiameter = 0.5 #ft

kS=0.699
kV=0.694
kA=0.993
kdriveKinematics = DifferentialDriveKinematics(ktrackWidth)
kmaxVelocity = 7.0
kmaxAccel = 0.25
kmaxJerk = 0.25
kramsete_B = 2.0
kramsete_Zeta = 0.7