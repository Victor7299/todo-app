from flask import Flask, render_template, request, abort, Response
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError



app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False, unique=True)
    is_done = db.Column(db.Integer, default=0)

    def __repr__(self) -> str:
        return f'<Todo: {self.title}>'
    
    def __str__(self) -> str:
        return f'<Todo: {self.title}>'

@app.before_first_request
def create_db():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def index():
    todos = Todo.query.all()
    context = {
        'todos': todos,
    }
    return render_template('index.html', **context)

@app.route('/todo/create', methods=['POST'])
def add_todo():
    if request.method == 'POST':
        title = str(request.form['todo_title']).strip()
        if not title: abort(400)
        todo = Todo(title=title)
        try:
            db.session.add(todo)
            db.session.commit()
        except IntegrityError as e:
            db.session.rollback()
            abort(400)
        else:
            return render_template('todo.html', todo=todo)

@app.route('/todo/<id>/update', methods=['PUT'])
def update_todo(id):
    if request.method == 'PUT':
        todo = Todo.query.get(id)
        todo.is_done = 1
        try:
            db.session.commit()
            return render_template('todo.html', todo=todo)
        except Exception as e:
            db.session.rollback()
            abort(400)


@app.route('/todo/<id>/delete', methods=['DELETE'])
def delete_todo(id):
    if request.method == 'DELETE':
        todo = Todo.query.get(id)
        try:
            db.session.delete(todo)
            db.session.commit()
            response = Response(status=200)
            return response
        except Exception as e:
            db.session.rollback()
            abort(400)



if __name__ == "__main__":
    app.run()
