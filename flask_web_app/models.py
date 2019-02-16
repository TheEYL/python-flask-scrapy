from flask_sqlalchemy import SQLAlchemy
# from werkzeug import generate_password_hash, check_password_hash


db = SQLAlchemy()
class Movies(db.Model):
  __tablename__ = 'movies'
  # uid = db.Column(db.Integer, primary_key = True)
  title = db.Column(db.String, primary_key = True)
  url = db.Column(db.String)
  image = db.Column(db.String)
  # email = db.Column(db.String(120), unique=True)
  # pwdhash = db.Column(db.String(54))

  def __init__(self, title, url, image):
    self.title = title.title()
    self.url = url.title()
    self.image = image.title()
    # self.email = email.lower()
    # self.set_password(password)

  # def set_password(self, password):
    # self.pwdhash = generate_password_hash(password)

  # def check_password(self, password):
    # return check_password_hash(self.pwdhash, password)
