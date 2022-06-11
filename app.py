from sqlite3 import dbapi2
from flask import Flask, render_template, url_for
#database adapter
from flask import SQLAlchemy


app = Flask(__name__)
#Define the path to the database, test.db
#/// -> indicate a relative path
#//// -> absolutepath
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///test.db'
#initializze the dbapi2
db = SQLAlchemy(app)

#create model class for the db
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    completed= db.Column(db.Integer, default=0)

@app.route('/')
def homepage():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)