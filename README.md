**NAO Speech pipe** 

**1. How to run** 

1. Make sure you have Naoqi(official package, can be installed from [here](https://www.aldebaran.com/en/support/pepper-naoqi-2-9/downloads-softwares)) setup and installed in your pc.
1. Configure the .bash\_profile file preset in your home directory.
1. Make sure your NAO robot is connected to the same network as your pc.
1. Then run the speech\_convert.sh file present in the speech\_pipe directory passing NAO’s ip address which can be accessed form pressing the button in it’s chest.
1. Your NAO robot is now ready to listen to you whenever touched on its head.
2. **General Details:** 



|<p>1\. Naoqi</p><p>This python library is provided by Aldebaran , which provides various functions to control the various sensors and actuators in the robot. </p>|
| - |
|<p>2\. Python version mismatch</p><p>Naoqi is configured for python2.7 but all the latest speech models are compatible with python3 which created a major hurdle which is solved by doing all the computationin python3 files and all the functions that involve direct interaction with the robot has to be defined in a separate python2.7 file. </p><p>python2.7 files: recording.py, touchreact\_record.py and speak\_nao.py</p><p>python3 files: Speech\_pipe.py</p>|

3. Latency: 

The current latency of the model is ~4 seconds. The latency depends on factors like internet speed, speech model and local processing capabilities of the user, out of  these three internet speed is a major factor which can increase or decrease the latency of the whose system by a factor of 2.
Various speech models were tested and out of which Google’s Gemini and Openai’s chatGPT 4 shows minimum latency.

**3. Installing Naoqi(for unix based systems):** 

1. The Naoqi package can be installed from [here](https://www.aldebaran.com/en/support/pepper-naoqi-2-9/downloads-softwares).
1. After installation of the Naoqi package, rename the folder as “pynaoqi” include the below mentioned commands into your .bash\_profile file present in the home directory.

export PYTHONPATH=${PHTHONPATH}:path/to/pynaoqi/lib/python2.7/site-packages export DYLD\_LIBRARY\_PATH=${DYLD\_LIBRARY\_PATH}:path/to/pynaoqi/lib export QI\_SDK\_PREFIX=path/to/pynaoqi

3. Now quit the terminal and run “source .bash\_profile”

**3. Description of code files inside the speech\_pipe directory** 

1. speech\_convert.sh: This script triggers the touchreact\_record.py file and monitor\_nao.sh script and looks out for any changes in the uploads folder which stores the user voice input which is later passed to chatGPT.
2. monitor\_nao.sh: This script is responsible for separately calling the Speech\_pipe.py and speak\_nao.py file.
2. touchreact\_record.py: This file checks whether the robot is touched on it’s head. As soon as the user touches the head of the robot this file calls the Recording\_thread function defined in the Recording.py file.
2. Recording.py: This file defines the Recording\_thread function which stores the users recording into the robot local home directory and then transfers the .wav audio file to the uploads folder by establishing an ssh connection.
2. Speech\_pipe.py: 
   1. Speech\_2\_txt function: This converts the audio file in to a text file by using audio transcribe provided by Openai and moves the audio file from uploads folder to the old\_file folder.
   1. model function: This function stores the response of chatGPT into ans.txt file taking the transcribed test file as input.
2. speak\_nao.py: This file simply just calls the ALTextToSpeech functionality provided by Naoqi and makes the NAO robot speak the response stored in ans.txt. 
