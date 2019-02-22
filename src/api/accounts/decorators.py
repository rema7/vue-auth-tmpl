import falcon


class HasPermission(object):
    def __init__(self, role_name):
        self.role_name = role_name

    def __call__(self, req, resp, resource, params):
        account = req.context['account']
        if self.role_name.lower() == 'admin':
            if account.admin is True:
                return
        raise falcon.HTTPForbidden()
