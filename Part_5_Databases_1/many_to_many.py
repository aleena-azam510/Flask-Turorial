from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///store_db.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
#association table
Customer_Product = db.Table(
     "customer_product",
     db.Column("customer_id",db.Integer,db.ForeignKey("customers.id")),
     db.Column("product_id",db.Integer,db.ForeignKey("products.id"))
)

class Customer(db.Model):
    __tablename__= "customers"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50),nullable=False)
    email = db.Column(db.String(50),nullable=False,unique = True)
    items = db.relationship("Product",backref="owners",secondary=Customer_Product)

    def __repr__(self):
        return f"Customers('{self.name}','{self.email}')"

class Product(db.Model):
    __tablename__= "products"
    id = db.Column(db.Integer,primary_key=True)
    product = db.Column(db.String(50),nullable=False)
    price = db.Column(db.Integer,nullable=False)

    def __repr__(self):
        return f"Products('{self.product}','{self.price}')"
    
#to form many to many relationship, i.e:both tables should have foreign key..so we create our own custom table for cleaner look..This table would have all possible combinations b/w both tables

#We will use association table
if __name__ == "__main__":
        app.run(debug=True)
# python
# import os
# >>> os.listdir()
# >>> from many_to_many import app , db
# >>> from many_to_many import Customer,Product
# >>> app_ctx = app.app_context()
# >>> app_ctx
# <flask.ctx.AppContext object at 0x00000176BAD36270>
# >>> app_ctx.push()
# >>> db.create_all()

#CREATING CUSTOMERS TABLE
# >>> steve = Customer(name = 'steve' , email = 'steve@mail.com')
# >>> tony = Customer(name = 'Tony' , email = 'tony@mail.com')
# >>> peter = Customer(name = 'Peter' , email = 'peter@mail.com')
# >>> matt = Customer(name = 'Matt' , email = 'matt@mail.com')

#CREATING PRODUCTS TABLE
# >>> bowl = Product(product='Bowl' , price=5)
# >>> plate = Product(product='Plate' , price=9)
# >>> knife = Product(product='Knife' , price=4)
# >>> scissor = Product(product='Scissors' , price=2.4)
# >>> cup = Product(product='Cup' , price=15)

#ADDING DATA TO BOTH TABLES
# >>> db.session.add_all([steve,tony,peter,matt,bowl,plate,knife,scissor,cup])
# >>> db.session.commit()

#ENTERING DATA IN ASSOCIATION TABLE
# >>> steve.items
# []
# >>> type(steve.items)
# <class 'sqlalchemy.orm.collections.InstrumentedList'>
# >>> cup
# Products('Cup','15')
# >>> cup.owners
# []
# >>> type(cup.owners)
# <class 'sqlalchemy.orm.collections.InstrumentedList'>
# >>> steve.items.append(cup)
# >>> steve.items
# [Products('Cup','15')]
# >>> steve.items.extend([bowl,plate])
# >>> steve.items
# [Products('Cup','15'), Products('Bowl','5'), Products('Plate','9')]
# >>> db.session.commit()

# >>> tony
# Customers('Tony','tony@mail.com')
# >>> tony.items
# []
# >>> tony.items.append(plate)
# >>> tony.items.extend([cup,scissor,knife])
# >>> db.session.commit()

# >>> peter
# Customers('Peter','peter@mail.com')
# >>> peter.items
# []
# >>> peter.items.append(bowl)
# >>> peter.items.extend([plate,knife,cup])
# >>> db.session.commit()

# >>> matt
# Customers('Matt','matt@mail.com')
# >>> matt.items
# []
# >>> matt.items.append(cup)
# >>> matt.items.extend([bowl,plate,knife])
# >>> db.session.commit()

#CHECKING WHICH ITEMS BELONG TO WHICH CUSTOMER
# cup.owners
# [Customers('steve','steve@mail.com'), Customers('Tony','tony@mail.com'), Customers('Peter','peter@mail.com'), Customers('Matt','matt@mail.com')]
# >>> plate.owners
# [Customers('steve','steve@mail.com'), Customers('Tony','tony@mail.com'), Customers('Peter','peter@mail.com'), Customers('Matt','matt@mail.com')]
# >>> knife.owners
# [Customers('Tony','tony@mail.com'), Customers('Peter','peter@mail.com'), Customers('Matt','matt@mail.co


#  cup.price
# 15
# >>> app_ctx.pop()
# >>> exit()
