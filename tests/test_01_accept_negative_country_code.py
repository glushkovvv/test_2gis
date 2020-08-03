"""
test_01_accept_negative_country_code
~~~~~~~~~~~~~~

The 2GIS API Test
Check negative country_code

:author: Vadim Glushkov
:copyright: Copyright 2019, The2GIS API Test"
:license: MIT
:version: 1.0.0
:maintainer: Vadim Glushkov
:email: plussg@yandex.ru
:status: Development
"""

import pytest
import json
from os.path import join, dirname
from jsonschema import Draft7Validator
from tools.string_manipulation import get_not_valid_country_code, get_space_and_end_character, get_special_character
from tools.api_responses import get_response
from tools.load_json_schema import load_json_schema


@pytest.mark.parametrize("country_code", get_space_and_end_character())
def test_01_accept_negation_space_char(setup_option, country_code):
    """Проверка ответов API при передачи пустоты, пробелов и т.п.

    :param setup_option: Установочные параметры
    :type setup_option: dict
    :param country_code: Код страны
    :type: chars
    :return:
    """

    api_url = setup_option['site_url']
    setup_params = {
        "country_code": country_code,
    }
    api_response = get_response(api_url, setup_params)
    json_content = json.loads(api_response.content.decode('utf-8'))
    response_message = f"""EndPoint: {api_url}?country_code={country_code}
    Status: {api_response.status_code}
    Body: {json_content}
    """
    assert api_response.status_code == 200, f"""Статус ответа {api_response.status_code} != 200\r\n""" + response_message
    relative_path = join('../datasets','json_error_schemas_country_code.json')
    filename = join(dirname(__file__), relative_path)
    schema = load_json_schema(filename=filename)
    check = Draft7Validator(schema=schema).is_valid(json_content)
    assert check, f"""Ошибка при валидации схемы негативного запроса кода страны {country_code}\r\n"""+response_message


@pytest.mark.parametrize("country_code", get_special_character(count_chars=1, len_list=10))
def test_02_accept_negation_special_one_char(setup_option, country_code):
    """Проверка ответов API при передачи одного специального сивола

    :param setup_option: Установочные параметры
    :type setup_option: dict
    :param country_code: Код страны
    :type country_code: str
    :return:
    """

    api_url = setup_option['site_url']
    setup_params = {
        "country_code": country_code,
    }
    api_response = get_response(api_url, setup_params)
    json_content = json.loads(api_response.content.decode('utf-8'))
    response_message = f"""EndPoint: {api_url}?country_code={country_code}
    Status: {api_response.status_code}
    Body: {json_content}
    """
    assert api_response.status_code == 200, f"""Статус ответа {api_response.status_code} != 200\r\n""" + response_message
    relative_path = join('../datasets', 'json_error_schemas_country_code.json')
    filename = join(dirname(__file__), relative_path)
    schema = load_json_schema(filename=filename)
    check = Draft7Validator(schema=schema).is_valid(json_content)
    assert check, f"""Ошибка при валидации схемы негативного запроса кода страны {country_code}\r\n""" + response_message


@pytest.mark.parametrize("country_code", get_special_character(count_chars=2, len_list=10 ))
def test_03_accept_negation_special_two_char(setup_option, country_code):
    """Проверка ответов API при передачи двух специальных сиволов

    :param setup_option: Установочные параметры
    :type setup_option: dict
    :param country_code: Код страны
    :type country_code: str
    :return:
    """

    api_url = setup_option['site_url']
    setup_params = {
        "country_code": country_code,
    }
    api_response = get_response(api_url, setup_params)
    json_content = json.loads(api_response.content.decode('utf-8'))
    response_message = f"""EndPoint: {api_url}?country_code={country_code}
    Status: {api_response.status_code}
    Body: {json_content}
    """
    assert api_response.status_code == 200, f"""Статус ответа {api_response.status_code} != 200\r\n""" + response_message
    relative_path = join('../datasets', 'json_error_schemas_country_code.json')
    filename = join(dirname(__file__), relative_path)
    schema = load_json_schema(filename=filename)
    check = Draft7Validator(schema=schema).is_valid(json_content)
    assert check, f"""Ошибка при валидации схемы негативного запроса кода страны {country_code}\r\n""" + response_message

@pytest.mark.parametrize("country_code", get_special_character(count_chars=3, len_list=10 ))
def test_04_accept_negation_special_three_char(setup_option, country_code):
    """Проверка ответов API при передачи трех специальныхсиволов

    :param setup_option: Установочные параметры
    :type setup_option: dict
    :param country_code: Код страны
    :type country_code: str
    :return:
    """

    api_url = setup_option['site_url']
    setup_params = {
        "country_code": country_code,
    }
    api_response = get_response(api_url, setup_params)
    json_content = json.loads(api_response.content.decode('utf-8'))
    response_message = f"""EndPoint: {api_url}?country_code={country_code}
    Status: {api_response.status_code}
    Body: {json_content}
    """
    assert api_response.status_code == 200, f"""Статус ответа {api_response.status_code} != 200\r\n""" + response_message
    relative_path = join('../datasets', 'json_error_schemas_country_code.json')
    filename = join(dirname(__file__), relative_path)
    schema = load_json_schema(filename=filename)
    check = Draft7Validator(schema=schema).is_valid(json_content)
    assert check, f"""Ошибка при валидации схемы негативного запроса кода страны {country_code}\r\n""" + response_message


