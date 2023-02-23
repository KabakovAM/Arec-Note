import csv
import datetime
import logg


def note_add(new_note):
    with open('id_note.csv', 'r', encoding='utf-8') as data_output:
        data = csv.reader(data_output)
        for line in data:
            id = int(*line)
    with open('id_note.csv', 'w', encoding='utf-8') as data_input:
        data = csv.writer(data_input, lineterminator='\n')
        data.writerow([id+1])
    data = datetime.datetime.now().strftime('%d.%m.%y %H:%M')
    new_note.insert(0, data)
    new_note.insert(0, id)
    with open('note.csv', 'a', encoding='utf-8') as data_input:
        data = csv.writer(data_input, delimiter=';', lineterminator='\n')
        data.writerow(new_note)
    logg.op_logger('Добавление', id)


def note_view_all():
    num_dic = {0: 0}
    i = 1
    with open('note.csv', 'r', encoding='utf-8') as data_output:
        data = csv.reader(data_output, delimiter=';')
        for line in data:
            print(f'\n{i}) Дата создания: {line[1]}\n   Заголовок: {line[2]}')
            num_dic[i] = line[0]
            i += 1
    return num_dic


def note_view(id):
    with open('note.csv', 'r', encoding='utf-8') as data_output:
        data = csv.reader(data_output, delimiter=';')
        for line in data:
            if line[0] == id:
                print(
                    f'\nДата создания: {line[1]}\nЗаголовок: {line[2]}\n{line[3]}')
    logg.op_logger('Просмотр', id)


def note_delete(id):
    delete = []
    with open('note.csv', 'r', encoding='utf-8') as data_output:
        data = csv.reader(data_output, delimiter=';')
        for line in data:
            if line[0] != id:
                delete.append(line)
    with open('note.csv', 'w', encoding='utf-8') as data_input:
        data = csv.writer(data_input, delimiter=';', lineterminator='\n')
        for i in range(0, len(delete)):
            data.writerow(delete[i])
    logg.op_logger('Удаление', id)


def note_change(id, change_note):
    with open('note.csv', 'r', encoding='utf-8') as data_output:
        data = csv.reader(data_output, delimiter=';')
        for line in data:
            if line[0] == id:
                data = datetime.datetime.now().strftime('%d.%m.%y %H:%M')
                change_note.insert(0, data)
                change_note.insert(0, id)
    note_delete(id)
    with open('note.csv', 'a', encoding='utf-8') as data_input:
        data = csv.writer(data_input, delimiter=';', lineterminator='\n')
        data.writerow(change_note)
    logg.op_logger('Изменение', id)
