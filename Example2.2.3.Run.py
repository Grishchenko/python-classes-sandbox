# Даны целые числа 1≤n≤10^18и 2≤m≤10^5, необходимо найти остаток от деления n-го числа Фибоначчи на m.
n, m = map(int, input().split())
def Fib_ostatok(n, m):
    """Функция записывает в список остаки от деления суммы двух предыдущих остатков на m.
    Согласно периоду Пизано период в остатках начинается с 0, 1. После этого цикл заканчивам.
    Остатком от деления n-го числа Фибоначчи на m будет элемент этого списка с номером равным
    остатку от деления n на длину периода."""
    ostatki = [0, 1]
    for i in range(2, 6*m):
        ostatki.append((ostatki[i-1] + ostatki[i-2]) % m)
        if ostatki[i] >= m:
            ostatki.append(ostatki[i] % m)
        if (ostatki[i] == 1 and ostatki[i-1] == 0):
            break
    return ostatki[n % (len(ostatki) - 2)]

print(Fib_ostatok(n, m))
#print(ostatki[n % (len(ostatki) - 2)])

