def gen(n):
    for num in range(1, n):
        digits = str(num)
        if len(set(digits)) == 1:
            yield num


n = int(input())
for i in gen(n):
    print(i)