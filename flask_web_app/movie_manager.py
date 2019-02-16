import os
from flask import Flask
from flask import render_template
from models import db

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config[ 'SQLALCHEMY_DATABASE_URI' ] = 'postgres://localhost/learningflask'
db.init_app(app)

@app.route("/")
def home():
    if request.form:
        print(request.form)
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)
