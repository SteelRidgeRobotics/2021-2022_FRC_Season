#!/usr/bin/env python3

import wpilib
import ctre



class MyRobot(wpilib.TimedRobot):
   

    def robotInit(self):
        self.fRight = ctre.WPI_TalonFX(0)
        self.fLeft = ctre.WPI_TalonFX(1) 
        self.bRight = ctre.WPI_TalonFX(2) 
        self.bLeft = ctre.WPI_TalonFX(3) 
        
        self.timer = wpilib.Timer()

    def disabledPeriodic(self):
        self.fRight.disable()
        self.fLeft.disable()
        self.bRight.disable()
        self.bLeft.disable()
        
    def autonomousInit(self):
        self.timer.start()  

    def autonomousPeriodic(self):
        if self.timer.get() <=5:
            self.fRight.set(0.5)
        
        if self.timer.get() <=10:
            self.fRight.set(0)
            self.fLeft.set(0.5)
            
        
        if self.timer.get() <=15:
            self.fLeft.set(0)
            self.bRight.set(0.5)
            
        
        if self.timer.get() <=20:
            self.bRight.set(0)
            self.bLeft.set(0.5)
            
        
        if self.timer.get() <= 25:
            self.bLeft.set(0)


if __name__ == "__main__":
    wpilib.run(MyRobot)
