# -*- coding: utf-8 -*-
"""
test_01_accept_negative_country_code_upper
~~~~~~~~~~~~~~

The 2GIS API Test
Check negative country_code upper character

:author: Vadim Glushkov
:copyright: Copyright 2019, The2GIS API Test"
:license: MIT
:version: 1.0.0
:maintainer: Vadim Glushkov
:email: plussg@yandex.ru
:status: Development
"""


import json
from os.path import join, dirname
import pytest
import allure
from jsonschema import Draft7Validator
from tools.string_manipulation import get_not_valid_country_code
from tools.api_responses import get_response
from tools.load_json_schema import load_json_schema


@allure.epic("Негативные тесты API")
@allure.suite("Фильтрация по коду страны. Заглавные латинские символы.")
@allure.title("Проверка ответов при передачи в качестве параметра code_country одного заглавного лат. символа")
@pytest.mark.parametrize("country_code",
                         get_not_valid_country_code(lang_uses='en',
                                                    char_size='upper',
                                                    count_chars=1,
                                                    len_list=10))
def test_13_accept_negative_country_upper_latin_one_char(setup_option, country_code):
    """Проверка ответов API при передачи в качестве кода страны одного заглавного латинского символа

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
    response_message = (f"  EndPoint: {api_url}?country_code={country_code}\n"
                        f"  Status:   {api_response.status_code}\n"
                        f"  Headers:  {api_response.headers}\n"
                        f"  Body:     {json_content}")
    assert api_response.status_code == 200, f"""Статус {api_response.status_code} != 200\r\n""" + response_message
    relative_path = join('../datasets', 'json_error_schemas_for_test.json')
    filename = join(dirname(__file__), relative_path)
    schema = load_json_schema(filename=filename)
    check = Draft7Validator(schema=schema).is_valid(json_content)
    assert check, f"""Ошибка при валидации json схемы {country_code}\r\n""" + response_message


@allure.epic("Негативные тесты API")
@allure.suite("Фильтрация по коду страны. Заглавные латинские символы.")
@allure.title("Проверка ответов при передачи в качестве параметра code_country двух заглавных лат. символов")
@pytest.mark.parametrize("country_code",
                         get_not_valid_country_code(lang_uses='en',
                                                    char_size='upper',
                                                    count_chars=2,
                                                    len_list=10))
def test_14_accept_negative_country_upper_latin_two_chars(setup_option, country_code):
    """Проверка ответов API при передачи в качестве кода страны двух заглавных латинских символов

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
    response_message = (f"  EndPoint: {api_url}?country_code={country_code}\n"
                        f"  Status:   {api_response.status_code}\n"
                        f"  Headers:  {api_response.headers}\n"
                        f"  Body:     {json_content}")
    assert api_response.status_code == 200, f"""Статус {api_response.status_code} != 200\r\n""" + response_message
    relative_path = join('../datasets', 'json_error_schemas_for_test.json')
    filename = join(dirname(__file__), relative_path)
    schema = load_json_schema(filename=filename)
    check = Draft7Validator(schema=schema).is_valid(json_content)
    assert check, f"""Ошибка при валидации json схемы  {country_code}\r\n""" + response_message


@allure.epic("Негативные тесты API")
@allure.suite("Фильтрация по коду страны. Заглавные латинские символы.")
@allure.title("Проверка ответов при передачи в качестве параметра code_country трех заглавных лат. символов")
@pytest.mark.parametrize("country_code",
                         get_not_valid_country_code(lang_uses='en',
                                                    char_size='upper',
                                                    count_chars=3,
                                                    len_list=10))
