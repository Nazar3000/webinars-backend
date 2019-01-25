from random import randint, choice
from faker import Faker

MIN_LENGTH = 6
MAX_LENGTH = 9

VOWELS = ('a', 'e', 'i', 'o', 'u', 'y')
CONSONANTS = ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z', 'sh',
              'zh', 'ch', 'kh', 'th')


def generate_nickname():
    """
    Generate fake nickname for en locale in lower case.
    :return: nickname: str, max_length = 9
    """
    is_vowels_first = bool(randint(0, 1))
    result = ''
    for i in range(0, randint(MIN_LENGTH, MAX_LENGTH)):
        is_even = i % 2 is 0
        if (is_vowels_first and is_even) or (not is_vowels_first and not is_even):
            result += choice(VOWELS)
        else:
            result += choice(CONSONANTS)

    return result.title().lower()


def generate_name(locale_list=[]):
    """
    Generate fake first_name.
    List of main localization: ['en', 'uk_UA', 'ru_RU']
    Link to list of all localization: https://github.com/joke2k/faker/tree/master/faker/providers/person
    If locale_list is empty - generator use all of available localization.

    :param locale_list: list, which can contain localization
    :return: fake first name.
    """
    if len(locale_list) > 0:
        fake = Faker(choice(locale_list))
    else:
        fake = Faker()
    return fake.first_name()

