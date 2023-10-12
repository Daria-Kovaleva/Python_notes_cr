import json
import datetime


def read_notes_file():
    try:
        with open("notes.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


notes = read_notes_file()


def save_notes(notes): # функция для сохранения заметки
    with open("notes.json", "w") as file:
        json.dump(notes, file)


def add_note(notes): # функция для создания заметки
    title = input("Введите заголовок заметки: ")
    text = input("Введите тело заметки: ")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_note = {
        'id': len(notes) + 1,
        'title': title,
        'text': text,
        'timestamp': timestamp
    }
    notes.append(new_note)
    save_notes(notes)
    print()
    print("Заметка успешно добавлена")

def print_notes(notes): # функция для вывода списка заметок
    for note in notes:
        print(f'ID: {note["id"]}')
        print(f'Заголовок: {note["title"]}')
        print(f'Тело заметки: {note["text"]}')
        print(f'Дата/время добавления или последнего изменения заметки: {note["timestamp"]}')
        print()
    if not notes:
        print('Заметок не найдено')


def filter_notes_by_date(notes): # функция для фильтрации заметок по дате
    date_str = input("Введите дату в формате ГГГГ-ММ-ДД: ")
    date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()

    filtered_notes = [note for note in notes if datetime.datetime.strptime(note["timestamp"], "%Y-%m-%d %H:%M:%S").date() == date]

    if filtered_notes:
        print("Заметки за указанную дату:")
        for note in filtered_notes:
            print(f"ID: {note['id']}")
            print(f"Заголовок: {note['title']}")
            print(f"Тело: {note['text']}")
            print(f"Дата/время добавления или последнего изменения зметки: {note['timestamp']}")
            print()
    else:
        print("Заметки за указанну дату не найдены")


def edit_note(notes): # функция для изменения заметки 
    note_id = int(input("Введите ID заметки для изменения: "))
    for note in notes:
        if note["id"] == note_id:
            new_title = input("Введите новый заголовок заметки: ")
            new_text = input("Введите новое тело заметки: ")
            note["title"] = new_title
            note["text"] = new_text
            note["timestamp"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_notes(notes)
            print("Заметка успешно изменена")
            return notes

    print("Заметка с введённым ID не найдена")


def delete_note(notes): # функция для удаления заметки
    note_id = int(input("Введите ID заметки для удаления: "))
    for note in notes:
        if note["id"] == note_id:
            notes.remove(note)
            save_notes(notes)
            print("Заметка успешно удалена")
            return notes
        else:
            print("Заметка с указанным ID не найдена")


while True:
    print()
    print("Выберите действие: ")
    print("1. Добавить новую заметку")
    print("2. Вывести все заметки")
    print("3. Вывести заметки за определённую дату")
    print("4. Изменить заметку")
    print("5. Удалить заметку")
    print("6. Выйти")

    print()

    choice = input("Введите номер действия: ")

    if choice == "1":
        add_note(notes)
    elif choice == "2":
        print_notes(notes)
    elif choice == "3":
        filter_notes_by_date(notes)
    elif choice == "4":
        edit_note(notes)
    elif choice == "5":
        delete_note(notes)
    elif choice == "6":
        break
    else:
        print("Такого действия нет")
