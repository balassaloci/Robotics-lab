import brickpi
import time
import os

interface=brickpi.Interface()
interface.initialize()

motors = [0,3]
speed = 1.0

interface.motorEnable(motors[0])
interface.motorEnable(motors[1])

cpid = 0.1

LEFTMOTORPARAMS = interface.MotorAngleControllerParameters()
LEFTMOTORPARAMS.maxRotationAcceleration = 6.0
LEFTMOTORPARAMS.minPWM = 18.0
LEFTMOTORPARAMS.maxRotationSpeed = 12.0
LEFTMOTORPARAMS.feedForwardGain = 255/20.0
LEFTMOTORPARAMS.pidParameters.minOutput = -255
LEFTMOTORPARAMS.pidParameters.maxOutput = 255
LEFTMOTORPARAMS.pidParameters.k_p = 456.0 * cpid
LEFTMOTORPARAMS.pidParameters.k_i = 150.0 * cpid
LEFTMOTORPARAMS.pidParameters.K_d = 40.0 * cpid

RIGHTMOTORPARAMS = interface.MotorAngleControllerParameters()
RIGHTMOTORPARAMS.maxRotationAcceleration = 6.0
RIGHTMOTORPARAMS.minPWM = 18.0
RIGHTMOTORPARAMS.maxRotationSpeed = 12.0
RIGHTMOTORPARAMS.feedForwardGain = 255/20.0
RIGHTMOTORPARAMS.pidParameters.minOutput = -255
RIGHTMOTORPARAMS.pidParameters.maxOutput = 255
RIGHTMOTORPARAMS.pidParameters.k_p = 444.0 * cpid
RIGHTMOTORPARAMS.pidParameters.k_i = 150.0 * cpid
RIGHTMOTORPARAMS.pidParameters.K_d = 40.0 * cpid




#TEST_KP = [x for x in range(300,901,100)]
TEST_KP = [100]
#TEST_KD = [i for i in range(5,201,5)]
#TEST_KI = [i for i in range(75,126,10)]
#TEST_ANGLE = [i for i in range (10,51,10)]
folder = "PID_log_" + "-".join("_".join(time.ctime().split(" ")).split(":"))
os.mkdir(folder)
angle = 20 #test rotation angle of 20 rads

interface.setMotorAngleControllerParameters(motors[0],LEFTMOTORPARAMS)
interface.setMotorAngleControllerParameters(motors[1],RIGHTMOTORPARAMS)

ratio_diff = 0.02
right_ratio = 1.00 - ratio_diff/2
left_ratio = 1.00 + ratio_diff/2

#interface.startLogging(folder + "/KP_TUNE_TEST.log")
for test_val in TEST_KP:
#	interface.startLogging("PID_log/KP_TUNE_VAL%d.log" %(test_val))
#	interface.startLogging(folder + "/KP_TUNE_%03d.log" % (test_val))
    interface.startLogging(folder + "/PID_TUNE_CONSTMULTI.log")
    #print "Now testing k_p of %03d..." %(test_val)
    #print "Now testing k_d value of %3d" %(test_val)
    interface.increaseMotorAngleReferences(motors,[60 * left_ratio,60 * right_ratio])
    time.sleep(9)
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
