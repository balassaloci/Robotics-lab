import brickpi
import time

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
wheel_circum = 5.5 * 3.14

def go_straigth(distance):
    angle = 6.28 * distance/wheel_circum
    
    interface.increaseMotorAngleReferences(motors,[angle,angle])
    
    while not interface.motorAngleReferencesReached(motors) :
    	motorAngles = interface.getMotorAngles(motors)
    	if motorAngles :
    		print "Motor angles: ", motorAngles[0][0], ", ", motorAngles[1][0]
    	time.sleep(0.1)

    print("Destination reached")

def turn_degree(radians):
    


interface.terminate()

