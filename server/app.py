from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import threading
import time
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

# Path to your .txt file for displaying content
TXT_FILE_PATH = '/app/test.txt'
# Path where you want to save incoming messages
SPEAK_NOW_FILE_PATH = '/app/speak_now.txt'

def read_txt_file():
    try:
        with open(TXT_FILE_PATH, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return "File not found."

def emit_txt_content():
    while True:
        content = read_txt_file()
        socketio.emit('file update', {'content': content})
        time.sleep(1)  # Update interval in seconds

@app.route('/')
def index():
    return render_template('frontend.html')

@socketio.on('getfile')
def handle_message(message):
     with open('/app/speak_now.txt', 'r') as file:
        file_content = file.read()
        emit('file_response', file_content)

@socketio.on('send message')
def handle_message(message):
    print('Received message:', message)
    # Save the message to speak_now.txt
    with open(SPEAK_NOW_FILE_PATH, 'a') as file:
        file.write(message + '\n')
    # Optional: Emit back an acknowledgment or update
    emit('message received', {'status': 'Message received'})

if __name__ == '__main__':
    # Start the thread that emits txt file updates
    threading.Thread(target=emit_txt_content, daemon=True).start()
    socketio.run(app, debug=True)
