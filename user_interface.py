import exception
import controller


def main_menu():
    print('\nArec-Note\nВыберите опцию:')
    print('\n1) Просмотр заметок.\n2) Создать заметку.\n0) Выйти из программы')
    data = input()
    if exception.menu(data, 2):
        return int(data)
    print('\nВведено неверное значение. Потворите ввод.')
    return main_menu()


def sub_menu():
    print('\nВыберите опцию:')
    print('\n1) Просмотреть заметку.\n2) Изменить заметку.\n0) Удалить заметку.')
    data = input()
    if exception.menu(data, 2):
        return int(data)
    print('\nВведено неверное значение. Потворите ввод.')
    return sub_menu()


def print_note(num_dic):
    print('\nВведите номер заметки для просмотра, изменения или удаления или нажмите 0 для выхода в главное меню.')
    data = input()
    if exception.id_note(data, num_dic):
        return num_dic[int(data)]
    print('\nВведено неверное значение. Потворите ввод.')
    return print_note(num_dic)


def new_note():
    lis = list()
    print('\nВведите заголовок заметки:')
    lis.append(input())
    print('\nВведите текст заметки:')
    lis.append(input())
    print('\nЗаметка успешно добавлена. Возврат в главное меню.')
    return lis


def change_note():
    lis = list()
    print('\nВведите новый заголовок заметки:')
    lis.append(input())
    print('\nВведите новый текст заметки:')
    lis.append(input())
    print('\nЗаметка успешно изменена. Возврат в главное меню.')
    return lis


def delete_note():
    print('\nЗаметка успешно удалена. Возврат в главное меню.')


def empty_note():
    print('\nЗаметок нет. Возврат в главное меню.')
    return controller.click_button()


def exc_file(num):
    if num == 0:
        print(
            '\nФайл id_note.csv не найден. Для работы приложения создан новый файл.')
    if num == 1:
        print('\nФайл note.csv не найден. Для работы приложения создан новый файл.')
