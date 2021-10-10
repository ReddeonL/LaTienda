from itertools import product
from flask import Flask,request,render_template,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import date, datetime


app = Flask(__name__)
# 'postgresql://<usuario>:<contraseña>@<direccion de la db>:<puerto>/<nombre de la db>
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost:5432/tiendadb'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://cpdxxdhbrovthw:25d3ec47451f8e836675f3227c1713ee6ad8a0319f81895a5f666d4363029d46@ec2-52-207-47-210.compute-1.amazonaws.com:5432/d80ef8qqjqdhd0'
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
@app.route('/facturas')
def get_factura():
    return render_template("facturas.html")
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
@app.route('/admin')
def homeadmin():
    return render_template("admin.html")

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

#creacion de admin
    admins=Admin(email_admin="chucho",password_admin="6666")
    db.session.add(admins)
    db.session.commit()     
#verificacion login para el admin
@app.route('/loginadmin', methods=["GET",'POST'])
def verify_admin():
    email=request.form["email_admin"]
    password=request.form["password_admin"]    
    admindb=Admin.query.filter(Admin.password==password,Admin.email==email)
    try:
        if(admindb[0] is not None):
            return redirect("homeadmin")
    except:
        return redirect("loginadmin")
#ver tabla de usuarios modo admin
@app.route('/homeadmin')
def tablausuarios():
    consultau = db.session.query(Admin).all()
    print(consultau)
    return render_template("homeadmin.html",datos = consultau)
@app.route('/deleteuser', methods=["GET",'POST'])
def del_user():
    requestdata=request.form
    name=requestdata["name"]
    productdb=Product.query.filter_by(name=name).first()
    db.session.delete(productdb)
    db.session.commit()
    return redirect("home")

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

@app.route('/deleteproduct', methods=["GET",'POST'])
def del_product():
    requestdata=request.form
    name=requestdata["name"]
    productdb=Product.query.filter_by(name=name).first()
    db.session.delete(productdb)
    db.session.commit()
    return redirect("home")

"""
@app.route('/estadisticos')
def estadisticos():
    return 'Esta es la pagina de estadisticos y resumen de datos'

@app.route('/administrador')
def administrador():
    return 'Esta es la pagina de administrador' """  

@app.route('/save_spents', methods=['GET','POST'])
def save_spents():
    if request.method == 'POST':
        storagecost = request.form["storagecost"]
        servicecost = request.form["servicecost"]
        admincost = request.form["admincost"]
        others = request.form["others"]
        date = request.form["date"]
        print("*" + "'" + date + "'" + "*")
        gastos = Gastos(storagecost, servicecost, admincost, others, "'" + date + "'")
        db.session.add(gastos)
        db.session.commit()

        gastos.date= date
        db.session.commit()
        return "Esta es la prueba"
    elif request.method == 'GET':
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
        changeUser.password = newPassword
        db.session.commit() 
    return retorno


@app.route('/facturas', methods=['GET'])
def get_facturas():
    id_factura=[]
    precio_venta=[]
    taxes=[]
    total=[]
    date_factura=[]

    for factura in Factura.query:
        id_factura.append(str(factura.id_factura))
        precio_venta.append(str(factura.precio_venta))
        taxes.append(str(factura.taxes))
        total.append(str(factura.total))
        date_factura.append(str(factura.fecha_venta))

    return render_template("facturas.html", id_factura=id_factura, precio_venta=precio_venta,
                            taxes=taxes, total=total, date_factura=date_factura)

#esta ruta y metodo reciben en (?nFactura=" ") el id de la factura para poder facturar
# El parametro debe recibirse usando el navegador, atraves de la ruta asi /facturar?nFactura=Ejemplo
@app.route('/facturar', methods=['GET'])
def get_facturar():
    id_factura= request.args.get('nFactura',None)
    factura = Factura.query.filter_by(id_factura=id_factura).first()

    if factura==None:
        return "Error: Hay un error en el id de la factura!"
    else:

        precio_venta=factura.precio_venta
        taxes=factura.taxes
        total=factura.total
        fecha_venta=factura.fecha_venta
        discount=[]
        amount_sold=[]
        product_price=[]
        name_product=[]

        ventas = Sold.query.filter(Sold.id_factura==factura.id_factura)
        for vent in ventas:
            discount.append(vent.discount)
            amount_sold.append(vent.amount_sold)
            product_price.append(Product.query.filter_by(id=vent.id_product).first().price_sale * vent.amount_sold)
            name_product.append(Product.query.filter_by(id=vent.id_product).first().name)
        
        return render_template("facturar.html", id_factura=id_factura, precio_venta=precio_venta,
                               taxes=taxes, total=total, fecha_venta=fecha_venta,discount=discount,
                               amount_sold=amount_sold, product_price=product_price, name_product=name_product)
 
if __name__ == "__main__":
    app.run(debug=True)