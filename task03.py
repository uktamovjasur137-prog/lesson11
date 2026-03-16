n = int(input("n: "))

if n < 15:
    for i in range(n, 15 + 1, 1):
        print(i)
elif n > 15:
    for i in range(n, 15 + 1, -1):
        print(i)