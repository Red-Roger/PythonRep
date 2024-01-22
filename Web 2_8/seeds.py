from models import Authors, Quotes
import connect
import json
import os

if os.path.exists("Web 2_8/authors.json"):
    path_a = os.getcwd() + '\\Web 2_8\\authors.json'
elif os.path.exists("authors.json"):
    path_a = 'authors.json'
if os.path.exists("Web 2_8/quotes.json"):
    path_q = os.getcwd() + '\\Web 2_8\\quotes.json'
elif os.path.exists("quotes.json"):
    path_q = 'quotes.json'


with open(path_a) as f1:
    authors = json.load(f1)
with open(path_q) as f2:
    quotes = json.load(f2)

for element in authors:
    Authors(fullname = element['fullname'], born_date = element['born_date'], born_location = element['born_location'], description = element['description']).save()

for element in quotes:
    auth = Authors.objects(fullname = element['author']).first()
    Quotes(tags = element['tags'], author = auth, quote = element['quote']).save()

