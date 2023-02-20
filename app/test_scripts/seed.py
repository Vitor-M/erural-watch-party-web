from flask import Flask
from models import db, Room, Participant

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin123@localhost:5432/watch_party_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

    room1 = Room(name='Room 1', video_url='https://www.youtube.com/watch?v=dQw4w9WgXcQ')
    room2 = Room(name='Room 2', video_url='https://www.youtube.com/watch?v=oHg5SJYRHA0')

    db.session.add_all([room1, room2])
    db.session.commit()

    participant1 = Participant(name='John', profile_src='https://example.com/john.png', room_id=room1.id)
    participant2 = Participant(name='Jane', profile_src='https://example.com/jane.png', room_id=room1.id)
    participant3 = Participant(name='Bob', profile_src='https://example.com/bob.png', room_id=room2.id)

    db.session.add_all([participant1, participant2, participant3])
    db.session.commit()

    print('Rooms:')
    for room in Room.query.all():
        print(room.name, room.video_url)

    print('Participants:')
    for participant in Participant.query.all():
        print(participant.name, participant.profile_src, participant.room.name)
