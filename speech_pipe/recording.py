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
 
	record.startMicrophonesRecording(record_path, 'wav', 16000, (0,0,1,0))
	time.sleep(2)
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








