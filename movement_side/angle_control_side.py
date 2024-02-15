#! /usr/bin/env python
# -*- encoding: UTF-8 -*-


import qi
import sys
import time
import json
from naoqi import ALProxy

def main(session):
    # Get the service ALMotion.
    motionProxy  = ALProxy("ALMotion","172.20.4.100" , 9559)
    postureProxy = ALProxy("ALRobotPosture", "172.20.4.100", 9559)
    tts    = ALProxy("ALTextToSpeech", "172.20.4.100", 9559)
    tts.say("I'm standing up")
    postureProxy.goToPosture("StandInit", 1.0)

    motionProxy.wakeUp()
    while(True):
        with open('angles_side.json', 'r') as json_file:
            data = json.load(json_file)

        motion_service  = session.service("ALMotion")

        motion_service.setStiffnesses("LArm", 1.0)
        motion_service.setStiffnesses("RArm", 1.0)
        motion_service.setStiffnesses("LLeg", 1.0)
        motion_service.setStiffnesses("RLeg", 1.0)
        fractionMaxSpeed = 0.1

        names = list(data.keys())
        angles = list(data.values())

        motion_service.setAngles(names,angles,fractionMaxSpeed)
        time.sleep(1)


if __name__ == "__main__":
    session = qi.Session()
    try:
        session.connect("tcp://" + "172.20.4.100"+ ":" + "9559")
    except RuntimeError:
        print ("Can't connect to Naoqi at ip \"" + "172.20.4.100" + "\" on port " + "9559" +".\n"
               "Please check your script arguments. Run with -h option for help.")
        sys.exit(1)
    main(session)
