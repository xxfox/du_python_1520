import os
import shutil

main_path = r'C:\Users\NewUser\PycharmProjects\esson 7\my_project'
copy_to = r'C:\Users\NewUser\PycharmProjects\esson 7\my_project\templates'

for root, dirs, files in os.walk(main_path):
    for dir in dirs:
        if dir == 'templates':
            print("Эту папку скопировать нельзя")
        else:
            shutil.copytree(os.path.join(root, dir), copy_to, dirs_exist_ok=True)

