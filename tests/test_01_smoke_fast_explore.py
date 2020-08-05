# -*- coding: utf-8 -*-
"""
test_01_smoke_search
~~~~~~~~~~~~~~

The 2GIS API Test
Fast smoke test

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
from tools.api_responses import get_response
from tools.load_json_schema import load_json_schema


@allure.epic("Смок тесты API")
@allure.suite("Смок тестирование статусов ответов")
@allure.title("Статус ответа при нечётком поиске, при фильтрации по коду страны, при постраничной разбивке")
@pytest.mark.parametrize("json_params", [{"q": "Влад"},
                                         {"country_code": "ru"},
                                         {"page": 1, "page_size": 5}])
def test_01_smoke_status_code(setup_option, json_params):
    """
    Проверяем статусы ответов сервера
    :param setup_option: Установочные параметры
    :type setup_option: dict
    :param json_params: Параметры GET запроса
    :type json_params: dict
    :return:
    """

    api_url = setup_option['site_url']
    request_params = json_params
    api_response = get_response(api_url, request_params)
    testing_message = (f"  EndPoint: {api_response.url}\n"
                       f"  Status:   {api_response.status_code}\n"
                       f"  Headers:  {api_response.headers}\n"
                       f"  Content:  {api_response.content}\n")
    assert api_response.status_code == 200, f"""Статус {api_response.status_code} != 200\r\n""" + testing_message


@allure.epic("Смок тесты API")
@allure.suite("Смок тестирование - соответствие ответа json схеме ")
@allure.title("Валидность ответа при нечётком поиске. При фильтрации по коду страны. При постраничной разбивке")
@pytest.mark.parametrize("json_params", [{"q": "Влад"},
                                         {"country_code": "ru"},
                                         {"page": 1, "page_size": 5}])
def test_01_smoke_valid_json_schema(setup_option, json_params):
    """
    Валидация тела ответа по правилам Draft7Validator (структура, имена ключей, тип значение)
    :param setup_option: Установочные параметры
    :type setup_option: dict
    :param json_params: Параметры GET запроса
    :type json_params: dict
    :return:
    """
    api_url = setup_option['site_url']
    request_params = json_params
    api_response = get_response(api_url, request_params)
    json_content = json.loads(api_response.content.decode('utf-8'))
    testing_message = (f"  EndPoint: {api_response.url}\n"
                       f"  Status: {api_response.status_code}\n"
                       f"  Headers: {api_response.headers}\n"
                       f"  Content: {api_response.content}")
    relative_path = join('../datasets', 'json_valid_schemas_for_test.json')
    filename = join(dirname(__file__), relative_path)
    schema = load_json_schema(filename=filename)
    check = Draft7Validator(schema=schema).is_valid(json_content)
    assert check, """Контент ответа не соответсвует json схеме\r\n""" + testing_message


@allure.epic("Смок тесты API")
@allure.suite("Смок тестирование - в ответе должны быть элементы")
@allure.title("Статус ответа при нечётком поиске. При фильтрации по коду страны. При постраничной разбивке")
@pytest.mark.parametrize("json_params", [{"q": "Влад"},
                                         {"country_code": "ru"},
                                         {"page": 1, "page_size": 5}])
def test_01_smoke_not_empty(setup_option, json_params):
    api_url = setup_option['site_url']
    request_params = json_params
    api_response = get_response(api_url, request_params)
    json_content = json.loads(api_response.content.decode('utf-8'))
    testing_message = (f"  EndPoint: {api_response.url}\n"
                       f"  Status:   {api_response.status_code}\n"
                       f"  Headers:  {api_response.headers}\n"
                       f"  Content:  {api_response.content}")
    if json_content.get("items"):
        check = True
    else:
        check = False
    assert check, """Нет необходимых элементов в ответе\r\n""" + testing_message


@allure.epic("Смок тесты API")
@allure.suite("Смок тестирование - загловок Content-Type")
@allure.title("Значение Content-Type при нечётком поиске. При фильтрации по коду страны. При постраничной разбивке")
@pytest.mark.parametrize("json_params", [{"q": "Влад"},
                                         {"country_code": "ru"},
                                         {"page": 1, "page_size": 5}])
def test_01_smoke_required_header(setup_option, json_params):
    """
    Проверяем, что возвращаемый заголовок Content-Type от сервера правильный application/json; charset=utf-8
    :param setup_option: Установочные параметры
    :type: dict
    :param json_params: Параметры запроса
    :return: dict
    """

    api_url = setup_option['site_url']
    request_params = json_params
    api_response = get_response(api_url, request_params)
    testing_message = (f"  EndPoint: {api_response.url}\n"
                       f"  Status:   {api_response.status_code}\n"
                       f"  Headers:  {api_response.headers}")
    if api_response.headers.get("Content-Type").lower() == "application/json; charset=utf-8":
        check = True
    else:
        check = False
    assert check, """Требуемый заголовок не найден\r\n""" + testing_message