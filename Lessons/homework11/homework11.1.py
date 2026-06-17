def sum_numbers(string):
    try:
        numbers = string.split(",")
        total = 0

        for numbers in numbers:
            total += int(numbers)

        return total

    except ValueError:

        return "Не можу це зробити - існують стрінгові значення!"

data = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3"]

for item in data:
    print(f"Сума чисел {sum_numbers(item)}")