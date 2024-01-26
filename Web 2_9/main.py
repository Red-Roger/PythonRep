from models import Authors, Quotes
import connect
import redis
from redis_lru import RedisLRU


#client = redis.StrictRedis(host="localhost", port=6379, password=None)
#cache = RedisLRU(client)

#@cache
#def author_request():
#    auth = Authors.objects(fullname__istartswith = string2search).first()
#    return auth

#def quotes_request():
#    quotes = Quotes.objects(tags__in = string2search)
#    return quotes

string2search = ""
while string2search != "exit":
    string2search = input ("Input smth to look for (<field>:<value>(type exit to exit)):")
    if string2search[:5] == "name:":
        string2search = string2search[5:].strip()
        auth = Authors.objects(fullname__istartswith = string2search).first()
        #auth = author_request()
        quotes = Quotes.objects(author = auth)
        for recs in quotes:
            print(f"name: {recs.author.fullname} quote: {recs.quote}")
    if string2search[:4] == "tag:":
        string2search = string2search[4:].strip().split(",")
        quotes = Quotes.objects(tags__in = string2search)
        #quotes = quotes_request()
        for recs in quotes:
            print(f"tags: {string2search} name: {recs.author.fullname} quote: {recs.quote}")


