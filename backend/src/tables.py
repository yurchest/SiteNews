from sqlalchemy import (
    Column,
    DateTime,
    Integer,
    Numeric,
    String,

)
from sqlalchemy_utils import URLType, PhoneNumberType
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime, timezone
from sqlalchemy.sql import expression
from sqlalchemy.ext.compiler import compiles
from sqlalchemy.types import DateTime

Base = declarative_base()


class UtcNow(expression.FunctionElement):
    type = DateTime()
    inherit_cache = True


@compiles(UtcNow, 'sqlite')
def pg_utcnow(element, compiler, **kw):
    return "datetime(CURRENT_TIMESTAMP, 'localtime')"


class News(Base):
    __tablename__ = "news"

    id = Column(Integer, primary_key=True)
    content = Column(String)
    url = Column(URLType)
    time_create = Column(DateTime, server_default=UtcNow())
    time_update = Column(DateTime, onupdate=UtcNow(), server_default=UtcNow())


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    username = Column(String, unique=True)
    phone_number = Column(String)
    password_hash = Column(String)
