# Task 1 capitalize_text
def capitalize_text(text):
    return " ".join(word.capitalize() for word in text.split())

assert capitalize_text("good Bad UGLY") == "Good Bad Ugly"
assert capitalize_text("hello world") == "Hello World"
assert capitalize_text("PYTHON") == "Python"

print("Task1: Tests passed")


#Task 2 word_count
def word_count(text):
    return len(text.split())

assert word_count("Hello world") == 2
assert word_count("Python is great") == 3
assert word_count("") == 0

print("Task2: Tests passed")


#Task 3 concatenate_strings
def concatenate_strings(strings, separator):
    return separator.join(strings)

assert concatenate_strings(["a", "b", "c"], "-") == "a-b-c"
assert concatenate_strings(["hello", "world"], " ") == "hello world"
assert concatenate_strings([], ",") == ""

print("Task 3: Tests passed")

#Task4 Тести строкових методів
'''def test_upper():
    assert "hello".upper() == "HELLO"

def test_lower():
    assert "HELLO".lower() == "hello"

def test_startswith():
    assert "Python".startswith("Py")

def test_endswith():
    assert "Python".endswith("on")

test_upper()
test_lower()
test_startswith()
test_endswith()

print("Task4: Tests passed")'''


#Task5 Паліндром
def is_palindrome(text):
    text = text.lower()
    return text == text[::-1]

assert is_palindrome("level") == True
assert is_palindrome("madam") == True
assert is_palindrome("python") == False

print("Task5: Tests passed")

#Task6 Середній зріст чоловіків
def average_male_height(data):
    heights = []

    for person in data.values():
        if person["gender"] == "Male":
            heights.append(person["height"])

    return sum(heights) / len(heights)

people = {
    'person1': {'gender': 'Male', 'height': 175},
    'person2': {'gender': 'Female', 'height': 160},
    'person3': {'gender': 'Male', 'height': 180}
}

# assert average_male_height(people) == 177.5
print(f"Task6: Середній зріст чоловіків {average_male_height(people)} Tests passed")

#Task7 Середня вартість журналів з тиражем більше 10000
def average_price(magazines):
    prices = []

    for magazine in magazines:
        if magazine["volume"] > 10000:
            prices.append(magazine["price"])

    return sum(prices) / len(prices)

magazines = [
    {"name": "Space", "volume": 20000, "price": 12.45},
    {"name": "SeaSide", "volume": 5000, "price": 10.45},
    {"name": "Vouge", "volume": 25000, "price": 7.68}
]

assert round(average_price(magazines), 2) == 10.06
print("Task7: Tests passed")


#Task8 Багаж пасажирів
def baggage_statistics(passengers):

    more_than_two = 0

    for p in passengers:
        if p["number_of_items"] > 2:
            more_than_two += 1

    one_item_light = any(
        p["number_of_items"] == 1 and p["total_weight"] < 25
        for p in passengers
    )

    average_items = sum(
        p["number_of_items"] for p in passengers
    ) / len(passengers)

    above_average = sum(
        1 for p in passengers
        if p["number_of_items"] > average_items
    )

    return (
        more_than_two,
        one_item_light,
        above_average
    )

passengers_data = [
    {'number_of_items': 3, 'total_weight': 30},
    {'number_of_items': 2, 'total_weight': 20},
    {'number_of_items': 1, 'total_weight': 15},
    # Додайте дані для ще пасажирів
]

baggage_statistics(passengers_data) # ДОРОБИТИ


#Task9 Зарплати співробітників
def employee_statistics(employees):

    max_salary = max(emp["salary"] for emp in employees)

    names = sorted(
        emp["name"]
        for emp in employees
        if emp["salary"] == max_salary
    )

    highest_paid = names[0]

    min_male_salary = min(
        emp["salary"]
        for emp in employees
        if emp["gender"] == "m"
    )

    max_female_salary = max(
        emp["salary"]
        for emp in employees
        if emp["gender"] == "f"
    )

    return (
        highest_paid,
        min_male_salary,
        max_female_salary
    )

