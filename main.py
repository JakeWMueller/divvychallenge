from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
# './DivvyChallenge.csv'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:pass@localhost/my_db'


db = SQLAlchemy(app)
class Divvy(db.Model):
    __tablename__= 'Divvy Data 2013'
    id = db.Column('tripid', db.Integer, primary_key=True)
    starttime = db.Column(db.DateTime(), default=datetime.utcnow)
    stoptime = db.Column(db.DateTime(), default=datetime.utcnow)
    from_station_id = db.Column(db.Text(), nullable=False)


def __init__(self, starttime, stoptime, from_station_id):
    self.starttime = starttime
    self.stoptime = stoptime
    self.from_station_id = from_station_id

if __name__ == "__main__":
    app.run(debug=True)

