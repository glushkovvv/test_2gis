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
import allure
import json
from os.path import join, dirname
from jsonschema import Draft7Validator
from tools.string_manipulation import get_not_valid_country_code
from tools.api_responses import get_response
from tools.load_json_schema import load_json_schema

@allure.epic("Негативные тесты API")
@allure.suite("Фильтрация по коду страны. Строчные латинские символы.")
@allure.title("Проверка ответов при передачи в качестве параметра code_country одного латинского символа")
@pytest.mark.parametrize("country_code",
                         get_not_valid_country_code(lang_uses='en',
                                                    char_size='lower',
                                                    count_chars=1,
                                                    len_list=10))
def test_05_accept_negative_country_lower_latin_one_char(setup_option, country_code):
    """Проверка ответов API при передачи в качестве кода страны одного строчного латинского символа

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


@allure.epic("Негативные тесты API")
@allure.suite("Фильтрация по коду страны. Строчные латинские символы.")
@allure.title("Проверка ответов при передачи в качестве параметра code_country двух строчных латинских символов")
@pytest.mark.parametrize("country_code",
                         get_not_valid_country_code(lang_uses='en',
                                                    char_size='lower',
                                                    count_chars=2,
                                                    len_list=10))
def test_06_accept_negative_country_lower_latin_two_chars(setup_option, country_code):
    """Проверка ответов API при передачи в качестве кода страны двух строчных латинских символов

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


@allure.epic("Негативные тесты API")
@allure.suite("Фильтрация по коду страны. Строчные латинские символы.")
@allure.title("Проверка ответов при передачи в качестве параметра code_country трех строчных латинских символов")
@pytest.mark.parametrize("country_code",
                         get_not_valid_country_code(lang_uses='en',
                                                    char_size='lower',
                                                    count_chars=3,
                                                    len_list=10))
def test_07_accept_negative_country_lower_latin_three_chars(setup_option, country_code):
    """Проверка ответов API при передачи в качестве кода страны трех строчных латинских символов

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


@allure.epic("Негативные тесты API")
@allure.suite("Фильтрация по коду страны. Строчные кириллические символы.")
@allure.title("Проверка ответов при передачи в качестве параметра code_country одного строчного кириллического символа")
@pytest.mark.parametrize("country_code",
                         get_not_valid_country_code(lang_uses='ru',
                                                    char_size='lower',
                                                    count_chars=1,
                                                    len_list=10))
def test_08_accept_negative_country_lower_cyrillic_one_char(setup_option, country_code):
    """Проверка ответов API при передачи в качестве кода страны одного строчного кириллического символа

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


@allure.epic("Негативные тесты API")
@allure.suite("Фильтрация по коду страны. Строчные кириллические символы.")
@allure.title("Проверка ответов при передачи в качестве параметра code_country двух строчных кириллических символов")
@pytest.mark.parametrize("country_code",
                         get_not_valid_country_code(lang_uses='ru',
                                                    char_size='lower',
                                                    count_chars=2,
                                                    len_list=10))
def test_09_accept_negative_country_lower_cyrillic_two_chars(setup_option, country_code):
    """Проверка ответов API при передачи в качестве кода страны двух строчных кириллических символов

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


@allure.epic("Негативные тесты API")
@allure.suite("Фильтрация по коду страны. Строчные кириллические символы.")
@allure.title("Проверка ответов при передачи в качестве параметра code_country трех строчных кириллических символов")
@pytest.mark.parametrize("country_code",
                         get_not_valid_country_code(lang_uses='ru',
                                                    char_size='lower',
                                                    count_chars=3,
                                                    len_list=10))
def test_10_accept_negative_country_lower_cyrillic_three_chars(setup_option, country_code):
    """Проверка ответов API при передачи в качестве когда страны трех строчных кириллических символов

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


@allure.epic("Негативные тесты API")
@allure.suite("Фильтрация по коду страны. Строчные кириллические и латинские символы.")
@allure.title("Проверка ответов при передачи в качестве параметра code_country двух строчных кир. или лат. символов")
@pytest.mark.parametrize("country_code",
                         get_not_valid_country_code(lang_uses='all',
                                                    char_size='lower',
                                                    count_chars=2,
                                                    len_list=10))
def test_11_accept_negative_country_lower_mix_two_chars(setup_option, country_code):
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


@allure.epic("Негативные тесты API")
@allure.suite("Фильтрация по коду страны. Строчные кириллические и латинские символы.")
@allure.title("Проверка ответов при передачи в качестве параметра code_country трех строчных кир. или лат. символов")
@pytest.mark.parametrize("country_code",
                         get_not_valid_country_code(lang_uses='all',
                                                    char_size='lower',
                                                    count_chars=3,
                                                    len_list=10))
def test_12_accept_negative_country_lower_mix_three_chars(setup_option, country_code):
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
