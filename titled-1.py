month = int(input("Введіть номер місяця, в якому ви народилися: "))
day = int(input("Введіть день місяця, в який ви народилися: "))

if month == 12:
    astro_sign = 'Стрілець' if (day < 22) else 'Козеріг'
elif month == 1:
    astro_sign = 'Козеріг' if (day < 20) else 'Водолій'
elif month == 2:
    astro_sign = 'Водолій' if (day < 19) else 'Риби'
elif month == 3:
    astro_sign = 'Риби' if (day < 21) else 'Овен'
elif month == 4:
    astro_sign = 'Овен' if (day < 20) else 'Телець'
elif month == 5:
    astro_sign = 'Телець' if (day < 21) else 'Близнюки'
elif month == 6:
    astro_sign = 'Близнюки' if (day < 21) else 'Рак'
elif month == 7:
    astro_sign = 'Рак' if (day < 23) else 'Лев'
elif month == 8:
    astro_sign = 'Лев' if (day < 23) else 'Діва'
elif month == 9:
    astro_sign = 'Діва' if (day < 23) else 'Терези'
elif month == 10:
    astro_sign = 'Терези' if (day < 23) else 'Скорпіон'
else:
    astro_sign = 'Скорпіон' if (day < 22) else 'Стрілець'

print("Ваш знак зодіаку: ", astro_sign)