@pytest.mark.parametrize("country_code",
                         get_not_valid_country_code(lang_uses='en',
                                                    char_size='lower',
                                                    count_chars=1,
                                                    len_list=10))
def test_05_accept_negation_country_one_lower_latin_char(setup_option, country_code):
    """Проверка ответов API при передачи одного строчного латинского символа

    :param setup_option: Установочные параметры
    :type setup_option: dict
    :param country_code: Код страны
    :type country_code: str
    :return:
    """

    api_url = setup_option['site_url']
    setup_params = {
        "country_code": country_code,
    }
    api_response = get_response(api_url, setup_params)
    json_content = json.loads(api_response.content.decode('utf-8'))
    response_message = f"""EndPoint: {api_url}?country_code={country_code}
    Status: {api_response.status_code}
    Body: {json_content}
    """
    assert api_response.status_code == 200, f"""Статус ответа {api_response.status_code} != 200\r\n""" + response_message
    relative_path = join('../datasets', 'json_error_schemas_country_code.json')
    filename = join(dirname(__file__), relative_path)
    schema = load_json_schema(filename=filename)
    check = Draft7Validator(schema=schema).is_valid(json_content)
    assert check, f"""Ошибка при валидации схемы негативного запроса кода страны {country_code}\r\n""" + response_message


@pytest.mark.parametrize("country_code",
                         get_not_valid_country_code(lang_uses='en',
                                                    char_size='lower',
                                                    count_chars=2,
                                                    len_list=10))
def test_06_accept_negation_country_two_lower_latin_chars(setup_option, country_code):
    """Проверка ответов API при передачи двух строчных латинских символов

    :param setup_option: Установочные параметры
    :type setup_option: dict
    :param country_code: Код страны
    :type country_code: str
    :return:
    """

    api_url = setup_option['site_url']
    setup_params = {
        "country_code": country_code,
    }
    api_response = get_response(api_url, setup_params)
    json_content = json.loads(api_response.content.decode('utf-8'))
    response_message = f"""EndPoint: {api_url}?country_code={country_code}
    Status: {api_response.status_code}
    Body: {json_content}
    """
    assert api_response.status_code == 200, f"""Статус ответа {api_response.status_code} != 200\r\n""" + response_message
    relative_path = join('../datasets', 'json_error_schemas_country_code.json')
    filename = join(dirname(__file__), relative_path)
    schema = load_json_schema(filename=filename)
    check = Draft7Validator(schema=schema).is_valid(json_content)
    assert check, f"""Ошибка при валидации схемы негативного запроса кода страны {country_code}\r\n""" + response_message


@pytest.mark.parametrize("country_code",
                         get_not_valid_country_code(lang_uses='en',
                                                    char_size='lower',
                                                    count_chars=3,
                                                    len_list=10))
def test_07_accept_negation_country_three_lower_latin_chars(setup_option, country_code):
    """Проверка ответов API при передачи трех строчных латинских символов

    :param setup_option: Установочные параметры
    :type setup_option: dict
    :param country_code: Код страны
    :type country_code: str
    :return:
    """

    api_url = setup_option['site_url']
    setup_params = {
        "country_code": country_code,
    }
    api_response = get_response(api_url, setup_params)
    json_content = json.loads(api_response.content.decode('utf-8'))
    response_message = f"""EndPoint: {api_url}?country_code={country_code}
    Status: {api_response.status_code}
    Body: {json_content}
    """
    assert api_response.status_code == 200, f"""Статус ответа {api_response.status_code} != 200\r\n""" + response_message
    relative_path = join('../datasets', 'json_error_schemas_country_code.json')
    filename = join(dirname(__file__), relative_path)
    schema = load_json_schema(filename=filename)
    check = Draft7Validator(schema=schema).is_valid(json_content)
    assert check, f"""Ошибка при валидации схемы негативного запроса кода страны {country_code}\r\n""" + response_message

@pytest.mark.parametrize("country_code",
                         get_not_valid_country_code(lang_uses='ru',
                                                    char_size='lower',
                                                    count_chars=1,
                                                    len_list=10))
def test_08_accept_negation_country_one_lower_cyrillic_char(setup_option, country_code):
    """Проверка ответов API при передачи одного строчного кириллического символа

    :param setup_option: Установочные параметры
    :type setup_option: dict
    :param country_code: Код страны
    :type country_code: str
    :return:
    """

    api_url = setup_option['site_url']
    setup_params = {
        "country_code": country_code,
    }
    api_response = get_response(api_url, setup_params)
    json_content = json.loads(api_response.content.decode('utf-8'))
    response_message = f"""EndPoint: {api_url}?country_code={country_code}
    Status: {api_response.status_code}
    Body: {json_content}
    """
    assert api_response.status_code == 200, f"""Статус ответа {api_response.status_code} != 200\r\n""" + response_message
    relative_path = join('../datasets', 'json_error_schemas_country_code.json')
    filename = join(dirname(__file__), relative_path)
    schema = load_json_schema(filename=filename)
    check = Draft7Validator(schema=schema).is_valid(json_content)
    assert check, f"""Ошибка при валидации схемы негативного запроса кода страны {country_code}\r\n""" + response_message

