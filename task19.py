max_age = None

age01 = int(input("age: "))
max_age = age01

for i in range(7 - 1):
    age = int(input("age: "))
    if age > max_age:
        max_age = age

print(max_age)