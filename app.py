from flask import Flask, render_template, request, url_for, redirect
#database adapter
from flask_sqlalchemy import SQLAlchemy
from datetime import date, datetime


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
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    #return a string every time we created a new element
    def __repr__(self):
        return '<Task %r> % self.id'

@app.route('/', methods=['POST','GET'])
def homepage():
    if request.method=='POST':
        task_content = request.form['content']
        new_task = Todo(content=task_content)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return "There was an error"
    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template('index.html', tasks = tasks)

@app.route('/delele/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return "There was an error deleting the task"
        
@app.route('/update/<int:id>',  methods=['POST','GET'])
def update(id):
    recent_update = db.Todo.get_or_404(id)
    try:
        db.session.commit(recent_update)
        return redirect('/')
    else:
        return "There was an error updating the task"



if __name__ == "__main__":
    app.run(debug=True)