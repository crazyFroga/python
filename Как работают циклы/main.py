# Попробуйте теперь самостоятельно подсчитать произведение всех чисел от 1 до N включительно.
P = 1  # заводим переменную-счётчик, в которой мы будем считать произведение
N = 5

# заводим цикл for, в котором мы будем проходить по всем числам от одного до N
for i in range(1, N + 1):
    print("Значение произведения на предыдущем шаге: ", P)
    print("Текущее число: ", i)
    P = P * i  # умножает текущее число i и перезаписываем значение суммы
    print("Значение произведения после умножения: ", P)
    print("---")
print("Конец цикла")
print()
print("Ответ: произведение равно = ", P)

