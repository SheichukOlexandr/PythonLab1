# Завдання 3. Варіант 17
def find_max_negative(arr):
    max_negative = None
    for num in arr:
        if num < 0:
            if max_negative is None or num > max_negative:
                max_negative = num
    return max_negative

def calculate_product_of_nonzero_odd_elements(arr):
    product = 1
    elements_used = []
    for num in arr:
        if num != 0 and num % 2 != 0:
            product *= num
            elements_used.append(num)
    return product, elements_used

def reverse_print_even_elements(arr):
    even_elements = [num for num in arr if num % 2 == 0]
    print("Масив парних елементів у зворотньому порядку:", even_elements[::-1])

# Введення масиву користувачем
arr = input("Введіть елементи масиву через пробіл: ").split()
# Перетворення введених значень у цілі числа
arr = [int(num) for num in arr]

max_negative = find_max_negative(arr)
product, elements_used = calculate_product_of_nonzero_odd_elements(arr)
reverse_print_even_elements(arr)

print("Максимальний від'ємний елемент:", max_negative)
print("Добуток ненульових непарних елементів:", product)
print("Числа, які були перемножені:", elements_used)
