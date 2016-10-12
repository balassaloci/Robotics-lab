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
mot0ref = data[:,1 + 2 * motorid]
mot0angle = data[:, 2 + 2 * motorid]

#x = np.linspace(0, 10)
plt.plot(x, mot0ref, label='Reference angle')
plt.plot(x, mot0angle, label='Actual angle')
plt.legend()

plt.title(filename + " motor " + str(motorid))


plt.show()
