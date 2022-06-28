from application import db

class Movies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    movie_name = db.Column(db.String(40), nullable=False)
    rel_yr = db.Column(db.Integer)
    dirID = db.Column(db.Integer, db.ForeignKey(Directors.id))

class Directors(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dir_name = db.Column(db.String(50), nullable=False)
    movie = db.Relationship('Movies', backref='movie')
