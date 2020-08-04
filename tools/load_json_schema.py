"""
load_json_schema
~~~~~~~~~~~~~~

The 2GIS API Test
Tools load json file

:author: Vadim Glushkov
:copyright: Copyright 2019, The2GIS API Test"
:license: MIT
:version: 1.0.0
:maintainer: Vadim Glushkov
:email: plussg@yandex.ru
:status: Development
"""


import json

def load_json_schema(filename=None):
    """ Loads the given schema file """

    if filename is None:
        return

    with open(filename) as schema_file:
        schema = json.loads(schema_file.read())

    return schema
