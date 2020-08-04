"""
test_01_accept_positive_page
~~~~~~~~~~~~~~

The 2GIS API Test
Check positive pages

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
from json import loads
from os.path import join, dirname
from jsonschema import Draft7Validator
from tools.string_manipulation import get_valid_country_code
from tools.api_responses import get_response, count_real_page
from tools.load_json_schema import load_json_schema

@allure.epic("Позитивные тесты API")
@allure.suite("Страницы. Проверка количества страниц.")
@allure.title("Сравнение реального количества страниц с вычисляемым")
@pytest.mark.parametrize("items_count", [ 5, 10, 15 ])
def test_01_positive_count_pages(setup_option, items_count):
    """Проверка вычисляемого количества страниц и получаемого в результате запросов.

    :param setup_option: Установочные параметры
    :type setup_option: dict
    :param items_count: Количество элементов на страницу
    :type items_count: int
    :return:
    """

    api_url = setup_option['site_url']

    setup_params = {
        "page": 1,
        "page_size": items_count
    }
    api_response = get_response(api_url, setup_params)
    content_json = loads(api_response.content.decode('utf-8'))

    calculate_pages = content_json["total"] // items_count
    if content_json["total"] % items_count:
        calculate_pages += 1
    pages = count_real_page(content_json["items"], items_count, api_url)
    assert pages == calculate_pages, \
        f"""Число вычислененных по элементам страниц ({calculate_pages}) не совпадает с реально полученными ({pages})
            Возможно дублирование элементов или неправильное указание для ключа total"""


@allure.epic("Позитивные тесты API.")
@allure.suite("Коды стран")
@allure.title("Сравнение выдаваемых кодов стран с разрешенными")
@pytest.mark.parametrize("items_count", [ 5, 10, 15 ])
def test_02_positive_pages_check_country(setup_option, items_count):
    """Просматриваем наличие на страницах только разрешенных кодов стран

    :param setup_option: Установочные параметры
    :type setup_option: dict
    :param items_count: Количество элементов на страницу
    :type items_count: int
    :return:
    """

    api_url = setup_option['site_url']

    page_params = {
        "page": 1,
        "page_size": items_count
    }
    api_response = get_response(api_url, page_params)
    content_json = loads(api_response.content.decode('utf-8'))

    pages = count_real_page(content_json["items"], items_count, api_url)

    for page in range(1, pages+1):
        page_params = {
            "page": page,
            "page_size": items_count
        }
        api_response = get_response(api_url, page_params)
        content_json = loads(api_response.content.decode('utf-8'))
        for item in content_json["items"]:
            assert item['country']['code'] in get_valid_country_code(), \
                f"""На странице {page} при количестве элементов на страницу {items_count}, 
                    попался элемент с кодом страны '{item['country']['code']}'"""


@allure.epic("Позитивные тесты API.")
@allure.suite("Страницы. Проверка соответствие json ответов эталонной json схеме")
@allure.title("Проверям соответсвие схеме постраничную выдачу для кол-ва элементов на страницу 5,10,15")
@pytest.mark.parametrize("items_count", [5, 10, 15])
def test_03_positive_pages_check_schemas(setup_option, items_count):
    """Проверка соответствия json схеме получаемых ответов от API

    :param setup_option: Установочные параметры
    :type setup_option: dict
    :param items_count: Количество элементов на страницу
    :type items_count: int
    :return:
    """

    api_url = setup_option['site_url']

    page_params = {
        "page": 1,
        "page_size": items_count
    }
    api_response = get_response(api_url, page_params)
    content_json = loads(api_response.content.decode('utf-8'))

    pages = count_real_page(content_json["items"], items_count, api_url)

    for page in range(1, pages + 1):
        page_params = {
            "page": page,
            "page_size": items_count
        }
        api_response = get_response(api_url, page_params)
        json_content = loads(api_response.content.decode('utf-8'))
        relative_path = join('../datasets', 'json_valid_schemas_country_code.json')
        filename = join(dirname(__file__), relative_path)
        schema = load_json_schema(filename=filename)
        check = Draft7Validator(schema=schema).is_valid(json_content)
        assert check, f"""На странице {page} при количестве элементов на страницу {items_count},
                        не проходит валидация схемы"""


@allure.epic("Позитивные тесты API.")
@allure.suite("Страницы. Проверка на наличие дубликатов на страницах")
@allure.title("Проверям на наличие дубликатов постраничную выдачу для кол-ва элементов на страницу 5,10,15")
@pytest.mark.parametrize("items_count", [5, 10, 15])
def test_04_positive_pages_first_duplicate(setup_option, items_count):
    """Проверка на наличие дубликатов при пространичных запросах

    :param setup_option: Установочные параметры
    :type setup_option: dict
    :param items_count: Количество эелментов на страницу
    :type items_count: int
    :return:
    """

    api_url = setup_option['site_url']

    page_params = {
        "page": 1,
        "page_size": items_count
    }
    api_response = get_response(api_url, page_params)
    content_json = loads(api_response.content.decode('utf-8'))

    pages = count_real_page(content_json["items"], items_count, api_url)
    all_items = []
    check_dub = True
    error_message = f"""Дубликаты:\r\n"""

    for page in range(1, pages + 1):
        page_params = {
            "page": page,
            "page_size": items_count
        }
        api_response = get_response(api_url, page_params)
        content_json = loads(api_response.content.decode('utf-8'))
        for item in content_json["items"]:
            if item in all_items:
                check_dub = False
                error_message += f"""EndPoint: {api_response.url}\r\n"""
                error_message += f"""На странице {page} обнаружен дубликат\r\n"""
                error_message += f"""{item}\r\n"""
            else:
                all_items.append(item)
    assert check_dub, error_message