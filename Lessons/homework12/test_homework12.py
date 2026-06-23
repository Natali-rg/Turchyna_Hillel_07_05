from Lessons.homework12.homework12 import (sum_numbers, average, revers_string, find_substring, get_string)
from Lessons.homework7.homework_07 import longest_word


def test_sum_positive_numbers():
    assert sum_numbers(5, 10) == 15


def test_sum_negative_numbers():
    assert sum_numbers(-5, -10) == -15


def test_average_list():
    assert average([1, 2, 3, 4, 5]) == 3


def test_average_one_number():
    assert average([10]) == 10


def test_reverse_string():
    assert revers_string("Python") == "nohtyP"


def test_reverse_empty_string():
    assert revers_string("") == ""


def test_longest_word():
    assert longest_word(["cat", "elephant", "dog"]) == "elephant"


def test_find_substring_exists():
    assert find_substring("Hello world", "world") == 6


def test_find_substring_not_exists():
    assert find_substring("Hello world", "cat") == -1


def test_get_string():
    assert get_string([1, "abc", True, "Python"]) == ["abc", "Python"]


def test_get_string_empty():
    assert get_string([1, 2, 3]) == []