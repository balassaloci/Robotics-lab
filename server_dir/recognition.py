import robolib as rb
import createLocationSignatures as ls
import time

#print sum([float(bot.readUltrasound()) for i in range(10)])/10.0
#bot.turn(90)

#rint time.localtime(time.time())

#bot.turn_sonar(360)

#ls.learn_location()

#ls.recognize_location()

depth_map = ls.bot.turn_poll(3)

for pair in depth_map:
    print "angle: %3.2f, depth %3.1f" % (pair[0],pair[1])