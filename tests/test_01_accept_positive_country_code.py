# -*- coding: utf-8 -*-
"""
test_01_accept_positive_country_code
~~~~~~~~~~~~~~

The 2GIS API Test
Check positive country_code

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
from tools.string_manipulation import get_valid_country_code
from tools.api_responses import get_response
from tools.load_json_schema import load_json_schema


@allure.epic("Позитивные тесты API.")
@allure.suite("Фильтрация по коду страны. Проверка количества страниц.")
@allure.title("Проверка, что выборка при фильтрации по коду страны не содержит других кодов стран")
@pytest.mark.parametrize("country_code", get_valid_country_code())
def test_01_accept_positive_response(setup_option, country_code):
    """
    Проверка фильтрации при разрешенных кодах стран

    :param setup_option: Установочные параметры
    :type setup_option: dict
    :param country_code: Код страны
    :type: str
    :return:
    """

    api_url = setup_option['site_url']
    setup_params = {
        "country_code": country_code,
    }
    api_response = get_response(api_url, setup_params)
    json_content = json.loads(api_response.content.decode('utf-8'))
    response_message = (f" EndPoint: {api_url}?country_code={country_code}\n"
                        f" EndPoint: {api_response.url}\n"
                        f" Status: {api_response.status_code}\n"
                        f" Body: {json_content}\n"
                        f"    ")
    assert api_response.status_code == 200, f"""Статус {api_response.status_code} != 200\r\n""" + response_message

    relative_path = join('../datasets', 'json_valid_schemas_for_test.json')
    filename = join(dirname(__file__), relative_path)
    schema = load_json_schema(filename=filename)
    check = Draft7Validator(schema=schema).is_valid(json_content)
    assert check, f"""Ошибка при валидации json схемы {country_code}\r\n""" + response_message

    for item in json_content["items"]:
        assert item["country"]["code"] == country_code, \
            f"""Элементы не отфильтрованы. В {country_code} попал {item}"""
