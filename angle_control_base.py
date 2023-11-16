#! /usr/bin/env python
# -*- encoding: UTF-8 -*-

"""Example: Use setAngles Method"""

import qi
import argparse
import sys
import time
import almath
import json
from naoqi import ALProxy

def main(session):
    """
    This example uses the setAngles method and setStiffnesses method
    in order to control joints.
    """
    prev = 0
    # Get the service ALMotion.
    motionProxy  = ALProxy("ALMotion","172.20.4.100" , 9559)
    postureProxy = ALProxy("ALRobotPosture", "172.20.4.100", 9559)
    motionProxy.wakeUp()
    while(True):
        with open('lshoulder.json', 'r') as json_file:
            data = json.load(json_file)
        if(data["left_shoulder"] != None):

            motion_service  = session.service("ALMotion")

            motion_service.setStiffnesses("LArm", 1.0)

            # Simple command for the HeadYaw joint at 10% max speed
            names            = "LElbowRoll"
            angles           = -(data["left_shoulder"])
            fractionMaxSpeed = 0.1
            motion_service.setAngles(names,angles,fractionMaxSpeed)
            prev = data["left_shoulder"]
            time.sleep(1)
            # motion_service.setStiffnesses("LArm", 0.0)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="172.20.4.100",
                        help="Robot IP address. On robot or Local Naoqi: use '127.0.0.1'.")
    parser.add_argument("--port", type=int, default=9559,
                        help="Naoqi port number")

    args = parser.parse_args()
    session = qi.Session()
    try:
        session.connect("tcp://" + args.ip + ":" + str(args.port))
    except RuntimeError:
        print ("Can't connect to Naoqi at ip \"" + args.ip + "\" on port " + str(args.port) +".\n"
               "Please check your script arguments. Run with -h option for help.")
        sys.exit(1)
    main(session)