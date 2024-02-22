#change ip here
from naoqi import ALProxy
import sys
import time

robotIP = str(sys.argv[1])
# robotIP = "192.168.8.160"

tts = ALProxy("ALTextToSpeech", robotIP, 9559)
while True:
    with open("speak_now.txt") as file: 
        data = file.read()
    open('manual_ans.txt', 'w').close()
    tts.say(data)
    time.sleep(1)
