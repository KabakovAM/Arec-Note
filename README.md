# Arec-Note

## Программа создана для работы с заметками. Реализованы функции просмотра, создания, изменения и удаления заметок. Для хранения заметок используются файлы формата csv. При выводе в консоль заметки сортируются по дате создания/изменения. Реализована защита от неправильного ввода данных в консоль и автоматического создания необходимых файлов для работы программы при их отсутствии.

## Модули:
* main - запуск программы.
* controller - контроллер всей программы, осуществляет взаимодействие между модулями.
* user_interface - пользовательский интерфейс, ввод и вывод данных из консоли.
* note - основной модуль программы в котором выполняются основные действия.
* exception - модуль ошибок и защиты от неверного ввода команд в консоль.
* logg - модуль логирования.
## Файлы:
* id_note - хранит в себе номер id заметок.
* note - хранит в себе заметки.
