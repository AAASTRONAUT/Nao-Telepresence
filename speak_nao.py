from naoqi import ALProxy
tts = ALProxy("ALTextToSpeech", "172.20.4.104", 9559)
with open("and.txt") as file: 
    data = file.read()
tts.say(data)