# Дано натуральное восьмизначное число. Выясните, является ли оно палиндромом
# (читается одинаково слева направо и справа налево).

# (Подсказка: использовать целочисленное деление и деление с остатком не нужно.
# Попробуйте преобразовать число к строке, а потом перевернуть эту строку. См. материал прошлого модуля)

x = str(input("Введите восьмизначное число:\n"))

if len(x) <8 or len(x) >= 9:
    print("Вы ввели неверное число")
elif x[::] == x[::-1]:
    print("Данное число является палиндромом")
else:
    print("Все плохо")
