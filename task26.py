count = 0

for i in range(7):
    age = int(input())
    
    if age < 21:
        count += 1

print(count)