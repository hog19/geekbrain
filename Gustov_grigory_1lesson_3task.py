percent = int(input('Введите число от 0 до 20: '))
if 0 < percent <= 1:
    print(percent, 'процент')
elif 1 < percent <= 4:
    print(percent, 'процента')
else:
    print(percent, 'процентов')