def test_15_accept_negative_country_upper_latin_three_chars(setup_option, country_code):
    """Проверка ответов API при передачи в качестве кода страны трех заглавных латинских символов

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
    response_message = (f"  EndPoint: {api_url}?country_code={country_code}\n"
                        f"  Status:   {api_response.status_code}\n"
                        f"  Headers:  {api_response.headers}\n"
                        f"  Body:     {json_content}")
    assert api_response.status_code == 200, f"""Статус {api_response.status_code} != 200\r\n""" + response_message
    relative_path = join('../datasets', 'json_error_schemas_for_test.json')
    filename = join(dirname(__file__), relative_path)
    schema = load_json_schema(filename=filename)
    check = Draft7Validator(schema=schema).is_valid(json_content)
    assert check, f"""Ошибка при валидации json схемы {country_code}\r\n""" + response_message


@allure.epic("Негативные тесты API")
@allure.suite("Фильтрация по коду страны. Заглавные кирилические символы.")
@allure.title("Проверка ответов при передачи в качестве параметра code_country одного заглавного кир. символа")
@pytest.mark.parametrize("country_code",
                         get_not_valid_country_code(lang_uses='ru',
                                                    char_size='upper',
                                                    count_chars=1,
                                                    len_list=10))
def test_16_accept_negative_country_upper_cyrillic_one_char(setup_option, country_code):
    """Проверка ответов API при передачи в качестве кода страны одного заглавного кириллического символа

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
    response_message = (f"  EndPoint: {api_url}?country_code={country_code}\n"
                        f"  Status:   {api_response.status_code}\n"
                        f"  Headers:  {api_response.headers}\n"
                        f"  Body:     {json_content}")
    assert api_response.status_code == 200, f"""Статус {api_response.status_code} != 200\r\n""" + response_message
    relative_path = join('../datasets', 'json_error_schemas_for_test.json')
    filename = join(dirname(__file__), relative_path)
    schema = load_json_schema(filename=filename)
    check = Draft7Validator(schema=schema).is_valid(json_content)
    assert check, f"""Ошибка при валидации json схемы {country_code}\r\n""" + response_message


@allure.epic("Негативные тесты API")
@allure.suite("Фильтрация по коду страны. Заглавные кирилические символы.")
@allure.title("Проверка ответов при передачи в качестве параметра code_country 2 заглавных кир. символов")
@pytest.mark.parametrize("country_code",
                         get_not_valid_country_code(lang_uses='ru',
                                                    char_size='upper',
                                                    count_chars=2,
                                                    len_list=10))
def test_17_accept_negative_country_upper_cyrillic_chars(setup_option, country_code):
    """Проверка ответов API при передачи в качестве кода страны двух заглавных кириллических символов

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
    response_message = (f"  EndPoint: {api_url}?country_code={country_code}\n"
                        f"  Status:   {api_response.status_code}\n"
                        f"  Headers:  {api_response.headers}\n"
                        f"  Body:     {json_content}")
    assert api_response.status_code == 200, f"""Статус {api_response.status_code} != 200\r\n""" + response_message
    relative_path = join('../datasets', 'json_error_schemas_for_test.json')
    filename = join(dirname(__file__), relative_path)
    schema = load_json_schema(filename=filename)
    check = Draft7Validator(schema=schema).is_valid(json_content)
    assert check, f"""Ошибка при валидации json схемы {country_code}\r\n""" + response_message


@allure.epic("Негативные тесты API")
@allure.suite("Фильтрация по коду страны. Заглавные кирилические символы.")
@allure.title("Проверка ответов при передачи в качестве параметра code_country 3 заглавных кир. символов")
@pytest.mark.parametrize("country_code",
                         get_not_valid_country_code(lang_uses='ru',
                                                    char_size='upper',
                                                    count_chars=3,
                                                    len_list=10))
def test_18_accept_negative_country_upper_cyrillic_three_chars(setup_option, country_code):
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
    response_message = (f"  EndPoint: {api_url}?country_code={country_code}\n"
                        f"  Status:   {api_response.status_code}\n"
                        f"  Headers:  {api_response.headers}\n"
                        f"  Body:     {json_content}")
    assert api_response.status_code == 200, f"""Статус {api_response.status_code} != 200\r\n""" + response_message
    relative_path = join('../datasets', 'json_error_schemas_for_test.json')
    filename = join(dirname(__file__), relative_path)
    schema = load_json_schema(filename=filename)
    check = Draft7Validator(schema=schema).is_valid(json_content)
    assert check, f"""Ошибка при валидации json схемы {country_code}\r\n""" + response_message


@allure.epic("Негативные тесты API")
@allure.suite("Фильтрация по коду страны. Заглавные кирилические или латинские символы.")
@allure.title("Проверка ответов при передачи в качестве параметра code_country 2 заглавных кир. или лат. символов")
@pytest.mark.parametrize("country_code",
                         get_not_valid_country_code(lang_uses='all',
                                                    char_size='upper',
                                                    count_chars=2,
                                                    len_list=10))
def test_19_accept_negative_country_upper_mix_two_chars(setup_option, country_code):
    """Проверка ответов API при передачи в качестве кода страны двух заглавных латинских или кириллических символов

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
    response_message = (f"  EndPoint: {api_url}?country_code={country_code}\n"
                        f"  Status:   {api_response.status_code}\n"
                        f"  Headers:  {api_response.headers}\n"
                        f"  Body:     {json_content}")
    assert api_response.status_code == 200, f"""Статус {api_response.status_code} != 200\r\n""" + response_message
    relative_path = join('../datasets', 'json_error_schemas_for_test.json')
    filename = join(dirname(__file__), relative_path)
    schema = load_json_schema(filename=filename)
    check = Draft7Validator(schema=schema).is_valid(json_content)
    assert check, f"""Ошибка при валидации json схемы {country_code}\r\n""" + response_message


