from fastapi import APIRouter
from models.note import noteCreate, nodeUpdate
from services import notes_service

router = APIRouter()

@router.post("/notes", status_code = 201)
def create_note(note: noteCreate):
    return notes_service.create_note(note)

@router.get("/notes")
def get_notes():
    return notes_service.get_all_notes()

@router.get("/notes/{note_id}")
def get_note_by_id(note: int):
    return notes_service.get_note_by_id(note)

@router.put("/notes/{note_id}")
def update(note_id: int, note: nodeUpdate):
    return notes_service.update_note(note_id, note)

@router.delete("/notes/{note_id}")
def delete(note_id: int):
    return notes_service.delete_notes(note_id)