from app import db

class Director(db.Model):
    director_id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(255), index=True, unique=True)
    bio = db.Column(db.Text)
    photo = db.Column(db.String(255))
    movies = db.relationship("Movie", backref="director")
    picked = db.relationship("MySeenList", backref="director")

class Movie(db.Model):
    movie_id = db.Column(db.Integer, primary_key=True) 
    director_id = db.Column(db.Integer, db.ForeignKey("director.director_id"))
    title = db.Column(db.String(255))
    plot = db.Column(db.Text)
    year = db.Column(db.Integer, index=True)
    country = db.Column(db.String(255))
    actors = db.Column(db.String(255))
    genre = db.Column(db.String(255))
    imdb_rank = db.Column(db.Float)
    poster = db.Column(db.String(255))

class Serie(db.Model):
    serie_id = db.Column(db.Integer, primary_key=True) 
    title = db.Column(db.String(255))
    plot = db.Column(db.Text)
    year = db.Column(db.Integer, index=True)
    network = db.Column(db.String(255))
    season_episodes = db.Column(db.String(255))
    poster = db.Column(db.String(255))
    
class Top10(db.Model):
    top10_id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey("movie.movie_id"))
    rank = db.Column(db.Integer)
    movie = db.relationship("Movie", uselist=False, backref="top10")

class About(db.Model):
    about_id = db.Column(db.Integer, primary_key=True, unique=True)
    about = db.Column(db.String(255))
    description = db.Column(db.Text)

class MySeenList(db.Model):
    myseenlist_id = db.Column(db.Integer, primary_key=True, unique=True)
    director_id = db.Column(db.Integer, db.ForeignKey("director.director_id"))
    tv = db.Column(db.Text)
    theater = db.Column(db.Text)
    date = db.Column(db.DateTime)
    def year(self):
        return self.date.year    
    def month(self):
        return self.date.month
    def monthName(self):
        array = ['', 'january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
        return array[self.month()]
