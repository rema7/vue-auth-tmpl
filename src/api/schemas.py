registration_request_schema = {
    '$schema': 'http://json-schema.org/draft-04/schema',
    'type': 'object',
    'additionalProperties': False,
    'properties': {
        'email': {
            'type': 'string'
        },
        'password': {
            'type': 'string'
        },
    },
    'required': [
        'email',
        'password',
    ]
}

auth_request_schema = {
    '$schema': 'http://json-schema.org/draft-04/schema',
    'type': 'object',
    'additionalProperties': False,
    'properties': {
        'email': {
            'type': 'string'
        },
        'password': {
            'type': 'string'
        },
    },
    'required': [
        'email',
        'password',
    ]
}

project_create_request_schema = {
    '$schema': 'http://json-schema.org/draft-04/schema',
    'type': 'object',
    'additionalProperties': False,
    'properties': {
        'key': {
            'type': 'string'
        },
        'title': {
            'type': 'string'
        },
        'description': {
            'type': 'string'
        },
    },
    'required': [
        'key',
        'title',
    ]
}

item_create_request_schema = {
    '$schema': 'http://json-schema.org/draft-04/schema',
    'type': 'object',
    'additionalProperties': False,
    'properties': {
        'type_key': {
            'type': 'string'
        },
        'title': {
            'type': 'string'
        },
        'description': {
            'type': 'string'
        },
    },
    'required': [
        'type_key',
        'title',
    ]
}

item_save_request_schema = {
    '$schema': 'http://json-schema.org/draft-04/schema',
    'type': 'object',
    'additionalProperties': False,
    'properties': {
        'title': {
            'type': 'string'
        },
        'description': {
            'type': 'string'
        },
    },
    'required': [
        'title',
    ]
}

item_type_create_request_schema = {
    '$schema': 'http://json-schema.org/draft-04/schema',
    'type': 'object',
    'additionalProperties': False,
    'properties': {
        'key': {
            'type': 'string'
        },
        'name': {
            'type': 'string'
        },
        'plural': {
            'type': 'string'
        },
    },
    'required': [
        'key',
        'name',
        'plural',
    ]
}

item_link_create_request_schema = {
    '$schema': 'http://json-schema.org/draft-04/schema',
    'type': 'object',
    'additionalProperties': False,
    'properties': {
        'action': {
            'type': 'string'
        },
        'item_key': {
            'type': 'string'
        },
    },
    'required': [
        'action',
        'item_key',
    ]
}
