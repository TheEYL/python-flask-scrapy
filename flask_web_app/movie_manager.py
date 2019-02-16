import os
from flask import Flask
from flask import render_template
from flask import request
from models import db, Movies

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
database="postgres"
user="postgres"
# password="password"


# app.config[ 'SQLALCHEMY_DATABASE_URI' ] = 'postgres://'+user+':'+password+'@localhost:5432/'+database
app.config[ 'SQLALCHEMY_DATABASE_URI' ] = 'postgres://'+user+'@localhost:5432/'+database
# TODO: make work automatically with installing postgres
db.init_app(app)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.form:
        try:
            # print(request.form)
            movie = Movies(title=request.form.get("title"), url=request.form.get("url"), image=request.form.get("image"))
            db.session.add(movie)
            db.session.commit()
        except Exception as e:
            print("failed to add book")
            print(e)
    movies = Movies.query.all()
    return render_template("home.html", movies=movies)


@app.route("/update", methods=["POST"])
def update():
    try:
        # newtitle = request.form.get("newtitle")
        # oldtitle = request.form.get("oldtitle")
        # book = Book.query.filter_by(title=oldtitle).first()
        # book.title = newtitle
        db.session.commit()
    except Exception as e:
        print("Couldn't update book title")
        print(e)
    return redirect("/")

@app.route("/delete", methods=["POST"])
def delete():
    # title = request.form.get("title")
    # book = Book.query.filter_by(title=title).first()
    db.session.delete(book)
    db.session.commit()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