@pytest.mark.parametrize("country_code",
                         get_not_valid_country_code(lang_uses='ru',
                                                    char_size='lower',
                                                    count_chars=2,
                                                    len_list=10))
def test_09_accept_negation_country_two_lower_cyrillic_chars(setup_option, country_code):
    """Проверка ответов API при передачи двух строчных кириллических символов

    :param setup_option: Установочные параметры
    :type setup_option: dict
    :param country_code: Код страны
    :type country_code: str
    :return:
    """
    api_url = setup_option['site_url']
    setup_params = {
        "country_code": country_code,
    }
    api_response = get_response(api_url, setup_params)
    json_content = json.loads(api_response.content.decode('utf-8'))
    response_message = f"""EndPoint: {api_url}?country_code={country_code}
    Status: {api_response.status_code}
    Body: {json_content}
    """
    assert api_response.status_code == 200, f"""Статус ответа {api_response.status_code} != 200\r\n""" + response_message
    relative_path = join('../datasets', 'json_error_schemas_country_code.json')
    filename = join(dirname(__file__), relative_path)
    schema = load_json_schema(filename=filename)
    check = Draft7Validator(schema=schema).is_valid(json_content)
    assert check, f"""Ошибка при валидации схемы негативного запроса кода страны {country_code}\r\n""" + response_message


@pytest.mark.parametrize("country_code",
                         get_not_valid_country_code(lang_uses='ru',
                                                    char_size='lower',
                                                    count_chars=3,
                                                    len_list=10))
def test_10_accept_negation_country_three_lower_cyrillic_chars(setup_option, country_code):
    """Проверка ответов API при передачи трех строчных кириллических символов

    :param setup_option: Установочные параметры
    :type setup_option: dict
    :param country_code: Код страны
    :type country_code: str
    :return:
    """

    api_url = setup_option['site_url']
    setup_params = {
        "country_code": country_code,
    }
    api_response = get_response(api_url, setup_params)
    json_content = json.loads(api_response.content.decode('utf-8'))
    response_message = f"""EndPoint: {api_url}?country_code={country_code}
    Status: {api_response.status_code}
    Body: {json_content}
    """
    assert api_response.status_code == 200, f"""Статус ответа {api_response.status_code} != 200\r\n""" + response_message
    relative_path = join('../datasets', 'json_error_schemas_country_code.json')
    filename = join(dirname(__file__), relative_path)
    schema = load_json_schema(filename=filename)
    check = Draft7Validator(schema=schema).is_valid(json_content)
    assert check, f"""Ошибка при валидации схемы негативного запроса кода страны {country_code}\r\n""" + response_message


@pytest.mark.parametrize("country_code",
                         get_not_valid_country_code(lang_uses='all',
                                                    char_size='lower',
                                                    count_chars=1,
                                                    len_list=10))
def test_11_accept_negation_country_one_lower_mix_char(setup_option, country_code):
    """Проверка ответов API при передачи одного строчного латинского или кириллического символа

    :param setup_option: Установочные параметры
    :type setup_option: dict
    :param country_code: Код страны
    :type country_code: str
    :return:
    """

    api_url = setup_option['site_url']
    setup_params = {
        "country_code": country_code,
    }
    api_response = get_response(api_url, setup_params)
    json_content = json.loads(api_response.content.decode('utf-8'))
    response_message = f"""EndPoint: {api_url}?country_code={country_code}
    Status: {api_response.status_code}
    Body: {json_content}
    """
    assert api_response.status_code == 200, f"""Статус ответа {api_response.status_code} != 200\r\n""" + response_message
    relative_path = join('../datasets', 'json_error_schemas_country_code.json')
    filename = join(dirname(__file__), relative_path)
    schema = load_json_schema(filename=filename)
    check = Draft7Validator(schema=schema).is_valid(json_content)
    assert check, f"""Ошибка при валидации схемы негативного запроса кода страны {country_code}\r\n""" + response_message


@pytest.mark.parametrize("country_code",
                         get_not_valid_country_code(lang_uses='all',
                                                    char_size='lower',
                                                    count_chars=2,
                                                    len_list=10))
