from flask import Flask,request,render_template,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import date, datetime


app = Flask(__name__)
# 'postgresql://<usuario>:<contraseña>@<direccion de la db>:<puerto>/<nombre de la db>
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost:5432/tiendadb'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://bgnwmbqjrsccns:61ecfc1393e4972635f3d29a4d8255d241334ef82b9fb95b73ae0ec92ab58897@ec2-34-197-135-44.compute-1.amazonaws.com:5432/dbboljujdiv748'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'some-secret-key'

db = SQLAlchemy(app)

# Importar los modelos

from models import Product, User, Admin, Lote, Sold, Factura, Gastos


# Crear el esquema de la DB
db.create_all()  
db.session.commit()


# Rutas de paginas
@app.route('/')
def inicio():
    return redirect('login')
@app.route('/login')
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
def get_factura():
    return render_template("factura.html")
@app.route('/ventas')
def get_ventas():
    return render_template("ventas.html")
@app.route('/inventario')
def inventario():
    consulta = db.session.query(Product).all()
    print(consulta)
    return render_template("inventario.html",datos = consulta)    

@app.route('/resproducto')
def resproducto():
    return render_template("registroproducto.html")
@app.route('/homeadmin')
def homeadmin():
    return render_template("homeadmin.html")

#funciones

#verificacion en login
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
#verificacion login para el admin
@app.route('/loginadmin', methods=["GET",'POST'])
def verify_admin():
    
    email=request.form["email"]
    password=request.form["password"]

    admindb=Admin.query.filter(Admin.password==password,Admin.email==email)
    try:
        if(admindb[0] is not None):
            return redirect("homeadmin")
    except:
        return redirect("loginadmin")

#ccrear usuario
@app.route('/create_user', methods=["GET",'POST'])
def create_user():
    email = request.form["email"]
    password = request.form["password"]
    user = User(email, password)
    db.session.add(user)
    db.session.commit()
    
    return redirect("login")

@app.route('/create_product', methods=['GET','POST'])
def create_product():
    name = request.form["name"]
    description = request.form["description"]
    pricebuy = request.form["price_buying"]
    category = request.form["category"]
    lote=request.form["lote"]
    price_sale= request.form["price_sale"]
    amount = request.form["amount"]

    producto = Product(name, description,pricebuy,category,lote,price_sale,amount)
    db.session.add(producto)
    db.session.commit()
    return redirect("inventario")

#@app.route("/mostrar_datos", methods=["GET",'POST'])


@app.route('/deleteproduct', methods=["GET",'POST'])
def del_product():
    requestdata=request.form
    name=requestdata["name"]
    productdb=Product.query.filter(name==name)
    db.session.delete(productdb)
    db.session.commit()
    return redirect("home")
    

#para traer info de la base de datos


"""
@app.route('/estadisticos')
def estadisticos():
    return 'Esta es la pagina de estadisticos y resumen de datos'

@app.route('/administrador')
def administrador():
    return 'Esta es la pagina de administrador' """  

@app.route('/save_spents', methods=['GET','POST'])
def save_spents():
    storagecost = request.form["storagecost"]
    servicecost = request.form["servicecost"]
    admincost = request.form["admincost"]
    others = request.form["others"]
    datetime = request.form["datetime"]

    gastos = Gastos(storagecost, servicecost, admincost, others, datetime)
    db.session.add(gastos)
    db.session.commit()
    return "Esta es la prueba"
    # render_template("TablaGastos.html")


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

if __name__ == "__main__":
    app.run(debug=True)