data = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
print(data)
for item in data:
    item_list = item.split()
    name = item_list[-1]
    print(f'Привет, {name.capitalize()}!')

