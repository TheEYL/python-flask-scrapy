import os
from flask import Flask, flash, render_template, request, redirect, url_for
from models import db, Movies
from flask_sqlalchemy import SQLAlchemy
from config import DATABASE, USER

app = Flask(__name__)
app.config[ 'SQLALCHEMY_DATABASE_URI' ] = 'postgres://'+USER+'@localhost:5432/'+DATABASE
# TODO: make work automatically with installing postgres
db.init_app(app)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST" and request.form:
        try:
            title = request.form.get("title")
            url = request.form.get("url")
            image = request.form.get("image")
            rating = request.form.get("rating")
            movie = Movies(title=title, url=url, image=image, rating=rating)
            db.session.add(movie)
            db.session.commit()
        except Exception as e:
            print("Failed to add movie")
            print(e)
    movies = Movies.query.all()
    return render_template("home.html", movies=movies)

@app.route("/create", methods=["GET"])
def create():
    return render_template("create.html")

@app.route("/update/<int:id>", methods=["GET", "POST"])
def update(id):
    if request.method == "POST":
        try:
            movie = Movies.query.filter_by(id=id).first()
            movie.title = request.form.get("newtitle")
            movie.url = request.form.get("newurl")
            movie.image = request.form.get("newimage")
            movie.rating = request.form.get("newrating")
            db.session.commit()
            return redirect("/")
        except Exception as e:
            print("Failed to update movie title")
            print(e)
    else:
        movie = Movies.query.filter_by(id=id).first()
        return render_template("update.html", movie=movie)

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


@app.route("/results", methods=["POST"])
def search():
    results = []
    search_string = request.form.get("search")
    if search_string:
        # TODO: fix query to search for all
        # qry = Movies.query.filter(title.like(search_string) | image.like(search_string) | Movies.url.like(search_string) | Movies.rating.like(search_string))
        # results = Movies.query.filter(Movies.title.like(search_string)).all()
        results = Movies.query.filter_by(title=search_string).all()
        return render_template('home.html', movies=results)
    else:
        print('in not results')
        # flash('No results found!')
        return redirect('/')
    # else:
    #     # display results
    #     print("**in elsey *************")
    #     print(results)
    #     return render_template('home.html', movies=results)

if __name__ == "__main__":
    app.run(debug=True)
