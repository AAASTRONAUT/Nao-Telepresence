import argparse
import motion
import time
import socket
import almath
from naoqi import ALProxy
import random

def computePath(proxy, effector, frame):
    dx      = 0.05                 # translation axis X (meters)
    dz      = 0.025               # translation axis Z (meters)
    dwy     = 7.0*almath.TO_RAD    # rotation axis Y (radian)

    useSensorValues = False

    path = []
    currentTf = []
    try:
        currentTf = proxy.getTransform(effector, frame, useSensorValues)
    except Exception, errorMsg:
        print str(errorMsg)
        print "This example is not allowed on this robot."
        exit()

    # 1
    targetTf  = almath.Transform(currentTf)
    targetTf *= almath.Transform(0.0, 0.0, dz)
    targetTf *= almath.Transform().fromRotY(dwy)
    path.append(list(targetTf.toVector()))

    # 2
    targetTf  = almath.Transform(currentTf)
    targetTf *= almath.Transform(0.1, 0.0, dz)
    path.append(list(targetTf.toVector()))

    # 3
    path.append(currentTf)

    return path

def dance():
    motionProxy  = ALProxy("ALMotion", "10.10.70.30", 9559)
    postureProxy = ALProxy("ALRobotPosture", "10.10.70.30", 9559)
    
    # end initialize proxy, begin go to Stand Init

    # Wake up robot
    motionProxy.wakeUp()
        
    # Send robot to Stand Init
    postureProxy.goToPosture("StandInit", 0.5)  
    tts    = ALProxy("ALTextToSpeech", "10.10.70.30", 9559)
    tts.say("Goal!")
    # end go to Stand Init, begin define control point
    effector        = "Torso"
    frame           =  motion.FRAME_ROBOT
    axisMask        = almath.AXIS_MASK_ALL
    isAbsolute      = True
    useSensorValues = False

    currentTf = almath.Transform(motionProxy.getTransform(effector, frame, useSensorValues))

    # end define control point, begin define target

    # Define the changes relative to the current position
    dx         = 0.03                    # translation axis X (meter)
    dy         = 0.03                    # translation axis Y (meter)
    dwx        = 8.0*almath.TO_RAD       # rotation axis X (rad)
    dwy        = 8.0*almath.TO_RAD       # rotation axis Y (rad)

    # point 01 : forward  / bend backward
    target1Tf = almath.Transform(currentTf.r1_c4, currentTf.r2_c4, currentTf.r3_c4)
    target1Tf *= almath.Transform(dx, 0.0, 0.0)
    target1Tf *= almath.Transform().fromRotY(-dwy)

    # point 02 : right    / bend left
    target2Tf = almath.Transform(currentTf.r1_c4, currentTf.r2_c4, currentTf.r3_c4)
    target2Tf *= almath.Transform(0.0, -dy, 0.0)
    target2Tf *= almath.Transform().fromRotX(-dwx)

    # point 03 : backward / bend forward
    target3Tf = almath.Transform(currentTf.r1_c4, currentTf.r2_c4, currentTf.r3_c4)
    target3Tf *= almath.Transform(-dx, 0.0, 0.0)
    target3Tf *= almath.Transform().fromRotY(dwy)

    # point 04 : left     / bend right
    target4Tf = almath.Transform(currentTf.r1_c4, currentTf.r2_c4, currentTf.r3_c4)
    target4Tf *= almath.Transform(0.0, dy, 0.0)
    target4Tf *= almath.Transform().fromRotX(dwx)

    path = []
    path.append(list(target1Tf.toVector()))
    path.append(list(target2Tf.toVector()))
    path.append(list(target3Tf.toVector()))
    path.append(list(target4Tf.toVector()))

    path.append(list(target1Tf.toVector()))
    path.append(list(target2Tf.toVector()))
    path.append(list(target3Tf.toVector()))
    path.append(list(target4Tf.toVector()))

    path.append(list(target1Tf.toVector()))
    path.append(list(currentTf.toVector()))

    timeOneMove  = 0.5 #seconds
    times = []
    for i in range(len(path)):
        times.append((i+1)*timeOneMove)

    # end define target, begin call motion api

    # call the cartesian control API

    motionProxy.transformInterpolations(effector, frame, path, axisMask, times)

