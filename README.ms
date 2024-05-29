<h1>INTERNET OF THINGS</h1>

<h2>Table of Contents</h2>

<ol>
    <li><a href="#introduction">Introduction</a></li>
    <li><a href="#methodology">Methodology</a>
        <ul>
            <li>2.1. General Details
                <ul>
                    <li>Voice Interaction</li>
                    <li>Motion through Telepresence</li>
                    <li>Video Streaming</li>
                </ul>
            </li>
            <li>2.2. Technical Details
                <ul>
                    <li>Voice Interaction Details</li>
                    <li>Motion through Telepresence Details</li>
                    <li>Video Streaming Details</li>
                </ul>
            </li>
        </ul>
    </li>
    <li><a href="#results-and-discussion">Results and Discussion</a></li>
    <li><a href="#references">References</a></li>
</ol>

<h2 id="introduction">Introduction</h2>

<p>The intersection of robotics and human-computer interaction has paved the path for several advances in the field of telepresence technology in recent years. Telepresence denotes the ability to be present or to be represented in a remote location through the use of robots. A user can use such a technology for remote control of machinery or for apparent participation in distant events where it might be impossible to go for humans. Telepresence is an exciting field that has the potential to change the world...</p>

<p>This project focuses on the integration of telepresence with the Nao humanoid robot developed by Softbank Robotics.</p>

<p><em>Figure: Nao at the IoT Lab</em></p>

<p>Developed by SoftBank Robotics, the Nao humanoid robot is 58 centimeters tall, and has several sensors, including cameras, microphones, and touch sensors, allowing for a holistic interaction with its surrounding environment. It has two 2D cameras to recognize shapes, objects, and people. It also has 7 touch sensors located on the head, hands, and feet, sonars, and an inertial unit to perceive its environment and locate itself in space. 4 directional microphones and speakers are also present to interact with...</p>

<p>The objective of this project is to establish a telepresence system in which the Nao robot mirrors the movements of a user in real-time. To achieve this, we have used concepts from computer vision techniques (OpenCV and TensorFlow). Using a camera system, the user's movements are captured, processed, and transmitted to the Nao robot for a streamlined telepresence experience.</p>

<p>In addition to replicating a person’s movement, our project integrates a voice interaction feature, adding another layer of user engagement with the Nao robot.</p>

<p><em>Figure: The potential of Nao Humanoid for better human-robot interaction</em></p>

<h2 id="methodology">Methodology</h2>

<h3>General Details</h3>

<p>In our project, we aimed to achieve the following three objectives:</p>
<ol>
    <li>Voice Interaction</li>
    <li>Motion through Telepresence</li>
    <li>Video Streaming</li>
</ol>

<h4>Voice Interaction</h4>

<p>One of the objectives of this project was to implement voice interaction with the NAO humanoid robot. This involves touch detection to initiate the voice interaction command. For example, using the tactile sensors on Nao's head, the user can initiate voice commands by simply touching its head. Once the touch is detected, a command is sent to the robot to start recording audio. The recorded audio file is subsequently forwarded to the Whisper API, which converts the spoken words into text.</p>

<h4>Motion through Telepresence</h4>

<p>This project uses the integration of MoveNet, an advanced motion tracking system, with the NAO robot, emphasizing the replication of human movements on the robot's platform. MoveNet, known for its precise human pose estimation, operates on a host system to capture and interpret intricate motion details. The project explores how the tracked motion data is seamlessly transmitted from the host system to the NAO robot. This involves understanding the communication protocols and synchronization mechanisms to ensure real-time and accurate transfer of movement parameters. The focus then shifts to the NAO robot's remarkable ability to faithfully replicate the tracked motions. By delving into the robot's kinematics and control systems, the report outlines the technical processes involved in translating received motion data into corresponding physical movements. Practical applications, such as interactive scenarios and collaborative tasks, underscore the potential of this integrated system, offering a glimpse into the evolving landscape of human-robot interaction propelled by advancements in motion tracking technology.</p>