@allure.epic("Негативные тесты API")
@allure.suite("Фильтрация по коду страны. Заглавные кирилические или латинские символы.")
@allure.title("Проверка ответов при передачи в качестве параметра code_country 3 заглавных кир. или лат. символов")
@pytest.mark.parametrize("country_code",
                         get_not_valid_country_code(lang_uses='all',
                                                    char_size='upper',
                                                    count_chars=3,
                                                    len_list=10))
def test_20_accept_negative_country_upper_mix_three_chars(setup_option, country_code):
    """Проверка ответов API при передачи в качестве кода страны трех заглавных латинских или кириллических символов

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
    response_message = (f"  EndPoint: {api_url}?country_code={country_code}\n"
                        f"  Status:   {api_response.status_code}\n"
                        f"  Headers:  {api_response.headers}\n"
                        f"  Body:     {json_content}")
    assert api_response.status_code == 200, f"""Статус {api_response.status_code} != 200\r\n""" + response_message
    relative_path = join('../datasets', 'json_error_schemas_for_test.json')
    filename = join(dirname(__file__), relative_path)
    schema = load_json_schema(filename=filename)
    check = Draft7Validator(schema=schema).is_valid(json_content)
    assert check, f"""Ошибка при валидации json схемы {country_code}\r\n""" + response_message


@allure.epic("Негативные тесты API")
@allure.suite("Фильтрация по коду страны. Заглавные или строчные латинские символы.")
@allure.title("Проверка ответов API при передачи в качестве code_country 2 заглавных или строчные лат. символов")
@pytest.mark.parametrize("country_code",
                         get_not_valid_country_code(lang_uses='en',
                                                    char_size='all',
                                                    count_chars=2,
                                                    len_list=10))
def test_21_accept_negative_country_mix_latin_two_chars(setup_option, country_code):
    """Проверка ответов API при передачи в качестве кода страныдвух заглавных или строчных латинских символов

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
    response_message = (f"  EndPoint: {api_url}?country_code={country_code}\n"
                        f"  Status:   {api_response.status_code}\n"
                        f"  Headers:  {api_response.headers}\n"
                        f"  Body:     {json_content}")
    assert api_response.status_code == 200, f"""Статус {api_response.status_code} != 200\r\n""" + response_message
    relative_path = join('../datasets', 'json_error_schemas_for_test.json')
    filename = join(dirname(__file__), relative_path)
    schema = load_json_schema(filename=filename)
    check = Draft7Validator(schema=schema).is_valid(json_content)
    assert check, f"""Ошибка при валидации json схемы {country_code}\r\n""" + response_message


