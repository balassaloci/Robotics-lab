import brickpi
import time
import math

interface=brickpi.Interface()
interface.initialize()

motors = [0,3]

interface.motorEnable(motors[0])
interface.motorEnable(motors[1])

motorParams = interface.MotorAngleControllerParameters()
motorParams.maxRotationAcceleration = 6.0
motorParams.maxRotationSpeed = 12.0
motorParams.feedForwardGain = 255/20.0
motorParams.minPWM = 18.0
motorParams.pidParameters.minOutput = -255
motorParams.pidParameters.maxOutput = 255
motorParams.pidParameters.k_p = 100.0
motorParams.pidParameters.k_i = 0.0
motorParams.pidParameters.k_d = 0.0

interface.setMotorAngleControllerParameters(motors[0],motorParams)
interface.setMotorAngleControllerParameters(motors[1],motorParams)

wheel_diam = 5.5
anti_lean_left = 1.01
anti_lean_right = 0.99

def go_straigth(distance):
    angle = 2 * distance/wheel_diam
    left_angle = angle * anti_lean_left
    right_angle = angle * anti_lean_right
    interface.increaseMotorAngleReferences(motors,[left_angle,right_angle])
    
    while not interface.motorAngleReferencesReached(motors) :
    	motorAngles = interface.getMotorAngles(motors)
    	if motorAngles :
    		print "Motor angles: ", motorAngles[0][0], ", ", motorAngles[1][0]
    	time.sleep(0.1)

    print("Destination reached")

shaft_length = 13.6

def turn(angle):
    angle /= 2
    circumference = shaft_length * math.pi
    turn_size = circumference * angle / 360
    const_multip = 0.723
    turn_size *= const_multip
    interface.increaseMotorAngleReferences(motors,[turn_size, -turn_size])
    
    while not interface.motorAngleReferencesReached(motors) :
    	motorAngles = interface.getMotorAngles(motors)
    	if motorAngles :
    		print "Motor angles: ", motorAngles[0][0], ", ", motorAngles[1][0]
    	time.sleep(0.1)

    print("Turn DONE")



    
#go_straigth(900)
turn(360*3)
#turn(90)
#turn(90)
#turn(90)

interface.terminate()

