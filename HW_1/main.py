#HomeWork 1

#1. Створіть функцію, яка підраховує кількість цифр у числі

def Counter(num):
    return len(str(abs(num)))

print("\nTask 1")
print("Result of 54:", Counter(54))

#2. Користувач вводить рядок, необхідно отримати кількість повторень кожного слова в рядку. Ігноруємо коми, крапки.

def word_counter(text):
    text = text.replace(",", "").replace(".", "")
    words = text.split()
    result = {}
    for word in words:
        word = word.lower()
        result[word] = result.get(word, 0) + 1
    return result

print("\nTask 2")
print("Result:", word_counter("Привет, я выполнил задание. Привет!"))

# 3. Створити список із цілих чисел. Його необхідно відфільтрувати, щоб у результаті залишилися парні числа. Вивести квадрати цих чисел, використовуючи map.

numbers = [1, 2, 3, 4, 5, 6]
even = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers)))
print("\nTask 3")
print("Result:", even)

# 4. Створіть словник, у якому кожна пара — це студент і список його оцінок
# * Вивести по кожному студенту середній бал
# * Вивести студента з максимальною оцінкою

students = {
    "Олег": [5, 4, 3],
    "Влад": [5, 5, 4],
    "Аня": [3, 3, 4]
}
for name, grades in students.items():
    avg = sum(grades) / len(grades)
max_student = max(students, key=lambda x: max(students[x]))
print("\nTask 4")
print("Result:", max_student)

# 5. Напишіть функцію, яка приймає рядок і повертає словник, де ключ — це символ рядка, а значення — кількість його повторень.

def char_count(s):
    result = {}
    for ch in s:
        result[ch] = result.get(ch, 0) + 1
    return result

print("\nTask 5")
print("Result:", char_count("Audi"))

# 6. Створіть кортеж із кількох рядків і чисел. Напишіть функцію, яка повертає новий кортеж, що містить лише числа.

def task_6(t):
    return tuple(i for i in t if isinstance(i, (int, float)))

print("\nTask 6")
print("Result:", task_6(("привіт", 10, 3.5, "hi", 7)))

# 7. Напишіть функцію, яка приймає список рядків і повертає список, у якому рядки відсортовані за довжиною.

def sort_by_length(lst):
    return sorted(lst, key=len)

print("\nTask 7")
print("Result:", sort_by_length(["авто", "пес", "квас"]))

# 8. Створіть словник із даними про співробітників компанії (ім’я, посада, зарплата). Напишіть функцію, яка сортує співробітників за зарплатою.

employees = [
    {"ім'я": "Іван", "посада": "менеджер", "зарплата": 12000},
    {"ім'я": "Оля", "посада": "бухгалтер", "зарплата": 25000},
    {"ім'я": "Петро", "посада": "кур'єр", "зарплата": 13500}
]

def sort_by_salary(data):
    return sorted(data, key=lambda x: x["зарплата"])

print("\nTask 8")
print("Result:", sort_by_salary(employees))

# 9. Використовуючи лямбда-вираз, створіть функцію, яка повертає найбільше з двох чисел.

max_num = lambda a, b: a if a > b else b

print("\nTask 9")
print("Result:", max_num(5, 9))

# 10. Напишіть функцію, яка знаходить усі унікальні елементи в списку і повертає їх у вигляді множини.

def task_10(lst):
    return set(lst)

print("\nTask 10")
print("Result:", task_10([1, 2, 2, 3, 4, 4]))


# 11. Створіть словник, де ключі — це числа від 1 до 10, а значення — їхні квадрати. Напишіть функцію, яка знаходить суму всіх значень у словнику.

def squares_sum():
    d = {i: i**2 for i in range(1, 11)}
    return sum(d.values())

print("\nTask 11")
print("Result:", squares_sum())


# 12. Напишіть функцію, яка приймає список чисел і повертає новий список, що містить лише ті числа, які більші за 10 і парні.

def filter_numbers(lst):
    return [x for x in lst if x > 10 and x % 2 == 0]

print("\nTask 12")
print("Result:", filter_numbers([4, 11, 12, 20, 3]))

# 13. Створіть кортеж із кількох чисел. Напишіть функцію, яка знаходить суму всіх чисел у кортежі.

def sum_tuple(t):
    return sum(t)

print("\nTask 13")
print("Result:", sum_tuple((1, 2, 3, 4)))


# 14. Напишіть лямбда-функцію, яка перевіряє, чи є число додатним.

is_positive = lambda x: x > 0

print("\nTask 14")
print("Result:", is_positive(-5))


# 15. Створіть словник, у якому зберігаються імена людей і їхній вік. Напишіть функцію, яка приймає вік і повертає список імен людей, старших за цей вік.

people = {"Іван": 25, "Оля": 30, "Петро": 19}

def older_than(age):
    return [name for name, a in people.items() if a > age]

print("\nTask 15")
print("Result:", older_than(20))

# 16. Створіть кортеж із чисел і напишіть функцію, яка знаходить найбільше і найменше значення в кортежі.

def min_max(t):
    return min(t), max(t)

print("\nTask 16")
print("Result:", min_max((4, 1, 8, 2)))

# 17. Використовуючи лямбда-вираз і функцію filter, знайдіть усі числа, які діляться на 3, у списку чисел.

nums = [1, 3, 6, 7, 9, 12, 14]
div_by_3 = list(filter(lambda x: x % 3 == 0, nums))
print("\nTask 17")
print("Result:", div_by_3)

# 18. Напишіть функцію, яка перетворює рядок у список кортежів, де кожен кортеж містить символ і його індекс у рядку.

def string_to_tuples(s):
    return [(ch, i) for i, ch in enumerate(s)]

print("\nTask 18")
print("Result:", string_to_tuples("Hello"))