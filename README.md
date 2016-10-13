# Quick references

Some important specs that we have

### Front of the robot
Front is always where the two wheels and most of the electronics sit

### Motor pins
Looking at the robot from above, the
LEFT motor is: PORT A
RIGHT motor is: PORT B

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
```Step size: 25
From 25 to 1000
minPWM = 18.0```

|Motor |Error square  |Proportional |
|------|-------------:|------------:|
|0     |0.236         |600          |
|1     |0.530         |625          |

Refining, step size: 5

