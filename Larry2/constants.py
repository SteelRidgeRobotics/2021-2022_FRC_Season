import math

# motors
kleftFrontSpeedID = 0
kleftRearSpeedID = 1
krightFrontSpeedID = 2
krightRearSpeedID = 3

kleftFrontDirectionID = 4
kleftRearDirectionID = 5
krightFrontDirectionID = 6
krightRearDirectionID = 7


kdriverControllerPort = 0
kdeadband = 0.085

#Encoders
ktimeoutMs = 10
kF = 0.0455 #Feed forward
kP = 0.01 #Proportional
kI = 0.0 #Integral
kD = 0.0 #Derivative
kcruiseVel = 10567.0 #Cruise Velocity at 50% of max
kcruiseAccel = 10567.0 #Cruise Acceleration same as velocity
kticksPerRev = 2048
kSlotIdx = 0
kPIDLoopIdx = 0 

ksteeringGearRatio = 150/7