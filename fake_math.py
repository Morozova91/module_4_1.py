from math import inf


# Создайте модули fake_math и true_math
# в которых создайте функции отвечающие за деление, но разными способами.
# В fake_math создайте функцию divide,
# которая принимает два параметра first и second.
# Функция должна возвращать результат деления first на second, но когда в second записан 0 - возвращать строку 'Ошибка'.
# В true_math создайте функцию divide, которая принимает два параметра first и second. Функция должна возвращать результат деления first на second, но когда в second записан 0 - возвращать бесконечность.
def divide(first, second):
    if second == 0:
        return 'Ошибка'
    else:
        return first/second


res1 = divide(5, 0)
res2 = divide(6,3)
print(res1)
print(res2)