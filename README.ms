# INTERNET OF THINGS



## Group 3: Telepresence System using NAO humanoid



### Submitted on: 27th November 2023



**Team Members:**

- Govind Tuli, ID No. 2021A3PS0130P

- Akshaya Venugopal, ID No. 2021AAPS0022P

- Shivansh Jain, ID No. 2021AAPS1634P

- Simran Moorjani, ID No. 2021A8PS2697P



## Table of Contents



1. [Introduction](#introduction)

2. [Methodology](#methodology)

   - 2.1. General Details

     - Voice Interaction

     - Motion through Telepresence

     - Video Streaming

   - 2.2. Technical Details

     - Voice Interaction Details

     - Motion through Telepresence Details

     - Video Streaming Details

3. [Results and Discussion](#results-and-discussion)

4. [References](#references)



## Introduction



The intersection of robotics and human-computer interaction has paved the path for several advances in the field of telepresence technology in recent years. Telepresence denotes the ability to be present or to be represented in a remote location through the use of robots. A user can use such a technology for remote control of machinery or for apparent participation in distant events where it might be impossible to go for humans. Telepresence is an exciting field that has the potential to change the world...



This project focuses on the integration of telepresence with the Nao humanoid robot developed by Softbank Robotics.



Figure: Nao at the IoT Lab



Developed by SoftBank Robotics, the Nao humanoid robot is 58 centimeters tall, and has several sensors, including cameras, microphones, and touch sensors, allowing for a holistic interaction with its surrounding environment. It has two 2D cameras to recognize shapes, objects, and people. It also has 7 touch sensors located on the head, hands, and feet, sonars, and an inertial unit to perceive its environment and locate itself in space. 4 directional microphones and speakers are also present to interact w...



The objective of this project is to establish a telepresence system in which the Nao robot mirrors the movements of a user in real-time. To achieve this, we have used concepts from computer vision techniques (OpenCV and TensorFlow). Using a camera system, the user's movements are captured, processed, and transmitted to the Nao robot for a streamlined telepresence experience.



In addition to replicating a person’s movement, our project integrates a voice interaction feature, adding another layer of user engagement with the Nao robot.



Figure: The potential of Nao Humanoid for better human-robot interaction



## Methodology



### General Details



In our project, we aimed to achieve the following three objectives:

1. Voice Interaction

2. Motion through Telepresence

3. Video Streaming



#### Voice Interaction



One of the objectives of this project was to implement voice interaction with the NAO humanoid robot. This involves touch detection to initiate the voice interaction command. For example, using the tactile sensors on Nao's head, the user can initiate voice commands by simply touching its head. Once the touch is detected, a command is sent to the robot to start recording audio. The recorded audio file is subsequently forwarded to the Whisper API, which converts the spoken words into text. 


#### Motion through Telepresence

This project uses the integration of MoveNet, an advanced motion tracking system, with the NAO robot, emphasizing the replication of human movements on the robot's platform. MoveNet, known for its precise human pose estimation, operates on a host system to capture and interpret intricate motion details. The project explores how the tracked motion data is seamlessly transmitted from the host system to the NAO robot. This involves understanding the communication protocols and synchronization mechanisms to ensure real-time and accurate transfer of movement parameters. The focus then shifts to the NAO robot's remarkable ability to faithfully replicate the tracked motions. By delving into the robot's kinematics and control systems, the report outlines the technical processes involved in translating received motion data into corresponding physical movements. Practical applications, such as interactive scenarios and collaborative tasks, underscore the potential of this integrated system, offering a glimpse into the evolving landscape of human-robot interaction propelled by advancements in motion tracking technology.

### Video Streaming

As part of our work on telepresence with the NAO humanoid, we've expanded our efforts into real-time video streaming. The project involves capturing live video through the NAO robot's top camera, positioned on its forehead, and streaming it via Flask on a dedicated webpage. This integration of video streaming aims to enhance the user's visual experience and enables remote observation and control. The top camera's placement provides a perspective similar to the user's line of sight, offering a good view of the environment. The Flask framework serves as the foundation for our web-based video streaming platform, ensuring efficient delivery of the captured footage. This will further enhance the telepresence experience, enabling the user to get live feedback about Nao’s environment and will potentially allow for deployment applications in remote areas.

## Results and Discussion

### Speech Pipeline

#### Latency Analysis

Changing the speech model is one way to cut down on the two to three seconds that are lost in the speech pipeline. The three seconds are lost due to output creation time from OpenAI's Whisper API, local processing time, and data communication speed from the robot to the pipeline.

### Telepresence

#### Movement Accuracy

The observed latency in movement replication, which was 1-2 seconds, could be explained by the computational burden of processing and recreating complex joint angles. The model could be further refined or real-time optimisation techniques could be used to reduce latency and improve accuracy. The Thunder model outperformed the Lightning pre-trained models from TensorFlow in terms of joint coordinate capture accuracy.

**2.2 2D to 3D Coordinates:**

Since using two cameras would have required more computational resources and increased program complexity, we decided against our initial attempt to convert 2D coordinates into 3D using a single camera configuration. Although 3D coordination accuracy improved, future work should concentrate on optimising joint angle calculations for more accurate movement replication.

### Video Stream

The blurriness and lack of focus in the video stream that the robot's eyes provided may have an impact on the user's impression of the scenario, therefore you might want to think about changing the camera's settings, raising the resolution, or investigating alternative camera modules.

## References

1. _Effector & Chain definitions — Aldebaran 2.5.11.14a documentation_. (n.d.).
   `http://doc.aldebaran.com/2-5/family/robots/bodyparts.html#nao-chains`
2. _Joint control — Aldebaran 2.5.11.14a documentation_. (n.d.).
   `http://doc.aldebaran.com/2-5/naoqi/motion/control-joint.html#control-joint`
3. _Cartesian control — Aldebaran 2.5.11.14a documentation_. (n.d.).
   [http://doc.aldebaran.com/2-5/naoqi/motion/control-cartesian.html#motion-cartesian-effectors](http://doc.aldebaran.com/2-5/naoqi/motion/control-cartesian.html#motion-cartesian-effectors)
4. Rosebrock, A. (2021c, April 17). _Live video streaming over network with OpenCV and ImageZMQ - PyImageSearch_. PyImageSearch.
   [https://pyimagesearch.com/2019/04/15/live-video-streaming-over-network-with-opencv-and-imagezmq/](https://pyimagesearch.com/2019/04/15/live-video-streaming-over-network-with-opencv-and-imagezmq/)
5. _movenet_. (n.d.). Kaggle.
   `https://www.kaggle.com/models/google/movenet/frameworks/tfLite/variations/singlepose-lightning/versions/1?tfhub-redirect=true`
6. Nao Official Documentation -
   [http://doc.aldebaran.com/2
