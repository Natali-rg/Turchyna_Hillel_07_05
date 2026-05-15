
alice_in_wonderland = ('"Would you tell me, please, which way I ought to go from here?"\n'
                       '"That depends a good deal on where you want to get to," said the Cat.\n'
                       '"I don\'t much care where ——" said Alice.\n'
                       '"Then it doesn\'t matter which way you go," said the Cat.\n'
                       '"—— so long as I get somewhere," Alice added as an explanation.\n'
                       '"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."')

# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк
print(f"{alice_in_wonderland}")

"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
aria_black_see = 436402
aria_azov_see = 37800
total_area = aria_black_see + aria_azov_see
print(f"Загальна площа яку займають моря становить {total_area} км2")


# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
total_goods = 375291
sum_goods_warehouse1_and_goods_warehouse2 = 250449
sum_goods_warehouse2_and_goods_warehouse3 = 222950
goods_warehouse1 = total_goods - sum_goods_warehouse2_and_goods_warehouse3
goods_warehouse2 = sum_goods_warehouse1_and_goods_warehouse2 - goods_warehouse1
goods_warehouse3 = sum_goods_warehouse2_and_goods_warehouse3 - goods_warehouse2
sum_goods_all_warehouses = goods_warehouse1 + goods_warehouse2 + goods_warehouse3
if total_goods==sum_goods_all_warehouses:
    print(f"Кількість товарів на 1 складі складає {goods_warehouse1} товарів\n"
          f"Кількість товарів на 2 складі складає {goods_warehouse2} товарів \n"
          f"Кількість товарів на 3 складі складає {goods_warehouse3} товарів")
else:
    print("Задача вирішено не правильно!")

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
month_computer_cost = 1179
month_count = 12+6
total_computer_cost = month_computer_cost * month_count
print(f"Загальна вартість комп'ютера становить {total_computer_cost} грн.")

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
example_a = 8019 % 8
example_b = 9907 % 9
example_c = 2789 % 5
example_d = 7248 % 6
example_e = 7128 % 5
example_f = 19224 % 9
print(f"Залишок від ділення приклад А {example_a}")
print(f"Залишок від ділення приклад B {example_b}")
print(f"Залишок від ділення приклад C {example_c}")
print(f"Залишок від ділення приклад D {example_d}")
print(f"Залишок від ділення приклад E {example_e}")
print(f"Залишок від ділення приклад F {example_f}")

# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
total_sum = 4 * 274 + 2 * 218 + 4 * 35 + 1 * 350 + 3 * 21
print(f"Сумма замовлення складає {total_sum} грн.")

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
page_count = 232 / 8
print(f"Знадобиться {page_count} сторінок")

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
distance = 1600
fuel_consumption = 9
volume_tank = 48

fuel_needed = distance / 100 * fuel_consumption
number_of_stops = fuel_needed / volume_tank
print(f"Для подорожі знадобиться {fuel_needed} літрів бензину")
print(f"Знадобляться {number_of_stops} заправок")
