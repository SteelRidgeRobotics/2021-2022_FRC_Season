import math

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

#Encoders
ktimeoutMs = 10

#Autonomous
kAutoBackupDistanceFeet = 8                                                                                                                                                                                                                                          
kAutoDriveSpeed = 1

#Motion Magic
kdistanceToTravel = 8.0
kSlotIdx = 0
kPIDLoopIdx = 0
kmotorCruiseVelocity = 15000 #please change this
kmotorAcceleration = 6000 #this too

kF = 0.0509563647
kP = 0.4
#11.25
kD = 0.0
kI = 0.0

kClimberRate = 10.0
# climber PID
kclimberF = 0.025
kclimberP = 0.0
kclimberD = 0.0
kclimberI = 0.0

#Physical constants
kunitsPerRotation = 2048.0
kwheelCircumference = 1.57 #this is in feet

kClimberHeight = 0.0
