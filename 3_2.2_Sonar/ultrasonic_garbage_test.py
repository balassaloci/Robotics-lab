import brickpi
import time

interface=brickpi.Interface()
interface.initialize()

port = 2 # port which ultrasoic sensor is plugged in to

interface.sensorEnable(port, brickpi.SensorType.SENSOR_ULTRASONIC);

i = 0

with open('sensor_values.csv','a') as f:

	while i in range (0,1000):
		usReading = interface.getSensorValue(port)

		if usReading :
			print usReading[0]
			f.write(str(usReading[0]) + ',')
		else:
			print '0'
			f.write('0,')
		i+=1
		time.sleep(0.05)

interface.terminate()
