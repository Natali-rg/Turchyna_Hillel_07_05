while True:

    word = input("Введіть слово з літерою 'h': ")

    if 'h' in word.lower():
        print("Є літера 'h'! Цикл завершено.")
        break
    else:
        print("У слові немає літери 'h'. Спробуйте ще раз.")