# Завдання 2. Варіант 17
import math

def calculate_y(n):
    y = 0
    for i in range(1, n+1):
        y += (i + 1) / i
    return y

n = int(input("Введіть натуральне число n: "))
result = calculate_y(n)
print("Значення y =", result)
