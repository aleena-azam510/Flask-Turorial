from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///ipl_db-2.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class Team(db.Model):
    __tablename__= "teams"
    id = db.Column(db.Integer,primary_key=True)
    team = db.Column(db.String(50),nullable=False,unique = True)
    state = db.Column(db.String(50),nullable=False)
    members = db.relationship("Player",backref="team")

    def __repr__(self):
        return f"Team('{self.team}','{self.state}')"
    
class Player(db.Model):
    __tablename__ = "players"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50),nullable=False)
    nationality = db.Column(db.String(50),nullable=False)
    team_id = db.Column(db.Integer,db.ForeignKey("teams.id"))

    def __repr__(self):
        return f"Player('{self.name}','{self.nationality}')"
    
if __name__ == "__main__":
        app.run(debug=True)

#os.listdir()
# ['db_crud_operation.py', 'instance', 'one_to_many.py', '__pycache__']
# >>> from one_to_many import app,db
# from one_to_many import Team,Player
# from one_to_many import Team,Player
# >>> app_ctx = app.app_context()
# >>> app_ctx
# <flask.ctx.AppContext object at 0x00000202DB645310>
#  app_ctx.push()
# >>> db.create_all()

#Adding data to team table

# csk = Team(team='CSK',state = 'Tamil Nadu')
# rcb = Team(team='RCB',state='Karnataka')
# mi = Team(team = 'MI',state='Maharashtara')
# db.session.add_all([csk,rcb])
# >>> db.session.commit()

#Adding data to Player table
# msd = Player(name='Dhoni',nationality='Indian',team=csk)

#Adding data to both tables
# db.session.add_all([mi,msd])
#  db.session.commit()

# moeen = Player(name = 'Moeen Ali',nationality='English',team=csk)
# >>> jadeja = Player(name = 'Ravindra Jadeja',nationality='Indian',team=csk)
# >>> kohli = Player(name = 'Virat Kohli',nationality='Indian',team=rcb)
# >>> faf = Player(name = 'FAF Du Plesis',nationality='South Africa',team=rcb)
# >>> rohit = Player(name = 'Rohit Sharma',nationality='Indian',team=mi)
# >>> tim  = Player(name = 'Tim David',nationality='Austrailian',team=mi)
# >>> db.session.add_all([moeen,jadeja,kohli,faf,rohit,tim])
# db.session.commit()

# Team.query.first()
# Team('CSK','Tamil Nadu')
# >>> csk_team = Team.query.first()
# >>> csk_team.members
# [Player('Dhoni','Indian'), Player('Moeen Ali','English'), Player('Ravindra Jadeja','Indian')]

# for pl in csk_team.members:
# ...     print(f"{pl.name} is an {pl.nationality} national")
# ...
# Dhoni is an Indian national
# Moeen Ali is an English national
# Ravindra Jadeja is an Indian national
# >>> msd_player = csk_team.members[0]
# >>> msd_player
# Player('Dhoni','Indian')
# >>> msd_player.team
# Team('CSK','Tamil Nadu')

# >>> app_ctx.pop()
# >>> exit()
