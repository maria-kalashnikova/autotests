"""
utf-8
Создан 03.11.2021

:author: maria.kalashnikova

Обучающий курс Python QA Engineer.
Домашняя работа №3. Распределитель книг между студентами.
"""
from csv import DictReader
import json

# Читаем данные по пользователям из файла и сохраняем в переменную
with open("users.json",  'r', newline='', encoding='utf-8') as users_file:
    users = json.loads(users_file.read())

# Читаем данные по книгам из файла и сохраняем в переменную
with open("books.csv",  'r', newline='', encoding='utf-8') as books_file:
    reader = DictReader(books_file)
    books = []
    for row in reader:
        books.append(row)

# Распределяем кинги по пользователям
user_index = 0
book_index = 0
while book_index != len(books) - 1:
    if user_index == len(users):
        user_index = 0
    if book_index <= user_index:
        users[user_index]["books"] = []
    users[user_index]["books"].append(books[book_index])
    user_index += 1
    book_index += 1

# Записываем результирующий файл
with open("result.json",  'w', newline='', encoding='utf-8') as results_file:
    json.dump(users, results_file, indent=4)
