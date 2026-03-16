total = 0

n = int(input("n: "))

for i in range(1, n + 1):
    total += i ** 3
    
print(total)