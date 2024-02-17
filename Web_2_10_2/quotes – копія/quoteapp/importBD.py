import sqlite3
import json
import os

path_a = os.getcwd() + '\\Web_2_10_2\\quotes\\quoteapp\\authors.json'
path_q = os.getcwd() + '\\Web_2_10_2\\quotes\\quoteapp\\quotes.json'
path_db = os.getcwd() + '\\Web_2_10_2\\quotes\\db.sqlite3'

conn = sqlite3.connect(path_db)

with open(path_a, 'r') as json_file:
    data = json.load(json_file)
    for item in data:
        conn.execute("INSERT INTO quoteapp_authors (fullname, born_date, born_location, description) VALUES (?, ?, ?, ?)", (item["fullname"], item["born_date"], item["born_location"], item["description"]))
conn.commit()
conn.close()