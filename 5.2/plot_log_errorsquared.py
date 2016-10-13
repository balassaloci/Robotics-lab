import numpy as np
import matplotlib.pyplot as plt
import sys
import os


if len(sys.argv) < 3:
    print("USAGE: plot_log.py FOLDERNAME MOTORID")
    quit()

foldername = sys.argv[1]
motorid = int(sys.argv[2])

error_dict = {}
for filename in os.listdir(foldername):
    data = np.loadtxt(foldername + "/" + filename)
    x = data[:,0]
    mot0ref = data[:,1 + 2 * motorid]
    mot0angle = data[:, 2 + 2 * motorid]
    error_sq = sum([(i-j)**2 for i,j in zip(mot0ref,mot0angle)])
    error_dict[error_sq] = filename
    #x = np.linspace(0, 10)

for k in sorted(error_dict):
    print k,error_dict[k]

#plt.plot(x, diffangle, label='Difference angle')
#plt.legend()

#plt.title(filename + " motor " + str(motorid))


#plt.show()
