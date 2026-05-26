text = input("Введіть строку: ")

unique_symbols = set(text)

if len(unique_symbols) > 10:
    print(True)
else:
    print(False)