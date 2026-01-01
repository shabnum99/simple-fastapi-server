from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

notes = []

note_id_counter = 1

class noteCreate(BaseModel):
    title: str
    content: str

@app.post("/notes")
def create_note(note: noteCreate):
    global note_id_counter

    new_note = {
        "id": note_id_counter,
        "title": note.title,
        "content": note.content
    }

    notes.append(new_note)
    note_id_counter = note_id_counter + 1

    return {
        "message" : "Note Created Successfully",
        "note" : new_note
    }

@app.get("/notes")
def get_notes():
    return {
        "count": len(notes),
        "notes": notes
    }

@app.get("/notes/{note_id}")
def get_note(note_id: int):
    for note in notes:
        if(note["id"]== note_id):
            return note
    return {"error": "No Note Found!"}


@app.delete("/notes/{note_id}")
def delete_notes(note_id: int):
    for index, note in enumerate(notes):
        if(note["id"] == note_id):
            deleted_note = notes.pop(index)
            return {
                "message": "Note Deleted Successfully!",
                "Deleted Node": deleted_note
            }
    return {"error": "Node Not Found!"}

class nodeUpdate(BaseModel):
    title: str
    content: str

@app.put("/notes/{note_id}")
def update_note(note_id: int, updated_note: nodeUpdate):
    for note in notes:
        if(note["id"] == note_id):
            note["title"] = update_note.title
            note["content"] = update_note.content
            return {
                "message": "Note updated Successfully",
                "Updated Note": note
            }
    return {"error": "No Note Found"}