adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""


##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("\n", " ")
print(f"TASK1 {adwentures_of_tom_sawer}")


# task 02 ==
""" Замініть .... на пробіл
"""
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("....", " ")
print(f"TASK2 {adwentures_of_tom_sawer}")


# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
adwentures_of_tom_sawer = " ".join(adwentures_of_tom_sawer.split())
print(f"TASK3 {adwentures_of_tom_sawer}")


# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
count_h = adwentures_of_tom_sawer.count("h")
print(f"TAS: Kількість літер h: {count_h}")


# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
words = adwentures_of_tom_sawer.split()
count_capital = 0
for item in words:
    if item.istitle():
        count_capital += 1
print(f"TASK5. Kількість cлів з великої літери: {count_capital}")


# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
first_tom = adwentures_of_tom_sawer.find("Tom")
second_tom = adwentures_of_tom_sawer.find("Tom", first_tom + 1)
print(f"TASK6. Позиція другого слова Tom: {second_tom}")


# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
#adwentures_of_tom_sawer_sentences = None
adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer.split(".")
print(f"TASK7. {adwentures_of_tom_sawer_sentences}")


# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
adwentures_of_tom_sawer_sentences_lower = adwentures_of_tom_sawer_sentences[3].lower()
print(f"TASK8. {adwentures_of_tom_sawer_sentences_lower}")


# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
found = False
for sentence in adwentures_of_tom_sawer_sentences:
    if sentence.strip().startswith("By the time"):
        found = True
        break
print(f"TASK9. Є речення з 'By the time': {found}")


# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
last_sentence = adwentures_of_tom_sawer_sentences[-2]
word_count = len(last_sentence.split())
print(f"Кількість слів в останньому реченні: {word_count}")