def kick():
    motionProxy  = ALProxy("ALMotion", "192.168.179.160", 9559)
    postureProxy = ALProxy("ALRobotPosture", "192.168.179.160", 9559)
    tts    = ALProxy("ALTextToSpeech", "192.168.179.160", 9559)
    tts.say("I'm Kicking the Ball.")
    # Wake up robot
    motionProxy.wakeUp()

    # # Send robot to Stand Init
    postureProxy.goToPosture("StandInit", 0.5)

    # # # Activate Whole Body Balancer
    isEnabled  = True
    motionProxy.wbEnable(isEnabled)

    # Legs are constrained fixed
    stateName  = "Fixed"
    supportLeg = "Legs"
    motionProxy.wbFootState(stateName, supportLeg)

    # Constraint Balance Motion
    isEnable   = True
    supportLeg = "Legs"
    motionProxy.wbEnableBalanceConstraint(isEnable, supportLeg)

    # Com go to LLeg
    supportLeg = "LLeg"
    duration   = 2.0
    motionProxy.wbGoToBalance(supportLeg, duration)

    # RLeg is free
    stateName  = "Free"
    supportLeg = "RLeg"
    motionProxy.wbFootState(stateName, supportLeg)

    # RLeg is optimized
    effector = "RLeg"
    axisMask = 63
    frame    = motion.FRAME_WORLD

    # Motion of the RLeg
    times   = [0.75, 1.5, 2.0]

    path = computePath(motionProxy, effector, frame)

    motionProxy.transformInterpolations(effector, frame, path, axisMask, times)
    
    # Example showing how to Enable Effector Control as an Optimization

    isActive     = False
    motionProxy.wbEnableEffectorOptimization(effector, isActive)
    
    stateName  = "Fixed"
    supportLeg = "Legs"
    motionProxy.wbFootState(stateName, supportLeg)
    
    # Deactivate Head tracking
    isEnabled = False
    motionProxy.wbEnable(isEnabled)

    # send robot to Pose Init
    postureProxy.goToPosture("StandInit", 0.3)

    # Go to rest position
    # motionProxy.rest()
def speak():
    tts = ALProxy("ALTextToSpeech", "10.10.70.30", 9559)
    tts.say("Bye Im going")

def moveforward():
    motion = ALProxy("ALMotion", "192.168.179.160", 9559)
    motion.setStiffnesses("Body", 1.0)
    tts    = ALProxy("ALTextToSpeech", "10.10.70.30", 9559)
    # motion.moveInit()
    motion.post.moveTo(0.60, 0, 0)
    tts.say("Moving Forward")


def rotateleft():
    motion = ALProxy("ALMotion", "10.10.70.30", 9559)
    motion.setStiffnesses("Body", 1.0)
    tts    = ALProxy("ALTextToSpeech", "10.10.70.30", 9559)
    motion.moveInit()
    motion.post.moveTo(0, 0,1.5)
    tts.say("Turning Left")


def rotateright():
    motion = ALProxy("ALMotion", "10.10.70.30", 9559)
    motion.setStiffnesses("Body", 1.0)
    tts    = ALProxy("ALTextToSpeech", "10.10.70.30", 9559)
    motion.moveInit()
    motion.post.moveTo(0, 0,-1.5)
    tts.say("Turning Right")

def movebackward():
    motion = ALProxy("ALMotion", "192.168.179.160", 9559)
    motion.setStiffnesses("Body", 1.0)
    tts    = ALProxy("ALTextToSpeech", "192.168.179.160", 9559)
    motion.moveInit()
    motion.post.moveTo(-0.6, 0, 0)
    tts.say("Moving Backward")

def standup():
    postureProxy = ALProxy("ALRobotPosture", "10.10.70.30", 9559)
    tts    = ALProxy("ALTextToSpeech", "10.10.70.30", 9559)
    tts.say("I'm standing up")
    postureProxy.goToPosture("StandInit", 1.0)

def sitdown():
    postureProxy = ALProxy("ALRobotPosture", "10.10.70.30", 9559)
    tts    = ALProxy("ALTextToSpeech", "10.10.70.30", 9559)
    tts.say("I'm Done.")
    postureProxy.goToPosture("Sit", 1.0)

'''
def lie_down():
    postureProxy = ALProxy("ALRobotPosture", "10.10.70.30", 9559)
    tts    = ALProxy("ALTextToSpeech", "10.10.70.30", 9559)
    tts.say("I'm lying down")
    postureProxy.goToPosture("LyingBelly", 1.0)
    postureProxy.goToPosture("StandInit", 1.0)



def dark_detect():
    dark = ALProxy("ALDarknessDetection","10.10.70.30",9559)
    print(dark.getDarknessThreshold())
'''

def lets_start():
    lastarg = -1
    serverSock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    serverSock.bind(("10.10.70.30",9559))
    while(1):
        data,addr = serverSock.recvfrom(1024)
        command = data.decode("utf-8");
        argument = int(command);
        if(lastarg != argument):
            lastarg = argument;
            print(argument)
            if(argument==1):
                 moveforward()
            elif(argument==2):
                dance()
            elif(argument==3):
                rotateleft()
            elif(argument==4):
                kick()
            elif(argument==5):
                rotateright()
            elif(argument==6):
                sitdown()
            elif(argument==7):
                movebackward()
            elif(argument==8):
                standup()
    #toggle_between_commands(int(argument))

    

# Driver program 
if __name__ == "__main__": 
    standup()
    dance()
    # standup()
    # sitdown()
    # kick()