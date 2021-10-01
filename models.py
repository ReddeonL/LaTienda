from app import db

# Tabla Song
class Product(db.Model):
    __tablename__ = 'Product'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    price_buying = db.Column(db.Float)
    Category = db.Column(db.String)
    id_lote = db.Column(db.Integer, primary_key=True)
    price_sale = db.Column(db.Float)
    amount = db.Column(db.String)

    def __init__(self, id, name, description, price_buying, category, price_sale,amount):
        self.id = id
        self.name= name
        self.description = description
        self.price_buying = price_buying
        self.Category = category
        self.price_sale = price_sale
        self.amount=amount

class User(db.Model):
    __tablename__ = 'User'

    id_user = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)

class Admin(db.Model):
    __tablename__ = 'Admin'

    id_admin = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email_admin = db.Column(db.String, unique=True)
    password_admin = db.Column(db.String)
class Lote(db.Model):
    __tablename__='Lote'
    id_lote = db.Column(db.ForeignKey("Product.id_lote"))
    due_date =db.Column(db.DateTime)
    amount = db.Column(db.ForeignKey("Product.amount"))
class Sold(db.Model):
    __tablename__='Venta'

    id_venta=db.Column(db.Integer, primary_key=True, autoincrement=True)
    sold_date=db.Column(db.DateTime)
    id_product=db.Column(db.ForeignKey("Product.id"))
    discount=db.Column(db.Float)
    id_factura=db.Column(db.Integer)
    amount_sold=db.Column(db.Integer)
class Factura(db.Model):
    __tablename__='Factura'
    id_factura=db.Column(db.ForeignKey("Sold.id_venta"))
    id_product=db.Column(db.ForeignKey("Product.id"))
    precio_venta=db.Column(db.ForeignKey("Product.price_sale"))
    taxes=db.Column(db.Column(db.Float))
    total=db.Column(db.Float)
    amount_sold=db.Column(db.ForeignKey("Sold.amount_sold"))
    discount=db.Column(db.ForeignKey("Sold.discount"))
    fecha_venta=db.Column(db.ForeignKey("Sold.sold_date"))