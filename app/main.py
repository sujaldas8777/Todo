from fastapi import FastAPI
from app.db.database import engine, Base
import app.db.models as models
from app.api.routes import todo, auth
app = FastAPI()

# Create all tables
Base.metadata.create_all(bind=engine)

# Include routes
app.include_router(auth.router)
app.include_router(todo.router)