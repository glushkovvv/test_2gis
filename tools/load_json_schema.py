import json
from jsonschema import Draft7Validator, SchemaError

def load_json_schema(filename=None):
    """ Loads the given schema file """

    if filename is None:
        return

    with open(filename) as schema_file:
        schema = json.loads(schema_file.read())

    # try:
    #     Draft7Validator.check_schema(schema)
    # except SchemaError as schemaError:
    #     print(schemaError)

    return schema