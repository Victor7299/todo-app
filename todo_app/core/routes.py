from flask import Blueprint, render_template, request, abort
from flask.wrappers import Response
from todo_app.core.models import Todo
from sqlalchemy.exc import IntegrityError

from todo_app.extensions import db

core = Blueprint(
    'core',
    __name__,
    url_prefix='/todos',
    template_folder='templates',
    static_folder='static',
    static_url_path='/static/core',
)


@core.route('/', methods=['GET', 'POST'])
def index():
    todos = Todo.query.all()
    context = {
        'todos': todos,
    }
    return render_template('core/index.html', **context)

@core.route('/todo/create', methods=['POST'])
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
            return render_template('core/todo.html', todo=todo)

@core.route('/todo/<id>/update', methods=['PUT'])
def update_todo(id):
    if request.method == 'PUT':
        todo = Todo.query.get(id)
        todo.is_done = 1
        try:
            db.session.commit()
            return render_template('core/todo.html', todo=todo)
        except Exception as e:
            db.session.rollback()
            abort(400)


@core.route('/todo/<id>/delete', methods=['DELETE'])
def delete_todo(id):
    if request.method == 'DELETE':
        todo = Todo.query.get(id)
        try:
            db.session.delete(todo)
            db.session.commit()
            return Response(status=200) 
        except Exception as e:
            db.session.rollback()
            abort(400)
