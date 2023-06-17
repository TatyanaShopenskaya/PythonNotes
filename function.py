import operation
import Note
import ui

n=1

def add():
    note = ui.create_note(n)
    array = operation.read_file()
    for notes in array:
        if Note.Note.get_id(note) == Note.Note.get_id(notes):
            Note.Note.set_id(note)
    array.append(note)
    operation.write_file(array, 'a')


def show(text):
    logic = True
    array = operation.read_file()
    if text == 'date':
        date = input('Введите дату для поиска заметки в формате ДД.ММ.ГГГГ:')
    for notes in array:
        if text == 'all':
            logic = False
            print(Note.Note.map_note(notes))
        if text == 'id':
            logic = False
            print('id: ' + Note.Note.get_id(notes))
        if text == 'date':
            logic = False
            if date in Note.Note.get_date(notes):
                print(Note.Note.map_note(notes))
    if logic == True:
        print('Заметки по данным параметрам не найдены.')


def id_edit_del_show(text):
    id = input('Введите id заметки: ')
    array = operation.read_file()
    logic = True
    for notes in array:
        if id == Note.Note.get_id(notes):
            logic = False
            if text == 'edit':
                note = ui.create_note(n)
                Note.Note.set_title(notes, note.get_title())
                Note.Note.set_body(notes, note.get_body())
                Note.Note.set_date(notes)
    
            if text == 'del':
                array.remove(notes)
            
            if text == 'show':
                print(Note.Note.map_note(notes))
    if logic == True:
        print('Попробуйте еще раз, данный id не обнаружен')
    operation.write_file(array, 'a')