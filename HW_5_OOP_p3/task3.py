# 3. Напишите метакласс, который не позволяет создавать классы с атрибутами, начинающимися с подчеркивания. 
# Если класс содержит такие атрибуты, метакласс должен выбрасывать исключение.
# Реализуйте метакласс, который проверяет атрибуты класса на соответствие этому ограничению.
# Напишите несколько классов с атрибутами, начинающимися с подчеркивания, и убедитесь, что будет выброшено исключение.

class NoPrivateAttributes(type):
    def __new__(cls, name, bases, attrs):
        for attr_name in attrs:
            if attr_name.startswith("_"):
                raise AttributeError(
                    f"Нельзя создавать атрибуты, начинающиеся с '_' в классе '{name}': {attr_name}"
                )

        return super().__new__(cls, name, bases, attrs)


class GoodClass(metaclass=NoPrivateAttributes):
    x = 10
    y = 20


try:
    class BadClass1(metaclass=NoPrivateAttributes):
        _secret = 123
except Exception as e:
    print("Ошибка:", e)

try:
    class BadClass2(metaclass=NoPrivateAttributes):
        value = 42
        _hidden_method = lambda self: None
except Exception as e:
    print("Ошибка:", e)
