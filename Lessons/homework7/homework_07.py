# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while True:
        result = number * multiplier
        # десь тут помила, а може не одна
        if  result > 25:
            # Enter the action to take if the result is greater than 25
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1
print("Task 1")
multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
print("\nTask 2")

def sum_nambers(a, b):
    return a + b
print(f"Сума двох чисел {sum_nambers(5, 10)}")

# a = int(input("Введіть число а "))
# b = int(input("Введіть число b "))
# def sum_nambers(a, b):
#     return a + b
# print(f"Сума двох чисел {sum_nambers(a, b)}")


# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
print("\nTask 3")
def average(numbers):
    return sum(numbers) / len(numbers)

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(f"Середнє арифметичне: {average(my_list)}")

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
print("\nTask 4")
def revers_string(text):
    return text[::-1]
print(f"Pядок у зворотному порядку {revers_string("I need a six-month vacation, twice a year.")}")

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
print("\nTask 5")

text = "I need a six-month vacation, twice a year."
words = text.split()

def longest_word(text):
    return max(text, key=len)

print(f"Найдовше слово {longest_word(words)}")

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""

print("\nTask 6")
def find_substring(str1, str2):
    return str1.find(str2)

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# task 7
'''ДЗ 6.3. Забери зі списку що потрібно: Є list з даними lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
Напишіть код, який свормує новий list (наприклад lst2),
 який містить лише змінні типу стрінг, які присутні в lst1. Данні в лісті можуть бути будь якими'''

print("\nTask 7")
def get_string(list):
    result = []
    for item in list:
        if isinstance(item, str):
            result.append(item)

    return result

list1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
list2 = get_string(list1)

print(list2)

# task 8
'''ДЗ 6.2. Цикл “Дочекайся літери”: Напишіть цикл, який буде вимагати від користувача ввести слово,
 в якому є літера "h" (враховуються як великі так і маленькі). Цикл не повинен завершитися, якщо користувач ввів слово без букви "h".'''

print("\nTask 8")
def wait_for_h_word():
    while True:

        word = input("Введіть слово з літерою 'h': ")

        if 'h' in word.lower():
            print("Є літера 'h'! Цикл завершено.")
            break
        else:
            print("У слові немає літери 'h'. Спробуйте ще раз.")

wait_for_h_word()

# task 9
'''ДЗ 6.1. Рахування унікальних символів в строці: Порахувати кількість унікальних символів в строці.
 Якщо їх більше 10 - вивести в консоль True, інакше - False. Строку отримати за допомогою функції input()'''

print("\nTask 9")
def check_unique_chars():
    text = input("Введіть строку: ")

    unique_symbols = set(text)

    if len(unique_symbols) > 10:
        print(True)
    else:
        print(False)

check_unique_chars()

# task 10
'''ДЗ 5.2. Лист кортежiв ( List of tuples): Заданий список кортежів (ім'я, прізвище, вік, професія, місце проживання): 
1) Додайте свій новий запис на початок даного списку. 
2) У модифікованому списку обміняйте елементи з індексами 1 і 5 (1<->5). Виведіть результат. 
3) Перевірте, чи всі люди в модифікованому списку з індексами 6, 10, 13 мають вік ≥ 30. Виведіть результат перевірки '''

print("\nTask 10")

people_records = [
  ('John', 'Doe', 28, 'Engineer', 'New York'),
  ('Alice', 'Smith', 35, 'Teacher', 'Los Angeles'),
  ('Bob', 'Johnson', 45, 'Doctor', 'Chicago'),
  ('Emily', 'Williams', 30, 'Artist', 'San Francisco'),
  ('Michael', 'Brown', 22, 'Student', 'Seattle'),
  ('Sophia', 'Davis', 40, 'Lawyer', 'Boston'),
  ('David', 'Miller', 33, 'Software Developer', 'Austin'),
  ('Olivia', 'Wilson', 27, 'Marketing Specialist', 'Denver'),
  ('Daniel', 'Taylor', 38, 'Architect', 'Portland'),
  ('Grace', 'Moore', 25, 'Graphic Designer', 'Miami'),
  ('Samuel', 'Jones', 50, 'Business Consultant', 'Atlanta'),
  ('Emma', 'Hall', 31, 'Chef', 'Dallas'),
  ('William', 'Clark', 29, 'Financial Analyst', 'Houston'),
  ('Ava', 'White', 42, 'Journalist', 'San Diego'),
  ('Ethan', 'Anderson', 36, 'Product Manager', 'Phoenix')
]

def process_people(records):
    # 1. додаємо новий запис на початок
    new_person = ('Natalia', 'Turchyna', 26, 'QA Engineer', 'Warsaw')
    records.insert(0, new_person)

    # 2. міняємо місцями елементи 1 і 5
    records[1], records[5] = records[5], records[1]

    # 3. перевірка віку на індексах 6, 10, 13
    indices_to_check = [6, 10, 13]

    result = all(records[i][2] >= 30 for i in indices_to_check)

    # вивід результату
    print("Modified list:")
    for item in records:
        print(item)

    print("\nAge check result:", result)

process_people(people_records)

"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""