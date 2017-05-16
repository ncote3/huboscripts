from Maestor import maestor

robot = maestor()


def main():
    robotRightArmMove()
    

def robotRightArmMove():
    robot.setProperties("RSR REP", "position position", "-1.38 -1.45")
    robot.waitForJoint("RSR")
    robot.waitForJoint("REP")
    for i in range(0, 3):
        robot.setProperties("RSY", "position", "0")
        robot.waitForJoint("RSY")
        robot.setProperties("RSY", "position", "2.50")
        robot.waitForJoint("RSY")
    robot.setProperties("RSR, REP, RSY", "position position position", "0 0 0")
    robot.waitForJoint("RSR")
    robot.waitForJoint("RSY")
    robot.waitForJoint("REP")


if  __name__ == '__main__':
    main()

