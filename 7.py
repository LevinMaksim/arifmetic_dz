a = int(input("Введите число: "))

sum = 0

while a > 0:
    if (a % 10) % 2 == 0:
        sum + a % 10
    a = a // 10

print(sum)
