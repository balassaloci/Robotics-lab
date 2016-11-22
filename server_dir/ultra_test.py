import time
import robolib

r = robolib.robolib()

def read():
    t = time.time()
    k = r.readUltrasound()
    t = time.time() - t

    print("%f\t\t%f" % (t, k))
    return t


r.turn_poll(0)
