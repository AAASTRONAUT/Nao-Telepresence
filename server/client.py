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

# create a Socket.IO client
sio = socketio.Client()

# Event handler for server responses
@sio.event
def file_response(data):
    print('File content received:', data)

# Function to request the file content
def request_file_content():
    sio.emit('getfile', '')  # Assuming the server expects an empty string for the file request

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

