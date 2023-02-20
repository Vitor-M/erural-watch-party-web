from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    video_url = db.Column(db.String(200))
    participants = db.relationship('Participant', backref='room')

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'video_url': self.video_url,
        }

class Participant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    profile_src = db.Column(db.String(200))
    room_id = db.Column(db.Integer, db.ForeignKey('room.id'))
    
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'profile_src': self.profile_src,
            'room_id': self.room_id
        }

    @staticmethod
    def get_by_id(participant_id):
        return Participant.query.filter_by(id=participant_id).first()