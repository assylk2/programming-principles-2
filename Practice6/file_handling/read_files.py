# Чтение файла
with open("example.txt", "r") as f:
    print(f.read())        # весь файл

# readline()
with open("example.txt", "r") as f:
    print(f.readline())    # 1 строка

# readlines()
with open("example.txt", "r") as f:
    lines = f.readlines()
    print(lines)