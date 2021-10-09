from datetime import date, datetime
from sqlalchemy.orm import backref
from servidor import db

# Tabla producto
class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    price_buying = db.Column(db.Float)
    category = db.Column(db.String)
    lote = db.Column(db.Date)
    price_sale = db.Column(db.Float)
    amount = db.Column(db.Integer)
    

    def __init__(self, name, description, price_buying, category,lote, price_sale,amount):
        
        self.name= name
        self.description = description
        self.price_buying = price_buying
        self.category = category
        self.lote=lote
        self.price_sale = price_sale
        self.amount=amount

class User(db.Model):
    __tablename__ = 'user'

    id_user = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)

    def __init__(self, email, password):
        self.email=email
        self.password=password

class Admin(db.Model):
    __tablename__ = 'admin'

    id_admin = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email_admin = db.Column(db.String, unique=True)
    password_admin = db.Column(db.String)
    def __init__(self,email_admin,password_admin):
        self.email_admin=email_admin
        self.password_admin=password_admin
        
class Lote(db.Model):
    __tablename__='lote'
    id_lote = db.Column(db.Integer, primary_key=True, autoincrement=True)
    due_date =db.Column(db.Date)
    amount = db.Column(db.Integer)
    def __init__(self,due_date,amount):

        self.due_date=due_date
        self.amount=amount


class Sold(db.Model):
    __tablename__='venta'

    id_venta=db.Column(db.Integer, primary_key=True, autoincrement=True)
    sold_date=db.Column(db.DateTime)
    id_product=db.Column(db.ForeignKey("products.id"))
    discount=db.Column(db.Float)
    #id_factura=db.Column(db.ForeignKey("factura.id_factura"))
    amount_sold=db.Column(db.Integer)
    def __init__(self,sold_date,discount,amount_sold):
        self.sold_date=sold_date
        self.discount=discount
        self.amount_sold=amount_sold

class Factura(db.Model):
    __tablename__='factura'
    id_factura=db.Column(db.Integer, primary_key=True, autoincrement=True)
    precio_venta=db.Column(db.Float)
    taxes=db.Column(db.Float)
    total=db.Column(db.Float)
    fecha_venta=db.Column(db.Date)
    def __init__(self, precio_venta, taxes, fecha_venta):
        self.precio_venta = precio_venta
        self.taxes=taxes
        total=precio_venta + taxes
        self.fecha_venta = fecha_venta


class Gastos(db.Model):
    __tablename__='Gastos'
    id_gasto=db.Column(db.Integer, primary_key=True,autoincrement=True)
    price_buy=db.Column(db.ForeignKey("product.price_buying"))
    amount=db.Column(db.ForeignKey("product.amount"))
    storagecost=db.Column(db.Float)
    servicecost=db.Column(db.Float)
    admincost=db.Column(db.Float)
    others=db.Column(db.Float)
    datetime=db.Column(db.Date)
    def  __init__(self,storagecost,servicecost,admincost, others, date):
        self.storagecost=storagecost
        self.servicecost=servicecost
        self.admincost=admincost
        self.others=others
        self.datetime = datetime