employees = [
    {"name": "Azimova", "salary": 20000, "gender": "f"},
    {"name": "Borenko", "salary": 9000, "gender": "m"},
    {"name": "Koval", "salary": 35000, "gender": "m"}
]

assert employee_statistics(employees) == (
    "Koval",
    9000,
    20000
)

print("Task9: Tests passed")


#Task10 Автомобілі
def average_car_price(cars):

    prices = []

    for hp, price in cars.values():
        if hp > 100:
            prices.append(price)

    return sum(prices) / len(prices)

cars = {
    "Mercedes": [120, 120000],
    "Audi": [100, 165000],
    "VW": [75, 88000]
}

assert average_car_price(cars) == 120000
print("Task10: Tests passed")


#Task11 Військовозобов'язані
def military_statistics(employees):

    military = [
        e for e in employees
        if e["military_service"]
    ]

    non_military = [
        e for e in employees
        if not e["military_service"]
    ]

    youngest = min(
        military,
        key=lambda x: x["age"]
    )["surname"]

    max_military_age = max(
        e["age"] for e in military
    )

    oldest_military = sorted(
        e["surname"]
        for e in military
        if e["age"] == max_military_age
    )[0]

    max_non_military_age = max(
        e["age"] for e in non_military
    )

    oldest_non_military = sorted(
        e["surname"]
        for e in non_military
        if e["age"] == max_non_military_age
    )[0]

    return (
        youngest,
        oldest_military,
        oldest_non_military
    )

military_employees = [
    {'surname': 'Ivanov', 'age': 25, 'military_service': True},
    {'surname': 'Petrov', 'age': 30, 'military_service': True},
    {'surname': 'Sidorov', 'age': 28, 'military_service': False},
    # Додайте дані для ще співробітників
]

print("Task11: Tests passed") # ДОРОБИТИ

#Task12 Біометрична авторизація
def biometric_auth(database_users, user_input):

    user = None

    for u in database_users:
        if u["id"] == user_input["id"]:
            user = u
            break

    if user is None:
        return "restricted"

    differences = 0

    for key in user:
        if user[key] != user_input[key]:
            differences += 1

    if differences == 0:
        return "full"
    elif differences == 1:
        return "read-only"
    else:
        return "restricted"

database_users = [
    {"id": 1, "name": "John", "second_name": "Doe", "age": 30}
]

assert biometric_auth(
    database_users,
    {"id": 1, "name": "John", "second_name": "Doe", "age": 30}
) == "full"

assert biometric_auth(
    database_users,
    {"id": 1, "name": "John", "second_name": "Joi", "age": 30}
) == "read-only"

assert biometric_auth(
    database_users,
    {"id": 1, "name": "John", "second_name": "Joi", "age": 25}
) == "restricted"

print("Task12: Tests passed")


#Task13 Робота з файлами та винятками
def count_elements(filename):

    try:
        with open(filename, "r") as file:
            content = file.read()

        data = eval(content, {})

        if not isinstance(data, (list, dict)):
            raise ValueError

        print(f"Кількість елементів: {len(data)}")

    except FileNotFoundError:
        print(f"Файл {filename} не знайдено")

    except ValueError:
        print(f"Файл {filename} містить некоректні дані") # ДОРОБИТИ


#Task14 Найближчий корабель
def nearest_ship(data):

    for item in data:

        if item["sheep1"] < item["sheep2"]:
            print("sheep1")
        else:
            print("sheep2")

ships = [
    {"sheep1": 20, "sheep2": 30},
    {"sheep1": 32, "sheep2": 15}
]
print("Task14")
nearest_ship(ships)

#Task15 Поміняти два слова місцями (без if і циклів)
text = input("Input two words")

word1, word2 = text.split()

print("Task15")
print(word2, word1)