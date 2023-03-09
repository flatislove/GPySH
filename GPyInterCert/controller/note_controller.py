from controller import operation_controller
from view import menu
from service import note_service

filename = "notes.json"
notes = note_service.read(filename)


def run():

    while True:
        menu.clear()
        action = menu.show_menu()
        if action == "0":
            break
        if action == "1":
            menu.clear()
            menu.show_message("\nALL NOTES")
            operation_controller.show_note(notes)
            menu.wait_input()
        elif action == "2":
            menu.clear()
            menu.show_message("\nADD NOTE")
            operation_controller.add_note(notes)
            menu.wait_input()
        elif action == "3":
            menu.clear()
            menu.show_message("\nFIND NOTE BY TEXT")
            operation_controller.find_by_note(notes)
            menu.wait_input()
        elif action == "4":
            menu.clear()
            menu.show_message("\nFIND NOTE BY DATE")
            operation_controller.find_by_date(notes)
            menu.wait_input()
        elif action == "5":
            menu.clear()
            menu.show_message("\nDELETE NOTE")
            operation_controller.delete_note(notes)
            menu.wait_input()
        elif action == "6":
            menu.clear()
            menu.show_message("\nEDIT NOTE")
            operation_controller.edit_note(notes)
            menu.wait_input()
        elif action == "7":
            menu.clear()
            menu.show_message("\nSAVE TO FILE")
            note_service.save(notes, filename)
