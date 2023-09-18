from datetime import datetime
import json
import text_fields

note_list = []

class Note:
    def __init__(self):
        self.note_datetime = datetime.now().strftime('%d.%m.%y / %H:%M')
        self.note_name = input('Введите заголовок заметки: ')
        self.note_text = input('Введите текст заметки: ')

    def save_dict(self):
        data = {'Дата': self.note_datetime, 'Заголовок': self.note_name, 'Текст': self.note_text}
        note_list.append(data)


def save_notes():
    note = Note()
    note.save_dict()
    with open('notes.json', 'w', encoding='UTF-8') as file:
        json.dump(note_list, file)
    print(text_fields.note_append)

def del_notes():
    with open('notes.json') as file:
        notes = json.load(file)
    del_name = input(text_fields.note_name)
    for note in notes:
        if note['Заголовок'] == del_name:
            notes.remove(note)
            with open('notes.json', 'w', encoding='UTF-8') as file:
                json.dump(notes, file)
            return(print(text_fields.note_del))
    return(print(text_fields.wrong_name))


def edit_note():
    with open('notes.json') as file:
        notes = json.load(file)
    edit_name = input(text_fields.note_name)
    for note in notes:
        if note['Заголовок'] == edit_name:
            note['Заголовок'] = input(text_fields.new_name)
            note['Текст'] = input(text_fields.edit_text)
            note['Дата'] = datetime.now().strftime('%d.%m.%y / %H:%M')
            with open('notes.json', 'w', encoding='UTF-8') as file:
                json.dump(notes, file)
            return (print(text_fields.save_text))
    return (print(text_fields.wrong_name))

def clear_notes():
    note_list = []
    with open('notes.json', 'w', encoding='UTF-8') as file:
        json.dump(note_list, file)
    print(text_fields.text_clear)