import json


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


person = Person("George", 20)

jsonStr = json.dumps(person.__dict__)

print(jsonStr)
