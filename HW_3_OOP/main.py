# 1) Створіть класи Book і Library, які будуть взаємодіяти між собою.
class Book:
    def __init__(self, title, author, pages, book_id):
        self.title = title
        self.author = author
        self.pages = pages
        self.book_id = book_id

    def info(self):
        return f"ID: {self.book_id}, Назва: {self.title}, Автор: {self.author}, Сторінок: {self.pages}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        self.books.append(book)

    def remove_book(self, book_id):
        self.books = [book for book in self.books if book.book_id != book_id]

    def find_by_title(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book.info()
        return "Книгу не знайдено"


lib = Library()
lib.add_book(Book("Тигролови", "Іван Багряний", 250, 1))
lib.add_book(Book("Місто", "Валер’ян Підмогильний", 300, 2))

print("Завдання 1")
print(lib.find_by_title("місто"))
lib.remove_book(1)
print(lib.find_by_title("Тигролови"))
print("..................................................................................................")

# //////////////////////////////////////////////////////////////////////////////////////////////////////////

# 2) Створіть класи страва, замовлення та ресторан.
class Dish:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def description(self):
        return f"{self.name} - {self.category}, {self.price} грн"

class Order:
    def __init__(self):
        self.dishes = []

    def add_dish(self, dish: Dish):
        self.dishes.append(dish)

    def remove_dish(self, dish_name):
        self.dishes = [d for d in self.dishes if d.name != dish_name]

    def total(self):
        return sum(d.price for d in self.dishes)

class Restaurant:
    def __init__(self):
        self.menu = []

    def add_dish_to_menu(self, dish: Dish):
        self.menu.append(dish)

    def show_menu(self):
        for dish in self.menu:
            print(dish.description())

rest = Restaurant()
rest.add_dish_to_menu(Dish("Піцца Маргарита", 120, "Піцца"))
rest.add_dish_to_menu(Dish("Борщ", 80, "Суп"))
rest.add_dish_to_menu(Dish("Стейк", 250, "М’ясо"))

print("Завдання 2")
print("Меню:")
rest.show_menu()

order = Order()
order.add_dish(rest.menu[0])
order.add_dish(rest.menu[2])

print("\nСума замовлення:", order.total(), "грн")
print("..................................................................................................")

# //////////////////////////////////////////////////////////////////////////////////////////////////////////

# 3) Облік студентів з файлами

import json

class Student:
    def __init__(self, name, age, grades: list):
        self.name = name
        self.age = age
        self.grades = grades

    def average_grade(self):
        return sum(self.grades) / len(self.grades)

class StudentDatabase:
    def __init__(self, filename):
        self.filename = filename

    def add_student(self, student: Student):
        try:
            students = self.read_students()
        except:
            students = []

        students.append({
            "name": student.name,
            "age": student.age,
            "grades": student.grades
        })

        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(students, f, ensure_ascii=False, indent=4)

    def read_students(self):
        with open(self.filename, "r", encoding="utf-8") as f:
            return json.load(f)

    def find_student(self, name):
        students = self.read_students()
        for st in students:
            if st["name"].lower() == name.lower():
                return st
        return "Студента не знайдено"

db = StudentDatabase("students.json")

student1 = Student("Влад", 20, [90, 85, 100])
student2 = Student("Аня", 19, [70, 88, 95])

db.add_student(student1)
db.add_student(student2)

print("Завдання 3")
print(db.read_students())
print(db.find_student("Влад"))
print("..................................................................................................")
