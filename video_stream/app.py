from flask import Flask,render_template,Response
import sys
import cv2
from naoqi import ALProxy
import numpy as np

IP = "172.20.4.100"  # Replace here with your Nao's IP address.
PORT = 9559

if len(sys.argv) > 1:
    IP = sys.argv[1]

videoProxy = ALProxy("ALVideoDevice", IP, PORT)
resolution = 1  # 1 for 320x240, 0 for 160x120
colorSpace = 11  # RGB

# Subscribe to the camera
videoClient = videoProxy.subscribe("python_client", resolution, colorSpace, 5)
app=Flask(__name__)


def generate_frames():
    while True:
        image = videoProxy.getImageRemote(videoClient)    

        width = image[0]
        height = image[1]
        array = image[6]

        # Create a numpy array from the image data
        img = np.frombuffer(array, dtype=np.uint8).reshape((height, width, 3))
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)  # Convert from RGB to BGR

        ret,buffer=cv2.imencode('.jpg',img)
        frame=buffer.tobytes()

        yield(b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video')
def video():
    return Response(generate_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__=="__main__":
    app.run(debug=True)