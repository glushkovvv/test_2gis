# -*- coding: utf-8 -*-
"""
test_01_accept_negative_country_code_special
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


import json
from os.path import join, dirname
import pytest
import allure
from jsonschema import Draft7Validator
from tools.string_manipulation import get_space_and_end_character, get_special_character
from tools.api_responses import get_response
from tools.load_json_schema import load_json_schema


@allure.epic("Негативные тесты API")
@allure.suite("Фильтрация по коду страны. Пустота, пробелы, табуляция, перевод строк и прочее")
@allure.title("Проверка ответов при передачи в качестве параметра code_country пустых симвлов пустоты, пробела и т.п.")
@pytest.mark.parametrize("country_code",
                         get_space_and_end_character())
def test_01_accept_negative_space_char(setup_option, country_code):
    """Проверка ответов API при передачи в качестве кода страны пустоты, пробелов и т.п.

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
    assert api_response.status_code == 200, f"""Статус {api_response.status_code} != 200\r\n""" + response_message
    relative_path = join('../datasets', 'json_error_schemas_country_code.json')
    filename = join(dirname(__file__), relative_path)
    schema = load_json_schema(filename=filename)
    check = Draft7Validator(schema=schema).is_valid(json_content)
    assert check, f"""Ошибка при валидации json схемы {country_code}\r\n"""+response_message


@allure.epic("Негативные тесты API")
@allure.suite("Фильтрация по коду страны. Специальные символы.")
@allure.title("Проверка ответов при передачи в качестве параметра code_country одного специального символа")
@pytest.mark.parametrize("country_code",
                         get_special_character(count_chars=1,
                                               len_list=10))
def test_02_accept_negative_special_one_char(setup_option, country_code):
    """Проверка ответов API при передачи в качестве кода страны одного специального сивола

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
    assert api_response.status_code == 200, f"""Статус {api_response.status_code} != 200\r\n""" + response_message
    relative_path = join('../datasets', 'json_error_schemas_country_code.json')
    filename = join(dirname(__file__), relative_path)
    schema = load_json_schema(filename=filename)
    check = Draft7Validator(schema=schema).is_valid(json_content)
    assert check, f"""Ошибка при валидации json схемы {country_code}\r\n""" + response_message


@allure.epic("Негативные тесты API")
@allure.suite("Фильтрация по коду страны. Специальные символы.")
@allure.title("Проверка ответов при передачи в качестве параметра code_country пустых комбинации из 2 спец. символов")
@pytest.mark.parametrize("country_code",
                         get_special_character(count_chars=2,
                                               len_list=10))
def test_03_accept_negative_special_two_char(setup_option, country_code):
    """Проверка ответов API при передачи в качестве кода страны двух специальных сиволов

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
    assert api_response.status_code == 200, f"""Статус {api_response.status_code} != 200\r\n""" + response_message
    relative_path = join('../datasets', 'json_error_schemas_country_code.json')
    filename = join(dirname(__file__), relative_path)
    schema = load_json_schema(filename=filename)
    check = Draft7Validator(schema=schema).is_valid(json_content)
    assert check, f"""Ошибка при валидации json схемы {country_code}\r\n""" + response_message


@allure.epic("Негативные тесты API")
@allure.suite("Фильтрация по коду страны. Специальные символы.")
@allure.title("Проверка ответов при передачи в качестве параметра code_country пустых комбинации из 3 спец. символов")
@pytest.mark.parametrize("country_code",
                         get_special_character(count_chars=3,
                                               len_list=10))
def test_04_accept_negative_special_three_char(setup_option, country_code):
    """Проверка ответов API при передачи в качестве кода страны трех специальных символов

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
    assert api_response.status_code == 200, f"""Статус {api_response.status_code} != 200\r\n""" + response_message
    relative_path = join('../datasets', 'json_error_schemas_country_code.json')
    filename = join(dirname(__file__), relative_path)
    schema = load_json_schema(filename=filename)
    check = Draft7Validator(schema=schema).is_valid(json_content)
    assert check, f"""Ошибка при валидации json схемы {country_code}\r\n""" + response_message
