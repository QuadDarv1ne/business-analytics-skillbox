"""
Задача №1. Калькулятор опыта

В компьютерной игре уровень персонажа определяется по набранным очкам опыта:
- Начальный уровень: 1
- Новый уровень даётся при достижении:
  * 1000 очков - уровень 2
  * 2500 очков - уровень 3
  * 5000 очков - уровень 4

Программа получает на вход количество очков опыта и выводит текущий уровень персонажа.
"""

experience = int(input("Введите количество опыта: "))

if experience >= 5000:
    level = 4
elif experience >= 2500:
    level = 3
elif experience >= 1000:
    level = 2
else:
    level = 1

print(f"Ваш уровень: {level}")



"""
Задача №2. Функция

Программа вычисляет значение функции Y по следующим правилам:
- Если X > 0: Y = X - 12
- Если X = 0: Y = 5
- Если X < 0: Y = X²

На вход подаётся число X, программа выводит значение Y.
"""

x = int(input("Введите икс: "))

if x > 0:
    y = x - 12
elif x == 0:
    y = 5
else:
    y = x ** 2

print(f"Игрек равен {y}")


"""
Задача №3. Поступление

Условия поступления:
1. Только первые 10 человек в списке поступают
2. Стипендия даётся если общий балл ≥ 290

Программа получает:
- Место в списке (целое число)
- Количество баллов (целое число)

Выводит сообщения о поступлении и получении стипендии.
"""

place = int(input("Введите место в списке поступающих: "))
score = int(input("Введите количество баллов за экзамены: "))

if place <= 10:
    print("Поздравляем, вы поступили!")
    if score >= 290:
        print("Бонусом вам будет начисляться стипендия.")
    else:
        print("Но вам не хватило баллов для стипендии.")
else:
    print("К сожалению, вы не поступили.")


"""
Задача №4. Опять двойка

Программа оценивает школьные оценки:
- Плохие оценки (2 или 3): "Плохо. Марш учиться!"
- Хорошие оценки (4 или 5): "Молодец! Можешь отдохнуть."

Оптимизированная версия программы без повторяющихся строк.
"""

rating = int(input('Что получил по математике? '))

if rating == 2 or rating == 3:
    print('Плохо. Марш учиться!')
elif rating == 4 or rating == 5:
    print('Молодец! Можешь отдохнуть.')
else:
    print('Введите оценку от 2 до 5')


"""
Задача №5. Вася хочет выигрывать

Программа анализирует три числа и определяет количество совпадений:
- 3: если все три числа одинаковы
- 2: если два числа одинаковы
- 0: если все числа разные

Выводит только число (3, 2 или 0).
"""

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))

if a == b == c:
    print("3 (все числа одинаковы)")
elif a == b or a == c or b == c:
    print("2 (два числа одинаковы)")
else:
    print("0 (все числа разные)")


"""
Задача №6. Новоселье

Критерии выбора квартиры:
1. Вариант 1: площадь ≥ 100м² и цена ≤ 10 млн
2. Вариант 2: площадь ≥ 80м² и цена ≤ 7 млн

Программа получает:
- Стоимость квартиры (в рублях)
- Площадь квартиры (в м²)

Выводит, подходит ли квартира под критерии.
"""

price = int(input("Введите стоимость квартиры (в рублях): "))
area = int(input("Введите площадь квартиры (в м²): "))

option1 = (area >= 100) and (price <= 10000000)
option2 = (area >= 80) and (price <= 7000000)

if option1 or option2:
    print("Квартира подходит под ваши критерии!")
else:
    print("Квартира не подходит под ваши критерии.")


"""
Задача №7. Почта

График работы почты:
- Открыта: 08:00-22:00
- Не работает:
  * Обед: 14:00-15:00
  * Разгрузка: 10:00-12:00 и 18:00-20:00

Программа получает текущий час (0-23) и сообщает,
можно ли получить посылку в это время.

Реализовано двумя способами:
1. Проверка когда можно получить
2. Проверка когда нельзя получить
"""

# Способ 1: Проверка когда можно получить
hour = int(input("Введите текущий час (0-23): "))

if (8 <= hour < 10) or (12 <= hour < 14) or (15 <= hour < 18) or (20 <= hour < 22):
    print("Можно получить посылку")
else:
    print("Посылку получить нельзя")

# Способ 2: Проверка когда нельзя получить
hour = int(input("Введите текущий час (0-23): "))

if hour < 8 or hour >= 22 or (10 <= hour < 12) or (14 <= hour < 15) or (18 <= hour < 20):
    print("Посылку получить нельзя")
else:
    print("Можно получить посылку")
