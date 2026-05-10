from sqlalchemy.orm import Session
from app.db.models import Todo
from app.Schemas.schema_todo import TodoCreate, TodoUpdate

# CREATE (Add Todo)
def create_todo(db: Session, todo, user_id: int):
    new_todo = Todo(
        title=todo.title,
        completed=False,
        user_id=user_id
    )

    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)

    return new_todo

# READ (Get All Todos)
def get_user_todos(db: Session, user_id: int):
    return db.query(Todo).filter(Todo.user_id == user_id).all()

# READ (Get by id)
def get_user_todo(db: Session, todo_id: int, user_id: int):
    return db.query(Todo).filter(
        Todo.id == todo_id,
        Todo.user_id == user_id
    ).first()

# UPDATE Todo
def update_todo(db:Session, todo_id:int, user_id: int, todo):
    existing_todo = db.query(Todo).filter(Todo.id == todo_id, Todo.user_id == user_id).first()

    if not existing_todo:
        return None

    if todo.title is not None:
        existing_todo.title = todo.title

    if todo.completed is not None:
        existing_todo.completed = todo.completed

    db.commit()
    db.refresh(existing_todo)

    return existing_todo


# DELETE Todo
def delete_todo(db: Session, todo_id: int, user_id: int):
    todo = db.query(Todo).filter(Todo.id == todo_id, Todo.user_id == user_id).first()

    if not todo:
        return None

    db.delete(todo)
    db.commit()

    return todo