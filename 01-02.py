import collections

result = []
with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    for line in f:
        file_str = line.split(' ')
        result.append((file_str[0], file_str[5][1:], file_str[6]))

spam_ip = collections.Counter(result).most_common(1)
print(spam_ip)

