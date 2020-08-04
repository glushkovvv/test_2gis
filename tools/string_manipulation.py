"""
load_json_schema
~~~~~~~~~~~~~~

The 2GIS API Test
Tools for string manipulation

:author: Vadim Glushkov
:copyright: Copyright 2019, The2GIS API Test"
:license: MIT
:version: 1.0.0
:maintainer: Vadim Glushkov
:email: plussg@yandex.ru
:status: Development
"""


from random import choices, sample
from string import ascii_letters, ascii_lowercase, ascii_uppercase
from itertools import product


def get_alphabet(lang_uses: str = 'all', char_size: str = 'all') -> str:
    """Выдает строку из символов алфавита по языкам и размеру символов
    :param lang_uses: Язык алфавита, принимает значение: all, en, ru
    :param char_size: Размер символа, принмает значение all, lower, upper
    :return: Возвращает алфавит в виде сроки с задаными параметрами
    """

    alphabet = ''
    if lang_uses == 'all':
        ru_symbol_lower = ''
        ru_symbol_upper = ''
        if char_size == 'all':
            for i in range(32):
                ru_symbol_lower += f'{chr(i + 1072)}'
                ru_symbol_upper += f'{chr(i + 1040)}'
                if i == 5:
                    ru_symbol_lower += f'{chr(1105)}'
                    ru_symbol_upper += f'{chr(1072)}'
            alphabet = ascii_letters + ru_symbol_lower + ru_symbol_upper
        elif char_size == 'lower':
            for i in range(32):
                ru_symbol_lower += f'{chr(i + 1072)}'
                if i == 5:
                    ru_symbol_upper += f'{chr(1072)}'
            alphabet = ascii_lowercase + ru_symbol_lower
        elif char_size == 'upper':
            for i in range(32):
                ru_symbol_upper += f'{chr(i + 1040)}'
                if i == 5:
                    ru_symbol_upper += f'{chr(1072)}'
            alphabet = ascii_uppercase + ru_symbol_upper
        else:
            alphabet = ''
    elif lang_uses == 'en':
        if char_size == 'all':
            alphabet = ascii_letters
        elif char_size == 'lower':
            alphabet = ascii_lowercase
        elif char_size == 'upper':
            alphabet = ascii_uppercase
        else:
            alphabet=''
    elif lang_uses == 'ru':
        ru_symbol_lower = ''
        ru_symbol_upper = ''
        if char_size == 'all':
            for i in range(32):
                ru_symbol_lower += f'{chr(i + 1072)}'
                ru_symbol_upper += f'{chr(i + 1040)}'
                if i == 5:
                    ru_symbol_lower += f'{chr(1105)}'
                    ru_symbol_upper += f'{chr(1072)}'
            alphabet = ru_symbol_lower + ru_symbol_upper
        elif char_size == 'lower':
            for i in range(32):
                ru_symbol_lower += f'{chr(i + 1072)}'
                if i == 5:
                    ru_symbol_upper += f'{chr(1072)}'
            alphabet = ru_symbol_lower
        elif char_size == 'upper':
            for i in range(32):
                ru_symbol_upper += f'{chr(i + 1040)}'
                if i == 5:
                    ru_symbol_upper += f'{chr(1072)}'
            alphabet = ru_symbol_upper
        else:
            alphabet = ''
    else:
        alphabet = ''

    return alphabet


def generator_string(lang_uses: str = 'all', char_count: int = 1,
                     char_size: str = 'lower') -> str:
    """

    :param lang_uses:
    :param char_count:
    :param char_size:
    :return:
    """


    random_string = ''.join(choices(get_alphabet(lang_uses=lang_uses, char_size=char_size), k=char_count))
    return random_string


def get_space_and_end_character() -> list:
    return [0, '',' ','\t', '\r','\n', '\r\n']


def get_special_character(count_chars: int = 2, len_list: int =1) -> list:
    alphabet_char ="~`@#№$%^&*()-_+={[]};:'\"\\|/,<.>?"
    mix_count = len(alphabet_char) ** count_chars
    if 0 < len_list <= mix_count:
        items = sample([''.join(x) for x in product(alphabet_char, repeat=count_chars)], len_list)
    else:
        items = sample([''.join(x) for x in product(alphabet_char, repeat=count_chars)], mix_count)
    return items


def get_valid_country_code() -> list:
    """Возвращает список возможных кодов стран

    :return: list
    """

    return ['ru', 'kg', 'kz', 'cz']


def get_not_valid_country_code(lang_uses: str='en',
                               len_list: int = 1,
                               count_chars: int =2,
                               char_size: str = 'lower') -> list:
    """
    Получить список не валидных двухсимвольных строк.
    В основе генерации используется декартовое произведение.
    Рекомендую использовать для +меньше 5.
    Степень от количества элементов в алфавите. 
    
    :param lang_uses: Символы какого языка использовать. По умолчанию 'en'
    :type lang_uses: str
    :param len_list: Размер отдаваемого списка.
    :type len_list: int
    :param count_chars: Длина одного элемента в списке
    :type count_chars: int
    :
    :return: list, Список из символов языка 
    """

    # Получаем алфавит для генерации строк
    alphabet_char = get_alphabet(lang_uses=lang_uses, char_size=char_size)
    alphabet_len = len(alphabet_char)
    valid_country_code = get_valid_country_code()

    if lang_uses == 'en' and count_chars == 2:
        mix_count = (alphabet_len ** count_chars) - len(valid_country_code)
    else:
        mix_count = (alphabet_len ** count_chars)
    
    # Генерация списка
    if len_list is None:
        items = sample(
            [''.join(x) for x in product(alphabet_char, repeat=count_chars)
                             if ''.join(x) not in valid_country_code], 1)
    elif len_list >= mix_count:
        items = sample([''.join(x) for x in product(alphabet_char, repeat=count_chars)
                             if ''.join(x) not in valid_country_code], mix_count)
    elif 0 < len_list < mix_count:
        items = sample([''.join(x) for x in product(alphabet_char, repeat=count_chars)
                             if ''.join(x) not in valid_country_code], len_list)
    else:
        items = sample([''.join(x) for x in product(alphabet_char, repeat=count_chars)
                       if ''.join(x) not in valid_country_code], 1)
    return items
