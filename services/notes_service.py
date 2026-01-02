from fastapi import HTTPException


notes = []

note_id_counter = 1

def create_note(note):
    global note_id_counter

    if not note.title.strip():
        raise HTTPException(status_code = 400, detail = "Title Cannot be empty")

    new_note = {
        "id": note_id_counter,
        "title": note.title,
        "content": note.content
    }

    notes.append(new_note)
    note_id_counter = note_id_counter + 1

    return new_note

def get_all_notes():
    return notes

def get_note_by_id(note_id: int):
    for note in notes:
        if(note["id"]== note_id):
            return note
    raise HTTPException(
        status_code = 404,
        detail = "Node Not Found"
    )


def delete_notes(note_id: int):
    for index, note in enumerate(notes):
        if(note["id"] == note_id):
            deleted_note = notes.pop(index)
            return deleted_note
    raise HTTPException(
        status_code = 404,
        detail = "Node Not Found"
    )

def update_note(note_id: int, updated_note):
    for note in notes:
        if(note["id"] == note_id):
            note["title"] = updated_note.title
            note["content"] = updated_note.content
            return note
    raise HTTPException(
        status_code = 404,
        detail = "Node Not Found"
    )