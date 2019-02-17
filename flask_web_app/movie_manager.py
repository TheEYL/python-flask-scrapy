import os
from flask import Flask, render_template, request, redirect, url_for
from models import db, Movies
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
database="postgres"
user="postgres"

app.config[ 'SQLALCHEMY_DATABASE_URI' ] = 'postgres://'+user+'@localhost:5432/'+database
# TODO: make work automatically with installing postgres
db.init_app(app)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST" and request.form:
        try:
            title = request.form.get("title")
            url = request.form.get("url")
            image = request.form.get("image")
            movie = Movies(title=title,url=url,image=image)
            db.session.add(movie)
            db.session.commit()
        except Exception as e:
            print("Failed to add movie")
            print(e)
    movies = Movies.query.all()
    return render_template("home.html", movies=movies)

@app.route("/update", methods=["POST"])
def update():
    try:
        newtitle = request.form.get("newtitle")
        oldtitle = request.form.get("oldtitle")
        movie = Movies.query.filter_by(title=oldtitle).first()
        movie.title = newtitle
        db.session.commit()
        return redirect("/")
    except Exception as e:
        print("Failed to update movie title")
        print(e)

@app.route("/delete/<int:id>", methods=["POST"])
def delete(id):
    try:
        movie = Movies.query.filter_by(id=id).first()
        db.session.delete(movie)
        db.session.commit()
        return redirect("/")
    except Exception as e:
        print("Failed to delete movie title")
        print(e)

if __name__ == "__main__":
    app.run(debug=True)
