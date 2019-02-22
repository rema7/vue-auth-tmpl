from datetime import datetime

from sqlalchemy import (
    BigInteger,
    Column,
    String,
    TIMESTAMP,
    Boolean
)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BaseInfo:
    __table__ = None

    def __init__(self, **kwargs):
        for column in self.__table__.columns.items():
            column_name = column[0]
            if column_name not in kwargs:
                default = getattr(self.__table__.c, column_name).default
                if default:
                    kwargs[column_name] = default.arg if not hasattr(default.arg, '__call__') else None

        super(BaseInfo, self).__init__(**kwargs)

    id = Column(BigInteger, primary_key=True)
    created_at = Column(TIMESTAMP, default=datetime.utcnow, nullable=False)
    updated_at = Column(TIMESTAMP, default=datetime.utcnow, nullable=False)


class Account(BaseInfo, Base):
    __tablename__ = 'accounts'

    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    active = Column(Boolean, nullable=False, default=False)

    def as_dict(self):
        return {
            'id': self.id,
            'email': self.email,
            'active': self.active
        }


class AccountToken(Base):
    __tablename__ = 'accounts_tokens'

    account_id = Column(BigInteger, nullable=False, primary_key=True)
    token = Column(String, nullable=False)

