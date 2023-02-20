from flask_socketio import SocketIO, join_room, leave_room, emit
from models import Participant, Room, db


socketio = SocketIO(cors_allowed_origins="*")

@socketio.on('connect')
def on_connect():
    emit("status", { "data": "Connected. Hello!" })

@socketio.on('disconnect')
def on_disconnect():
    emit("status", { "data": "Disconnected. Bye!" })

@socketio.on('list_participants')
def list_participants(data):
    room_id = data['room_id']
    rooms = []
    print(socketio.server.manager.rooms.items())
    for room in socketio.server.manager.rooms.keys():
        participants = []
        for participant, participant_id in socketio.server.manager.get_participants(room, room=room_id):
            participants.append(participant_id)
        rooms.append({'room': room, 'participants': participants})

    emit('participants_list',{'rooms': rooms}, room=room_id, broadcast=True)

@socketio.on('join')
def on_join(data):
    participant_id = data['participant_id']
    room_id = data['room_id']
    participant = Participant.query.get(participant_id)
    if participant is not None:
        if participant.room_id != room_id:
            if participant.room_id is not None:
                leave_room(participant.room_id)
            participant.room_id = room_id
            db.session.commit()
        join_room(room_id)
        room = Room.query.get(room_id)
        emit('room_message', f"Welcome to room {room.name}, {participant.name}", room=room_id)

@socketio.on('leave')
def on_leave(data):
    participant_id = data['participant_id']
    participant = Participant.query.get(participant_id)
    if participant is not None:
        if participant.room_id is not None:
            room = Room.query.get(participant.room_id)
            leave_room(participant.room_id)
            participant.room_id = None
            db.session.commit()
            emit('room_message', f"{participant.name} leave the room {room.name}", room=room.room_id)

@socketio.on('play')
def on_play(data):
    room_id = data['room_id']
    time = data['time']
    emit('play', {'time': time}, room=room_id, broadcast=True)

@socketio.on('pause')
def on_pause(data):
    room_id = data['room_id']
    time = data['time']
    emit('pause', {'time': time}, room=room_id, broadcast=True)