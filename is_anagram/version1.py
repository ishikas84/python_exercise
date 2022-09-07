import functools


def is_anagram(str1: str, str2: str) -> bool:
    if len(str1) == len(str2):
        str1_list = sorted(str1.lower())
        str2_list = sorted(str2.lower())
        return functools.reduce(lambda x, y: x and y, map(lambda a, b: a == b, str1_list, str2_list), True)
    return False
