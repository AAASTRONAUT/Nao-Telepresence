from naoqi import ALProxy
import sys
import time
import hashlib

def file_hash(filepath):
    """Calculate the MD5 hash of a file's contents."""
    with open(filepath, 'rb') as f:
        file_contents = f.read()
    return hashlib.md5(file_contents).hexdigest()

def main(robotIP, port=9559):
    tts = ALProxy("ALTextToSpeech", robotIP, port)
    prev_hash = None

    while True:
        current_hash = file_hash("speak_now.txt")
        if current_hash != prev_hash:
            with open("speak_now.txt") as file: 
                data = file.read()
            open('manual_ans.txt', 'w').close()
            tts.say(data)
            prev_hash = current_hash
        time.sleep(1)

if __name__ == "__main__":
    robotIP = str(sys.argv[1]) if len(sys.argv) > 1 else "192.168.8.160"
    main(robotIP)