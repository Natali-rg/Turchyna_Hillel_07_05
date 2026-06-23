def sum_numbers(a, b):
    return a + b


def average(numbers):
    return sum(numbers) / len(numbers)


def revers_string(text):
    return text[::-1]


def find_substring(str1, str2):
    return str1.find(str2)


def get_string(lst):
    result = []

    for item in lst:
        if isinstance(item, str):
            result.append(item)

    return result