def test_12_accept_negation_country_two_lower_mix_chars(setup_option, country_code):
    """Проверка ответов API при передачи двух строчных латинских или кириллических символов

    :param setup_option: Установочные параметры
    :type setup_option: dict
    :param country_code: Код страны
    :type country_code: str
    :return:
    """

    api_url = setup_option['site_url']
    setup_params = {
        "country_code": country_code,
    }
    api_response = get_response(api_url, setup_params)
    json_content = json.loads(api_response.content.decode('utf-8'))
    response_message = f"""EndPoint: {api_url}?country_code={country_code}
    Status: {api_response.status_code}
    Body: {json_content}
    """
    assert api_response.status_code == 200, f"""Статус ответа {api_response.status_code} != 200\r\n""" + response_message
    relative_path = join('../datasets', 'json_error_schemas_country_code.json')
    filename = join(dirname(__file__), relative_path)
    schema = load_json_schema(filename=filename)
    check = Draft7Validator(schema=schema).is_valid(json_content)
    assert check, f"""Ошибка при валидации схемы негативного запроса кода страны {country_code}\r\n""" + response_message


@pytest.mark.parametrize("country_code",
                         get_not_valid_country_code(lang_uses='all',
                                                    char_size='lower',
                                                    count_chars=3,
                                                    len_list=10))
def test_13_accept_negation_country_three_lower_mix_chars(setup_option, country_code):
    """Проверка ответов API при передачи трех строчных латинских или кириллических символов

    :param setup_option: Установочные параметры
    :type setup_option: dict
    :param country_code: Код страны
    :type country_code: str
    :return:
    """

    api_url = setup_option['site_url']
    setup_params = {
        "country_code": country_code,
    }
    api_response = get_response(api_url, setup_params)
    json_content = json.loads(api_response.content.decode('utf-8'))
    response_message = f"""EndPoint: {api_url}?country_code={setup_option, country_code}
    Status: {api_response.status_code}
    Body: {json_content}
    """
    assert api_response.status_code == 200, f"""Статус ответа {api_response.status_code} != 200\r\n""" + response_message
    relative_path = join('../datasets', 'json_error_schemas_country_code.json')
    filename = join(dirname(__file__), relative_path)
    schema = load_json_schema(filename=filename)
    check = Draft7Validator(schema=schema).is_valid(json_content)
    assert check, f"""Ошибка при валидации схемы негативного запроса кода страны {country_code}\r\n""" + response_message


@pytest.mark.parametrize("country_code",
                         get_not_valid_country_code(lang_uses='en',
                                                    char_size='upper',
                                                    count_chars=1,
                                                    len_list=10))
def test_14_accept_negation_country_one_upper_latin_char(setup_option, country_code):
    """Проверка ответов API при передачи одного заглавного латинского символа

    :param setup_option: Установочные параметры
    :type setup_option: dict
    :param country_code: Код страны
    :type country_code: str
    :return:
    """
    api_url = setup_option['site_url']
    setup_params = {
        "country_code": country_code,
    }
    api_response = get_response(api_url, setup_params)
    json_content = json.loads(api_response.content.decode('utf-8'))
    response_message = f"""EndPoint: {api_url}?country_code={country_code}
    Status: {api_response.status_code}
    Body: {json_content}
    """
    assert api_response.status_code == 200, f"""Статус ответа {api_response.status_code} != 200\r\n""" + response_message
    relative_path = join('../datasets', 'json_error_schemas_country_code.json')
    filename = join(dirname(__file__), relative_path)
    schema = load_json_schema(filename=filename)
    check = Draft7Validator(schema=schema).is_valid(json_content)
    assert check, f"""Ошибка при валидации схемы негативного запроса кода страны {country_code}\r\n""" + response_message


@pytest.mark.parametrize("country_code",
                         get_not_valid_country_code(lang_uses='en',
                                                    char_size='upper',
                                                    count_chars=2,
                                                    len_list=10))
def test_15_accept_negation_country_two_upper_latin_chars(setup_option, country_code):
    """Проверка ответов API при передачи двух заглавных латинских символов

    :param setup_option: Установочные параметры
    :type setup_option: dict
    :param country_code: Код страны
    :type country_code: str
    :return:
    """

    api_url = setup_option['site_url']
    setup_params = {
        "country_code": country_code,
    }
    api_response = get_response(api_url, setup_params)
    json_content = json.loads(api_response.content.decode('utf-8'))
    response_message = f"""EndPoint: {api_url}?country_code={country_code}
    Status: {api_response.status_code}
    Body: {json_content}
    """
    assert api_response.status_code == 200, f"""Статус ответа {api_response.status_code} != 200\r\n""" + response_message
    relative_path = join('../datasets', 'json_error_schemas_country_code.json')
    filename = join(dirname(__file__), relative_path)
    schema = load_json_schema(filename=filename)
    check = Draft7Validator(schema=schema).is_valid(json_content)
    assert check, f"""Ошибка при валидации схемы негативного запроса кода страны {country_code}\r\n""" + response_message


@pytest.mark.parametrize("country_code",
                         get_not_valid_country_code(lang_uses='en',
                                                    char_size='upper',
                                                    count_chars=3,
                                                    len_list=10))
