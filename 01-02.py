def odd_nums(n):
    for i in range(1, n + 1, 2):
        yield i
    print('---Stop Iteration---')

"""
Второй вариант фукции с условием
"""


def odd_nums_2(n):
    for i in range(0, n + 1, 1):
        if i % 2 != 0:
            yield i
    print('---Stop Iteration---')


odd_nums_2_15 = odd_nums_2(15)
odd_nums_15 = odd_nums(15)

"""
Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя ключевое слово yield.
"""
n_max = int(input("Введите число: "))
odd_nums_gen = (el for el in range(1, n_max + 1, 2))

"""
При помощи Comprehensions
"""

odd_nums_comprehensions = [el for el in range(1, n_max + 1, 2)]
print(odd_nums_comprehensions)

