# нужно получить последнюю цифру большого числа Фибоначчи. Эффективный алгоритм.
n = int(input())
Fib_last_number = [0 for i in range(n+1)]
print(Fib_last_number)
Fib_last_number[1] = 1
Fib_last_number[2] = 1
Fib_last_number[3] = 2
Fib_last_number[4] = 3
Fib_last_number[5] = 5
Fib_last_number[6] = 8
for j in range(7, n+1):
	Fib_last_number[j] = (Fib_last_number[j-1] + Fib_last_number[j-2]) % 10
	if Fib_last_number[j] > 10:
		Fib_last_number[j] = Fib_last_number % 10
print(Fib_last_number)
print(Fib_last_number[n])