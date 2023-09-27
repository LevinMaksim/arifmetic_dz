a = int(input("Введите число: "))

sum = 0
val = 1

while a > 0:
    sum += a % 10
    val *= a % 10
    a = a // 10
print(f"Сумма - {sum}")
print(f"Произведение - {val}")