<h4>Video Streaming</h4>

<p>As part of our work on telepresence with the NAO humanoid, we've expanded our efforts into real-time video streaming. The project involves capturing live video through the NAO robot's top camera, positioned on its forehead, and streaming it via Flask on a dedicated webpage. This integration of video streaming aims to enhance the user's visual experience and enables remote observation and control. The top camera's placement provides a perspective similar to the user's line of sight, offering a good view of the environment. The Flask framework serves as the foundation for our web-based video streaming platform, ensuring efficient delivery of the captured footage. This will further enhance the telepresence experience, enabling the user to get live feedback about Nao’s environment and will potentially allow for deployment applications in remote areas.</p>

<h2 id="results-and-discussion">Results and Discussion</h2>

<h3>Speech Pipeline</h3>

<h4>Latency Analysis</h4>

<p>Changing the speech model is one way to cut down on the two to three seconds that are lost in the speech pipeline. The three seconds are lost due to output creation time from OpenAI's Whisper API, local processing time, and data communication speed from the robot to the pipeline.</p>

<h3>Telepresence</h3>

<h4>Movement Accuracy</h4>

<p>The observed latency in movement replication, which was 1-2 seconds, could be explained by the computational burden of processing and recreating complex joint angles. The model could be further refined or real-time optimisation techniques could be used to reduce latency and improve accuracy. The Thunder model outperformed the Lightning pre-trained models from TensorFlow in terms of joint coordinate capture accuracy.</p>

<h4>2.2 2D to 3D Coordinates:</h4>

<p>Since using two cameras would have required more computational resources and increased program complexity, we decided against our initial attempt to convert 2D coordinates into 3D using a single camera configuration. Although 3D coordination accuracy improved, future work should concentrate on optimising joint angle calculations for more accurate movement replication.</p>

<h3>Video Stream</h3>

<p>The blurriness and lack of focus in the video stream that the robot's eyes provided may have an impact on the user's impression of the scenario, therefore you might want to think about changing the camera's settings, raising the resolution, or investigating alternative camera modules.</p>

<h2 id="references">References</h2>

<ol>
    <li><em>Effector & Chain definitions — Aldebaran 2.5.11.14a documentation</em>. (n.d.).
       <a href="http://doc.aldebaran.com/2-5/family/robots/bodyparts.html#nao-chains">http://doc.aldebaran.com/2-5/family/robots/bodyparts.html#nao-chains</a></li>
    <li><em>Joint control — Aldebaran 2.5.11.14a documentation</em>. (n.d.).
       <a href="http://doc.aldebaran.com/2-5/naoqi/motion/control-joint.html#control-joint">http://doc.aldebaran.com/2-5/naoqi/motion/control-joint.html#control-joint</a></li>
    <li><em>Cartesian control — Aldebaran 2.5.11.14a documentation</em>. (n.d.).
       <a href="http://doc.aldebaran.com/2-5/naoqi/motion/control-cartesian.html#motion-cartesian-effectors">http://doc.aldebaran.com/2-5/naoqi/motion/control-cartesian.html#motion-cartesian-effectors</a></li>
    <li>Rosebrock, A. (2021c, April 17). <em>Live video streaming over network with OpenCV and ImageZMQ - PyImageSearch</em>. PyImageSearch.
       <a href="https://pyimagesearch.com/2019/04/15/live-video-streaming-over-network-with-opencv-and-imagezmq/">https://pyimagesearch.com/2019/04/15/live-video-streaming-over-network-with-opencv-and-imagezmq/</a></li>
    <li><em>movenet</em>. (n.d.). Kaggle.
       <a href="https://www.kaggle.com/models/google/movenet/frameworks/tfLite/variations/singlepose-lightning/versions/1?tfhub-redirect=true">https://www.kaggle.com/models/google/movenet/frameworks/tfLite/variations/singlepose-lightning/versions/1?tfhub-redirect=true</a></li>
</ol>
