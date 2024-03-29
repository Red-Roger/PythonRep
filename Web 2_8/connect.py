from mongoengine import connect
import configparser
import time
import os

config = configparser.ConfigParser()


if os.path.exists("Web 2_8/config.ini"):
    config.read('Web 2_8/config.ini')
elif os.path.exists("config.ini"):
    config.read('config.ini')

mongo_user = config.get('DB', 'user')
mongodb_pass = config.get('DB', 'pass')
db_name = config.get('DB', 'db_name')
domain = config.get('DB', 'domain')

connect(host=f"""mongodb+srv://{mongo_user}:{mongodb_pass}@{domain}/{db_name}?retryWrites=true&w=majority""", ssl=True)

time.sleep(1)