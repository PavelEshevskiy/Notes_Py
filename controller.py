import view
import model

def start():
    while True:
        choice = view.main_menu()
        match choice:
            case 1:
                view.read_notes()
            case 2:
                model.save_notes()
            case 3:
                model.edit_note()
            case 4:
                model.del_notes()
            case 5:
                model.clear_notes()
            case 6:
                break