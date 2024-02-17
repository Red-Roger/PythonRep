import psycopg2
import json
import os
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "notes.settings")
try:
    from django.core.management import execute_from_command_line
except ImportError as exc:
    raise ImportError(
        "Couldn't import Django. Are you sure it's installed and "
        "available on your PYTHONPATH environment variable? Did you "
        "forget to activate a virtual environment?"
    ) from exc
execute_from_command_line(sys.argv)



from .models import Authors


def imp():


    #path_a = os.getcwd() + '\\Web_2_10_2\\quotes\\quotes\\quoteapp\\authors.json'
    #path_q = os.getcwd() + '\\Web_2_10_2\\quotes\\quotes\\quoteapp\\quotes.json'

    path_a = os.getcwd() + '\\quoteapp\\authors.json'
    path_q = os.getcwd() + '\\quoteapp\\quotes.json'

    path_db = 'dbname=postgres user=postgres password=root'

    conn = psycopg2.connect(path_db)
    #cur = conn.cursor()
    """
    with open(path_a, 'r') as json_file:
        data = json.load(json_file)
        for item in data:
            cur.execute("INSERT INTO quoteapp_authors (fullname, born_date, born_location, description) VALUES (%s, %s, %s, %s)", (item["fullname"], item["born_date"], item["born_location"], item["description"]))

    with open(path_q, 'r') as json_file:
        data = json.load(json_file)
        for item in data:
            cur.execute("INSERT INTO quoteapp_quotes (tags, quote) VALUES (%s, %s)", (item["tags"], item["quote"]))
    """
    #cur.close()


    with open(path_a, 'r') as json_file:
        data = json.load(json_file)
        for item in data:
            Authors.objects.create (fullname = item["fullname"], born_date = item["born_date"], born_location = item["born_location"], description = item["description"])

    conn.commit()
    conn.close()

if __name__ == "__main__":
    imp()