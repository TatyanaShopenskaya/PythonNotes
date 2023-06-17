import Note


def create_note(n):
    title = check_len_text_input(input('Заголовок заметки: '),n)
    body = check_len_text_input(input('Текст заметки: '),n)
    return Note.Note(title=title, body=body)


def menu():
    print("\nВведите номер нужного действия:\n\n1 - получение списка всех заметок\n2 - создание новой заметки\n3 - удаление заметки\n4 - редактирование заметки\n5 - поиск заметки по дате\n6 - поиск заметки по id\n7 - выход из приложения\n\nВведите номер действия: ")


def check_len_text_input(text, n):
    while len(text) <= n:
        text = input('Введите текст: ')
    else:
        return text


