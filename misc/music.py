from naoqi import ALProxy

nao_ip = "10.10.70.30"
nao_port = 9559

# Connect to the ALAudioDevice proxy
audio_device = ALProxy("ALAudioDevice", nao_ip, nao_port)

# Connect to the ALAudioPlayer proxy
audio_player = ALProxy("ALAudioPlayer", nao_ip, nao_port)

# Specify the path to the WAV file on the robot
wav_file_path = "/home/nao/music.wav"

# Play the WAV file
audio_player.playFile(wav_file_path)
# audio_player.stop(wav_file_path)
