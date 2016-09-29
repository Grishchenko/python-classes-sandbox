a, b = map(int, input().split())
def Euclide(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    if a >= b:
        return Euclide(a % b, b)
    if b >= a:
        return Euclide(a, b % a)

print(Euclide(a, b))