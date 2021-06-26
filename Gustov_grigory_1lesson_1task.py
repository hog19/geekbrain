time = ['Лет', 'Мес', 'День', 'Час', 'Мин', 'Сек']
duration = int(input('Введите секунды: '))
if 0 < duration < 60:
    print(duration, time[5])
elif duration < 3600:
    print(str(duration//60), time[4], str(duration % 60), time[5])
elif duration < 8640:
    print(str(duration//3600), time[3], str(duration % 3600 // 60), time[4], str(duration % 60), time[5])
else:
    print(str(duration // 86400), time[2], str((duration % 8600) // 3600), time[3], str(duration % 8600 % 3600 // 60), time[4], str(duration % 60), time[5])