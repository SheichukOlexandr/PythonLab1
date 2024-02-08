# Завдання 1. Варіант 17
import math

def z(a, b):
    if a >= 15:
        return math.sin(2 * a) + math.cos(2 * b)
    else:
        return math.sqrt(a) + b**2

a = float(input("Введіть значення a: "))
b = float(input("Введіть значення b: "))

result = z(a, b)
print("Результат функції z: ", result)
