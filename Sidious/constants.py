import math



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

#Physical constants

