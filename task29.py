total = 0

n = int(input("Nechta daromad: "))

for i in range(n):
    money = int(input())
    total += money

average = total / n

print(float(average))