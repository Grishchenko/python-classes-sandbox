"""Задача на программирование: покрыть отрезки точками



По данным nn отрезкам необходимо найти множество точек минимального размера,
для которого каждый из отрезков содержит хотя бы одну из точек.

В первой строке дано число 1≤n≤100 отрезков. Каждая из последующих n строк содержит по два числа 0≤l≤r≤10^9,
задающих начало и конец отрезка. Выведите оптимальное число m точек и сами m точек.
Если таких множеств точек несколько, выведите любое из них."""

def sortByTwoElement(list):
    # Функция для сортировки списка, элементы которого тоже списки. Сортирутся по второму элементу.
    return list[1]

n = int(input())
lst = []
for i in range(n):
    l, r = map(int, input().split())
    d = [l, r]
    lst.append(d)
print(lst)
lst.sort(key=sortByTwoElement)
print(lst)

setPoints = []
def minPointsInInterval(list):
    i = 0
    while len(list) > 1:
        if list[i][1] < list[i+1][0]:
            setPoints.append(list[i][1])
            del list[i]
        elif list[i][1] == list[i+1][0]:
            list[i + 1] = [list[i][1], list[i+1][0]]
            del list[i]
        else:
            if list[i][0] >= list[i+1][0]:
                list[i+1] = list[i]
                del list[i]
            else:
                list[i+1] = [list[i+1][0], list[i][1]]
                del list[i]
        print(list)
    if len(setPoints) == 0:
        setPoints.append(list[0][1])
        return setPoints
    else:
        lastElement = setPoints.pop()
        setPoints.append(lastElement)
        if list[0][0] <= lastElement and lastElement <= list[0][1]:
            return setPoints
        else:
            setPoints.append(list[0][1])
            return setPoints

minPointsInInterval(lst)
print(len(setPoints))
for elem in setPoints:
    print(elem, end=' ')


