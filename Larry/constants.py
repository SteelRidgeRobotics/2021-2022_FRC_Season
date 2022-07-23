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
kdeadband = 0.15

#Encoders
ktimeoutMs = 10
kF = 0.05282272 #Feed forward
kP = 0.3 #Proportional
kI = 0.002 #Integral
kD = 3 #Derivative
kIzone = 130
kcruiseVel = 10567.0 #Cruise Velocity at 50% of max
kcruiseAccel = 10567.0 #Cruise Acceleration same as velocity
kticksPerRev = 2048
kSlotIdx = 0
kPIDLoopIdx = 0 

ksteeringGearRatio = 150/7