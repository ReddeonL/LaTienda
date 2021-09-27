from app import db

# Tabla Song
class Song(db.Model):
    __tablename__ = 'Song'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    artist = db.Column(db.String)
    genre = db.Column(db.String)
    album = db.Column(db.String, nullable=True)
    year = db.Column(db.Integer, nullable=True)
    link = db.Column(db.String, unique=True)

    def __init__(self, name, artist, genre, album, year, link):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.album = album
        self.year = year
        self.link = link

class User(db.Model):
    __tablename__ = 'User'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)

class FavoriteSong(db.Model):
    __tablename__ = 'FavoriteSong'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.ForeignKey("User.id"))
    song_id = db.Column(db.ForeignKey("Song.id"))