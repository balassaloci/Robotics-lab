import brickpi
import time
import os
import math

class robolib:
    def __init__(self):
        self.interface=brickpi.Interface()
        self.interface.initialize()

        self.motors = [0,3]
        self.speed = 1.0
        self.interface.motorEnable(self.motors[0])
        self.interface.motorEnable(self.motors[1])
        LEFTMOTORPARAMS = self.interface.MotorAngleControllerParameters()
        LEFTMOTORPARAMS.maxRotationAcceleration = 6.0
        LEFTMOTORPARAMS.minPWM = 18.0
        LEFTMOTORPARAMS.maxRotationSpeed = 12.0
        LEFTMOTORPARAMS.feedForwardGain = 255/20.0
        LEFTMOTORPARAMS.pidParameters.minOutput = -255
        LEFTMOTORPARAMS.pidParameters.maxOutput = 255
        LEFTMOTORPARAMS.pidParameters.k_p = 456.0 
        LEFTMOTORPARAMS.pidParameters.k_i = 350.0
        LEFTMOTORPARAMS.pidParameters.K_d = 40.0
        RIGHTMOTORPARAMS = self.interface.MotorAngleControllerParameters()
        RIGHTMOTORPARAMS.maxRotationAcceleration = 6.0
        RIGHTMOTORPARAMS.minPWM = 18.0
        RIGHTMOTORPARAMS.maxRotationSpeed = 12.0
        RIGHTMOTORPARAMS.feedForwardGain = 255/20.0
        RIGHTMOTORPARAMS.pidParameters.minOutput = -255
        RIGHTMOTORPARAMS.pidParameters.maxOutput = 255
        RIGHTMOTORPARAMS.pidParameters.k_p = 444.0
        RIGHTMOTORPARAMS.pidParameters.k_i = 350.0
        RIGHTMOTORPARAMS.pidParameters.K_d = 40.0

        self.interface.setMotorAngleControllerParameters(self.motors[0],LEFTMOTORPARAMS)
        self.interface.setMotorAngleControllerParameters(self.motors[1],RIGHTMOTORPARAMS)

        self.right_ratio = 0.99
        self.left_ratio  = 1.01

        self.wheel_diam = 5.5
        self.anti_lean_left = 1.01
        self.anti_lean_right = 0.99
        self.shaft_length = 13.6

    def __del__(self):
        self.interface.terminate()

    def straight(self, distance):
        angle = 2 * distance/self.wheel_diam
        left_angle = angle * self.anti_lean_left
        right_angle = angle * self.anti_lean_right
        self.interface.increaseMotorAngleReferences(self.motors, [left_angle,right_angle])
        
        while not self.interface.motorAngleReferencesReached(self.motors) :
            motorAngles = self.interface.getMotorAngles(self.motors)
            if motorAngles :
                    print "Motor angles: ", motorAngles[0][0], ", ", motorAngles[1][0]
            time.sleep(0.1)
    
        print("Destination reached")
    
    
    def turn(self, angle):
        angle /= 2
        circumference = self.shaft_length * math.pi
        turn_size = circumference * angle / 360
        const_multip = 0.72
        turn_size *= const_multip
        self.interface.increaseMotorAngleReferences(self.motors,[turn_size, -turn_size])
    
        
        while not self.interface.motorAngleReferencesReached(self.motors) :
            motorAngles = self.interface.getMotorAngles(self.motors)
            if motorAngles:
                    print "Motor angles: ", motorAngles[0][0], ", ", motorAngles[1][0]
            time.sleep(0.1)
    
        print("Turn DONE")

    def sense(self):
        touch_port = 1
        self.interface.sensorEnable(touch_port, brickpi.SensorType.SENSOR_TOUCH)

        while True:
            result = self.interface.getSensorValue(touch_port)
            if result:
                touched = result[0]
                print(str(touched))

            time.sleep(0.1)


