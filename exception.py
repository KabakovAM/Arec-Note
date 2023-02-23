import csv
import user_interface


def menu(num, n):
    if num.isdigit() and 0 <= int(num) <= n:
        return True
    return False


def id_note(id, num_dic):
    if int(id) in num_dic or int(id) == 0:
        return True
    return False


def exc_file():
    try:
        file_1 = open('id_note.csv')
    except IOError as e:
        with open('id_note.csv', 'w') as data_input_1:
            data = csv.writer(data_input_1, lineterminator='\n')
            data.writerow('0')
            user_interface.exc_file(0)
    try:
        file_2 = open('note.csv')
    except IOError as e:
        with open('note.csv', 'w') as data_input_2:
            user_interface.exc_file(1)
