#for mic test specifically on a raspberry pi, which has a button activated record. If using another system, comment out the mic_test.py line.
#nohup python3 mic_test.py
while true; do
#Checks directory iteratively for file. If anything new, then starts calling python code for whisper and ChatGPT.
    if inotifywait -e create "/home/sensorlab/Desktop/project/uploads"; then
        echo "A new file appeared!"
        python3 Speech_pipe.py
        #for making nao speak
        python speak_nao.py
    fi
done