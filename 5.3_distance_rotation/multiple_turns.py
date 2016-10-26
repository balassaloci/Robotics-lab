import robolib


robot = robolib.robolib()
#robot.straight(40)

def Left90deg():
    robot.turn(-90)

def Right90deg():
    robot.turn(90)


while True:
    robot.straight(40)
    Left90deg()
    Right90deg()
    robot.straight(-40)


