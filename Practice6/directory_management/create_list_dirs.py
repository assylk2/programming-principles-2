import os

# Создать папку
os.mkdir("my_folder")

# Вложенные папки
os.makedirs("parent/child")

# Текущая папка
print(os.getcwd())

# Список файлов
print(os.listdir())

# Перейти в папку
os.chdir("my_folder")

# Удалить папку
os.rmdir("my_folder")