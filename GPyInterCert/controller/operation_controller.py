from service import note_service
from view import menu
from model.note import Note
import datetime
from service import input_check_service


def add_note(notes):
    title = menu.get_value("Enter title")
    text = menu.get_value("Enter text")
    note = Note(title, text)
    notes.append(note)
    menu.show_message("Note added successfully!")


def find_by_note(notes):
    substring = menu.get_value("Enter text to search")
    found_notes = []
    for note in notes:
        if substring in note.title or substring in note.text:
            found_notes.append(note)
    menu.show_minimalize_notes(found_notes)


def find_by_date(notes):
    menu.show_message("Date format: YYYY-MM-dd")
    begin_date_str = menu.get_value("Enter start date")
    end_date_str = menu.get_value("Enter end date")
    if input_check_service.check_date(begin_date_str) and input_check_service.check_date(end_date_str):
        begin_date = datetime.datetime.strptime(
            begin_date_str, '%Y-%m-%d').date()
        end_date = datetime.datetime.strptime(end_date_str, '%Y-%m-%d').date()
        filtered_notes = list(
            filter(lambda x: begin_date <= x.date <= end_date, notes))
        menu.show_minimalize_notes(filtered_notes)
    else:
        menu.show_message("Incorrect format")


def delete_note(notes):
    menu.show_minimalize_notes(notes)
    index = menu.get_value("Enter the Note #(number) to delete")
    if input_check_service.check_correct_index(notes, index):
        del notes[int(index)-1]
        menu.show_message("Note successfully deleted!")
    else:
        menu.show_message("Incorrect value")


def edit_note(notes):
    menu.show_minimalize_notes(notes)
    index = menu.get_value("Enter the Note #(number) to edit")
    if input_check_service.check_correct_index(notes, index):
        title = menu.get_value(
            "Enter a new title value (press Enter to leave the old value)")
        text = menu.get_value(
            "Enter a new text value (press Enter to leave the old value)")
        note_service.edit(notes[int(index)-1], title, text)
        menu.show_message("Note edited successfully!")
    else:
        menu.show_message("Incorrect value")


def show_note(notes):
    menu.show_minimalize_notes(notes)
    index = menu.get_value("Enter the Note #(number) to show")
    if input_check_service.check_correct_index(notes, index):
        menu.show_note(notes[int(index)-1])
    else:
        menu.show_message("Incorrect value")