def test_16_accept_negation_country_three_upper_latin_chars(setup_option, country_code):
    """Проверка ответов API при передачи трех заглавных латинских символов

    :param setup_option: Установочные параметры
    :type setup_option: dict
    :param country_code: Код страны
    :type country_code: str
    :return:
    """

    api_url = setup_option['site_url']
    setup_params = {
        "country_code": country_code,
    }
    api_response = get_response(api_url, setup_params)
    json_content = json.loads(api_response.content.decode('utf-8'))
    response_message = f"""EndPoint: {api_url}?country_code={country_code}
    Status: {api_response.status_code}
    Body: {json_content}
    """
    assert api_response.status_code == 200, f"""Статус ответа {api_response.status_code} != 200\r\n""" + response_message
    relative_path = join('../datasets', 'json_error_schemas_country_code.json')
    filename = join(dirname(__file__), relative_path)
    schema = load_json_schema(filename=filename)
    check = Draft7Validator(schema=schema).is_valid(json_content)
    assert check, f"""Ошибка при валидации схемы негативного запроса кода страны {country_code}\r\n""" + response_message


@pytest.mark.parametrize("country_code",
                         get_not_valid_country_code(lang_uses='ru',
                                                    char_size='upper',
                                                    count_chars=1,
                                                    len_list=10))
def test_17_accept_negation_country_one_upper_cyrillic_char(setup_option, country_code):
    """Проверка ответов API при передачи одного заглавного кириллического символа

    :param setup_option: Установочные параметры
    :type setup_option: dict
    :param country_code: Код страны
    :type country_code: str
    :return:
    """

    api_url = setup_option['site_url']
    setup_params = {
        "country_code": country_code,
    }
    api_response = get_response(api_url, setup_params)
    json_content = json.loads(api_response.content.decode('utf-8'))
    response_message = f"""EndPoint: {api_url}?country_code={country_code}
    Status: {api_response.status_code}
    Body: {json_content}
    """
    assert api_response.status_code == 200, f"""Статус ответа {api_response.status_code} != 200\r\n""" + response_message
    relative_path = join('../datasets', 'json_error_schemas_country_code.json')
    filename = join(dirname(__file__), relative_path)
    schema = load_json_schema(filename=filename)
    check = Draft7Validator(schema=schema).is_valid(json_content)
    assert check, f"""Ошибка при валидации схемы негативного запроса кода страны {country_code}\r\n""" + response_message

@pytest.mark.parametrize("country_code",
                         get_not_valid_country_code(lang_uses='ru',
                                                    char_size='upper',
                                                    count_chars=2,
                                                    len_list=10))
def test_18_accept_negation_country_two_upper_cyrillic_chars(setup_option, country_code):
    """Проверка ответов API при передачи двух заглавных кириллических символов

    :param setup_option: Установочные параметры
    :type setup_option: dict
    :param country_code: Код страны
    :type country_code: str
    :return:
    """

    api_url = setup_option['site_url']
    setup_params = {
        "country_code": country_code,
    }
    api_response = get_response(api_url, setup_params)
    json_content = json.loads(api_response.content.decode('utf-8'))
    response_message = f"""EndPoint: {api_url}?country_code={country_code}
    Status: {api_response.status_code}
    Body: {json_content}
    """
    assert api_response.status_code == 200, f"""Статус ответа {api_response.status_code} != 200\r\n""" + response_message
    relative_path = join('../datasets', 'json_error_schemas_country_code.json')
    filename = join(dirname(__file__), relative_path)
    schema = load_json_schema(filename=filename)
    check = Draft7Validator(schema=schema).is_valid(json_content)
    assert check, f"""Ошибка при валидации схемы негативного запроса кода страны {country_code}\r\n""" + response_message

@pytest.mark.parametrize("country_code",
                         get_not_valid_country_code(lang_uses='ru',
                                                    char_size='upper',
                                                    count_chars=3,
                                                    len_list=10))
def test_19_accept_negation_country_three_upper_cyrillic_chars(setup_option, country_code):
    """Проверка ответов API при передачи трех заглавных кириллических символов

    :param setup_option: Установочные параметры
    :type setup_option: dict
    :param country_code: Код страны
    :type country_code: str
    :return:
    """

    api_url = setup_option['site_url']
    setup_params = {
        "country_code": country_code,
    }
    api_response = get_response(api_url, setup_params)
    json_content = json.loads(api_response.content.decode('utf-8'))
    response_message = f"""EndPoint: {api_url}?country_code={country_code}
    Status: {api_response.status_code}
    Body: {json_content}
    """
    assert api_response.status_code == 200, f"""Статус ответа {api_response.status_code} != 200\r\n""" + response_message
    relative_path = join('../datasets', 'json_error_schemas_country_code.json')
    filename = join(dirname(__file__), relative_path)
    schema = load_json_schema(filename=filename)
    check = Draft7Validator(schema=schema).is_valid(json_content)
    assert check, f"""Ошибка при валидации схемы негативного запроса кода страны {country_code}\r\n""" + response_message


@pytest.mark.parametrize("country_code",
                         get_not_valid_country_code(lang_uses='all',
                                                    char_size='upper',
                                                    count_chars=1,
                                                    len_list=10))
