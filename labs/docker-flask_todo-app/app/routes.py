from flask import render_template, request, redirect, url_for, jsonify
from app import app, db
from app.models import Todo

@app.route('/')
def index():
    todos = Todo.query.all()
    return render_template('index.html', todos=todos)

@app.route('/todo/create', methods=['POST'])
def create_todo():
    title = request.form.get('title')
    description = request.form.get('description')
    
    if not title:
        return redirect(url_for('index'))
    
    new_todo = Todo(title=title, description=description)
    db.session.add(new_todo)
    db.session.commit()
    
    return redirect(url_for('index'))

@app.route('/todo/<int:id>/toggle', methods=['POST'])
def toggle_todo(id):
    todo = Todo.query.get_or_404(id)
    todo.completed = not todo.completed
    db.session.commit()
    
    return redirect(url_for('index'))

@app.route('/todo/<int:id>/delete', methods=['POST'])
def delete_todo(id):
    todo = Todo.query.get_or_404(id)
    db.session.delete(todo)
    db.session.commit()
    
    return redirect(url_for('index'))

@app.route('/todo/<int:id>')
def view_todo(id):
    todo = Todo.query.get_or_404(id)
    return render_template('todo.html', todo=todo)

# API endpoints for JSON responses
@app.route('/api/todos')
def get_todos():
    todos = Todo.query.all()
    return jsonify([
        {
            'id': todo.id,
            'title': todo.title,
            'description': todo.description,
            'completed': todo.completed,
            'created_at': todo.created_at.isoformat()
        } for todo in todos
    ])