# import socketio

# # create a Socket.IO client
# sio = socketio.Client()

# # Event handler for server responses
# @sio.event
# def file_response(data):
#     print('File content received:', data)

# # Connect to the server
# sio.connect('ws://134.209.146.184:5000', wait_timeout = 10)

# # Request the content of a file
# sio.emit('getfile', '')

# # Keep the client running to listen for responses
# try:
#     sio.wait()
# except KeyboardInterrupt:
#     sio.disconnect()

import socketio
import schedule
import time


TXT_FILE_PATH = '/Users/shivansh/Desktop/Naotelepresense/server/test.txt'  # Update this path as necessary

# create a Socket.IO client
sio = socketio.Client()

# Event handler for server responses
@sio.event
def file_response(data):
    print('File content received:', data)

@sio.event
def txt_message_updated(data):
    print('File content updated on server')

# Function to request the file content
def request_file_content():
    sio.emit('getfile', '')  # Assuming the server expects an empty string for the file request

def update_file_content():
    with open(TXT_FILE_PATH, 'r') as file:
        file_content = file.read()
        sio.emit('update message', file_content)  # Assuming the server expects an empty string for the file request

# Connect to the server
sio.connect('ws://134.209.146.184:5000', wait_timeout=10)

# Schedule the file request to run every X seconds
interval_seconds = 1  # Adjust the interval as needed
schedule.every(interval_seconds).seconds.do(request_file_content)

# Keep the client running and the scheduler in a loop
try:
    while True:
        schedule.run_pending()
        time.sleep(1)
except KeyboardInterrupt:
    sio.disconnect()

