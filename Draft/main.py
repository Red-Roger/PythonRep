import collections

Cat = collections.namedtuple("Cat", ["nickname", "age", "owner"])


def convert_list(cats):
    result = []
    if isinstance (cats[0], tuple):
        for value in cats:
            diction = {}
            diction["nickname"] = value.nickname
            diction["age"] = value.age
            diction["owner"] = value.owner
            result.append (diction)
    
    if isinstance (cats[0], dict):
        Cat = collections.namedtuple("Cat", ["nickname", "age", "owner"])
        for value in cats:
            cat = Cat(value["nickname"], value["age"], value["owner"])
            result.append (cat)
    return result


param1 = [
    {"nickname": "Mick", "age": 5, "owner": "Sara"},
    {"nickname": "Barsik", "age": 7, "owner": "Olga"},
    {"nickname": "Simon", "age": 3, "owner": "Yura"},
]

param2 = [Cat("Mick", 5, "Sara"), Cat("Barsik", 7, "Olga"), Cat("Simon", 3, "Yura")]

cats = param1
print (convert_list (cats))