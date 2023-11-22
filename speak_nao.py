from naoqi import ALProxy
tts = ALProxy("ALTextToSpeech", "172.20.4.100", 9559)
with open("ans.txt") as file: 
    data = file.read()
open('ans.txt', 'w').close()
tts.say(data)