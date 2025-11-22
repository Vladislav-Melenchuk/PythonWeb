# 2. Создайте дескриптор LogDescriptor, который:
# Логирует каждый доступ к атрибуту, включая чтение и запись.

class LogDescriptor:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        print(f"Чтение атрибута {self.name}")
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        print(f"Запись атрибута {self.name}: {value}")
        instance.__dict__[self.name] = value


class TestLog:
    value = LogDescriptor()

    def __init__(self, value):
        self.value = value


t = TestLog(10)
print(t.value)
t.value = 100
