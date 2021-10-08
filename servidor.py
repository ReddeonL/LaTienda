from flask import Flask,request,render_template,redirect,url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# 'postgresql://<usuario>:<contraseña>@<direccion de la db>:<puerto>/<nombre de la db>
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost:5432/tiendadb'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://bgnwmbqjrsccns:61ecfc1393e4972635f3d29a4d8255d241334ef82b9fb95b73ae0ec92ab58897@ec2-34-197-135-44.compute-1.amazonaws.com:5432/dbboljujdiv748'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'some-secret-key'

db = SQLAlchemy(app)

# Importar los modelos
from models import Product, User, Admin, Lote, Sold, Factura

# Crear el esquema de la DB
db.create_all()  #aca me menciona el error
db.session.commit()


# Rutas de paginas
@app.route('/')
def get_home():
    return render_template("home.html")
"""

@app.route('/gastos')
def gastos_room():
    return render_template("gastos.html")

@app.route('/inventario')
def inventario():
    return render_template("inventario.html")

@app.route('/factura')
def factura():
    return render_template("factura.html")

@app.route('/estadisticos')
def estadisticos():
    return 'Esta es la pagina de estadisticos y resumen de datos'

@app.route('/administrador')
def administrador():
    return 'Esta es la pagina de administrador' """  

if __name__ == "__main__":
    app.run()



#Rutas de metodos
@app.route('/updatePasswordUser', methods=['POST'])
def get_vencido():

    request_data = request.form
    email = request_data['email']
    newPassword = request_data['newPassword']
    changeUser = User.query.filter_by(email=email).first()
    retorno = "Actualización exitosa" 

    if changeUser==None:
        #aqui se debe poner una alerta en el navegador que diga que el correo no existe
        retorno = "Fallo de actualización, "  + email + " no existe en la base de datos."
    else:
        cp = User.query.filter_by(email="Ramon").first()
        changeUser.password = newPassword
        db.session.commit()
    return retorno

