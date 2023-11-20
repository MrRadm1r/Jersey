# Пример: mypythonscript.py
import ctypes

# Загрузка динамической библиотеки
mylib = ctypes.CDLL('./mylib.dll')  # Имя библиотеки может отличаться

# Вызов функции из библиотеки
mylib.my_function()