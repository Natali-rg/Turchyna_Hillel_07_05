# Генератори

#Task1 Генератор парних чисел від 0 до N

def even_numbers(n):
    for i in range (0, n+1, 2):
        yield i


print('Task 1')
for numbers in even_numbers(10):
    print(numbers)


#Task2 Генератор чисел Фібоначчі до N

def fibonacci (n):
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, b + a


print('Task 2')
for numbers in fibonacci(50):
    print(numbers)


# Ітератори

# Task3 Ітератор для зворотного виведення списку

class ReversIterator:

    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index ==0:
            raise StopIteration

        self.index -=1
        return self.data[self.index]

numbers = [10, 20, 30, 40, 50, 60]

print('Task 3')
for i in ReversIterator(numbers):
    print(i)

# Task 4 Ітератор парних чисел від 0 до N

class EvenIterator:

    def __init__(self, number):
        self.number = number
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.number:
            raise StopIteration

        value = self.current
        self.current += 2
        return value

print('Task 4')
for n in EvenIterator(20):
    print(n)

# Декоратори

# Task 5 Декоратор, який логує аргументи та результат функції

print('Task 5')

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def logger(func):
    def wrapper(*args, **kwargs):
        logging.info(f"Виклик функції {func.__name__}")
        logging.info(f"Аргументи: args={args}, kwargs={kwargs}")

        result = func(*args, **kwargs)

        logging.info(f"Результат: {result}")
        return result

    return wrapper


@logger
def add(a, b):
    return a + b

add(5, 7)

'''def logger(func):
    def wrapper(*args, **kwargs):
        print("Аргументи:", args, kwargs)

        result = func(*args, **kwargs)

        print("Task 5. Результат:", result)
        return result

    return wrapper


@logger
def add(a, b):
    return a + b

add(5, 7)'''

# Task 6  Декоратор для обробки винятків

def exception_handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as error:
            print("Сталася помилка:", error)

    return wrapper


@exception_handler
def divide(a, b):
    return a / b


# Перевірка
print('Task 6')
print(divide(10, 2))
print(divide(10, 0))