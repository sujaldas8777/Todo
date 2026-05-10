from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.api.deps import get_current_user
from app.db.models import Todo
import app.crud.crud_todo as crud_todo
import app.Schemas.schema_todo as schema_todo

# Create router
router = APIRouter(prefix="/todos", tags=["Todos"])

# Client → Route → Schema → CRUD → Database → Response Schema → Client

# Create API (POST)
@router.post("/", response_model=schema_todo.TodoResponse)
def create_todo(todo: schema_todo.TodoCreate, 
                db: Session = Depends(get_db),
                user_id: int = Depends(get_current_user)):
    return crud_todo.create_todo(db, todo, user_id)

# GET ALL
@router.get("/", response_model=list[schema_todo.TodoResponse])
def get_all(
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user)
):
    return crud_todo.get_user_todos(db, user_id)

# GET Single
@router.get("/{todo_id}", response_model=schema_todo.TodoResponse)
def get_one(todo_id: int, 
            db: Session = Depends(get_db),
            user_id: int = Depends(get_current_user)):
    todo = crud_todo.get_user_todo(db, todo_id, user_id)

    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")

    return todo

# UPDATE
@router.put("/{todo_id}", response_model=schema_todo.TodoResponse)
def update(todo_id: int, 
           todo: schema_todo.TodoUpdate, 
           db: Session = Depends(get_db),
           user_id: int = Depends(get_current_user)):
    updated = crud_todo.update_todo(db, todo_id, user_id, todo)

    if not updated:
        raise HTTPException(status_code=404, detail="Todo not found")

    return updated

# DELETE
@router.delete("/{todo_id}")
def delete(todo_id: int, 
           db: Session = Depends(get_db),
           user_id: int = Depends(get_current_user)):
    deleted = crud_todo.delete_todo(db, todo_id, user_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Todo not found")

    return {"message": "Todo deleted successfully"}


'''Request comes
   ↓
get_db() called
   ↓
DB session created
   ↓
Passed to route (db)
   ↓
CRUD uses db
   ↓
Response sent
   ↓
DB session closed'''