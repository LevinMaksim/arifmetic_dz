val = int(input("Введите число: "))
step = int(input("Введите степень: "))
fin_val = 1

for i in range(step):
    fin_val *= val
print(fin_val)
