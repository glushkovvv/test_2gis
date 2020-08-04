# -*- coding: utf-8 -*-
"""
conftest
~~~~~~~~~~~~~~~

Configuration file for pytest framework.

:author: Vadim Glushkov
:copyright: Copyright 2020, Check skills for 2GIS "
:license: BSD
:version: 1.0.0
:maintainer: Vadim Glushkov
:email: plussg@yandex.ru
:status: Development
"""


import pytest


def pytest_addoption(parser):
    """Добавляем возможность приема именованных аргументов из командой строки
            в тестах при запуске pytest

    """
    parser.addoption("--site_url",
                     action="store",
                     type="string",
                     default="https://regions-test.2gis.com/1.0/regions",
                     dest='URL API',
                     help="Endpoint тестируемого API")


@pytest.fixture(scope='function')
def setup_option(request):
    """Создаем объект для удобство работы с переменными в тестовых методах

    """
    setup_parameters = {}
    if request.config.getoption('--site_url'):
        setup_parameters['site_url'] = request.config.getoption('--site_url')
    return setup_parameters
