sentence = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
print(id(sentence))
for index, i in enumerate(sentence):
    if i.isalpha() == False:
        sentence[index] = i.zfill(2)
        if not i.isalpha() and not i.isdigit():
            sentence[index] = i.zfill(3)
print(sentence)
count = 0
for index, i in enumerate(sentence[count:]):
    if i.isalpha() == False:
        sentence.insert(index + count, '"')
        sentence.insert(index + count + 2, '"')
        count += 2
print(sentence)
print(' '.join(sentence))
print(id(sentence))
