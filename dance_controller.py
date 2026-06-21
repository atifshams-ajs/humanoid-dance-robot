from controller import Robot

# Create the robot instance
robot = Robot()
timestep = int(robot.getBasicTimeStep())

# Helper function to get a motor by name and set default velocity
def get_motor(name):
    motor = robot.getDevice(name)
    motor.setVelocity(0.8)
    return motor

# Initialize all motors we need for the dance
RShoulderPitch = get_motor("RShoulderPitch")
LShoulderPitch = get_motor("LShoulderPitch")
RShoulderRoll  = get_motor("RShoulderRoll")
LShoulderRoll  = get_motor("LShoulderRoll")
RElbowRoll     = get_motor("RElbowRoll")
LElbowRoll     = get_motor("LElbowRoll")
HeadPitch      = get_motor("HeadPitch")
HeadYaw        = get_motor("HeadYaw")

# Wait function to pause between movements
def wait(duration_ms):
    steps = duration_ms // timestep
    for _ in range(steps):
        robot.step(timestep)

# Movement 1: Bow
# The robot lowers its head and brings both arms down as a greeting
def bow():
    print("Movement 1: Bow")
    HeadPitch.setPosition(0.4)
    RShoulderPitch.setPosition(1.5)
    LShoulderPitch.setPosition(1.5)
    RElbowRoll.setPosition(0.5)
    LElbowRoll.setPosition(-0.5)
    wait(1500)
    # Return to neutral position
    HeadPitch.setPosition(0.0)
    RShoulderPitch.setPosition(0.0)
    LShoulderPitch.setPosition(0.0)
    RElbowRoll.setPosition(0.0)
    LElbowRoll.setPosition(0.0)
    wait(800)

# Movement 2: Wave
# The robot raises its right arm and waves side to side
# while turning its head to follow the motion
def wave():
    print("Movement 2: Wave")
    for i in range(3):
        RShoulderPitch.setPosition(-1.0)
        RShoulderRoll.setPosition(-0.5)
        RElbowRoll.setPosition(0.3)
        HeadYaw.setPosition(0.3)
        wait(500)
        RShoulderPitch.setPosition(-1.0)
        RShoulderRoll.setPosition(-1.0)
        RElbowRoll.setPosition(0.8)
        HeadYaw.setPosition(-0.3)
        wait(500)
    # Return to neutral position
    RShoulderPitch.setPosition(0.0)
    RShoulderRoll.setPosition(0.0)
    RElbowRoll.setPosition(0.0)
    HeadYaw.setPosition(0.0)
    wait(600)

# Movement 3: Clap
# Both arms move inward and outward repeatedly to simulate clapping
def clap():
    print("Movement 3: Clap")
    for i in range(4):
        RShoulderRoll.setPosition(-0.4)
        LShoulderRoll.setPosition(0.4)
        RElbowRoll.setPosition(0.3)
        LElbowRoll.setPosition(-0.3)
        wait(350)
        RShoulderRoll.setPosition(-1.3)
        LShoulderRoll.setPosition(1.3)
        RElbowRoll.setPosition(0.8)
        LElbowRoll.setPosition(-0.8)
        wait(350)

# Movement 4: Arm Raise
# Both arms are raised above the head and brought back down
def arm_raise():
    print("Movement 4: Arm Raise")
    for i in range(2):
        RShoulderPitch.setPosition(-1.5)
        LShoulderPitch.setPosition(-1.5)
        RElbowRoll.setPosition(0.5)
        LElbowRoll.setPosition(-0.5)
        wait(700)
        RShoulderPitch.setPosition(0.0)
        LShoulderPitch.setPosition(0.0)
        RElbowRoll.setPosition(0.0)
        LElbowRoll.setPosition(0.0)
        wait(700)

# Movement 5: Head Groove
# The robot moves its head left and right while
# alternating arm positions to create a rhythmic effect
def head_groove():
    print("Movement 5: Head Groove")
    for i in range(3):
        HeadYaw.setPosition(0.4)
        RShoulderRoll.setPosition(-0.8)
        LShoulderPitch.setPosition(-0.8)
        wait(500)
        HeadYaw.setPosition(-0.4)
        RShoulderRoll.setPosition(-0.3)
        LShoulderPitch.setPosition(0.0)
        wait(500)
    # Return to neutral position
    HeadYaw.setPosition(0.0)
    RShoulderRoll.setPosition(0.0)
    wait(600)

# Main dance sequence
print("=== Dance Routine Starting ===")
bow()
wave()
clap()
head_groove()
arm_raise()
clap()
bow()
print("=== Dance Routine Complete ===")

# Keep the simulation running after dance is complete
while robot.step(timestep) != -1:
    pass