import robolib

robot = robolib.robolib()

def instruct():
    print("Commands: \tf: Forward\tb: Backward\tr: Right Turn\tl: LeftTurn")

instruct()

while True:
    inp = input("Command: ")

    if inp == "f":
        robot.straight(40)
    elif inp == "b":
        robot.straight(-40)
    elif inp == "r":
        robot.turn(90)
    elif inp == "l":
        robot.turn(-90)
    else:
        print("Couldn't parse command!")
        instruct()

