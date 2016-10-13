import brickpi
import time
from math import pi

interface=brickpi.Interface()
interface.initialize()

motors = [1,1]
speed = 1.0

current_mot = 0

interface.motorEnable(motors[0])
interface.motorEnable(motors[1])

LEFTMOTORPARAMS = interface.MotorAngleControllerParameters()
LEFTMOTORPARAMS.maxRotationAcceleration = 6.0
LEFTMOTORPARAMS.minPWM = 18.0
LEFTMOTORPARAMS.maxRotationSpeed = 12.0
LEFTMOTORPARAMS.feedForwardGain = 255/20.0
LEFTMOTORPARAMS.pidParameters.minOutput = -255
LEFTMOTORPARAMS.pidParameters.maxOutput = 255
LEFTMOTORPARAMS.pidParameters.k_p = 100.0
LEFTMOTORPARAMS.pidParameters.k_i = 0.0
LEFTMOTORPARAMS.pidParameters.k_d = 0.0

RIGHTMOTORPARAMS = interface.MotorAngleControllerParameters()
RIGHTMOTORPARAMS.maxRotationAcceleration = 6.0
RIGHTMOTORPARAMS.minPWM = 18.0
RIGHTMOTORPARAMS.maxRotationSpeed = 12.0
RIGHTMOTORPARAMS.feedForwardGain = 255/20.0
RIGHTMOTORPARAMS.pidParameters.minOutput = -255
RIGHTMOTORPARAMS.pidParameters.maxOutput = 255
RIGHTMOTORPARAMS.pidParameters.k_p = 100.0
RIGHTMOTORPARAMS.pidParameters.k_i = 0.0
RIGHTMOTORPARAMS.pidParameters.k_d = 0.0



TEST_KP = [i for i in range(25,1001,25)]


	
for test_val in TEST_KP:

	interface.startLogging("KP_TUNE_VAL_%d.log" % (test_val))
	
	print "Now testing k_p value of %d" %(test_val)

	LEFTMOTORPARAMS.pidParameters.k_p = test_val
	RIGHTMOTORPARAMS.pidParameters.k_p = test_val
	interface.setMotorAngleControllerParameters(motors[0],LEFTMOTORPARAMS)
	interface.setMotorAngleControllerParameters(motors[1],RIGHTMOTORPARAMS)

	angle = 20 #test rotation angle of 20 rads
	
	interface.increaseMotorAngleReferences(motors,[angle,angle])

	interface.stopLogging()

interface.terminate()
