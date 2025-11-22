# 6. Создайте метакласс, который проверяет, что каждый атрибут класса является строкой. Если атрибут не является строкой, выбрасывайте исключение.
# Реализуйте метакласс, который проверяет тип атрибутов класса.
# Напишите класс с атрибутами разных типов (например, строками и числами) и убедитесь, что метакласс выбрасывает исключение, если тип атрибута некорректен.

class StringAttributesOnly(type):
    def __new__(cls, name, bases, attrs):

        for attr_name, value in attrs.items():

            if attr_name.startswith("__") and attr_name.endswith("__"):
                continue

            if not isinstance(value, str):
                raise TypeError(
                    f"Ошибка: атрибут '{attr_name}' в классе '{name}' "
                    f"должен быть строкой, а не {type(value).__name__}"
                )

        return super().__new__(cls, name, bases, attrs)

class GoodClass(metaclass=StringAttributesOnly):
    title = "Hello"
    description = "Some text"

try:
    class BadClass(metaclass=StringAttributesOnly):
        text = "OK"
        number = 123     
except Exception as e:
    print(e)
