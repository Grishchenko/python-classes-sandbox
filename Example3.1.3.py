"""Задача на программирование: различные слагаемые

По данному числу 1≤n≤10^9 найдите максимальное число k, для которого n можно представить как сумму k различных натуральных слагаемых.
Выведите в первой строке число k, во второй — k слагаемых."""

n = int(input())

list_Addend = []
def maxDiffAddend(n):
    if n == 1 or n == 2:
        list_Addend.append(n)
        return list_Addend
    else:
        i = 1
        while n > 0:
            if n - i > i or n - i == 0:
                list_Addend.append(i)
                n = n - i
                i += 1
            else:
                list_Addend.append(n)
                break
        return list_Addend

maxDiffAddend(n)
print(len(list_Addend))
for el in list_Addend:
    print(el, end=' ')

