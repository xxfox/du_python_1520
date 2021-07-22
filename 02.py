import yaml
import os


def create_file(path, name):
    os.chdir(path)
    if name not in os.listdir(path):
        with open(name, 'w', encoding='utf-8') as f:
            print(f'Создан файл: {name}')
            f.write('')


def create_folder(path, name):
    if name not in os.listdir():
        os.mkdir(os.path.join(path, name))
        print("It's ok")


def is_file_or_folder(path, name):
    if name.find('.') != -1:
        create_file(path, name)
    else:
        create_folder(path, name)


config = yaml.load_all(open('config.yaml'), Loader=yaml.Loader)
main_path = os.getcwd()

for item in config:
    for key, value in item.items():
        is_file_or_folder(main_path, key)
        child_path = os.path.join(main_path, key)
        for i in value:
            if type(i) == dict:
                for k, v in i.items():
                    is_file_or_folder(child_path, k)
                    is_file_or_folder(os.path.join(child_path, k), v)
            else:
                is_file_or_folder(os.path.join(main_path, key), i)