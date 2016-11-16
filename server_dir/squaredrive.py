import robolib

robot = robolib.robolib()

def do_square():
    for _ in range(4):
        robot.straight(40)
        robot.turn(90)

do_square()
print("Done with the square")