def test_20_accept_negation_country_one_upper_mix_char(setup_option, country_code):
    """Проверка ответов API при передачи одного заглавного или строчного латинского или кириллического символа

     :param setup_option: Установочные параметры
     :type setup_option: dict
     :param country_code: Код страны
     :type country_code: str
     :return:
     """

    api_url = setup_option['site_url']
    setup_params = {
        "country_code": country_code,
    }
    api_response = get_response(api_url, setup_params)
    json_content = json.loads(api_response.content.decode('utf-8'))
    response_message = f"""EndPoint: {api_url}?country_code={country_code}
    Status: {api_response.status_code}
    Body: {json_content}
    """
    assert api_response.status_code == 200, f"""Статус ответа {api_response.status_code} != 200\r\n""" + response_message
    relative_path = join('../datasets', 'json_error_schemas_country_code.json')
    filename = join(dirname(__file__), relative_path)
    schema = load_json_schema(filename=filename)
    check = Draft7Validator(schema=schema).is_valid(json_content)
    assert check, f"""Ошибка при валидации схемы негативного запроса кода страны {country_code}\r\n""" + response_message


@pytest.mark.parametrize("country_code",
                         get_not_valid_country_code(lang_uses='all',
                                                    char_size='upper',
                                                    count_chars=2,
                                                    len_list=10))
def test_21_accept_negation_country_two_upper_mix_chars(setup_option, country_code):
    """Проверка ответов API при передачи двух заглавных латинских или кириллических символов

     :param setup_option: Установочные параметры
     :type setup_option: dict
     :param country_code: Код страны
     :type country_code: str
     :return:
     """

    api_url = setup_option['site_url']
    setup_params = {
        "country_code": country_code,
    }
    api_response = get_response(api_url, setup_params)
    json_content = json.loads(api_response.content.decode('utf-8'))
    response_message = f"""EndPoint: {api_url}?country_code={country_code}
    Status: {api_response.status_code}
    Body: {json_content}
    """
    assert api_response.status_code == 200, f"""Статус ответа {api_response.status_code} != 200\r\n""" + response_message
    relative_path = join('../datasets', 'json_error_schemas_country_code.json')
    filename = join(dirname(__file__), relative_path)
    schema = load_json_schema(filename=filename)
    check = Draft7Validator(schema=schema).is_valid(json_content)
    assert check, f"""Ошибка при валидации схемы негативного запроса кода страны {country_code}\r\n""" + response_message


@pytest.mark.parametrize("country_code",
                         get_not_valid_country_code(lang_uses='all',
                                                    char_size='upper',
                                                    count_chars=3,
                                                    len_list=10))
def test_22_accept_negation_country_three_upper_mix_chars(setup_option, country_code):
    """Проверка ответов API при передачи трех заглавных латинских или кириллических символов

     :param setup_option: Установочные параметры
     :type setup_option: dict
     :param country_code: Код страны
     :type country_code: str
     :return:
     """

    api_url = setup_option['site_url']
    setup_params = {
        "country_code": country_code,
    }
    api_response = get_response(api_url, setup_params)
    json_content = json.loads(api_response.content.decode('utf-8'))
    response_message = f"""EndPoint: {api_url}?country_code={country_code}
    Status: {api_response.status_code}
    Body: {json_content}
    """
    assert api_response.status_code == 200, f"""Статус ответа {api_response.status_code} != 200\r\n""" + response_message
    relative_path = join('../datasets', 'json_error_schemas_country_code.json')
    filename = join(dirname(__file__), relative_path)
    schema = load_json_schema(filename=filename)
    check = Draft7Validator(schema=schema).is_valid(json_content)
    assert check, f"""Ошибка при валидации схемы негативного запроса кода страны {country_code}\r\n""" + response_message

@pytest.mark.parametrize("country_code",
                         get_not_valid_country_code(lang_uses='en',
                                                    char_size='all',
                                                    count_chars=1,
                                                    len_list=10))
def test_023_accept_negation_country_one_mix_latin_char(setup_option, country_code):
    """Проверка ответов API при передачи одного заглавного или строчного латинского символа

     :param setup_option: Установочные параметры
     :type setup_option: dict
     :param country_code: Код страны
     :type country_code: str
     :return:
     """

    api_url = setup_option['site_url']
    setup_params = {
        "country_code": country_code,
    }
    api_response = get_response(api_url, setup_params)
    json_content = json.loads(api_response.content.decode('utf-8'))
    response_message = f"""EndPoint: {api_url}?country_code={country_code}
    Status: {api_response.status_code}
    Body: {json_content}
    """
    assert api_response.status_code == 200, f"""Статус ответа {api_response.status_code} != 200\r\n""" + response_message
    relative_path = join('../datasets', 'json_error_schemas_country_code.json')
    filename = join(dirname(__file__), relative_path)
    schema = load_json_schema(filename=filename)
    check = Draft7Validator(schema=schema).is_valid(json_content)
    assert check, f"""Ошибка при валидации схемы негативного запроса кода страны {country_code}\r\n""" + response_message

@pytest.mark.parametrize("country_code",
                         get_not_valid_country_code(lang_uses='en',
                                                    char_size='all',
                                                    count_chars=2,
                                                    len_list=10))
