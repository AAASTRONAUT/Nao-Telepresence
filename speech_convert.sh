#!/bin/bash
nohup python touchreact_record.py &

# Ensure monitor_nao.sh is executable
chmod u+x monitor_nao.sh

while true; do
    fswatch -o /Users/akshayavenugopal1/3rd_Year/IOT/Project/speech_pipe/uploads | xargs -n1 -I{} /Users/akshayavenugopal1/3rd_Year/IOT/Project/speech_pipe/monitor_nao.sh
done
