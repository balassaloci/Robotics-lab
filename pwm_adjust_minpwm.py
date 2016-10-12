import brickpi
import time

interface=brickpi.Interface()
interface.initialize()

motors = [1,1]
speed = 1.0

current_mot = 0

interface.motorEnable(motors[0])
#interface.motorEnable(motors[1])

motorParams = interface.MotorAngleControllerParameters()
motorParams.maxRotationAcceleration = 6.0
#motorParams.minPWM = 18.0
motorParams.maxRotationSpeed = 12.0
motorParams.feedForwardGain = 255/20.0
motorParams.pidParameters.minOutput = -255
motorParams.pidParameters.maxOutput = 255
motorParams.pidParameters.k_p = 100.0
motorParams.pidParameters.k_i = 0.0
motorParams.pidParameters.k_d = 0.0

interface.setMotorAngleControllerParameters(motors[0],motorParams)
#interface.setMotorAngleControllerParameters(motors[1],motorParams)

	
while True:
	minPWM = float(input("Enter new pwm: "))

	interface.startLogging("minPWM_M%i_%f.log" % (motors[0], minPWM))
	motorParams.minPWM = minPWM
	interface.setMotorAngleControllerParameters(motors[0],motorParams)
	interface.setMotorRotationSpeedReferences([motors[0]],[speed])

print("Commands are: f: forward\tr:reverse\ts:stop\tspin")
while True:
	r = raw_input("cmd: ")
	if r == "f":
		interface.setMotorRotationSpeedReferences(motors,[speed,speed])
	elif r == "r":
		interface.setMotorRotationSpeedReferences(motors,[-speed,-speed])
	elif r == "s":
		interface.setMotorRotationSpeedReferences(motors,[0,0])
	elif r == "spin":
		interface.setMotorRotationSpeedReferences(motors,[-6,6])
	elif r == "bspin":
		interface.setMotorRotationSpeedReferences(motors,[6,-6])
		
		
		

for x in range(6,100):
	print("speed: " + str(x))
	time.sleep(1)
	
	

interface.terminate()
