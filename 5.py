val = int(input('Введите число: '))

number = 1
prev_number = 1

for _ in range(val):
    print(number)
    number, prev_number = number + prev_number, number
    
