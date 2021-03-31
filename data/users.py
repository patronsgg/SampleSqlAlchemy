import sqlalchemy as sa
from sqlalchemy import orm
from datetime import datetime
from werkzeug.security import generate_password_hash, \
    check_password_hash
from .db_session import SqlAlchemyBase


class User(SqlAlchemyBase):
    __tablename__ = 'users'

    id = sa.Column(sa.Integer, primary_key=True,
                   autoincrement=True)
    name = sa.Column(sa.String, nullable=True)
    about = sa.Column(sa.String, nullable=True)
    email = sa.Column(sa.String, unique=True,
                      nullable=True)
    created_date = sa.Column(sa.DateTime,
                             default=datetime.now)
    hashed_password = sa.Column(sa.String, nullable=True)

    news = orm.relation('News', back_populates='user')

    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)
