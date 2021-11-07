# Создайте два класса Directory (папка) и File (файл).
# Класс Directory должен иметь следующие поля:
#     - название (name типа str);
#     - родительская папка (root типа Directory);
#     - список файлов (files типа список, состоящий из экземпляров File)
#     - список подпапок (sub_directories типа список, состоящий из экземпляров Directory).
# Класс Directory должен иметь следующие поля:
#     - добавление папки в список подпапок (add_sub_directory принимающий экземпляр Directory и
#         присваивающий поле root для принимаемого экземпляра);
#     - удаление папки из списка подпапок (remove_sub_directory, принимающий экземпляр Directory
#         и обнуляющий у него поле root. Метод также удаляет папку из списка sub_directories).
#     - добавление файла в папку (add_file, принимающий экземпляр File и присваивающий ему поле
#       directory - см. класс File ниже);
#     - удаление файла из папки (remove_file, принимающий экземпляр File и обнуляющий у него поле
#      directory. Метод удаляет файл из списка files).
# Класс File должен иметь следующие поля:
#     - название (name типа str);
#     - папка (directory типа Directory);

from typing import *


class Directory:
    td = TypeVar('type_directory')
    # name: str
    # root: td
    # file_list: list = []
    # sub_directories: list = []

    def __init__(self, name: str, root: td, file_list: list, sub_directories: list):
        self.name = name
        self.root = root
        self.f_list = file_list
        self.s_dir: list = sub_directories

    def add_sub_directory(self, dir: td):
        dir.root = self.name
        return self.s_dir.append(self)

    def remove_sub_directory(self):
        self.root = None
        return self.s_dir.remove(self)

    def add_file(self, file: 'File'):
        file.dir = self.name
        return self.f_list.append(file)

    def remove_file(self, file: 'File'):
        file.dir = None
        return self.f_list.remove(file)


class File:
    def __init__(self, name: str, directory: 'Directory' = None):
        self.name = name
        self.dir = directory


a = Directory('A', 'main', [], [])
b1 = Directory('B1', None, [], [])
b2 = Directory('B2', None, [], [])
f1 = File('F1.txt')
f2 = File('F2.py')

a.add_sub_directory(b1)
a.add_sub_directory(b2)

a.add_file(f1)
b1.add_file(f2)

print(a.s_dir)
print(b1.f_list)

print('file', f1.name, 'is in directory', f1.dir, '\nfile', f2.name, 'is in directory', f2.dir,
      '\n which is in directory', b1.root)
