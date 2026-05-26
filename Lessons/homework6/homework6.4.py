numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_sum = 0

for num in numbers:

    if num % 2 == 0:
        even_sum += num

print(f"Сума парних чисел: {even_sum}")