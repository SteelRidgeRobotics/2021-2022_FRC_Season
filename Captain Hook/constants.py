import math
import wpilib

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

# pneumatics
ksolenoidModuleType = wpilib.PneumaticsModuleType.CTREPCM
ksolenoidModule = 0

# intake ports
kintakeSolenoidLeftPort = 0
kintakeSolenoidRightPort = 1

# launcher port
klauncherSolenoidPort = 2
