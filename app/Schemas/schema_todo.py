from pydantic import BaseModel, Field

class TodoBase(BaseModel):
    title: str = Field(..., min_length=3, max_length=100)

class TodoCreate(TodoBase):
    pass

class TodoUpdate(BaseModel):
    title: str | None = None
    completed: bool | None = None

class TodoResponse(TodoBase):
    id: int
    completed: bool

    class Config:
        from_attributes = True