def test_24_accept_negation_country_two_mix_latin_chars(setup_option, country_code):
    """Проверка ответов API при передачи двух заглавных или строчных латинских символов

     :param setup_option: Установочные параметры
     :type setup_option: dict
     :param country_code: Код страны
     :type country_code: str
     :return:
     """

    api_url = setup_option['site_url']
    setup_params = {
        "country_code": country_code,
    }
    api_response = get_response(api_url, setup_params)
    json_content = json.loads(api_response.content.decode('utf-8'))
    response_message = f"""EndPoint: {api_url}?country_code={country_code}
    Status: {api_response.status_code}
    Body: {json_content}
    """
    assert api_response.status_code == 200, f"""Статус ответа {api_response.status_code} != 200\r\n""" + response_message
    relative_path = join('../datasets', 'json_error_schemas_country_code.json')
    filename = join(dirname(__file__), relative_path)
    schema = load_json_schema(filename=filename)
    check = Draft7Validator(schema=schema).is_valid(json_content)
    assert check, f"""Ошибка при валидации схемы негативного запроса кода страны {country_code}\r\n""" + response_message


@pytest.mark.parametrize("country_code",
                         get_not_valid_country_code(lang_uses='en',
                                                    char_size='all',
                                                    count_chars=3,
                                                    len_list=10))
def test_25_accept_negation_country_three_mix_latin_chars(setup_option, country_code):
    """Проверка ответов API при передачи трех заглавных или строчных латинских символов

     :param setup_option: Установочные параметры
     :type setup_option: dict
     :param country_code: Код страны
     :type country_code: str
     :return:
     """

    api_url = setup_option['site_url']
    setup_params = {
        "country_code": country_code,
    }
    api_response = get_response(api_url, setup_params)
    json_content = json.loads(api_response.content.decode('utf-8'))
    response_message = f"""EndPoint: {api_url}?country_code={country_code}
    Status: {api_response.status_code}
    Body: {json_content}
    """
    assert api_response.status_code == 200, f"""Статус ответа {api_response.status_code} != 200\r\n""" + response_message
    relative_path = join('../datasets', 'json_error_schemas_country_code.json')
    filename = join(dirname(__file__), relative_path)
    schema = load_json_schema(filename=filename)
    check = Draft7Validator(schema=schema).is_valid(json_content)
    assert check, f"""Ошибка при валидации схемы негативного запроса кода страны {country_code}\r\n""" + response_message


@pytest.mark.parametrize("country_code",
                         get_not_valid_country_code(lang_uses='ru',
                                                    char_size='all',
                                                    count_chars=1,
                                                    len_list=10))
def test_26_accept_negation_country_one_mix_cyrillic_char(setup_option, country_code):
    """Проверка ответов API при передачи одного заглавного или строчного кириллического символа

     :param setup_option: Установочные параметры
     :type setup_option: dict
     :param country_code: Код страны
     :type country_code: str
     :return:
     """

    api_url = setup_option['site_url']
    setup_params = {
        "country_code": country_code,
    }
    api_response = get_response(api_url, setup_params)
    json_content = json.loads(api_response.content.decode('utf-8'))
    response_message = f"""EndPoint: {api_url}?country_code={country_code}
    Status: {api_response.status_code}
    Body: {json_content}
    """
    assert api_response.status_code == 200, f"""Статус ответа {api_response.status_code} != 200\r\n""" + response_message
    relative_path = join('../datasets', 'json_error_schemas_country_code.json')
    filename = join(dirname(__file__), relative_path)
    schema = load_json_schema(filename=filename)
    check = Draft7Validator(schema=schema).is_valid(json_content)
    assert check, f"""Ошибка при валидации схемы негативного запроса кода страны {country_code}\r\n""" + response_message

@pytest.mark.parametrize("country_code",
                         get_not_valid_country_code(lang_uses='ru',
                                                    char_size='all',
                                                    count_chars=2,
                                                    len_list=10))
def test_27_accept_negation_country_two_mix_cyrillic_chars(setup_option, country_code):
    """Проверка ответов API при передачи двух заглавных или строчных кирилических символов

     :param setup_option: Установочные параметры
     :type setup_option: dict
     :param country_code: Код страны
     :type country_code: str
     :return:
     """

    api_url = setup_option['site_url']
    setup_params = {
        "country_code": country_code,
    }
    api_response = get_response(api_url, setup_params)
    json_content = json.loads(api_response.content.decode('utf-8'))
    response_message = f"""EndPoint: {api_url}?country_code={country_code}
    Status: {api_response.status_code}
    Body: {json_content}
    """
    assert api_response.status_code == 200, f"""Статус ответа {api_response.status_code} != 200\r\n""" + response_message
    relative_path = join('../datasets', 'json_error_schemas_country_code.json')
    filename = join(dirname(__file__), relative_path)
    schema = load_json_schema(filename=filename)
    check = Draft7Validator(schema=schema).is_valid(json_content)
    assert check, f"""Ошибка при валидации схемы негативного запроса кода страны {country_code}\r\n""" + response_message

@pytest.mark.parametrize("country_code",
                         get_not_valid_country_code(lang_uses='ru',
                                                    char_size='all',
                                                    count_chars=3,
                                                    len_list=10))
