import os
from model.note import Note
from typing import List


def show_menu():

    while True:
        clear()
        print("Choose operation:")
        print("1 - See All Notes")
        print("2 - Add Note")
        print("3 - Find by substring")
        print("4 - Find by date")
        print("5 - Delete Note")
        print("6 - Edit Note")
        print("7 - Save to file")
        print("0 - exit")
        action = input("Enter the action: ")
        if action in ["0", "1", "2", "3", "4", "5", "6", "7"] and len(action) == 1:
            return action


def clear():
    os.system('clear')


def show_message(message):
    print(message)


def wait_input():
    input("Press any key...")


def get_value(message):
    print(f"{message}: ", end="")
    return input()


def show_minimalize_notes(notes: List[Note]):
    number = 1
    for note in notes:
        print("# ", number)
        number += 1
        print(note)
        print("\n")


def show_note(note:Note):
    clear()
    if note == None:
        print("Note is null")
    else:
        print("ID:\n",note.id)
        print("TITLE:\n", note.title)
        print("DATE CREATE/UPDATE:\n", note.date)
        print("TEXT:\n", note.text)
