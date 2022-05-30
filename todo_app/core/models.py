from todo_app.extensions import db

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False, unique=True)
    is_done = db.Column(db.Integer, default=0)

    def __repr__(self) -> str:
        return f'<Todo: {self.title}>'
    
    def __str__(self) -> str:
        return f'<Todo: {self.title}>'