def test_28_accept_negation_country_three_mix_cyrillic_chars(setup_option, country_code):
    """Проверка ответов API при передачи трех заглавных или строчных кирилических символов

     :param setup_option: Установочные параметры
     :type setup_option: dict
     :param country_code: Код страны
     :type country_code: str
     :return:
     """

    api_url = setup_option['site_url']
    setup_params = {
        "country_code": country_code,
    }
    api_response = get_response(api_url, setup_params)
    json_content = json.loads(api_response.content.decode('utf-8'))
    response_message = f"""EndPoint: {api_url}?country_code={country_code}
    Status: {api_response.status_code}
    Body: {json_content}
    """
    assert api_response.status_code == 200, f"""Статус ответа {api_response.status_code} != 200\r\n""" + response_message
    relative_path = join('../datasets', 'json_error_schemas_country_code.json')
    filename = join(dirname(__file__), relative_path)
    schema = load_json_schema(filename=filename)
    check = Draft7Validator(schema=schema).is_valid(json_content)
    assert check, f"""Ошибка при валидации схемы негативного запроса кода страны {country_code}\r\n""" + response_message


@pytest.mark.parametrize("country_code",
                         get_not_valid_country_code(lang_uses='all',
                                                    char_size='all',
                                                    count_chars=1,
                                                    len_list=10))
def test_29_accept_negation_country_one_mix_mix_char(setup_option, country_code):
    """Проверка ответов API при передачи одного заглавного или строчного кирилического или латинского символа

      :param setup_option: Установочные параметры
      :type setup_option: dict
      :param country_code: Код страны
      :type country_code: str
      :return:
      """

    api_url = setup_option['site_url']
    setup_params = {
        "country_code": country_code,
    }
    api_response = get_response(api_url, setup_params)
    json_content = json.loads(api_response.content.decode('utf-8'))
    response_message = f"""EndPoint: {api_url}?country_code={country_code}
    Status: {api_response.status_code}
    Body: {json_content}
    """
    assert api_response.status_code == 200, f"""Статус ответа {api_response.status_code} != 200\r\n""" + response_message
    relative_path = join('../datasets', 'json_error_schemas_country_code.json')
    filename = join(dirname(__file__), relative_path)
    schema = load_json_schema(filename=filename)
    check = Draft7Validator(schema=schema).is_valid(json_content)
    assert check, f"""Ошибка при валидации схемы негативного запроса кода страны {country_code}\r\n""" + response_message


@pytest.mark.parametrize("country_code",
                         get_not_valid_country_code(lang_uses='all',
                                                    char_size='all',
                                                    count_chars=2,
                                                    len_list=10))
def test_30_accept_negation_country_two_mix_mix_chars(setup_option, country_code):
    """Проверка ответов API при передачи двух заглавных или строчных кирилических или латинских символов

      :param setup_option: Установочные параметры
      :type setup_option: dict
      :param country_code: Код страны
      :type country_code: str
      :return:
      """

    api_url = setup_option['site_url']
    setup_params = {
        "country_code": country_code,
    }
    api_response = get_response(api_url, setup_params)
    json_content = json.loads(api_response.content.decode('utf-8'))
    response_message = f"""EndPoint: {api_url}?country_code={country_code}
    Status: {api_response.status_code}
    Body: {json_content}
    """
    assert api_response.status_code == 200, f"""Статус ответа {api_response.status_code} != 200\r\n""" + response_message
    relative_path = join('../datasets', 'json_error_schemas_country_code.json')
    filename = join(dirname(__file__), relative_path)
    schema = load_json_schema(filename=filename)
    check = Draft7Validator(schema=schema).is_valid(json_content)
    assert check, f"""Ошибка при валидации схемы негативного запроса кода страны {country_code}\r\n""" + response_message


@pytest.mark.parametrize("country_code",
                         get_not_valid_country_code(lang_uses='all',
                                                    char_size='all',
                                                    count_chars=3,
                                                    len_list=10))
def test_31_accept_negation_country_three_mix_mix_chars(setup_option, country_code):
    """Проверка ответов API при передачи трех заглавных или строчных кирилических или латинских символов

      :param setup_option: Установочные параметры
      :type setup_option: dict
      :param country_code: Код страны
      :type country_code: str
      :return:
      """

    api_url = setup_option['site_url']
    setup_params = {
        "country_code": country_code,
    }
    api_response = get_response(api_url, setup_params)
    json_content = json.loads(api_response.content.decode('utf-8'))
    response_message = f"""EndPoint: {api_url}?country_code={country_code}
    Status: {api_response.status_code}
    Body: {json_content}
    """
    assert api_response.status_code == 200, f"""Статус ответа {api_response.status_code} != 200\r\n""" + response_message
    relative_path = join('../datasets', 'json_error_schemas_country_code.json')
    filename = join(dirname(__file__), relative_path)
    schema = load_json_schema(filename=filename)
    check = Draft7Validator(schema=schema).is_valid(json_content)
    assert check, f"""Ошибка при валидации схемы негативного запроса кода страны {country_code}\r\n""" + response_message