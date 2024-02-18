from naoqi import ALProxy
import time
import paramiko
import os

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
		if time.time() - last_audio_time > 2:
			print("Pause detected. Stopping recording.")
			break

		audio_data = audio.getFrontMicEnergy()
		if audio_data > 0: #test to set the value	
			last_audio_time = time.time()

		# time.sleep(0.1)
        
	record.stopMicrophonesRecording()
 
	print ('record over')
	ssh = paramiko.SSHClient() 
	ssh.load_host_keys(os.path.expanduser(os.path.join("~", ".ssh", "known_hosts")))
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(robotIP, username="nao", password="nao")
	sftp = ssh.open_sftp()
	sftp.get('/home/nao/record.wav', '/home/iotlabgpupc1/Desktop/Naotelepresense/speech_pipe/uploads/record.wav')
	sftp.close()
	ssh.close()








