# 1. Создайте дескриптор PositiveValue, который:
# Разрешает устанавливать только положительные числа. Используйте этот дескриптор в классе BankAccount для проверки баланса счета.
# Добавьте возможность создать объект BankAccount с заданным именем владельца и начальными средствами.
# Если попытаться установить отрицательное значение или ноль, выбрасывает ValueError.

class PositiveValue:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Значение должно быть положительным числом")
        instance.__dict__[self.name] = value


class Name:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError("Имя должно быть строкой")
        if not value.isalpha():
            raise ValueError("Имя должно содержать только буквы")
        if not value[0].isupper():
            raise ValueError("Имя должно начинаться с заглавной буквы")
        instance.__dict__[self.name] = value


class BankAccount:
    owner = Name()
    balance = PositiveValue()

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance


acc = BankAccount("Влад", 1000)
print(acc.owner, acc.balance)

try:
    acc.balance = -50
except ValueError as e:
    print("Ошибка:", e)

try:
    acc.owner = "ivan"
except ValueError as e:
    print("Ошибка:", e)
