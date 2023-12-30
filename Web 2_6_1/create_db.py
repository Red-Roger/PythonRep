import sqlite3
import os

def create_db():
    # читаємо файл зі скриптом для створення БД
    current_dir = os.getcwd()
    current_script = current_dir + '\\Web 2_6_1\\courses.sql'
    with open(current_script, 'r') as f:
        sql = f.read()

    # створюємо з'єднання з БД (якщо файлу з БД немає, він буде створений)
    current_db = current_dir + '\\Web 2_6_1\\courses.db'
    with sqlite3.connect(current_db) as con:
        cur = con.cursor()
        # виконуємо скрипт із файлу, який створить таблиці в БД
        cur.executescript(sql)


if __name__ == "__main__":
    create_db()