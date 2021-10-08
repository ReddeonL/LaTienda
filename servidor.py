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
from models import Gastos, Product, User, Admin, Lote, Sold, Factura

# Crear el esquema de la DB
db.create_all()  #aca me menciona el error
db.session.commit()


# Rutas de paginas

@app.route('/login'and'/')
def get_login():
    return render_template("login.html")
@app.route('/home')
def get_home():
    return render_template("home.html")
#paginas de login a singup
@app.route('/signup')
def get_signup():
    return render_template("signup.html")
@app.route('/forgetpass')
def get_forget():
    return render_template("forgetpass.html")
#paginas enlaces del home     
@app.route('/gastos')
def get_gastos():
    return render_template("gastos.html")
@app.route('/factura')
def get_home():
    return render_template("factura.html")
@app.route('/ventas')
def get_ventas():
    return render_template("ventas.html")
@app.route('/inventario')
def inventario():
    return render_template("inventario.html")
@app.route('/resproducto')
def resproducto():
    return render_template("registroproducto.html")


@app.route('/create_user', methods=["GET",'POST'])
def create_user():
    email = request.form["email"]
    password = request.form["password"]

    user = User(email, password)
    db.session.add(user)
    db.session.commit()
    
    return redirect("login")

@app.route('/verify_user', methods=["GET",'POST'])
def verify_user():
    
    email=request.form["email"]
    password=request.form["password"]

    userdb=User.query.filter(User.password==password,User.email==email)
    try:
        if(userdb[0] is not None):
            return redirect("home")
    except:
        return redirect("login")

@app.route('/create_product', methods=['GET','POST'])
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

    return redirect("inventario")


"""
En la función, por ejemplo:
@app.route("/mostrar_datos")
def mostrarDatos():
    consulta = db.session.query(Product).all()
    return render_template("inventario.html",datos = consulta)

    
@app.route('/gastos', methods=['POST'])
def create_product():
    storagecost = request.form["storagecost"]
    description = request.form["description"]
   

    gastos = Gastos(storagecost, t)
    db.session.add(gastos)
    db.session.commit()
    return redirect(url_for("home.html"))"""

#para traer info de la base de datos
"""@app.route('/dbusers', methods=['GET'])
def create_user():
    names=User.query.all() 
    for r in names:
        print(r.email)"""


"""


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
