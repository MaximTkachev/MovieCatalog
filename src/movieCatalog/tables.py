import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = sa.Column(sa.Integer, primary_key=True)
    username = sa.Column(sa.Text, unique=True)
    email = sa.Column(sa.Text, unique=True)
    name = sa.Column(sa.Text)
    password_hash = sa.Column(sa.Text)
