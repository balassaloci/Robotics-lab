import numpy as np
import matplotlib.pyplot as plt
import sys

#plt.hold(False)

if len(sys.argv) < 3:
    print("USAGE: plot_log.py LOGNAME MOTORID")
    quit()

filename = sys.argv[1]
motorid = int(sys.argv[2])

data = np.loadtxt(filename)
x = data[:,0]
x = [i-x[0] for i in x]

leftref = data[:,1]
leftangle = data[:,2]
diffleftangle = leftref - leftangle
rightref = data[:,3]
rightangle = data[:,4]
diffrightangle = rightref - rightangle

plt.plot(x, diffleftangle, label='Difference angle_left')
plt.plot(x, diffrightangle, label='Difference angle_right')
plt.legend()

plt.title(filename)


plt.show()
