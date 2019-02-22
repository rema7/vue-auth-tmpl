"""

"""

from yoyo import step

__depends__ = {}

CREATE_TABLE = '''
CREATE TABLE accounts (
    id SERIAL PRIMARY KEY,
    email varchar not null UNIQUE,
    password varchar not null,
    active boolean not null default false,
    created_at timestamp default now(),
    updated_at timestamp default now()
);
CREATE TABLE accounts_activation_key (
    account_id bigint not null,
    activation_key varchar not null
);
CREATE TABLE accounts_tokens (
    account_id bigint not null,
    token varchar not null
);
'''

DROP_TABLE = '''
DROP TABLE accounts_tokens;
DROP TABLE accounts;
'''

steps = [
    step(CREATE_TABLE, DROP_TABLE)
]
