import re

re_ip = re.compile(r'^\d+[.]\d+[.]\d+[.]\d')
re_datetime = re.compile(r'\[(.+)]')
re_type = re.compile(r'GET|POST')
re_resource = re.compile(r'[/]\w+[/]\w+\s')
re_code = re.compile(r'(?<="\s)\d{3}\s')
re_size = re.compile(r'(?<=\d{3}\s)\d+')
re_from_hell = re.compile(r"(^\d+[.]\d+[.]\d+[.]\d+) .+\[(.+)] \"(GET|POST) (.+)\" (\d{3}) (\d+)")


with open('ip.txt', 'r') as f:
    for line in f:
        print(re_from_hell.findall(line))
