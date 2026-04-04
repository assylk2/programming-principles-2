import shutil
import os

# Копирование
shutil.copy("example.txt", "backup.txt")

# Удаление
if os.path.exists("backup.txt"):
    os.remove("backup.txt")