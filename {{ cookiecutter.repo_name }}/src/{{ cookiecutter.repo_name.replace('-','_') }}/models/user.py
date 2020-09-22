users = {
    'item_title': 'user',

    'resource_methods': ["POST", "GET"],
    'item_methods': ["GET", "PUT", "DELETE"],

    'schema': {
        'name': {'type': 'string', 'required': True},
        'metadata': {'allow_unknown': True},
    },
}