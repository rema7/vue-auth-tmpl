from api.auth.helpers import generate_password_hash
from db.models import Account
from decorators import with_db_session
from qa.data import test_accounts

created_accounts = []
created_projects = []


@with_db_session
def qa_generate_data(
        db_session=None
):
    for account in test_accounts:
        account_db = Account(
            email=account['email'],
            password=generate_password_hash(account['password']),
            active=True
        )
        db_session.add(account_db)
        db_session.flush()
        created_accounts.append(account_db)

    # account_db = next(acc for acc in created_accounts if acc.owner is True)

    db_session.commit()

