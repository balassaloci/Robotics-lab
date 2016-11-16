import particleData as pd
import robolib
import helperFunctions as f
import time

r = robolib.robolib()

while True:
    k = r.readUltrasound();
    print("measurement: %s" % str(k));

    time.sleep(0.05)

