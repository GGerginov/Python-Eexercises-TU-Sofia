import json


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


personJson = '{ "name":"George", "age":20}'

person = json.loads(personJson)

output = Person(person["name"], person["age"])

print(output.name)
print(output.age)
