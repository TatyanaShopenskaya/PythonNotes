from datetime import datetime    # для даты
import uuid                      # для id 


class Note:
    def __init__(self, id = str(uuid.uuid1())[0:3], date = str(datetime.now().strftime("%d.%m.%Y %H:%M:%S")), title = "text", body = "text"):
        self.id = id
        self.date = date
        self.title = title
        self.body = body
        

    def get_id(note):
        return note.id

    def get_title(note):
        return note.title

    def get_body(note):
        return note.body

    def get_date(note):
        return note.date

    def set_id(note):
        note.id = str(uuid.uuid1())[0:3]

    def set_title(note, title):
        note.title = title

    def set_body(note, body):
        note.body = body

    def set_date(note):
        note.date = str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))

    def to_string(note):
        return note.id + ';'  + note.date + ';' + note.title + ';' + note.body

    def map_note(note):
        return '\nid: ' + note.id + '\n' + 'Дата и время: ' + note.date + '\n' + 'Заголовок: ' + note.title + '\n' + 'Текст заметки: ' + note.body 