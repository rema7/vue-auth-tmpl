import falcon

from api.decorators import validate_request
from api.helpers import is_email_valid
from api.auth.helpers import generate_password_hash, verify_password, generate_token
from api.auth.schemas import auth_request_schema, registration_request_schema
from db.models import Account, AccountToken
from decorators import with_db_session


class LoginResource:
    @staticmethod
    @with_db_session
    def handle_post(email, password, db_session=None):
        is_email_valid(email)

        account = db_session.query(Account).filter(Account.email == email).first()
        if account is None or verify_password(password, account.password) is not True:
            raise falcon.HTTPNotFound(
                title='Wrong email or password',
            )

        token = generate_token()
        db_session.add(AccountToken(
            account_id=account.id,
            token=token,
        ))
        db_session.commit()

        return {
            'token': token,
        }

    @validate_request(auth_request_schema)
    def on_post(self, req, resp):
        body = req.context['body']

        resp.body = self.handle_post(
            email=body['email'],
            password=body['password']
        )


class RegistrationResource:
    @staticmethod
    @with_db_session
    def handle_post(email, password, db_session=None):
        is_email_valid(email)

        account = db_session.query(Account).filter(Account.email == email).first()
        if account is not None:
            raise falcon.HTTPConflict(
                title='Account already exist',
            )
        password_hash = generate_password_hash(password)
        new_account = Account(
            email=email,
            password=password_hash,
        )
        db_session.add(new_account)
        db_session.commit()

        return {
            'status': 'ok'
        }

    @validate_request(registration_request_schema)
    def on_post(self, req, resp):
        body = req.context['body']

        resp.body = self.handle_post(
            email=body['email'],
            password=body['password']
        )
