from flask import Flask, jsonify, render_template
from flask_socketio import SocketIO, emit
import threading
import time
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

TXT_FILE_PATH = '/Users/shivansh/Desktop/Naotelepresense/server/test.txt'  # Update this path as necessary
SPEAK_NOW_FILE_PATH = '/Users/shivansh/Desktop/Naotelepresense/server/speak_now.txt'

def read_txt_file():
    try:
        with open(TXT_FILE_PATH, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return "File not found."

@app.route('/')
def index():
    return render_template('frontend.html')

@app.route('/get-text')
def get_text():
    content = read_txt_file()
    return jsonify({'content': content})

@socketio.on('getfile')
def handle_message(message):
    with open(SPEAK_NOW_FILE_PATH, 'r') as file:
        file_content = file.read()
    emit('file_response', file_content)

@socketio.on('send message')
def handle_send_message(message):
    print('Received message:', message)
    # Save the message to speak_now.txt
    with open(SPEAK_NOW_FILE_PATH, 'w') as file:
        file.write(message + '\n')
    # Emit back an acknowledgment or update
    emit('message received', {'status': 'Message received'})

if __name__ == '__main__':
    socketio.run(app, debug=True)

