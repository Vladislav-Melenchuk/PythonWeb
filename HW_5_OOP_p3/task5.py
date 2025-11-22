# 5. Напишите метакласс, который не позволяет классам наследовать другие классы, если в имени родительского класса есть подстрока "Forbidden".
# Реализуйте метакласс, который проверяет имя родительского класса и запрещает наследование от классов с подстрокой "Forbidden" в имени.
# Напишите несколько классов с этим метаклассом, и попробуйте создать класс, наследующий от запрещенного класса.

class NoForbiddenMeta(type):
    def __new__(cls, name, bases, attrs):

        for parent in bases:
            if "Forbidden" in parent.__name__:
                raise TypeError(
                    f"Нельзя наследоваться от класса {parent.__name__}, "
                    f"так как он содержит 'Forbidden' в имени!"
                )

        return super().__new__(cls, name, bases, attrs)


class ForbiddenClass:
    pass


class Normal(metaclass=NoForbiddenMeta):
    pass

try:
    class BadChild(ForbiddenClass, metaclass=NoForbiddenMeta):
        pass
except Exception as e:
    print("Ошибка:", e)

class GoodChild(Normal, metaclass=NoForbiddenMeta):
    pass

g = GoodChild()
print("GoodChild создан")
