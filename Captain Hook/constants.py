import math
import wpilib
from wpimath.kinematics import DifferentialDriveKinematics
#Controller ports
kdriverControllerPort = 0
kfunctionsControllerPort = 1

#Motors
kfrontLeft = 0
kbackLeft = 1
kfrontRight = 2
kbackRight = 3

kclimber1 = 4
kclimber2 = 5

kintakeBottom = 6
kintakeTop = 7

#Encoders
ktimeoutMs = 10

#Physical constants
kunitsPerRotation = 2048.0
kwheelCircumference = 1.57 #this is in feet
ktrackWidth = 0.99761 #not accurate need to get value

#Motion Magic
kdistanceToTravel = 8.0
kSlotIdx = 0
kPIDLoopIdx = 0
kmotorCruiseVelocity = 15000 #please change this
kmotorAcceleration = 6000 #this too

kF = 0.0509563647
kP = 0.375
kD = 11.25
kI = 0.0

#Robot Characteristics
kS=0.55843
kV=2.395
kA=0.18422

#Trajectory Constants
kmaxVelocity = 3.0
kmaxAccel = 1.5
kmaxJerk = 0.75
kramsete_B = 2.0
kramsete_Zeta = 0.7
kdriveKinematics = DifferentialDriveKinematics(ktrackWidth)
kmaxVelocity = 3.0
kmaxAccel = 1.5

# pneumatics
ksolenoidModuleType = wpilib.PneumaticsModuleType.CTREPCM
ksolenoidModule = 0

# intake ports
kintakeSolenoidIn = 5
kintakeSolenoidOut = 4

# launcher port
klauncherSolenoidIn = 7
klauncherSolenoidOut = 6

kgearRatio = 10.71
kwheelDiameter = 0.5

kticksPerRev = 2048