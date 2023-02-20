import socketio

sio = socketio.Client()

@sio.event
def connect():
    print('Connected to server',)

@sio.event
def disconnect():
    print('Disconnected from server')

@sio.event
def message(data):
    print('Received message: ' + str(data))

@sio.event
def play(data):
    print('Received play event from server' + str(data))

@sio.event
def pause(data):
    print('Received pause event from server' + str(data))

@sio.event
def leave(data):
    print('Received leave event from server' + str(data))

@sio.event
def room_message(data):
    print('Received message: ' + str(data))

@sio.event
def status(data):
    print('Conn Status: ' + str(data))

@sio.event
def participants_list(data):
    print("Participantes:", data)

sio.connect('http://localhost:5000')

room_id = input('Enter room ID: ')
participant_id = input('Enter your Id: ')
sio.emit('join', {'room_id': room_id, 'participant_id': participant_id})

while True:
    message = input("message: ")
    if message == 'play':
        sio.emit('play', {'room_id': room_id, 'participant_id': 1, 'time':2.5})
    elif message == 'pause':
        sio.emit('pause', {'room_id': room_id, 'participant_id': 1, 'time':3.78})
    elif message == 'message':
        sio.emit('teste')
    elif message == 'ps':
        sio.emit('list_participants', {'room_id': room_id})
    elif message == 'exit':
        sio.emit('leave', {'room_id': room_id, 'participant_id': 1})
        sio.disconnect()
        break
