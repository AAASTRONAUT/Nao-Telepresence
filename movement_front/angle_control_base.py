
import qi
import argparse
import sys
import time
import almath
import json
from naoqi import ALProxy

IP = "172.20.30.134"

def main(session):
    motionProxy  = ALProxy("ALMotion",IP , 9559)
    postureProxy = ALProxy("ALRobotPosture", IP , 9559)
    tts    = ALProxy("ALTextToSpeech", IP , 9559)
    tts.say("I'm standing up")
    postureProxy.goToPosture("StandInit", 1.0)

    motionProxy.wakeUp()
    
    while(True):
        with open('angles_front.json', 'r') as json_file:
            data = json.load(json_file)

        motion_service  = session.service("ALMotion")

        motion_service.setStiffnesses("LArm", 1.0)
        motion_service.setStiffnesses("RArm", 1.0)
        motion_service.setStiffnesses("LLeg", 1.0)
        motion_service.setStiffnesses("RLeg", 1.0)
        fractionMaxSpeed = 0.3

        names = list(data.keys())
        angles = list(data.values())

        motion_service.setAngles(names,angles,fractionMaxSpeed)
        time.sleep(1)


if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default=IP,
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