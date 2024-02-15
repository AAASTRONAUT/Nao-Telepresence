#change ip here
from naoqi import ALProxy
import sys

robotIP = str(sys.argv[1])
# robotIP = "192.168.8.160"

tts = ALProxy("ALTextToSpeech", robotIP, 9559)
with open("ans.txt") as file: 
    data = file.read()
open('ans.txt', 'w').close()
tts.say(data)
