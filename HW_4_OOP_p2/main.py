# Завдання 1
class Engine:
    def start_engine(self):
        print("Двигатель запустился")

    def stop_engine(self):
        print("Двигатель заглушон")


class Vehicle:
    def __init__(self, max_speed):
        self.max_speed = max_speed

    def drive(self):
        print(f"Едет на максимальной скорости: {self.max_speed}")


class Car(Engine, Vehicle):
    def __init__(self, model, max_speed):
        Vehicle.__init__(self, max_speed)
        self.model = model

    def drive(self):
        print(f"Модель: {self.model} едет со скоростью -> {self.max_speed}")


class Boat(Engine, Vehicle):
    def __init__(self, boat_type, max_speed):
        Vehicle.__init__(self, max_speed)
        self.boat_type = boat_type

    def drive(self):
        print(f"{self.boat_type} плывет со скоростью -> {self.max_speed}")


class AmphibiousVehicle(Car, Boat):
    def __init__(self, model, boat_type, max_speed, is_on_land=True):
        Car.__init__(self, model, max_speed)
        Boat.__init__(self, boat_type, max_speed)
        self.is_on_land = is_on_land

    def drive(self):
        if self.is_on_land:
            print(f"{self.model} едет со скоростью -> {self.max_speed}")
        else:
            print(f"{self.boat_type} плывет со скоростью -> {self.max_speed}")


print("=== Анфибия ===")
amphi = AmphibiousVehicle("AmphiX", "motor boat", 60, is_on_land=True)
amphi.start_engine()
amphi.drive()
amphi.is_on_land = False
amphi.drive()
amphi.stop_engine()

# Завдання 2
class Book:
    def __init__(self, title, author, pages):
        self._title = title
        self._author = author
        self._pages = pages

    @property
    def title(self):
        return self._title
    
    @property
    def author(self):
        return self._author

    @property
    def pages(self):
        return self._pages

    def __lt__(self, other):
        return self.pages < other.pages

    def __le__(self, other):
        return self.pages <= other.pages

    def __gt__(self, other):
        return self.pages > other.pages

    def __ge__(self, other):
        return self.pages >= other.pages

    def __eq__(self, other):
        return self.pages == other.pages

    def __str__(self):
        return f"'{self.title}' автор: {self.author} ({self.pages} страниц)"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        self.books.append(book)

    def __iadd__(self, book: Book):
        self.add_book(book)
        return self

    def remove_book(self, book: Book):
        if book in self.books:
            self.books.remove(book)

    def __isub__(self, book: Book):
        self.remove_book(book)
        return self

    def __contains__(self, book: Book):
        return book in self.books

    def __len__(self):
        return len(self.books)

lib = Library()

b1 = Book("Кобзар", "Тарас Шевченко", 350)
b2 = Book("Тигролови", "Іван Багряний", 280)

lib += b1
lib += b2

print(len(lib))       
print(b1 in lib)      
print(b1 > b2)        
lib -= b2
print(len(lib))       
print(b1)

# Завдання 3
class MethodCache:
    def __init__(self, method):
        self.method = method
        self.cache = {}

    def __get__(self, instance, owner):
        def wrapper(*args, **kwargs):
            key = (args, tuple(kwargs.items()))

            if key in self.cache:
                print("вернул")
                return self.cache[key]

            result = self.method(instance, *args, **kwargs)
            self.cache[key] = result
            return result

        return wrapper

class Calculator:
    @MethodCache
    def multiply(self, a, b):
        print("...")
        return a * b


calc = Calculator()

print(calc.multiply(3, 5))
print(calc.multiply(3, 5))  
print(calc.multiply(2, 10))
print(calc.multiply(2, 10))  
