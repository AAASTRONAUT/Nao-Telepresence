import socketio

# create a Socket.IO client
sio = socketio.Client()

# Event handler for server responses
@sio.event
def file_response(data):
    print('File content received:', data)

# Connect to the server
sio.connect('ws://134.209.146.184:5000', wait_timeout = 10)

# Request the content of a file
sio.emit('getfile', '')

# Keep the client running to listen for responses
try:
    sio.wait()
except KeyboardInterrupt:
    sio.disconnect()
