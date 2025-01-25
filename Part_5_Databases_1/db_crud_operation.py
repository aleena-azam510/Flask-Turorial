from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///employees_db.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
class Employee(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50),nullable=False)
    age = db.Column(db.Integer ,nullable=False)
    email = db.Column(db.String(50),nullable=False,unique = True)

    def __repr__(self):
        return f"Employee('{self.name}','{self.age}','{self.email}')"
#WRITE IN ANACONDA PROMPT
#CREATING DATABASE
# python 
# import os
# >>> os.listdir()
# ['db_crud_operation.py']
# >>> from db_crud_operation import app,db
# >>> app_context = app.app_context()
# >>> app_context
# <flask.ctx.AppContext object at 0x00000141B203DD30>
# >>> app_context.push()
# >>> db.create_all()

# ADD DATA TO DATABASE
#  from db_crud_operation import Employee
# >>> michael = Employee(name='Michael',age=42,email='michael@gmail.com')
# >>> michael
# Employee('Michael','42','michael@gmail.com')
# >>> dwight = Employee(name='Dwightl',age=32,email='dwight@gmail.com')
# >>> Jim = Employee(name='Jim',age=30,email='jim@gmail.com')
# >>> elsa = Employee(name='Elsa',age=29,email='elsa@gmail.com')

#CREATE 
#db.session.add(michael)
# >>> db.session.commit()
# >>> db.session.add_all([dwight,Jim,elsa])
# >>> db.session.commit()

# RETREIVE
# RETRIEVING DATA FROM THE DATABASE

#  mike = employees[0]
# >>> mike.name
# 'Michael'
# >>> mike.age
# 42
# >>> mike.email
# 'michael@gmail.com'
# >>> for emp in employees:
# ...     print(f"{emp.name} who is {emp.age} years old,has email {emp.email}")

#Filtering
# Employee.query.first()
# Employee('Michael','42','michael@gmail.com')
# >>> Employee.query.filter_by(name='Jim')
# <flask_sqlalchemy.query.Query object at 0x00000202DB542D70>
# >>> Employee.query.filter_by(name='Jim').all()
# [Employee('Jim','30','jim@gmail.com')]
# Employee.query.filter_by(name='Jim').first()
# Employee('Jim','30','jim@gmail.com')

# Extracting data based on ID
# db.session.get(Employee,1)
# Employee('Michael','42','michael@gmail.com')

#UPDATING
#  mike.age = 50
# >>> mike
# Employee('Michael','50','michael@gmail.com')
# >>> db.session.commit()

#DELETING
#  db.session.delete(Jim)
# >>> db.session.commit()
if __name__ == "__main__":
    app.run(debug=True)