@allure.epic("Негативные тесты API")
@allure.suite("Фильтрация по коду страны. Заглавные или строчные латинские символы.")
@allure.title("Проверка ответов API при передачи в качестве code_country 3 заглавных или строчные лат. символов")
@pytest.mark.parametrize("country_code",
                         get_not_valid_country_code(lang_uses='en',
                                                    char_size='all',
                                                    count_chars=3,
                                                    len_list=10))
def test_22_accept_negative_country_three_mix_latin_chars(setup_option, country_code):
    """Проверка ответов API при передачи в качестве кода страны трех заглавных или строчных латинских символов

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
    response_message = (f"  EndPoint: {api_url}?country_code={country_code}\n"
                        f"  Status:   {api_response.status_code}\n"
                        f"  Headers:  {api_response.headers}\n"
                        f"  Body:     {json_content}")
    assert api_response.status_code == 200, f"""Статус {api_response.status_code} != 200\r\n""" + response_message
    relative_path = join('../datasets', 'json_error_schemas_for_test.json')
    filename = join(dirname(__file__), relative_path)
    schema = load_json_schema(filename=filename)
    check = Draft7Validator(schema=schema).is_valid(json_content)
    assert check, f"""Ошибка при валидации json схемы {country_code}\r\n""" + response_message


@allure.epic("Негативные тесты API")
@allure.suite("Фильтрация по коду страны. Заглавные или строчные кириллические символы.")
@allure.title("Проверка ответов API при передачи в качестве code_country 2 заглавных или строчные кир. символов")
@pytest.mark.parametrize("country_code",
                         get_not_valid_country_code(lang_uses='ru',
                                                    char_size='all',
                                                    count_chars=2,
                                                    len_list=10))
def test_23_accept_negative_country_mix_cyrillic_two_chars(setup_option, country_code):
    """Проверка ответов API при передачи в качесве кода страны двух заглавных или строчных кирилических символов

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
    response_message = (f"  EndPoint: {api_url}?country_code={country_code}\n"
                        f"  Status:   {api_response.status_code}\n"
                        f"  Headers:  {api_response.headers}\n"
                        f"  Body:     {json_content}")
    assert api_response.status_code == 200, f"""Статус {api_response.status_code} != 200\r\n""" + response_message
    relative_path = join('../datasets', 'json_error_schemas_for_test.json')
    filename = join(dirname(__file__), relative_path)
    schema = load_json_schema(filename=filename)
    check = Draft7Validator(schema=schema).is_valid(json_content)
    assert check, f"""Ошибка при валидации json схемы {country_code}\r\n""" + response_message


@allure.epic("Негативные тесты API")
@allure.suite("Фильтрация по коду страны. Заглавные или строчные кириллические символы.")
@allure.title("Проверка ответов API при передачи в качестве code_country 3 заглавных или строчные кир. символов")
@pytest.mark.parametrize("country_code",
                         get_not_valid_country_code(lang_uses='ru',
                                                    char_size='all',
                                                    count_chars=3,
                                                    len_list=10))
def test_24_accept_negative_country_mix_cyrillic_three_chars(setup_option, country_code):
    """Проверка ответов API при передачи в качестве кода страны трех заглавных или строчных кирилических символов

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
    response_message = (f"  EndPoint: {api_url}?country_code={country_code}\n"
                        f"  Status:   {api_response.status_code}\n"
                        f"  Headers:  {api_response.headers}\n"
                        f"  Body:     {json_content}")
    assert api_response.status_code == 200, f"""Статус {api_response.status_code} != 200\r\n""" + response_message
    relative_path = join('../datasets', 'json_error_schemas_for_test.json')
    filename = join(dirname(__file__), relative_path)
    schema = load_json_schema(filename=filename)
    check = Draft7Validator(schema=schema).is_valid(json_content)
    assert check, f"""Ошибка при валидации json схемы {country_code}\r\n""" + response_message
