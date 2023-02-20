CREATE TABLE Room (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    video_url VARCHAR(200)
);

CREATE TABLE Participant (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    profile_src VARCHAR(200),
    room_id INTEGER,
    FOREIGN KEY (room_id) REFERENCES Room(id)
);
