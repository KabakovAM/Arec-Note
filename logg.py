import datetime


def op_logger(op, id):
    time = datetime.datetime.now().strftime('%d.%m.%y || %H:%M')
    with open('log.txt', 'a', encoding='utf_8') as data_input:
        data_input.write(f'{time}; {id} {op}\n')
