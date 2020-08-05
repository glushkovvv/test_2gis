# -*- coding: utf-8 -*-
"""
test_01_accept_time_get_headers
~~~~~~~~~~~~~~

The 2GIS API Test
Check time get headers

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
from tools.api_responses import get_response


@allure.epic("Поизитивные тесты API")
@allure.suite("Позитивное тестирование время ответов")
@allure.title("Проверка время ответа при нечётком поиске, при фильтрации по коду страны, при постраничной разбивке")
@pytest.mark.parametrize("json_params", [{"page": 1, "page_size": 5},
                                         {"country_code": "ru", "page": 1, "page_size": 5},
                                         {"q": "ОРСК"}])
def test_01_time_response_for_valid_request(setup_option, json_params):
    """
    Проверяем время ответов сервера при валидных запросах
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
                       f"  Content:  {api_response.content}")
    check = api_response.elapsed.total_seconds() <= 0.2
    assert check, f"""Время ответа {api_response.elapsed.total_seconds()} больше 0.2 сек\r\n""" + testing_message


@allure.epic("Смок тесты API")
@allure.suite("Позитивное тестирование время ответов")
@allure.title("Проверка время ответа при нечётком поиске, при фильтрации по коду страны, при постраничной разбивке")
@pytest.mark.parametrize("json_params", [{"page": 1, "page_size": 2},
                                         {"country_code": "tz", "page": 1, "page_size": 5},
                                         {"q": "ОР"}])
def test_01_time_response_for_invalid_request(setup_option, json_params):
    """
    Проверяем время ответов сервера при невалидных запросах
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
                       f"  Content:  {api_response.content}")
    check = api_response.elapsed.total_seconds() <= 0.5
    assert check, f"""Время ответа {api_response.elapsed.total_seconds()} больше 0.5 сек\r\n""" + testing_message
