import brickpi
import time
import os

interface=brickpi.Interface()
interface.initialize()

motors = [0,3]
speed = 1.0

interface.motorEnable(motors[0])
interface.motorEnable(motors[1])

LEFTMOTORPARAMS = interface.MotorAngleControllerParameters()
LEFTMOTORPARAMS.maxRotationAcceleration = 6.0
LEFTMOTORPARAMS.minPWM = 18.0
LEFTMOTORPARAMS.maxRotationSpeed = 12.0
LEFTMOTORPARAMS.feedForwardGain = 255/20.0
LEFTMOTORPARAMS.pidParameters.minOutput = -255
LEFTMOTORPARAMS.pidParameters.maxOutput = 255
LEFTMOTORPARAMS.pidParameters.k_p = 456.0
LEFTMOTORPARAMS.pidParameters.k_i = 250.0
LEFTMOTORPARAMS.pidParameters.k_d = 60.0

RIGHTMOTORPARAMS = interface.MotorAngleControllerParameters()
RIGHTMOTORPARAMS.maxRotationAcceleration = 6.0
RIGHTMOTORPARAMS.minPWM = 18.0
RIGHTMOTORPARAMS.maxRotationSpeed = 12.0
RIGHTMOTORPARAMS.feedForwardGain = 255/20.0
RIGHTMOTORPARAMS.pidParameters.minOutput = -255
RIGHTMOTORPARAMS.pidParameters.maxOutput = 255
RIGHTMOTORPARAMS.pidParameters.k_p = 444.0
RIGHTMOTORPARAMS.pidParameters.k_i = 100.0
RIGHTMOTORPARAMS.pidParameters.k_d = 60.0


TEST_KP = [516,516,516,516,516,546,546,546,546,546]
#TEST_KD = [i for i in range(5,201,5)]
#TEST_KI = [i for i in range(75,126,10)]
#TEST_ANGLE = [i for i in range (10,51,10)]
folder = "PID_log_" + "-".join("_".join(time.ctime().split(" ")).split(":"))
os.mkdir(folder)
angle = 20 #test rotation angle of 20 rads

interface.setMotorAngleControllerParameters(motors[0],LEFTMOTORPARAMS)
interface.setMotorAngleControllerParameters(motors[1],RIGHTMOTORPARAMS)

#interface.startLogging(folder + "/KP_TUNE_TEST.log")
for test_val in TEST_KP:
	#interface.startLogging("PID_log/KP_800_KD_TUNE_VAL%d.log" %(test_val))
	interface.startLogging(folder + "/KP_TUNE_%03d.log" % (test_val))
	
	print "Now testing k_p of %03d..." %(test_val)
	#print "Now testing k_d value of %3d" %(test_val)
	LEFTMOTORPARAMS.pidParameters.k_p = test_val
	interface.increaseMotorAngleReferences(motors,[60,60])

	time.sleep(5)	

	interface.stopLogging()
	temp = raw_input('press any key to continue')

	#interface.increaseMotorAngleReferences([motors[0]],[0])
#interface.stopLogging()
#for test_val in TEST_KP:
#	interface.startLogging(folder + "/KP_TUNE_RIGHT_VAL_%03d.log" % (test_val))
	#interface.startLogging("PID_log/KP_800_KD_TUNE_VAL%d.log" %(test_val))
#	print "Now testing k_p value of %03d for the right motor" %(test_val)
	#RIGHTMOTORPARAMS.pidParameters.k_p = test_val
#	interface.setMotorAngleControllerParameters(motors[1],RIGHTMOTORPARAMS)
#	angle = 20 #test rotation angle of 20 rads
#	interface.increaseMotorAngleReferences([motors[1]],[angle])

#	time.sleep(7)

#	interface.stopLogging()
	#interface.increaseMotorAngleReferences([motors[1]],[0])

interface.terminate()
