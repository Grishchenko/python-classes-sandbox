n = int(input())
Fib_spisok = [0 for i in range(n+1)]
print(Fib_spisok)
Fib_spisok[1] = 1
for j in range(2, n+1):
	Fib_spisok[j] = Fib_spisok[j-1] + Fib_spisok[j-2]
print(Fib_spisok)
print(Fib_spisok[n])