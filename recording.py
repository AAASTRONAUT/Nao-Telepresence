

from naoqi import ALProxy
import time
import paramiko
import os


robot_IP = "172.20.4.100"
robot_PORT = 9559
global tts, audio, record, aup 
# ----------> Connect to robot <----------
tts = ALProxy("ALTextToSpeech", robot_IP, robot_PORT)
audio = ALProxy("ALAudioDevice", robot_IP, robot_PORT)
record = ALProxy("ALAudioRecorder", robot_IP, robot_PORT)
aup = ALProxy("ALAudioPlayer", robot_IP, robot_PORT)
def saySomething(tts, sentence):
	tts.say(sentence)

def Recording_thread():
	saySomething(tts, "Do you have any questions?")
	print('start recording...')
	record_path = '/home/nao/record.wav'
	record.startMicrophonesRecording(record_path, 'wav', 16000, (0,0,1,0))
	time.sleep(5)
	record.stopMicrophonesRecording()
	print ('record over')
	ssh = paramiko.SSHClient() 
	ssh.load_host_keys(os.path.expanduser(os.path.join("~", ".ssh", "known_hosts")))
	ssh.connect("172.20.4.100", username="nao", password="nao")
	sftp = ssh.open_sftp()
	sftp.get('/home/nao/record.wav', '/Users/akshayavenugopal1/3rd_Year/IOT/Project/speech_pipe/uploads/record.wav')
	sftp.close()
	ssh.close()








