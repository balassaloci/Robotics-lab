import numpy as np
import matplotlib.pyplot as plt
import sys


if len(sys.argv) < 3:
    print("USAGE: plot_log.py LOGNAME MOTORID")
    quit()

filename = sys.argv[1]
motorid = int(sys.argv[2])

data = np.loadtxt(filename)
x = data[:,0]
leftref = data[:,1]
leftangle = data[:,2]
rightref = data[:,3]
rightangle = data[:,4]

#Zero all data
x = [i-x[0] for i in x]
leftref = [i-leftref[0] for i in leftref]
leftangle = [i-leftangle[0] for i in leftangle]
rightref = [i-rightref[0] for i in rightref]
rightangle = [i-rightangle[0] for i in rightangle]


plt.plot(x, leftref, label='left ref angle')
plt.plot(x, leftangle, label='left actual angle')

plt.plot(x, rightref, label='right ref angle')
plt.plot(x, rightangle, label='right actual angle')

plt.legend()

plt.title(filename)


plt.show()
