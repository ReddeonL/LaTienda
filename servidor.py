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
    return render_template("signup.html")

@app.route('/create-user', methods=['POST'])
def create_user():
    email = request.form["email"]
    password = request.form["password"]

    user = User(email, password)
    db.session.add(user)
    db.session.commit()
    return render_template("login.html")
@app.route('/verify_user',methods=['POST'])
def verify_user():
    request_info=request.form
    email=request_info["Email"]
    password=request_info["Contraseña"]
    user=User.query.filter(User.password==password,User.email==email)
    try:
        if(user[0] is not None):
            return render_template("home.html")
    except:
        return render_template("login.html")

@app.route('/create_product', methods=['POST'])
def create_product():
    name = request.form["name"]
    description = request.form["description"]
    pricebuy = request.form["price_buying"]
    category = request.form["category"]
    price_sale= request.form["price_sale"]
    amount = request.form["amount"]

    producto = Product(name, description,pricebuy,category,price_sale,amount)
    db.session.add(producto)
    db.session.commit()

    return "registro exitoso"

#para traer info de la base de datos
"""@app.route('/dbusers', methods=['GET'])
def create_user():
    names=User.query.all() 
    for r in names:
        print(r.email)"""


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
