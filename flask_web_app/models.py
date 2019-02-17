from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Movies(db.Model):
  __tablename__ = 'movies'
  id = db.Column(db.Integer, primary_key = True, autoincrement = True)
  title = db.Column(db.String)
  url = db.Column(db.String)
  image = db.Column(db.String)
  rating = db.Column(db.String)

  def __init__(self, title, url, image, rating):
    self.title = title.title()
    self.url = url.title()
    self.image = image.title()
    self.rating= rating.title()
