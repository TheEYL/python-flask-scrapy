import os
from flask import Flask
from flask import render_template
from flask import request
from models import db, Movies

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config[ 'SQLALCHEMY_DATABASE_URI' ] = 'postgres://learningflask:leo@localhost:5432/learningflask'
db.init_app(app)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.form:
        print(request.form)
    movies = Movies.query.all()
    return render_template("home.html", movies=movies)

if __name__ == "__main__":
    app.run(debug=True)
