from model.note import Note
from typing import List
from datetime import datetime, date
import json
import uuid
import os.path


def save(notes: List[Note], filename):
    note_list = []
    for note in notes:
        note_list.append({
            'id': str(note.id),
            'title': note.title,
            'text': note.text,
            'date': str(note.date)
        })
    with open(filename, 'w') as f:
        json.dump(note_list, f, indent=4)


def read(filename) -> List[Note]:
    if not os.path.isfile(filename):
        return []

    with open(filename, 'r') as f:
        try:
            data = f.read()
            if not data:
                return []
            notes_data = json.loads(data)
        except json.decoder.JSONDecodeError:
            return []

    notes = []
    for note_data in notes_data:
        id = uuid.UUID(note_data['id'])
        title = note_data['title']
        text = note_data['text']
        date = datetime.strptime(note_data['date'], '%Y-%m-%d').date()
        notes.append(Note(title, text, id, date))
    return notes


def add(note: Note, notes: List[Note]):
    notes.append(note)


def edit(note: Note, title, text):
    if title != "":
        note.title = title
    if text != "":
        note.text = text
    note.date = date.today()


def delete(note: Note, notes: List[Note]):
    notes.remove(note)
