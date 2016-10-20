# Quick references

Some important specs that we have

### Front of the robot
Front is always where the two wheels and most of the electronics sit

### Motor pins
Looking at the robot from above, the
LEFT motor is: PORT A
RIGHT motor is: PORT D

### MAC of the PI
Here:
``` 80:1f:02:af:5e:1c ```
The RPI IP lookup page is [Here](https://www.doc.ic.ac.uk/~jrj07/robotics/index.cgi)


## Some interesting code we have

### Log plotter
In the 5.2 folder, we have a python file ```plot_log.py```
Usage:
```
python plot_log.py LOGNAME MOTORNO
```

# Baby Steps

## PID tuning

### P value
```Step size: 100
From 100 to 800
minPWM = 18.0```

|Motor |Error square  |Proportional |
|------|-------------:|------------:|
|0     |0.392         |700          |
|1     |0.318         |700          |

Period of Oscillation (P_u), for Motor 0 = 0.25425


LEFT MOTOR: KP = KU = 760, start = 61.1539, stop = 62.9988, cycles = 8, PU = 0.2306 seconds

New KP = 456 (0.6 * KU)
KI = 3954 (2KP/PU)
KD = 13.1 (KP*PU / 8)

RIGHT MOTOR: KP = KU = 740, start = 165.485, stop = 168.448, cycles = 13, PU = 0.2279 seconds

New KP = 444 (0.6 * KU)
KI = 3896 (2KP/PU)
KD = 12.6 (KP*PU / 8)

KI values are way too high, adjust downwards.
