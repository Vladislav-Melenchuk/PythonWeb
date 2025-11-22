# 4. Создайте метакласс, который автоматически добавляет в каждый класс метод hello(), который выводит строку "Hello from <имя класса>".
# Реализуйте метакласс, который добавляет метод hello() в каждый класс.
# Напишите несколько классов, использующих этот метакласс, и вызовите метод hello() для каждого класса.

class HelloMeta(type):
    def __new__(cls, name, bases, attrs):

        def hello(self):
            print("Hello from", name)

        attrs["hello"] = hello

        new_class = super().__new__(cls, name, bases, attrs)
        return new_class


class A(metaclass=HelloMeta):
    pass


class B(metaclass=HelloMeta):
    value = 10


class C(metaclass=HelloMeta):
    def foo(self):
        return "bar"
    
a = A()
b = B()
c = C()

a.hello()
b.hello()
c.hello()
