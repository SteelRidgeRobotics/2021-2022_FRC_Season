#Controller ports
kdriverControllerPort = 0
kfunctionsControllerPort = 1

#Motion Magic
kMagicDistance = 96.0 / 12.0 #IMPORTANT: THIS IS IN INCHES (96.0 / 12.0 = 8.0 FEET)
kSlotIdx = 0
kPIDLoopIdx = 0
kMagicVelocity = 15000 #this and acceleration should be changed
kMagicAcceleration = 6000

kP = 0.155
kI = 0.0
kD = 1.55
kF = 0.05

#SimpleAuto
kSimplePercent = 1.0
kSimpleDistance = 96.0 / 12.0
#Motors
kfrontLeft = 0
kbackLeft = 1
kfrontRight = 2
kbackRight = 3
kslowFactor = 0.5

#Encoders
ktimeoutMs = 10

#Physical constants
kunitsPerRotation = 2048.0
kwheelCircumference = 1.57 #in feet