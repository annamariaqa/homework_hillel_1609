def even_numbers(n):
    for i in range(0, n + 1, 2):
        yield i

N = 10
for num in even_numbers(N):
    print(num)
