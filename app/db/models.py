from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from app.db.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True)
    password = Column(String)

class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    completed = Column(Boolean, default=False)

    user_id = Column(Integer, ForeignKey("users.id"))