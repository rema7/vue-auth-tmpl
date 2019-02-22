import falcon
import jsonschema

from validate_email import validate_email


def validate_schema(json, schema):
    try:
        jsonschema.validate(json, schema)
    except jsonschema.ValidationError as e:
        raise falcon.HTTPBadRequest(
            'Failed data validation',
            e.message
        )


def is_email_valid(email):
    if not validate_email(email):
        msg = 'Invalid email {}'.format(email)
        raise falcon.HTTPInvalidParam(
            msg=msg,
            param_name='email'
        )
