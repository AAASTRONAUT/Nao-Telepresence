#!/bin/bash

my_string="172.17.100.236"

if [ "$#" -eq 1 ]; then
    my_string="$1"
fi

# Start python2 script with the string as an argument
nohup python2 touchreact_record.py "$my_string" &

# Ensure monitor_nao.sh is executable
chmod u+x monitor_nao.sh "$my_string"

while true; do
    # Pass the string as an argument to monitor_nao.sh
    fswatch -o /Users/shivansh/Desktop/Naotelepresense/speech_pipe/uploads | xargs -n1 -I{} /Users/shivansh/Desktop/Naotelepresense/speech_pipe/monitor_nao.sh "$my_string"
done
