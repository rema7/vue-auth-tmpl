import falcon

import settings as app_settings
from api.accounts.resources import AccountResource
from api.auth.resources import LoginResource, RegistrationResource
from api.resources import SettingsResource

from middlewares import ContentEncodingMiddleware, SecureMiddleware


app = falcon.API(middleware=[
    SecureMiddleware(),
    ContentEncodingMiddleware(),
])

app.add_route(app_settings.SETTINGS_ROUTE, SettingsResource())

if app_settings.DISABLE_SIGNUP is False:
    app.add_route(app_settings.REGISTER_ROUTE, RegistrationResource())

app.add_route(app_settings.LOGIN_ROUTE, LoginResource())
app.add_route(app_settings.ACCOUNT_ROUTE, AccountResource())
