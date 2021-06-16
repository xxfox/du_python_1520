#Создаю список кубов нечетных чисел
numbers = []
for i in range(1, 1001, 1):
    if i % 2 != 0:
        number = i ** 3
        numbers.append(number)
print("Создан список кубов нечетных чисел: ", numbers)
#Создаю список чисел, делящихся на 7 без остатка и вычисляю их сумму
new_numbers = []
for item in numbers:
    num = item
    sum_num = 0
    while num % 10 != 0:
        sum_num += num % 10
        num = num // 10
    if sum_num % 7 == 0:
        new_numbers.append(item)
print(new_numbers)
result = 0
for number in new_numbers:
    result += number
print(result)
#Прибавляю к списку 17 и вычисляю сумму
for num in range(len(numbers)):
    numbers[num] += 17
print(numbers)
final_list = []
final_result = 0
for item in numbers:
    num = item
    sum_num = 0
    while num % 10 != 0:
        sum_num += num % 10
        num = num // 10
    if sum_num % 7 == 0:
        final_result += item
print(final_result)









