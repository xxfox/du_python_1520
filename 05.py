src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
unique_nums = set()
non_unique = set()

for el in src:
    if el not in non_unique:
        unique_nums.add(el)
    else:
        unique_nums.discard(el)
    non_unique.add(el)

unique_nums_sort = [el for el in src if el in unique_nums]
print(unique_nums_sort)



