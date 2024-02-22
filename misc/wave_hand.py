from naoqi import ALProxy

# Set the IP address and port number of the robot
nao_ip = "10.10.70.30"
nao_port = 9559

# Connect to the motion proxy
motion_proxy = ALProxy("ALMotion", nao_ip, nao_port)

# Connect to the posture proxy
posture_proxy = ALProxy("ALRobotPosture", nao_ip, nao_port)

# Wake up the robot
motion_proxy.wakeUp()

# Go to the stand posture
posture_proxy.goToPosture("Stand", 0.5)

# Define the joint names for the wave motion including the wrist
joint_names = ["RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw"]

# Move the arm to the initial waving position
initial_angles = [0.0, -0.3, 1.5, 1.0, 0.0] # Angles are in radians, last for RWristYaw
motion_proxy.angleInterpolation(joint_names, initial_angles, [1.0]*5, True)

# Perform the waving motion
for _ in range(3):  # Repeat the wave 3 times
    # Elbow up (wave up) and open wrist
    angles_up = [0.0, -0.3, 1.5, 1.4, 1.0] # Adjust the last two values for elbow roll and wrist yaw
    motion_proxy.angleInterpolation(joint_names, angles_up, [0.5]*5, True)
    
    # Elbow down (wave down) and reset wrist
    angles_down = [0.0, -0.3, 1.5, 1.0, 0.0] # Adjust the last two values for elbow roll and wrist yaw
    motion_proxy.angleInterpolation(joint_names, angles_down, [0.5]*5, True)

# Return the arm to the initial position
motion_proxy.angleInterpolation(joint_names, initial_angles, [1.0]*5, True)

# Put the robot back into a resting position
posture_proxy.goToPosture("Stand", 0.5)

