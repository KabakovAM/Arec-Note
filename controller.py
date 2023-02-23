import user_interface
import note
import exception


def click_button():
    exception.exc_file()
    data = user_interface.main_menu()
    if data == 1:
        num_dic = note.note_view_all()
        if len(num_dic) == 1:
            return user_interface.empty_note()
        id = user_interface.print_note(num_dic)
        if id == 0:
            return click_button()
        return click_button_2(id)
    if data == 2:
        new_note = user_interface.new_note()
        note.note_add(new_note)
        return click_button()
    if data == 0:
        return


def click_button_2(id):
    data = user_interface.sub_menu()
    if data == 1:
        note.note_view(id)
    if data == 2:
        change_note = user_interface.change_note()
        note.note_change(id, change_note)
    if data == 0:
        note.note_delete(id)
        user_interface.delete_note()
    return click_button()
