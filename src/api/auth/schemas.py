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
