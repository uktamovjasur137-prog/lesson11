n = int(input("Nechta son: "))

first = int(input())
max_num = first
min_num = first

for i in range(n - 1):
    num = int(input())
    
    if num > max_num:
        max_num = num
    if num < min_num:
        min_num = num

average = (max_num + min_num) / 2

print(float(average))