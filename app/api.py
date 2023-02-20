from flask import Blueprint, jsonify, request
from models import db, Room, Participant

api = Blueprint('api', __name__, url_prefix='/watch')


# endpoints da API REST
@api.route('/participants', methods=['POST'])
def create_participant():
    name = request.json['name']
    profile_src = request.json['profile_src']
    room_id = request.json['room_id']

    participant = Participant(name=name, profile_src=profile_src, room_id=room_id)
    db.session.add(participant)
    db.session.commit()

    return jsonify(participant.serialize()), 201

@api.route('/participants/<int:id>', methods=['PUT'])
def update_participant(id):
    participant = Participant.query.get(id)

    if not participant:
        return jsonify({'error': 'Participant not found'}), 404
    
    name = request.json['name']
    profile_src = request.json['profile_src']
    room_id = request.json['room_id']
    
    # Update room data
    if name:
        participant.name = name
    if profile_src:
        participant.profile_src = profile_src
    if room_id:
        participant.room_id = room_id
    

    db.session.commit()
    return jsonify(participant.serialize()), 200

@api.route('/room', methods=['POST'])
def create_room():
    name = request.json['name']
    video_url = request.json['video_url']

    room = Room(name=name, video_url=video_url)
    db.session.add(room)
    db.session.commit()

    return jsonify(room.serialize()), 201

@api.route('/room/<int:id>', methods=['PUT'])
def update_room(id):
    room = Room.query.get(id)

    if not room:
        return jsonify({'error': 'Room not found'}), 404
    
    name = request.json['name']
    video_url = request.json['video_url']
    
    # Update room data
    if name:
        room.name = name
    if video_url:
        room.video_url = video_url

    db.session.commit()
    return jsonify(room.serialize()), 200


@api.route('/room/<int:id>', methods=['GET'])
def get_room(id):
    room = Room.query.get(id)

    if not room:
        return jsonify({'error': 'Room not found'}), 404

    return jsonify(room.serialize()), 200


@api.route('/participants/<int:id>', methods=['GET'])
def get_participant(id):
    participant = Participant.query.get(id)

    if not participant:
        return jsonify({'error': 'Participant not found'}), 404

    return jsonify(participant.serialize()), 200


@api.route('/rooms', methods=['GET'])
def get_all_rooms():
    rooms = Room.query.all()
    return jsonify([room.serialize() for room in rooms]), 200


@api.route('/participants/by-room/<int:room_id>', methods=['GET'])
def get_participants_by_room(room_id):
    participants = Participant.query.filter_by(room_id=room_id).all()
    return jsonify([participant.serialize() for participant in participants]), 200


@api.route('/rooms/search', methods=['GET'])
def search_rooms():
    name = request.args.get('name')
    id = request.args.get('id')

    if name:
        rooms = Room.query.filter(Room.name.like(f'%{name}%')).all()
    elif id:
        rooms = Room.query.filter_by(id=id).all()
    else:
        return jsonify({'error': 'You must provide a name or an id parameter'}), 400

    return jsonify([room.serialize() for room in rooms]), 200


@api.route('/participants/<int:id>', methods=['DELETE'])
def delete_participant(id):
    participant = Participant.query.get(id)

    if not participant:
        return jsonify({'error': 'Participant not found'}), 404

    db.session.delete(participant)
    db.session.commit()

    return jsonify({'message': 'Participant deleted successfully'}), 200


@api.route('/room/<int:id>', methods=['DELETE'])
def delete_room(id):
    room = Room.query.get(id)

    if not room:
        return jsonify({'error': 'Room not found'}), 404

    # seta o campo room_id como None nos registros dos participantes que estavam na sala
    participants = Participant.query.filter_by(room_id=id).all()
    for participant in participants:
        participant.room_id = None

    db.session.delete(room)
    db.session.commit()

    return jsonify({'message': 'Room deleted successfully'}), 200

if __name__ == '__main__':
    api.run(debug=True)