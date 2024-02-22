from naoqi import ALProxy
import time
import paramiko
import os
import random

uxwords = [
    "Let me ponder that for a moment; I'm still absorbing information, so I need a little time to process.",
    "I'm in the midst of learning, so give me a second to gather my thoughts.",
    "Hmm, that's a good question. I'm still navigating through my learning journey, so I might take a bit to respond.",
    "I'm piecing together the knowledge as we speak; patience is appreciated as I figure this out.",
    "I'm still on my learning curve, so let's explore this together. Allow me a moment to think it through.",
    "Interesting point! I'm continuously learning, so I need a minute to contemplate that.",
    "I'm in the process of expanding my understanding, so let me take a moment to deliberate.",
    "As I'm still evolving in my learning, I might need a little time to reflect on your query.",
    "Bear with me; I'm assimilating new information every day, so I need some time to consider your question.",
    "I'm keen to learn more, so let me carefully think about what you've asked. Just a moment."
]

def saySomething(tts, sentence):
	tts.say(sentence)

def Recording_thread(robotIP = "192.168.11.160"):

	robot_PORT = 9559
	global tts, audio, record, aup 
	# ----------> Connect to robot <----------
	tts = ALProxy("ALTextToSpeech", robotIP, robot_PORT)
	audio = ALProxy("ALAudioDevice", robotIP, robot_PORT)
	record = ALProxy("ALAudioRecorder", robotIP, robot_PORT)
	aup = ALProxy("ALAudioPlayer", robotIP, robot_PORT)
    
	saySomething(tts, "How can I help you today?")
	print('start recording...')
	record_path = '/home/nao/record.wav'

	record.stopMicrophonesRecording()
	record.startMicrophonesRecording(record_path, 'wav', 16000, (0,0,1,0))
	start_time = time.time()
	last_audio_time = time.time()
	
	while True:
        # Check if 2 seconds have passed since the last audio
		if time.time() - last_audio_time > 1.5:
			print("Pause detected. Stopping recording.")
			break

		audio_data = audio.getFrontMicEnergy()
		if audio_data > 300: #test to set the value	
			last_audio_time = time.time()

		# time.sleep(0.1)
        
	record.stopMicrophonesRecording()
 
	print ('record over')
	ssh = paramiko.SSHClient() 
	ssh.load_host_keys(os.path.expanduser(os.path.join("~", ".ssh", "known_hosts")))
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(robotIP, username="nao", password="nao")
	sftp = ssh.open_sftp()
	sftp.get('/home/nao/record.wav', '/Users/shivansh/Desktop/Naotelepresense/speech_pipe/uploads/record.wav')
	sftp.close()
	ssh.close()
	tts = ALProxy("ALTextToSpeech", robotIP, 9559)
	line = uxwords[random.randint(0 , 9)]
	print(line)
	tts.say(line)








