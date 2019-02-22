from api.helpers import validate_schema


def validate_request(schema):
    def decor(func):
        def wrapper(self, req, resp, *args, **kwargs):
            json = req.context['body']
            validate_schema(json, schema)
            return func(self, req, resp, *args, **kwargs)
        return wrapper
    return decor

