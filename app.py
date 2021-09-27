from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# 'postgresql://<usuario>:<contraseña>@<direccion de la db>:<puerto>/<nombre de la db>
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost:5432/rockoladb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'some-secret-key'

db = SQLAlchemy(app)

# Importar los modelos
from models import Song

# Crear el esquema de la DB
db.create_all()
db.session.commit()

# Rutas de paginas
@app.route('/')
def get_home():
    return 'Este es el home'

@app.route('/signup')
def sign_up():
    return 'Esta es la pagina de registro'

@app.route('/logout')
def log_out():
    return 'Esta es la pagina de logout'

@app.route('/gastos')
def gastos_room():
    return 'Esta es la pagina de gastos de la tienda'

@app.route('/inventario')
def inventario():
    return 'Esta es la pagina de inventario'

@app.route('/factura')
def factura():
    return 'Esta es la pagina de resumen de compra'

@app.route('/estadisticos')
def estadisticos():
    return 'Esta es la pagina de estadisticos y resumen de datos'

@app.route('/administrador')
def administrador():
    return 'Esta es la pagina de administrador'


# Rutas de otras acciones
@app.route('/producto', methods=['GET','POST'])
def crud_song():
    if request.method == 'GET':
        # Hago algo
        print("Llegó un GET")

        # insertar canción
        name = "Perfect"
        artist = "Ed Sheeran"
        genre = "Rock"
        album = "Romanticonas de Viviana"
        year = 2017
        link = "https://youtu.be/2Vv-BfVoq4g"

        entry = Song(name,artist,genre,album,year,link)
        db.session.add(entry)
        db.session.commit()

        return 'Esto fue un GET'

    elif request.method == 'POST':
        # Registrar una cancion
        request_data = request.form
        name = request_data['name']
        artist = request_data['artist']
        genre = request_data['genre']

        print("Nombre:" + name)
        print("Artista:" + artist)
        print("Genero:" + genre)

        # Insertar en la base de datos la canción

        return 'Se registro la canción exitosamente'


@app.route('/updatesong')
def update_song():
    old_name = "Imagine"
    new_name = "Despacito"
    old_song = Song.query.filter_by(name=old_name).first()
    old_song.name = new_name
    db.session.commit()
    return "Actualización exitosa"


@app.route('/getsongs')
def get_songs():
    songs = Song.query.all()
    print(songs[0].artist)
    return "Se trajo la lista de canciones"


@app.route('/deletesong')
def delete_song():
    song_name = "Despacito"
    song = Song.query.filter_by(name=song_name).first()
    db.session.delete(song)
    db.session.commit()
    return "Se borro la canción"

'''
@app.route('/post-request', methods=['POST'])
def post_req():
    request_data = request.form
    print(request_data)
    print(request_data['name'])

    return "Post success"

'''