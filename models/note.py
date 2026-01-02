from pydantic import BaseModel

class noteCreate(BaseModel):
    title: str
    content: str

class nodeUpdate(BaseModel):
    title: str
    content: str