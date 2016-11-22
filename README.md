# LOG EVERYTHING YOU DO HERE

14th Nov - Piotr, Loci - Edited inital particleDataStructures.py to begin implementing likelihoods

15th Nov - Piotr, Bing, Ravi - Finished Lab 3 ex 2 & ex 3 **in particleData.py**. Video https://www.youtube.com/watch?v=xzzpS3yD7CY&feature=youtu.be

16th Nov - Piotr, Bing, Ravi, Loci
+ Assessed lab 3 (full marks :neckbeard: :bowtie:).
+ Cleaned up server_dir - new file names, old code in old_server_dir [Ravi]
+ Wrote sonar turn function (done), and absolute sonar turn function (needs calibration) in server_dir/robolib.py [Ravi]
+ Wrote initial plan for signatures in server_dir/createLocationSignatures.py [Ravi] 
+ Added 360 degree sonar motor [Piotr]

18th Nov - Piotr, Bing
+ Made motor spin by 360 degrees, in increments of 10 degrees, and create signature of sonar scans from it
+ Created code to store location signature in .dat file

--------------------------------------------

## TODOs
- [X] Tune angle turning on carpet
- [X] Tune distance moving on carpet
- [X] Write sonar turn function in robolib.py 
- [X] Added timer for motor movement, to speed up movement  
- [X] Add turnable sonar sensor
- [X] Write function to create a location signature (characterize_location) in createLocationSignatures.py
- [X] Write function to compare two signatures (compare_signatures) in createLocationSignatures.py
- [ ] Tune **small** angle (roughly 10 degrees) tuning on carpet


--------------------------------------------

## MAC of the PI
Here:

> 80:1f:02:af:5e:1c 

The RPI IP lookup page is [Here](https://www.doc.ic.ac.uk/~jrj07/robotics/index.cgi)















<!---
# Quick references

Some important specs that we have

### Front of the robot
Front is always where the two wheels and most of the electronics sit

### Motor pins
Looking at the robot from above, the
LEFT motor is: PORT A
RIGHT motor is: PORT D



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

### 5.4 Drive in a square
|Measurement|X      |Y      |
|-----------|-------|-------|
|1          |-0.4   |-0.8   |
|2          |-0.4   |-0.8   |
|3          |0.6    |0.55   |
|4          |0.6    |0.30   |
|5          |0.6    |0.00   |
|6          |0.6    |0.00   |
|7          |0.6    |-0.35  |
|8          |0.3    |0.00   |
|9          |0.9    |0.00   |
|10         |0.45   |-0.25  |

Based on these measurements, we have calculated the following covariance matrix. For the method of calculations, please see ```Lab1_5_4_Cov_Matrix.ods```


![alt text](https://github.com/balassaloci/Robotics-lab/raw/master/images/5_4_cov_matrix.png "Covariance matrix")
-->


