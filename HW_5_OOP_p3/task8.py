# 8. Создайте протокол Serializable, который требует реализации метода serialize(). Реализуйте два класса: Person и Book, которые будут реализовывать этот метод для преобразования объектов в строковый формат JSON.
# Протокол Serializable должен содержать метод serialize().
# Классы Person и Book должны реализовывать метод serialize(), возвращающий строку в формате JSON.
# Напишите функцию serialize_object(), которая будет принимать объект и вызывать его метод serialize().

from typing import Protocol
import json

class Serializable(Protocol):
    def serialize(self) -> str:
        ...

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def serialize(self) -> str:
        return json.dumps({
            "name": self.name,
            "age": self.age
        })

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def serialize(self) -> str:
        return json.dumps({
            "title": self.title,
            "author": self.author,
            "year": self.year
        })

def serialize_object(obj: Serializable) -> str:
    return obj.serialize()

p = Person("Vlad", 20)
b = Book("Python OOP", "James Smith", 2022)

print(serialize_object(p))
print(serialize_object(b))
