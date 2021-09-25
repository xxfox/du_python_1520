import json
import os

main_path = r'my_project\templates'
all_files = list((item for item in os.scandir(main_path)))
keys = (10, 50, 100)
info_dict = {}

for key in keys:
    count = 0
    extension = []
    for file in all_files[:]:
        if os.stat(file).st_size < key:
            extension.append(((file.name).split('.'))[-1])
            count += 1
            if file.name in extension:
                all_files.remove(file)
    info_dict[key] = (count, list(set(extension)))
print(info_dict)

with open('extension.json', 'w') as f:
    json.dump(info_dict, f)
