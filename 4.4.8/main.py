# Проверить, все ли элементы в списке являются уникальными.
# (Подсказка: используйте возможности set)

unic = list(input("Введите числа:\n"))


print(len(unic) == len(set(unic)))